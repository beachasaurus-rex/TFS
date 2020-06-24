import unittest
from abc import ABC

class TestBase(ABC):
    def _IsWithinTolerance(self, testValue, actualValue,
    tolerance):
        isLToETMax = (testValue <= actualValue * (1+tolerance))
        isGToETMin = (testValue >= actualValue * (1-tolerance))
        return isLToETMax and isGToETMin

class UnitTest(TestBase, unittest.TestCase):
    def IsWithinTolerance(self, testValue, actualValue, tol):
        return self._IsWithinTolerance(testValue,
        actualValue, tol)
