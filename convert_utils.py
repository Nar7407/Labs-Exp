import constants

# Unit-conversion helpers; all factors come from constants.py


def km_to_miles(km):
    """Convert a distance from kilometres to miles."""
    return km * constants.KM_TO_MILES


def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit."""
    return celsius * constants.FAHRENHEIT_SCALE + constants.FAHRENHEIT_OFFSET


def kg_to_pounds(kg):
    """Convert a mass from kilograms to pounds."""
    return kg * constants.KG_TO_POUNDS