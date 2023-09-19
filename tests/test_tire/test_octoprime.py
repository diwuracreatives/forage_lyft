import unittest

from tire.octoprimeTire import OctoprimeTire


class TestCarriganTires(unittest.TestCase):
    def does_needs_service(self):
        tire_wear = [0.2, 0.1, 0.6, 0.3]
        tires = OctoprimeTire(tire_wear)
        self.assertTrue(tires.needs_service())

    def doesnot_needs_service(self):
        tire_wear = [0.1, 0.2, 0.3, 0.3]
        tires = OctoprimeTire(tire_wear)
        self.assertFalse(tires.needs_service())