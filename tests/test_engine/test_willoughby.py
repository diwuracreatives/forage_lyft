import unittest
from engine.willoughbyEngine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
       def does_needs_service(self):
            engine = WilloughbyEngine(current_mileage=60500, last_service_mileage=20)
            self.assertTrue(engine.needs_service)

       def doesnot_needs_service(self):
            engine = WilloughbyEngine(current_mileage=60001, last_service_mileage=50)
            self.assertFalse(engine.needs_service)


if __name__ == "__main__":
    unittest.main()
   