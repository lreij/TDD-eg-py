# -*- coding:utf-8 -*-
"""Test-Driven Development by example.
Multi-currency money."""

import unittest


class Dollar:

    def __init__(self, amount):
        self.amount = amount 

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def __eq__(self, obj):
        return self.amount == obj.amount


class TestTDD(unittest.TestCase):

    def testMultiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEquals(10, product.amount)
        product = five.times(3)
        self.assertEquals(15, product.amount)

    def testEquality(self):
        self.assertTrue(Dollar(5) == Dollar(5))
        self.assertFalse(Dollar(5) == Dollar(6))


if __name__ == '__main__':
    unittest.main()
