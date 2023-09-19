import unittest
from battery.splinderBattery import SpindlerBattery
from datetime import date

today = date.today()

class TestSplinderBattery(unittest.TestCase):
       def does_needs_service(self):
            battery = SpindlerBattery(current_date=today, last_service_date=date.isoformat(("2021-05-15")))
            self.assertTrue(battery.needs_service)

       def doesnot_needs_service(self):
            battery = SpindlerBattery(current_date=today, last_service_date=date.isoformat(("2022-11-25")))
            self.assertFalse(battery.needs_service)


if __name__ == "__main__":
    unittest.main()
   