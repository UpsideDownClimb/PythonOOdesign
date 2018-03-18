from roulette.bin import Bin
from roulette.outcome import Outcome
import random

class Wheel(object):

    """Docstring for Wheel class"""

    __slots__ = ['bins', 'rng', 'allOutcomes']

    def __init__(self, rng = None):
        """TODO: to be defined. """
        self.bins = tuple( Bin() for i in range(38) )
        self.rng  = rng or random.Random()
        self.allOutcomes = set()

    def addOutcome(self, binIndex, outcome):
        """
        :outcome: An Outcome class object to be added to a numbered bin in tuple
        :number: Index of bin in the tuple in range from 0 to 37
        """
        self.allOutcomes |= set([outcome])
        self.bins[binIndex].add(outcome)

    def getOutcome(self, outcomeName):
        """
        """
        outcome = None

        for element in self.allOutcomes:
            if element.name == outcomeName:
                outcome = element
                break

        return(outcome)

    def next(self):
        """Return random bin"""
        return self.rng.choice(self.bins)
