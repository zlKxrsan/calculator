# calculator.py
#
# Basic functions to handle calculations.
# Handles calculation requests and returns results.
#
# Author: Lawan Mai
# Created: 28.04.2025
# Version: 1.1


def calculate(function):
    try:
        result = eval(function)
    except ZeroDivisionError as e:
        result = "Division by zero"
    except SyntaxError as e:
        result = "Invalid Input"
    except Exception as e:
        result = "unhandled error occurred"

    return result
