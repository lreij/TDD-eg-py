# -*- coding:utf-8 -*-
"""Test-Driven Development by example.
Multi-currency money."""

import unittest


class Money:
    
    def __init__(self, amount, currency):
        self._amount = amount 
        self._currency = currency

    def __eq__(self, obj):
        return self._amount == obj._amount and \
        self.currency() == obj.currency()

    def times(self, multiplier):
        return Franc(self._amount * multiplier, 
            self._currency)

    def currency(self):
        return self._currency

    @classmethod
    def dollar(self, amount):
        return Dollar(amount, "USD")

    @classmethod
    def franc(self, amount):
        return Franc(amount, "CHF")


class Dollar(Money):
    pass


class Franc(Money):
    pass


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

    def testCurrency(self):
        self.assertEquals("USD", Money.dollar(1).currency())
        self.assertEquals("CHF", Money.franc(1).currency())

    def testDifferenctClassEquality(self):
        self.assertTrue(Money(10, "CHF") == Franc(10, "CHF"))


if __name__ == '__main__':
    unittest.main()
