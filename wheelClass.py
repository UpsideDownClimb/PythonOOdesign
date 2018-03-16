from binClass import Bin
from outcomeClass import Outcome
import random

class Wheel(object):

    """Docstring for Wheel class"""
    
    __slots__ = ['bins', 'rng']

    def __init__(self, rng = None):
        """TODO: to be defined. """
        self.bins = tuple( Bin() for i in range(38) )
        self.rng  = rng or random.Random()

    def addOutcome(self, binIndex: int, outcome: Outcome) -> None:
        """
        :outcome: An Outcome class object to be added to a numbered bin in tuple
        :number: Index of bin in the tuple in range from 0 to 37
        """
        self.bins[binIndex].add(outcome)

    def next(self) -> Bin:
        """Return random bin"""
        binChoice = self.rng.choice(self.bins)

    def get(self, binIndex: int) -> Bin:
        """
        :binIndex: Bin index: 0-37
        """
        return(self.bins[binIndex])

        
