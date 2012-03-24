# -*- coding:utf-8 -*-
"""Test-Driven Development by example.
Multi-currency money."""

import unittest


class Dollar:

    def __init__(self, amount):
        self.amount = amount 

    def times(self, multiplier):
        self.amount *= multiplier


class TestTDD(unittest.TestCase):

    def testMultiplication(self):
        five = Dollar(5)
        five.times(2)
        self.assertEquals(10, five.amount)


if __name__ == '__main__':
    unittest.main()
