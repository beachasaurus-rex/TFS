from numpy import *

from test.testbases import *

from src.fluids import *
from src.systems import *

class testFunctions(UnitTest):

    def setUp(self):
        states = BuildStates(1,8,FluidState,Water)

        self.Connectables = [Device(1, [states[0], states[7]]),
        Node(2, states[0:2]), Device(3, states[1:3]),
        Node(4, states[2:4]), Device(5, states[3:5]),
        Node(6, states[4:6]), Device(7, states[5:7]),
        Node(8, states[-2:])
        ]
        self.States = states

    def test_GetEquipment_ReturnsOnlyDevices(self):
        expEquip = self.Connectables[0:7:2]
        testEquip = GetEquipment(self.Connectables)

        #if both are the same length & all of the expected
        #equipment are found in the results, then the results
        #must be identical
        self.assertTrue(len(expEquip) == len(testEquip))
        for curExpEquip in expEquip:
            self.assertTrue(curExpEquip in testEquip)

    def test_GetUniqueStates_ReturnsOnlyUniqueStates(self):
        expUniqueStates = self.States
        testStates = GetUniqueStates(self.Connectables)

        #if both are the same length & all of the expected
        #states are found in the results, then the results
        #must be identical
        self.assertTrue(len(expUniqueStates) == len(testStates))
        for curExpState in expUniqueStates:
            self.assertTrue(curExpState in testStates)

    def test_GetUniqueStateIds_ReturnsCorrectIds(self):
        expUniqueIds = [state.Id for state in self.States]
        testIds = GetUniqueStateIds(self.Connectables)

        #if both are the same length & all of the expected
        #IDs are found in the results, then the results
        #must be identical
        self.assertTrue(len(expUniqueIds) == len(testIds))
        for curExpId in expUniqueIds:
            self.assertTrue(curExpId in testIds)

    def test_BuildConnectionMatrix_CorrectlyBuildsMatrix(self):
        expMatrix = array([
        [1,0,0,0,0,0,0,1],
        [1,1,0,0,0,0,0,0],
        [0,1,1,0,0,0,0,0],
        [0,0,1,1,0,0,0,0],
        [0,0,0,1,1,0,0,0],
        [0,0,0,0,1,1,0,0],
        [0,0,0,0,0,1,1,0],
        [0,0,0,0,0,0,1,1]])
        testMat = BuildConnectionMatrix(self.Connectables)

        #the matrices should have the same dimensions
        expDims = expMatrix.shape
        testDims = testMat.shape
        self.assertTrue(expDims[0] == testDims[0])
        self.assertTrue(expDims[1] == testDims[1])
        for m in range(0,expDims[0]):
            for n in range(0,expDims[1]):
                #the matrices should have the same elements
                self.assertTrue(expMatrix[m,n] == testMat[m,n])

    def test_BuildConnectionMatrix_CorrectlyBuildsComplexMatrix(self):
        states = BuildStates(1,17,FluidState,Water)
        connectables = [Device(1, [states[0], states[10], states[15]]),
        Device(2, [states[1], states[11], states[14]]),
        Node(3, states[0:3]),
        Device(4, [states[2], states[3], states[13], states[14]]),
        Node(5, states[3:6]),
        Device(6, [states[4], states[6]]),
        Device(7, [states[5], states[7], states[16]]),
        Device(8, [states[12], states[13], states[15], states[16]]),
        Node(9, states[6:9]),
        Device(10, [states[8], states[9], states[12]]),
        Node(11, states[9:12])
        ]
        expMatrix = array([
        [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0],
        [0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0],
        [0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1],
        [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0]])
        testMat = BuildConnectionMatrix(connectables)

        #the matrices should have the same dimensions
        expDims = expMatrix.shape
        testDims = testMat.shape
        self.assertTrue(expDims[0] == testDims[0])
        self.assertTrue(expDims[1] == testDims[1])
        for m in range(0,expDims[0]):
            for n in range(0,expDims[1]):
                #the matrices should have the same elements
                self.assertTrue(expMatrix[m,n] == testMat[m,n])

    def test_BuildStateDataDict_CorrectlyBuildsDictionary(self):
        stateData = [StateDataPoint(1,500,IndependentVariable.Temperature),
        StateDataPoint(3,500,IndependentVariable.Temperature),
        StateDataPoint(5,500,IndependentVariable.Temperature),
        StateDataPoint(7,500,IndependentVariable.Temperature),
        StateDataPoint(2,500,IndependentVariable.Temperature),
        StateDataPoint(4,500,IndependentVariable.Temperature),
        StateDataPoint(6,500,IndependentVariable.Temperature),
        StateDataPoint(8,500,IndependentVariable.Temperature),
        StateDataPoint(1,5,IndependentVariable.Pressure)
        ]
        expDictData = [(1, (stateData[0], stateData[8])),
        (2, tuple([stateData[4]])),
        (3, tuple([stateData[1]])),
        (4, tuple([stateData[5]])),
        (5, tuple([stateData[2]])),
        (6, tuple([stateData[6]])),
        (7, tuple([stateData[3]])),
        (8, tuple([stateData[7]])),
        ]
        expDict = dict(expDictData)
        uniqueIds = GetUniqueStateIds(self.Connectables)
        testDict = BuildStateDataDict(stateData, uniqueIds)
        #both dictionaries should have the same number of entries
        self.assertTrue(len(expDict) == len(testDict))
        for expKey, expVal in expDictData:
            #all expected keys should be found in the test dict
            self.assertTrue(expKey in testDict)
            testVal = testDict[expKey]
            #both tuples should have the same number of entries
            self.assertTrue(len(expVal) == len(testVal))
            for i in range(0,len(expVal)):
                #all tuple entries should be the same
                self.assertTrue(expVal[i] == testVal[i])
