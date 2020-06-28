from numpy import *

from src.states import *
from src.devices import *

class System:
    def __init__(self, name, connectables):
        self.Name = name
        self.Network = connectables
        self.ConnectionMatrix = BuildConnectionMatrix(connectables)
        self.Equipment = GetEquipment(connectables)
        self.UniqueStates = GetUniqueStates(connectables)

class StateDataPoint:
    def __init__(self, stateId, val, independentVar):
        self.StateId = stateId
        self.Value = val
        self.IndependentVariable = independentVar

    def __eq__(self, other):
        if isinstance(other, StateDataPoint):
            sameIds = self.StateId == other.StateId
            sameVals = self.Value == other.Value
            sameVars = self.IndependentVariable == other.IndependentVariable
            return sameIds and sameVals and sameVars

    def __ne__(self, other):
        return not(self.__eq__(other))

def BuildStateDataDict(stateData, uniqueStateIds):
    #Builds a dictionary that holds input data for each
    #state.
    #Key = the state's ID
    #Value = a tuple of state data points
    
    numUniqueIds = len(uniqueStateIds)
    dictData = []
    for i in range(0,numUniqueIds):
        refId = uniqueStateIds[i]
        numPoints = len(stateData)
        bucket = []
        for j in range(0,numPoints):
            if refId == stateData[j].StateId:
                bucket.append(stateData[j])

        imBucket = tuple(bucket)
        dictData.append((refId, imBucket))

    return dict(dictData)

def GetEquipment(connectables):
    numConnectables = len(connectables)

    #collect any instances of Device
    equipment = []
    for i in range(0,numConnectables):
        curConnectable = connectables[i]
        if isinstance(curConnectable, Device):
            equipment.append(curConnectable)

    return equipment

def GetUniqueStates(connectables):
    numConnectables = len(connectables)

    #gather all of the states
    states = []
    for i in range(0,numConnectables):
        states.extend(connectables[i].States)

    #remove duplicate elements
    return list(set(states))

def GetUniqueStateIds(connectables):
    numConnectables = len(connectables)

    #gather all of the state Ids
    stateIds = []
    for i in range(0,numConnectables):
        curConnectable = connectables[i]
        numStates = len(curConnectable.States)
        for j in range(0,numStates):
            curState = curConnectable.States[j]
            stateIds.append(curState.Id)

    #remove duplicate elements
    return list(set(stateIds))

def BuildConnectionMatrix(connectables):
    #Rectangular matrix meant to show which devices hold
    #specific states, and it is used to traverse the system.
    #A row indicates which states a device contains.
    #A column indicates which devices a state is a member.


    m = len(connectables)
    uniqueStateIds = GetUniqueStateIds(connectables)
    n = len(uniqueStateIds)

    #build connection matrix by identifying which states are connected to
    #connectables
    conMat = zeros((m,n))
    for i in range(0,m):
        for j in range(0,n):
            numDevStates = len(connectables[i].States)
            for k in range(0,numDevStates):
                curStateId = connectables[i].States[k].Id
                if curStateId == uniqueStateIds[j]:
                    conMat[i,j] = 1
                    break

    return conMat
