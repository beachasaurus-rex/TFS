from abc import ABC

from src.cinterop import *

class ThermoProperties(ABC):
    #notes:
    #   --enthalpy, entropy, internal energy, volume, isobaric
    #     heat capacity, and isochoric heat capacity are all
    #     per unit mass quantities

    #constructor
    #propertyFunction must be a method
    def __init__(self):
        self._P = float('nan')
        self._T = float('nan')
        self._h = float('nan')
        self._s = float('nan')
        self._u = float('nan')
        self._v = float('nan')
        self._cp = float('nan')
        self._cv = float('nan')

    #getters
    def GetPressure(self):
        return self._P
    def GetTemperature(self):
        return self._T
    def GetEnthalpy(self):
        return self._h
    def GetEntropy(self):
        return self._s
    def GetInternalEnergy(self):
        return self._u
    def GetSpecificVolume(self):
        return self._v
    def GetCp(self):
        return self._cp
    def GetCv(self):
        return self._cv

class WaterThermoProperties(ThermoProperties):

    _owtp = OWTP()

    def __init__(self):
        super(ThermoProperties, self).__init__()
        self._x = float('nan')

    def GetVaporQuality(self):
        return self._x

    def SetProperties_PT(self, P, T):
        isInOWTPR5 = P <= self._owtp.MaxP_R5 \
        and P > self._owtp.MinP \
        and T <= self._owtp.MaxT \
        and T >= self._owtp.MinT_R5

        isInOWTPR1thru4 = P <= self._owtp.MaxP \
        and P >= self._owtp.MinP \
        and T <= self._owtp.MinT_R5 \
        and T >= self._owtp.MinT

        if not(isInOWTPR1thru4 or isInOWTPR5):
            #crash if outside of bounds
            raise NotImplementedError()

        self._P = P
        self._T = T
        self._v = self._owtp.v_PT(P,T)
        self._u = self._owtp.u_PT(P,T)
        self._s = self._owtp.s_PT(P,T)
        self._h = self._owtp.h_PT(P,T)
        self._cp = self._owtp.cp_PT(P,T)
        self._cv = self._owtp.cv_PT(P,T)
        self._x = float('nan')
    def SetProperties_Ph(self, P, h):
        isInOWTPR1thru4 = P <= self._owtp.MaxP \
        and P > self._owtp.MinP \
        and h <= self._owtp.MaxH \
        and h >= self._owtp.MinH

        if not(isInOWTPR1thru4):
            #crash if outside of bounds
            raise NotImplementedError()

        self._P = P
        self._T = self._owtp.T_Ph(P,h)
        self._v = self._owtp.v_Ph(P,h)
        self._u = self._owtp.u_Ph(P,h)
        self._s = self._owtp.s_Ph(P,h)
        self._h = h
        self._cp = self._owtp.cp_Ph(P,h)
        self._cv = self._owtp.cv_Ph(P,h)
        self._x = self._owtp.x_Ph(P,h)
    def SetProperties_Ps(self, P, s):
        isInOWTPR1thru4 = P <= self._owtp.MaxP \
        and P > self._owtp.MinP \
        and s <= self._owtp.MaxS \
        and s >= self._owtp.MinS

        if not(isInOWTPR1thru4):
            #crash if outside of bounds
            raise NotImplementedError()

        self._P = P
        self._T = self._owtp.T_Ps(P,s)
        self._v = self._owtp.v_Ps(P,s)
        self._u = self._owtp.u_Ps(P,s)
        self._s = s
        self._h = self._owtp.h_Ps(P,s)
        self._cp = self._owtp.cp_Ps(P,s)
        self._cv = self._owtp.cv_Ps(P,s)
        self._x = self._owtp.x_Ps(P,s)
    def SetProperties_hs(self, h, s):
        isInOWTPR1thru4 = h <= self._owtp.MaxH \
        and h >= self._owtp.MinH \
        and s <= self._owtp.MaxS \
        and s >= self._owtp.MinS \

        if not(isInOWTPR1thru4):
            #crash if outside of bounds
            raise NotImplementedError()

        self._P = self._owtp.P_hs(h,s)
        self._T = self._owtp.T_hs(h,s)
        self._v = self._owtp.v_hs(h,s)
        self._u = self._owtp.u_hs(h,s)
        self._s = s
        self._h = h
        self._cp = self._owtp.cp_hs(h,s)
        self._cv = self._owtp.cv_hs(h,s)
        self._x = self._owtp.x_hs(h,s)
    def SetProperties_Px(self, P, x):
        T = self._owtp.TSat_P(P)

        isInOWTPR4 = P <= self._owtp.CritP \
        and P > self._owtp.MinP \
        and x <= self._owtp.MaxX \
        and x >= self._owtp.MinX \
        and T <= self._owtp.MaxT_R4 \
        and T >= self._owtp.MinT

        if not(isInOWTPR4):
            #crash if outside of bounds
            raise NotImplementedError()

        self._P = P
        self._T = T
        self._v = self._owtp.v_Px(P,x)
        self._u = self._owtp.u_Px(P,x)
        self._s = self._owtp.s_Px(P,x)
        self._h = self._owtp.h_Px(P,x)
        self._x = x

        #at this point, linearly interpolate between the cps
        #and cvs @ 0 and 1 vapor quality

        if (x <= 1e-08):
            cpLow = self._owtp.cp_Ps(P, self._s)
            cvLow = self._owtp.cv_Ps(P, self._s)
        else:
            s = self._owtp.s_Px(P,0)
            cpLow = self._owtp.cp_Ps(P, s)
            cvLow = self._owtp.cv_Ps(P, s)

        if (1.0 - x <= 1e-08):
            cpHigh = self._owtp.cp_Ps(P, self._s)
            cvHigh = self._owtp.cv_Ps(P, self._s)
        else:
            s = self._owtp.s_Px(P,1)
            cpHigh = self._owtp.cp_Ps(P, s)
            cvHigh = self._owtp.cv_Ps(P, s)

        self._cp = cpLow + x * (cpHigh - cpLow)
        self._cv = cvLow + x * (cvHigh - cvLow)
    def SetProperties_Tx(self, T, x):
        P = self._owtp.PSat_T(T)

        isInOWTPR4 = P <= self._owtp.CritP \
        and P > self._owtp.MinP \
        and x <= self._owtp.MaxX \
        and x >= self._owtp.MinX \
        and T <= self._owtp.MaxT_R4 \
        and T >= self._owtp.MinT

        if not(isInOWTPR4):
            #crash if outside of bounds
            raise NotImplementedError()

        self._P = P
        self._T = T
        self._v = self._owtp.v_Tx(T,x)
        self._u = self._owtp.u_Tx(T,x)
        self._s = self._owtp.s_Tx(T,x)
        self._h = self._owtp.h_Tx(T,x)
        self._x = x

        #at this point, linearly interpolate between the cps
        #and cvs @ 0 and 1 vapor quality

        if (x <= 1e-08):
            cpLow = self._owtp.cp_Ps(P, self._s)
            cvLow = self._owtp.cv_Ps(P, self._s)
        else:
            s = self._owtp.s_Tx(T,0)
            cpLow = self._owtp.cp_Ps(P, s)
            cvLow = self._owtp.cv_Ps(P, s)

        if (1.0 - x <= 1e-08):
            cpHigh = self._owtp.cp_Ps(P, self._s)
            cvHigh = self._owtp.cv_Ps(P, self._s)
        else:
            s = self._owtp.s_Tx(T,1)
            cpHigh = self._owtp.cp_Ps(P, s)
            cvHigh = self._owtp.cv_Ps(P, s)

        self._cp = cpLow + x * (cpHigh - cpLow)
        self._cv = cvLow + x * (cvHigh - cvLow)

if __name__ == "__main__":
    pass
