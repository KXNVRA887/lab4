"""Юнит-тесты для модулей validators и operations."""

import unittest
from unittest.mock import patch

import logger
from operations import heat_amount, heating_class
from validators import validate_range, input_mass, input_t1, input_t2


class TestValidateRange(unittest.TestCase):
    """Проверка validate_range."""

    def test_inside(self):
        self.assertEqual(validate_range(5, 1, 10), (True, ""))

    def test_low_bound(self):
        self.assertTrue(validate_range(1, 1, 10)[0])

    def test_high_bound(self):
        self.assertTrue(validate_range(10, 1, 10)[0])

    def test_below(self):
        ok, msg = validate_range(0, 1, 10)
        self.assertFalse(ok)
        self.assertNotEqual(msg, "")

    def test_above(self):
        ok, msg = validate_range(11, 1, 10)
        self.assertFalse(ok)
        self.assertNotEqual(msg, "")


class TestInputMass(unittest.TestCase):
    """Циклический ввод массы."""

    def setUp(self):
        logger.clear()

    @patch("validators.input", side_effect=["abc", "2000", "50"])
    def test_loop(self, _):
        self.assertEqual(input_mass(), 50.0)
        self.assertEqual(len(logger.get_entries()), 2)

    @patch("validators.input", side_effect=["0.1"])
    def test_low_bound(self, _):
        self.assertEqual(input_mass(), 0.1)

    @patch("validators.input", side_effect=["1000"])
    def test_high_bound(self, _):
        self.assertEqual(input_mass(), 1000.0)


class TestInputT1(unittest.TestCase):
    """Циклический ввод начальной температуры."""

    def setUp(self):
        logger.clear()

    @patch("validators.input", side_effect=["x", "-100", "20"])
    def test_loop(self, _):
        self.assertEqual(input_t1(), 20.0)
        self.assertEqual(len(logger.get_entries()), 2)

    @patch("validators.input", side_effect=["-50"])
    def test_low_bound(self, _):
        self.assertEqual(input_t1(), -50.0)

    @patch("validators.input", side_effect=["100"])
    def test_high_bound(self, _):
        self.assertEqual(input_t1(), 100.0)


class TestInputT2(unittest.TestCase):
    """Циклический ввод конечной температуры (t2 > t1)."""

    def setUp(self):
        logger.clear()

    @patch("validators.input", side_effect=["20", "10", "80"])
    def test_t2_not_greater(self, _):
        self.assertEqual(input_t2(20.0), 80.0)
        self.assertEqual(len(logger.get_entries()), 2)

    @patch("validators.input", side_effect=["1500", "500"])
    def test_out_of_range(self, _):
        self.assertEqual(input_t2(20.0), 500.0)
        self.assertEqual(len(logger.get_entries()), 1)

    @patch("validators.input", side_effect=["1000"])
    def test_high_bound(self, _):
        self.assertEqual(input_t2(20.0), 1000.0)


class TestOperations(unittest.TestCase):
    """Проверка расчётов и классификации."""

    def test_water(self):
        self.assertAlmostEqual(heat_amount(10, 4200, 20, 80), 2520000.0)

    def test_oil(self):
        self.assertAlmostEqual(heat_amount(10, 2000, 20, 80), 1200000.0)

    def test_steel(self):
        self.assertAlmostEqual(heat_amount(10, 500, 20, 80), 300000.0)

    def test_class_5(self):
        self.assertEqual(heating_class(5), "малый нагрев")

    def test_class_10(self):
        self.assertEqual(heating_class(10), "нормальный нагрев")

    def test_class_50(self):
        self.assertEqual(heating_class(50), "нормальный нагрев")

    def test_class_100(self):
        self.assertEqual(heating_class(100), "нормальный нагрев")

    def test_class_150(self):
        self.assertEqual(heating_class(150), "интенсивный нагрев")


if __name__ == "__main__":
    unittest.main()
