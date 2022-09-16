import unittest
import meter

class TestMeter(unittest.TestCase):

    def test_consumption(self):
        """
        Confirms consumption is between 0 and 9000
        """
        amount = meter.Meter.consumption()

        self.assertGreater(amount, 0)
        self.assertLess(amount, 9000)

    def test_get_meter_value(self):
        """
        Confirms meter value stored is returned
        """
        m = meter.Meter(3000)
        current_meter, time = m.get_meter_value()
        self.assertEqual(3000, current_meter)

    def test_update_meter_value(self):
        """
        Confirms meter value is changed
        """
        m = meter.Meter(3000)
        m.update_meter_value()

        self.assertNotEqual(3000, m.get_meter_value())


