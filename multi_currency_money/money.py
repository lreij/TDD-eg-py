# -*- coding:utf-8 -*-
"""Test-Driven Development by example.
Multi-currency money."""

import unittest


class Money:
    
    def __init__(self, amount):
        self._amount = amount 

    def __eq__(self, obj):
        return self._amount == obj._amount and \
        self.__class__ == obj.__class__


class Dollar(Money):

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)


class Franc(Money):

    def times(self, multiplier):
        return Franc(self._amount * multiplier)


class TestTDD(unittest.TestCase):

    def testMultiplication(self):
        five = Dollar(5)
        self.assertEquals(Dollar(10), five.times(2))
        self.assertEquals(Dollar(15), five.times(3))

    def testEquality(self):
        self.assertTrue(Dollar(5) == Dollar(5))
        self.assertFalse(Dollar(5) == Dollar(6))
        self.assertTrue(Franc(5) == Franc(5))
        self.assertFalse(Franc(5) == Franc(6))
        self.assertFalse(Franc(5) == Dollar(5))

    def testFrancMultiplication(self):
        five = Franc(5)
        self.assertEquals(Franc(10), five.times(2))
        self.assertEquals(Franc(15), five.times(3))


if __name__ == '__main__':
    unittest.main()
