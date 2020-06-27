from abc import ABC

from src.states import *

class Connectable(ABC):
    def __init__(self, id, states):
        self.States = states
        self.Id = id

    def __eq__(self, other):
        if isinstance(other, Connectable):
            return self.Id == other.Id

    def __ne__(self, other):
        return not(self.__eq__(other))

class Node(Connectable):
    def __init__(self, id, states):
        super(Node, self).__init__(id, states)

class Device(Connectable):
    def __init__(self, id, states):
        super(Device, self).__init__(id, states)

class SteamGenerator(Device):
    def __init__(self, id, waterStates, name):
        super(SteamGenerator, self).__init__(id, waterStates)
        self.Name = name

class HeatExchanger(Device):
    def __init__(self, id, waterStates, name):
        super(HeatExchanger, self).__init__(id, waterStates)
        self.Name = name

class SteamTurbine(Device):
    def __init__(self, id, waterStates, name):
        super(HeatExchanger, self).__init__(id, waterStates)
        self.Name = name

if __name__ == "__main__":
    pass
