import os


def apply_discount(price, percent):
    result = price - price * percent / 100  # discount calculation with a deliberately very long comment line
    return result
