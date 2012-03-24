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

    def times(self, multiplier):
        pass
        
    @classmethod
    def dollar(self, amount):
        return Dollar(amount)

    @classmethod
    def franc(self, amount):
        return Franc(amount)


class Dollar(Money):

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)


class Franc(Money):

    def times(self, multiplier):
        return Franc(self._amount * multiplier)


class TestTDD(unittest.TestCase):

    def testMultiplication(self):
        five = Money.dollar(5)
        self.assertEquals(Money.dollar(10), five.times(2))
        self.assertEquals(Money.dollar(15), five.times(3))

    def testEquality(self):
        self.assertTrue(Money.dollar(5) == Money.dollar(5))
        self.assertFalse(Money.dollar(5) == Money.dollar(6))
        self.assertTrue(Money.franc(5) == Money.franc(5))
        self.assertFalse(Money.franc(5) == Money.franc(6))
        self.assertFalse(Money.franc(5) == Money.dollar(5))

    def testFrancMultiplication(self):
        five = Money.franc(5)
        self.assertEquals(Money.franc(10), five.times(2))
        self.assertEquals(Money.franc(15), five.times(3))


if __name__ == '__main__':
    unittest.main()
