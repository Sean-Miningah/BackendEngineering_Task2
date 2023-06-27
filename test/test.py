import unittest
from datetime import date
# import sys 
# sys.path.append("..")

from ..carfactory import CarFactory


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(last_service_date, today, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = date.today()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_calliope(last_service_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = date.today()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_calliope(last_service_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(
            last_service_mileage=last_service_mileage, 
            current_mileage=current_mileage, 
            current_date=today, last_service_date=last_service_date)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(
            last_service_mileage=last_service_mileage, 
            current_mileage=current_mileage, 
            current_date=today, last_service_date=last_service_date)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = date.today()
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.create_glissade(
            last_service_mileage=last_service_mileage, 
            current_mileage=current_mileage, 
            current_date=last_service_date, last_service_date=last_service_date)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = date.today()
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.create_glissade(
            last_service_mileage=last_service_mileage, 
            current_mileage=current_mileage, 
            current_date=last_service_date, last_service_date=last_service_date)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        car = CarFactory.create_palindrome(warning_light_is_on, last_service_date, last_service_date)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        car = CarFactory.create_palindrome(warning_light_is_on, last_service_date, last_service_date)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = date.today()
        warning_light_is_on = True

        car = CarFactory.create_palindrome(warning_light_is_on, last_service_date, last_service_date)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = date.today()
        warning_light_is_on = False

        car = CarFactory.create_palindrome(warning_light_is_on, last_service_date, last_service_date)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(last_service_mileage, current_mileage, today, last_service_date)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = car = CarFactory.create_rorschach(last_service_mileage, current_mileage, today, last_service_date)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = date.today()
        current_mileage = 60001
        last_service_mileage = 0

        car = car = CarFactory.create_rorschach(last_service_mileage, current_mileage, last_service_date, last_service_date)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = date.today()
        current_mileage = 60000
        last_service_mileage = 0

        car = car = car = CarFactory.create_rorschach(last_service_mileage, current_mileage, last_service_date, last_service_date)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(last_service_mileage, current_mileage, today, last_service_date)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(last_service_mileage, current_mileage, today, last_service_date)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = date.today()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_thovex(last_service_mileage, current_mileage, last_service_date, last_service_date)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = date.today()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_thovex(last_service_mileage, current_mileage, last_service_date, last_service_date)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
