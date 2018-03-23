from roulette.bet import Bet

class Passenger57(object):

    """Docstring for Passenger57. """
    __slots__ = ['black', 'table', 'wheel', 'winnings', 'losses']
    BET_AMOUNT = 10

    def __init__(self, table, wheel):
        """TODO: to be defined1. """
        self.wheel = wheel
        self.table = table
        self.black = self.wheel.getOutcome("Black")
        self.winnings = []
        self.losses   = []

    def placeBets(self):
        betToPlace = Bet(self.BET_AMOUNT, self.black)
        self.table.placeBet(betToPlace)

    def win(self, bet):
        self.winnings.append(bet.winAmount())

    def lose(self, bet):
        self.losses.append(bet.loseAmount())
