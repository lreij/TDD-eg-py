# -*- coding:utf-8 -*-
"""Test-Driven Development by example.
Multi-currency money."""

import unittest


class Dollar:

    def __init__(self, amount):
        self.__amount = amount 

    def times(self, multiplier):
        return Dollar(self.__amount * multiplier)

    def __eq__(self, obj):
        return self.__amount == obj.__amount


class TestTDD(unittest.TestCase):

    def testMultiplication(self):
        five = Dollar(5)
        self.assertEquals(Dollar(10), five.times(2))
        self.assertEquals(Dollar(15), five.times(3))

    def testEquality(self):
        self.assertTrue(Dollar(5) == Dollar(5))
        self.assertFalse(Dollar(5) == Dollar(6))


if __name__ == '__main__':
    unittest.main()
