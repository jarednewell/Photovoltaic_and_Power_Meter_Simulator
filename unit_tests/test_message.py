import message
import unittest
import socket
import settings

from unittest.mock import patch


class TestMessage(unittest.TestCase):

    def setUp(self):
        # create test environment
        self.queue = 'test'
        self.to_send = "Nice"

        # use test queue not production
        with patch('message.settings',
                   queue_name=self.queue,
                   rabbitmq_host='localhost',
                   exchange=''
                   ):

            self.msg = message.Message()
            # clean out queue
            self.msg.channel.queue_purge(queue=self.queue)

    def tearDown(self):
        # clean out queue and close connection
        if self.msg.connection.is_open:
            self.msg.channel.queue_purge(queue=self.queue)
            self.msg.connection.close()

    def test_init(self):
        """
        Confirms the setup of the message broker connection
        """
        channel = self.msg.connection.channel()

        # confirm settings are read in
        self.assertIs(self.msg.parameters.host, settings.rabbitmq_host)
        self.assertEqual(self.msg.parameters.port, settings.default_port)
        self.assertEqual(self.msg.queue.title(), self.queue.capitalize())

        # confirm state
        self.assertTrue(self.msg.connection.is_open)
        self.assertTrue(channel.is_open)
        self.assertEqual(0, self.msg.active_queue.method.message_count)

        # confirm exception handling when the connection parameters have failed
        with patch('message.settings', rabbitmq_host="broken"):
            self.assertRaises(socket.gaierror, message.Message)

    def test_publish(self):
        """
        Confirms if test_publish send a message to a queue
        """

        self.msg.publish(message=self.to_send)
        # Does not acknowledge the method therefore it remains in the queue
        details, properties, body = \
            self.msg.channel.basic_get(queue=self.queue, auto_ack=False)

        self.assertEqual(self.to_send, body.decode())
        self.assertEqual(1, self.msg.active_queue.method.message_count)

    def test_consume(self):
        """
        Confirms the consumption of a message from a queue
        """
        queued_message_count = self.msg.active_queue.method.message_count

        item = self.msg.consume()

        # returns a tuple of None,None,None results when no messages exists
        if queued_message_count > 1:
            self.assertEqual(item.decode(), self.to_send)
        else:
            self.assertIsNone(item)

    def test_close(self):
        """
        Confirms the closure of a connection using close
        """
        self.msg.close()
        self.assertTrue(self.msg.connection.is_closed)