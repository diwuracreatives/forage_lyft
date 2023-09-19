import unittest

from tire.carriganTire import CarriganTire


class TestCarriganTires(unittest.TestCase):
    def does_needs_service(self):
        tire_wear = [0.2, 0.2, 0.5, 0.4]
        tires = CarriganTire(tire_wear)
        self.assertTrue(tires.needs_service())

    def doesnot_needs_service(self):
        tire_wear = [0.1, 0.1, 0.3, 0.3]
        tires = CarriganTire(tire_wear)
        self.assertFalse(tires.needs_service())