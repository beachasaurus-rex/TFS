from test.testbases import *

from src.fluids import *

class testFluid(UnitTest):
    numVars = 5

    def setUp(self):
        self.fluid = Fluid(self.numVars)

    def test_VerifyCorrectlyBuildsVariableVector(self):
        testNumVars = len(self.fluid.GetIndependentVariables())
        self.assertTrue(self.numVars, testNumVars)


class testWater(UnitTest):
    _tol = 0.01

    def setUp(self):
        self.fluid = Water()

    def test_VerifyEnters_PT(self):
        indVars = [IndependentVariable.Pressure,
        IndependentVariable.Temperature]
        self.fluid.SetIndependentVariables(indVars)

        refP = 3
        refT = 300
        expH = 0.115331273E+03
        self.fluid.SetProperties(P=refP, T=refT)
        testH = self.fluid.GetEnthalpy()

        isWithinTol = self.IsWithinTolerance(expH, testH,
        self._tol)
        self.assertTrue(isWithinTol)

    def test_VerifyEnters_Ps(self):
        indVars = [IndependentVariable.Pressure,
        IndependentVariable.Entropy]
        self.fluid.SetIndependentVariables(indVars)

        refP = 3
        refS = 0.392294792
        expH = 0.115331273E+03
        self.fluid.SetProperties(P=refP, s=refS)
        testH = self.fluid.GetEnthalpy()

        isWithinTol = self.IsWithinTolerance(expH, testH,
        self._tol)
        self.assertTrue(isWithinTol)

    def test_VerifyEnters_Ph(self):
        indVars = [IndependentVariable.Pressure,
        IndependentVariable.Enthalpy]
        self.fluid.SetIndependentVariables(indVars)

        refP = 3
        refH = 0.115331273E+03
        expS = 0.392294792
        self.fluid.SetProperties(P=refP, h=refH)
        testS = self.fluid.GetEntropy()

        isWithinTol = self.IsWithinTolerance(expS, testS,
        self._tol)
        self.assertTrue(isWithinTol)

    def test_VerifyEnters_Px(self):
        indVars = [IndependentVariable.Pressure,
        IndependentVariable.VaporQuality]
        self.fluid.SetIndependentVariables(indVars)

        refP = 0.0365398932
        refX = 0.641808120
        expH = 1800.0
        self.fluid.SetProperties(P=refP, x=refX)
        testH = self.fluid.GetEnthalpy()

        isWithinTol = self.IsWithinTolerance(expH, testH,
        self._tol)
        self.assertTrue(isWithinTol)

    def test_VerifyEnters_Tx(self):
        indVars = [IndependentVariable.Temperature,
        IndependentVariable.VaporQuality]
        self.fluid.SetIndependentVariables(indVars)

        refT = 3.468475498E+02
        refX = 0.641808120
        expH = 1800.0
        self.fluid.SetProperties(T=refT, x=refX)
        testH = self.fluid.GetEnthalpy()

        isWithinTol = self.IsWithinTolerance(expH, testH,
        self._tol)
        self.assertTrue(isWithinTol)

if __name__ == '__main__':
    unittest.main()
