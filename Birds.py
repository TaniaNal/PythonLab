from enum import Enum

class BirdsType(Enum)
    DONTRUNAWAY = 1
    RUNAWAY = 2
    
class Birds:

    def __init__(self, weight, isRunAway, name):
        self.name = name
        self.weight = weight
        self.isRunAway = isRunAway

    def __str__(self):
        return "Name: " + str(self.name) + ", weight: " + str(self.weight) + ", is run away: " + str(self.isRunAway)
