from abc import ABC
from enum import Enum

from src.properties import *

class IndependentVariable(Enum):
    Unknown = 0
    Pressure = 1
    Temperature = 2
    Enthalpy = 3
    Entropy = 4
    VaporQuality = 5

class Fluid(ABC):
    def __init__(self, numIVars):
        self._numIVars = numIVars
        self._iVars = [IndependentVariable.Unknown] \
                       * numIVars

    def GetIndependentVariables(self):
        return self._iVars
    def SetIndependentVariables(self, indVarList):
        for i in range(self._numIVars):
            self._iVars[i] = indVarList[i]

class Water(Fluid):

    def __init__(self):
        super(Water, self).__init__(2)
        self._thermoProps = WaterThermoProperties()
        self._iVarCombos = self._DefineIVarCombos()

    def GetPressure(self):
        return self._thermoProps.GetPressure()
    def GetTemperature(self):
        return self._thermoProps.GetTemperature()
    def GetEnthalpy(self):
        return self._thermoProps.GetEnthalpy()
    def GetEntropy(self):
        return self._thermoProps.GetEntropy()
    def GetInternalEnergy(self):
        return self._thermoProps.GetInternalEnergy()
    def GetSpecificVolume(self):
        return self._thermoProps.GetSpecificVolume()
    def GetCp(self):
        return self._thermoProps.GetCp()
    def GetCv(self):
        return self._thermoProps.GetCv()
    def GetVaporQuality(self):
        return self._thermoProps.GetVaporQuality()

    def SetProperties(self, **kwargs):
        #assume correct combinations are passed
        P = kwargs.get('P', None)
        T = kwargs.get('T', None)
        x = kwargs.get('x', None)
        s = kwargs.get('s', None)
        h = kwargs.get('h', None)

        ivars = self._iVars
        for ivarcombo in self._iVarCombos:
            isPT = IndependentVariable.Pressure in ivars \
            and IndependentVariable.Temperature in ivars

            isPh = IndependentVariable.Pressure in ivars \
            and IndependentVariable.Enthalpy in ivars

            isPs = IndependentVariable.Pressure in ivars \
            and IndependentVariable.Entropy in ivars

            isPx = IndependentVariable.Pressure in ivars \
            and IndependentVariable.VaporQuality in ivars

            isTx = IndependentVariable.Temperature in ivars \
            and IndependentVariable.VaporQuality in ivars

            ishs = IndependentVariable.Enthalpy in ivars \
            and IndependentVariable.Entropy in ivars

            if not set(ivarcombo).issubset(ivars):
                continue
                
            elif isPs:
                self._thermoProps.SetProperties_Ps(P,s)
                return

            elif isPh:
                self._thermoProps.SetProperties_Ph(P,h)
                return

            elif isPx:
                self._thermoProps.SetProperties_Px(P,x)
                return

            elif isPT:
                self._thermoProps.SetProperties_PT(P,T)
                return

            elif isTx:
                self._thermoProps.SetProperties_Tx(T,x)
                return

            elif ishs:
                self._thermoProps.SetProperties_hs(h,s)
                return

    def _DefineIVarCombos(self):
        #combinations:
        #   P,s // h,s // P,T
        #   P,h // P,x // T,x
        iVarCombos = [
            [IndependentVariable.Entropy, IndependentVariable.Pressure],
            [IndependentVariable.Entropy, IndependentVariable.Enthalpy],
            [IndependentVariable.Pressure, IndependentVariable.Temperature],
            [IndependentVariable.Pressure, IndependentVariable.Enthalpy],
            [IndependentVariable.Pressure, IndependentVariable.VaporQuality],
            [IndependentVariable.Temperature, IndependentVariable.VaporQuality]
        ]

        return iVarCombos

if __name__ == "__main__":
    pass
