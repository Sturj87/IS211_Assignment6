## IS211 A#6 SAAR TURJEMAN

import unittest
from conversions import*

class CelsiusTestCase(unittest.TestCase):
    """Tests for celsius for `conversions.py`."""

    def test_celsius_to_kelvin(self):
        """Tests validate correct temperature conversions."""
        self.assertTrue(373.15 == round(convertCelsiusToKelvin(100), 2))
        self.assertTrue(293.15 == round(convertCelsiusToKelvin(20), 2))
        self.assertTrue(200 == round(convertCelsiusToKelvin(-73.15), 2))
        self.assertTrue(308.15 == round(convertCelsiusToKelvin(35), 2))
        self.assertTrue(1 == round(convertCelsiusToKelvin(-272.15), 2))

    def test_celsius_to_fahrenheit(self):
        """Tests validate correct temperature conversions."""
        self.assertTrue(50 == round(convertCelsiusToFahrenheit(10), 2))
        self.assertTrue(176 == round(convertCelsiusToFahrenheit(80), 2))
        self.assertTrue(113 == round(convertCelsiusToFahrenheit(45), 2))
        self.assertTrue(-27.4 == round(convertCelsiusToFahrenheit(-33), 2))
        self.assertTrue(-58.47 == round(convertCelsiusToFahrenheit(-50.25), 2))


class FahrenheitTestCase(unittest.TestCase):
    """Tests for fahrenheit for `conversions.py`."""

    def test_fahrenheit_to_kelvin(self):
        """Tests validate correct temperature conversions."""
        self.assertTrue(310.93 == round(convertFahrenheitToKelvin(100), 2))
        self.assertTrue(255.37 == round(convertFahrenheitToKelvin(-0.67), 2))
        self.assertTrue(273.15 == round(convertFahrenheitToKelvin(32), 2))
        self.assertTrue(290.93 == round(convertFahrenheitToKelvin(64), 2))
        self.assertTrue(235.93 == round(convertFahrenheitToKelvin(-35), 2))

    def test_kelvin_to_celsius(self):
        """Tests validate correct temperature conversions."""
        self.assertTrue(-273.15 == round(convertKelvinToCelsius(0), 2))
        self.assertTrue(-100.00 == round(convertKelvinToCelsius(173.15), 2))
        self.assertTrue(0.00 == round(convertKelvinToCelsius(273.15), 2))
        self.assertTrue(37.78 == round(convertKelvinToCelsius(310.93), 2))
        self.assertTrue(106.85 == round(convertKelvinToCelsius(380), 2))


class KelvinTestCase(unittest.TestCase):
    """Tests for kelvin for `conversions.py`."""

    def test_kelvin_to_fahrenheit(self):
        """Tests validate correct temperature conversions."""
        self.assertTrue(80.33 == round(convertKelvinToFahrenheit(300), 2))
        self.assertTrue(-459.67 == round(convertKelvinToFahrenheit(0), 2))
        self.assertTrue(-379.67 == round(convertKelvinToFahrenheit(50), 2))
        self.assertTrue(-179.67 == round(convertKelvinToFahrenheit(100), 2))
        self.assertTrue(-999.67 == round(convertKelvinToFahrenheit(-300), 2))

    def test_kelvin_to_celsius(self):
        """Tests validate correct temperature conversions."""
        self.assertTrue(-153.15 == round(convertKelvinToCelsius(120), 2))
        self.assertTrue(-273.15 == round(convertKelvinToCelsius(0), 2))
        self.assertTrue(325.85 == round(convertKelvinToCelsius(599), 2))
        self.assertTrue(-173.15 == round(convertKelvinToCelsius(100), 2))
        self.assertTrue(406.85 == round(convertKelvinToCelsius(680), 2))


if __name__ == '__main__':
    unittest.main()