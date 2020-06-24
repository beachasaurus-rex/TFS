from test.testbases import *

from src.cinterop import *

class testOWTP(UnitTest):
    _tol = 0.01

    def setUp(self):
        self.owtp = OWTP()

    def test_ReturnsReferenceValue(self):
        P = 3
        T = 300
        sExp = 0.392294792
        sTest = self.owtp.s_PT(P, T);
        isWithinTol = self.IsWithinTolerance(sExp, sTest,
        self._tol)

        self.assertTrue(isWithinTol)

if __name__ == '__main__':
    unittest.main()
