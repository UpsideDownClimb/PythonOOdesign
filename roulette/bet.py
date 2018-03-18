from roulette.wheel import Wheel

class Bet(object):

    """Docstring for Bet. """

    def __init__(self, betAmount, outcome):
        """TODO: to be defined1. """
        self.betAmount = betAmount
        self.outcome = outcome

    def winAmount(self):
        total = outcome.winAmount(amount) + betAmount
        return(total)

    def loseAmount(self):
        return(betAmount)

    def __str__(self):
        return("{0} on {1}".format(self.betAmount, self.outcome))

    def __repr__(self):
        return("Bet({0}, {1})".format(self.betAmount, self.outcome))


