class Table(object):

    """Docstring for Table. """

    __slots__ = ['limit', 'minimum', 'bets']

    def __init__(self, minimum = 1, limit = 10000):
        """TODO: to be defined.

        :minimum: TODO
        :limit: TODO

        """
        self.minimum = minimum
        self.limit = limit
        self.bets = []

    def placeBet(self, bet):
        """TODO: Docstring for placeBet.
        :bet: Bet class to be added to the table
        """
        if self.isValid(bet):
            self.bets.append(bet)
        else:
            raise InvalidBet()

    def isValid(self, bet):
        """TODO: Docstring for isValid.
        :bet: TODO
        :returns: TODO
        """
        minimumCheck = bet.betAmount > self.minimum
        limitCheck   = sum(bet.betAmount for bet in self.bets) < self.limit
        return minimumCheck and limitCheck

    def __iter__(self):
        return bets[:]

    def __str__(self):
        """TODO: Docstring for __str__.
        :returns: TODO

        """
        initialLine = "Placed bets:\n"
        betsLines   = ('{0} placed on {1}'.format(bet.betAmount, bet.outcome) for bet in self.bets)
        return initialLine + '\n'.join(betsLines)

    def __repr__(self):
        return "Table(" + ", ".join(str(bet) for bet in self.bets) + ")"
