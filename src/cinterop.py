from ctypes import CDLL, CFUNCTYPE, c_double

class OWTP:

    MaxP = 100
    MaxP_R5 = 50
    MinP = 0
    CritP = 22.064

    MaxT = 2273.15
    MinT_R5 = 1073.15
    MaxT_R4 = 647.096
    MinT = 273.15

    MaxH = 4000
    MinH = -0.042

    MaxS = 10
    MinS = -0.0002

    MaxX = 1
    MinX = 0

    def __init__(self):
        self._lib = CDLL("src/OWTP.dll")
        protoTwoParams = CFUNCTYPE(c_double, c_double, c_double)
        protoOneParam = CFUNCTYPE(c_double, c_double)
        ptApi = (1, "P"), (1, "T")
        phApi = (1, "P"), (1, "h")
        psApi = (1, "P"), (1, "s")
        hsApi = (1, "h"), (1, "s")
        txApi = (1, "T"), (1, "x")
        pxApi = (1, "P"), (1, "x")

        #properties as functions of pressure and temperature
        self.v_PT = protoTwoParams(("v_P_T", self._lib), ptApi)
        self.u_PT = protoTwoParams(("u_P_T", self._lib), ptApi)
        self.s_PT = protoTwoParams(("s_P_T", self._lib), ptApi)
        self.h_PT = protoTwoParams(("h_P_T", self._lib), ptApi)
        self.cp_PT = protoTwoParams(("cp_P_T", self._lib), ptApi)
        self.cv_PT = protoTwoParams(("cv_P_T", self._lib), ptApi)
        self.w_PT = protoTwoParams(("w_P_T", self._lib), ptApi)

        #properties as functions of pressure and enthalpy
        self.v_Ph = protoTwoParams(("v_P_h", self._lib), phApi)
        self.u_Ph = protoTwoParams(("u_P_h", self._lib), phApi)
        self.s_Ph = protoTwoParams(("s_P_h", self._lib), phApi)
        self.T_Ph = protoTwoParams(("T_P_h", self._lib), phApi)
        self.cp_Ph = protoTwoParams(("cp_P_h", self._lib), phApi)
        self.cv_Ph = protoTwoParams(("cv_P_h", self._lib), phApi)
        self.w_Ph = protoTwoParams(("w_P_h", self._lib), phApi)
        self.x_Ph = protoTwoParams(("x_P_h", self._lib), phApi)

        #properties as functions of pressure and entropy
        self.v_Ps = protoTwoParams(("v_P_s", self._lib), psApi)
        self.u_Ps = protoTwoParams(("u_P_s", self._lib), psApi)
        self.h_Ps = protoTwoParams(("h_P_s", self._lib), psApi)
        self.T_Ps = protoTwoParams(("T_P_s", self._lib), psApi)
        self.cp_Ps = protoTwoParams(("cp_P_s", self._lib), psApi)
        self.cv_Ps = protoTwoParams(("cv_P_s", self._lib), psApi)
        self.w_Ps = protoTwoParams(("w_P_s", self._lib), psApi)
        self.x_Ps = protoTwoParams(("x_P_s", self._lib), phApi)

        #properties as functions of enthalpy and entropy
        self.v_hs = protoTwoParams(("v_h_s", self._lib), hsApi)
        self.u_hs = protoTwoParams(("u_h_s", self._lib), hsApi)
        self.P_hs = protoTwoParams(("P_h_s", self._lib), hsApi)
        self.T_hs = protoTwoParams(("T_h_s", self._lib), hsApi)
        self.cp_hs = protoTwoParams(("cp_h_s", self._lib), hsApi)
        self.cv_hs = protoTwoParams(("cv_h_s", self._lib), hsApi)
        self.w_hs = protoTwoParams(("w_h_s", self._lib), hsApi)
        self.x_hs = protoTwoParams(("x_h_s", self._lib), phApi)

        #properties as functions of pressure and quality
        self.v_Px = protoTwoParams(("v_P_x", self._lib), pxApi)
        self.u_Px = protoTwoParams(("u_P_x", self._lib), pxApi)
        self.h_Px = protoTwoParams(("h_P_x", self._lib), pxApi)
        self.s_Px = protoTwoParams(("s_P_x", self._lib), pxApi)

        #properties as functions of temperature and quality
        self.v_Tx = protoTwoParams(("v_T_x", self._lib), txApi)
        self.u_Tx = protoTwoParams(("u_T_x", self._lib), txApi)
        self.h_Tx = protoTwoParams(("h_T_x", self._lib), txApi)
        self.s_Tx = protoTwoParams(("s_T_x", self._lib), txApi)

        #saturation properties
        self.PSat_T = protoOneParam(("PSat_T", self._lib))
        self.TSat_P = protoOneParam(("TSat_P", self._lib))

if __name__ == "__main__":
    pass
