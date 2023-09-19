import unittest
import engine.capuletEngine as CapuletEngine



class TestCapuletEngine(unittest.TestCase):
       def does_needs_service(self):
            engine = CapuletEngine(current_mileage=30500, last_service_mileage=20)
            self.assertTrue(engine.needs_service)

       def doesnot_needs_service(self):
            engine = CapuletEngine(current_mileage=28000, last_service_mileage=50)
            self.assertFalse(engine.needs_service)


if __name__ == "__main__":
    unittest.main()
   