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
        return Money(self._amount * multiplier, 
            self._currency)

    def currency(self):
        return self._currency

    def plus(self, addend):
        return Sum(self, addend)

    def reduce(self, to):
        return self

    @classmethod
    def dollar(self, amount):
        return Money(amount, "USD")

    @classmethod
    def franc(self, amount):
        return Money(amount, "CHF")


class Bank:

    def reduce(self, source, to):
        return source.reduce(to)


class Sum:

    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, to):
        amount = self.augend._amount + self.addend._amount
        return Money(amount, to)


class TestTDD(unittest.TestCase):

    def testMultiplication(self):
        five = Money.dollar(5)
        self.assertEquals(Money.dollar(10), five.times(2))
        self.assertEquals(Money.dollar(15), five.times(3))

    def testEquality(self):
        self.assertTrue(Money.dollar(5) == Money.dollar(5))
        self.assertFalse(Money.dollar(5) == Money.dollar(6))
        self.assertFalse(Money.franc(5) == Money.dollar(5))

    def testFrancMultiplication(self):
        five = Money.franc(5)
        self.assertEquals(Money.franc(10), five.times(2))
        self.assertEquals(Money.franc(15), five.times(3))

    def testCurrency(self):
        self.assertEquals("USD", Money.dollar(1).currency())
        self.assertEquals("CHF", Money.franc(1).currency())

    def testSimpleAddition(self):
        five = Money.dollar(5)
        sum = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(sum, "USD")
        self.assertEquals(Money.dollar(10), reduced)

    def testPlusReturnsSum(self):
        five = Money.dollar(5)
        sum = five.plus(five)
        self.assertEquals(five, sum.augend)
        self.assertEquals(five, sum.addend)

    def testReduceSum(self):
        sum = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum, "USD")
        self.assertEquals(Money.dollar(7), result)

    def testReduceMoney(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        self.assertEquals(Money.dollar(1), result)


if __name__ == '__main__':
    unittest.main()
