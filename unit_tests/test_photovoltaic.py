import photovoltaic
import unittest


class TestMessage(unittest.TestCase):

    def test_model(self):
        # Outside of the normal distribution
        zero_hours = [[6,0],[22,0]]
        # The mean of the normal distribution
        greatest_hour = 14
        # Maximum output at the mean in kW
        greatest_output = 3.2

        # Ensures the output doesn't exceed greatest output
        for hour in range(zero_hours[0][0], zero_hours[1][0]):
            self.assertLessEqual(
                photovoltaic.Photovoltaic.power_model(hour, 0),
                greatest_output)

        # Ensures the between the zero hours the output remains 0.0
        for hour in range(zero_hours[1][0], zero_hours[0][0]):
            self.assertEqual(0.0,
                             photovoltaic.Photovoltaic.power_model(hour, 0))

        # For each zero hour and minutes the output is 0.0
        for t in zero_hours:
            amount = photovoltaic.Photovoltaic.power_model(t[0],t[1])
            self.assertEqual(0.0, amount)

        self.assertEqual(greatest_output,
                         photovoltaic.Photovoltaic.power_model(greatest_hour))
