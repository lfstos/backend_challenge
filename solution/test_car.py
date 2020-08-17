from unittest import TestCase
from solution.car import Car


class CarTestCase(TestCase):

    def test_refuel_with_six_hundred_twenty_four_percent(self):
        car = Car()
        car.liters = 624
        self.assertEqual('1250%', car.refuel())

    def test_refuel_with_six_hundred_twenty_six_percent(self):
        car = Car()
        car.liters = 626
        self.assertEqual('626%', car.refuel())

    def test_refuel_with_three_percent(self):
        car = Car()
        car.liters = 3
        self.assertEqual('1250%', car.refuel())

    def test_refuel_with_over_a_hundred_percent(self):
        car = Car()
        car.liters = 150
        self.assertEqual('1250%', car.refuel())

    def test_refuel_with_five_percent(self):
        car = Car()
        car.liters = 5
        self.assertEqual('1250%', car.refuel())

    def test_create_new_car(self):
        self.assertEqual(f'Liters: 1250, Tyres: 4', Car().create_car())

    def test_get_car_status(self):
        car = Car()
        car.liters = 70
        car.tyres = 3
        self.assertEqual(f'Liters: 70, Tyres: 3', car.get_car_stauts())

    def test_no_create_tyres(self):
        car = Car()
        car.disagree = 280
        self.assertEqual('Pneu não criado', car.create_tyres())

    def test_create_tyres(self):
        car = Car()
        car.disagree = 286
        self.assertEqual('Pneu criado', car.create_tyres())

    def test_new_car(self):
        self.assertEqual(f'Liters: 1250, Tyres: 4', Car().create_car())

    def test_manitenance_liters(self):
        car = Car()
        car.piece = 'liters'
        self.assertEqual(f'Liters: 1250, Tyres: 4', car.maintenance())

    def test_manitenance_tyres(self):
        car = Car()
        car.piece = 'tyres'
        self.assertEqual(f'Liters: 1250, Tyres: 4', car.maintenance())

    def test_travel_ten_thousand_kilometers(self):
        car = Car()
        car.total_km = 10000
        car.disagree = 280
        self.assertEqual(f'Liters: 1250, Tyres: 4', car.travel())

    def test_travel_ten_thousand_kilometers_and_tyres_greater_than_hundred_and_eighty(self):
        car = Car()
        car.total_km = 10000
        car.disagree = 282
        self.assertEqual(f'Liters: 1250, Tyres: 4', car.travel())

    def test_travel_ten_thousand_kilometers_and_tyres_disagree_two_hundred_and_ninety_kilometers(self):
        car = Car()
        car.total_km = 10000
        car.disagree = 290
        self.assertEqual(f'Liters: 1250, Tyres: 4', car.travel())