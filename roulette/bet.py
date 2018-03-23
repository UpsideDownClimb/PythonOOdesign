from roulette.wheel import Wheel
from roulette.outcome import Outcome

class Bet(object):

    """Docstring for Bet
    """

    def __init__(self, betAmount: int, outcome: Outcome):
        """TODO: to be defined1. """
        self.betAmount = betAmount
        self.outcome = outcome

    def winAmount(self):
        return(self.outcome.winAmount(self.betAmount))

    def loseAmount(self):
        return(self.betAmount)

    def __str__(self):
        return("{0} on {1}".format(self.betAmount, self.outcome))

    def __repr__(self):
        return("Bet({0}, {1})".format(self.betAmount, self.outcome))


