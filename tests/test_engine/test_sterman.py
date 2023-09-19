import unittest
from engine.sternmanEngine import SternmanEngine

class TestStermanEngine(unittest.TestCase):
       def does_needs_service(self):
            engine = SternmanEngine(is_warning_light_on=True)
            self.assertTrue(engine.needs_service)

       def doesnot_needs_service(self):
            engine = SternmanEngine(is_warning_light_on=False)
            self.assertFalse(engine.needs_service)


if __name__ == "__main__":
    unittest.main()
    