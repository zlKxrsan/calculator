# calculator.py
#
# Basic functions to handle calculations.
# Handles calculation requests and returns results.
#
# Author: Lawan Mai
# Created: 28.04.2025
# Version: 1.0


def calculate(num1, num2, operation):
    if operation == "add":
        result = add(num1, num2)
    elif operation == "subtract":
        result = subtract(num1, num2)
    elif operation == "multiply":
        result = multiply(num1, num2)
    elif operation == "divide":
        result = divide(num1, num2)

    return result


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Error: division by zero"
    return num1 / num2
