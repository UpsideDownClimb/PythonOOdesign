from roulette.bin import Bin
from roulette.outcome import Outcome
import random

class Wheel(object):

    """Docstring for Wheel class"""
    
    __slots__ = ['bins', 'rng']

    def __init__(self, rng = None):
        """TODO: to be defined. """
        self.bins = tuple( Bin() for i in range(38) )
        self.rng  = rng or random.Random()

    def addOutcome(self, binIndex, outcome):
        """
        :outcome: An Outcome class object to be added to a numbered bin in tuple
        :number: Index of bin in the tuple in range from 0 to 37
        """
        self.bins[binIndex].add(outcome)

    def next(self):
        """Return random bin"""
        return self.rng.choice(self.bins)


    def get(self, binIndex):
        """
        :binIndex: Bin index: 0-37
        """
        return(self.bins[binIndex])

        
