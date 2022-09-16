import logging
import pika
import settings
import socket

from typing import AnyStr, Tuple


class Message:
    """
    Used to send and receive message to a RabbitMQ message broker
    """

    def __init__(self):

        self.queue = settings.queue_name
        self.active_queue = None

        try:
            self.parameters = pika.ConnectionParameters(settings.rabbitmq_host)
            self.connection = pika.BlockingConnection(self.parameters)
            self.channel = self.connection.channel()
            self.active_queue = self.channel.queue_declare(queue=self.queue)

        except socket.gaierror as e:
            logging.error(f"Connection failed - {settings.rabbitmq_host} "
                         f"host failed or is incorrectly configured")
            raise e

    def publish(self, message: AnyStr) -> None:
        """
        Used to send a message to the queue
        :param message: string
        :return: None
        """
        self.channel.basic_publish(exchange=settings.exchange,
                                   routing_key=self.queue,
                                   body=message)

        return None

    def consume(self) -> Tuple:
        """
        Retrives queued messages - takes a call back method
        :return: string (json)
        """
        delivery_message, basic_properties, item = \
            self.channel.basic_get(queue=self.queue, auto_ack=True)

        return item

    def close(self) -> None:
        """
        Finalise connection
        :return: None
        """
        if self.connection.is_open:
            self.connection.close()

        return None
