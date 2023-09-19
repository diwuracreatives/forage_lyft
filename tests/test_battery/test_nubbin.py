import unittest
from battery.nubbinBattery import NubbinBattery
from datetime import date

today = date.today()

class TestRubbinBattery(unittest.TestCase):
       def does_needs_service(self):
            battery = NubbinBattery(current_date=today, last_service_date=date.isoformat(("2017-06-15")))
            self.assertTrue(battery.needs_service)

       def doesnot_needs_service(self):
            battery = NubbinBattery(current_date=today, last_service_date=date.isoformat(("2023-01-15")))
            self.assertFalse(battery.needs_service)


if __name__ == "__main__":
    unittest.main()
   