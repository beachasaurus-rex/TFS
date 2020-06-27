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
