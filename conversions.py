## IS211 A#6 SAAR TURJEMAN

def convertCelsiusToKelvin(degrees):
    """ This function converts from Celsius to Kelvin.
   """
    kelvin = degrees + 273.15
    return kelvin


def convertCelsiusToFahrenheit(degrees):
    """This function converts from Celsius to Fahrenheit.
    """
    Fahrenheit = (degrees * 1.8) + 32
    return Fahrenheit


def convertFahrenheitToCelsius(degrees):
    """This function converts from Fahrenheit to Celsius.
    """
    Celsius = (degrees - 32.0) * 5./9
    return Celsius


def convertFahrenheitToKelvin(degrees):
    """This function converts from Fahrenheit to Kelvin.

    """
    Kelvin = ((degrees + 459.67) * 5 / 9)
    return Kelvin

def convertKelvinToCelsius(degrees):
    """This function converts from Kelvin to Celsius.
    """
    Celsius = degrees - 273.15
    return Celsius


def convertKelvinToFahrenheit(degrees):
    """This function converts from Kelvin to Fahrenheit.
    """
    Fahrenheit_KC = convertKelvinToCelsius(degrees)
    Fahrenheit = convertCelsiusToFahrenheit(Fahrenheit_KC)
    return Fahrenheit
