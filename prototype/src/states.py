from abc import ABC

from src.fluids import *

class State(ABC):
    def __init__(self, id):
        self.Id = id

    def __eq__(self, other):
        if isinstance(other, State):
            return other.Id == self.Id

    def __ne__(self, other):
        return not(self.__eq__(other))

    def __repr__(self):
        return "State(%d)" % self.Id

    def __hash__(self):
        return hash(self.__repr__())

class FluidState(State):
    def __init__(self, id, fluid):
        super(FluidState, self).__init__(id)
        self.Fluid = fluid

def BuildState(id, stateClass, fluidClass):
    if stateClass.__name__ == 'FluidState':
        if fluidClass.__name__ == 'Water':
            return FluidState(id, Water())

def BuildStates(startId, numStates, stateClass, fluidClass):
    return [BuildState(startId + i, stateClass, fluidClass) \
    for i in range(0,numStates)]

if __name__ == "__main__":
    pass
