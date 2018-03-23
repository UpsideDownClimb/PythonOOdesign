class RouletteGame(object):

    """Docstring for Game. """

    def __init__(self, wheel, table):
        """TODO: to be defined1. """
        self.wheel = wheel
        self.table = table

    def cycle(self, player):
        """TODO: Docstring for cycle.
        :returns: TODO

        """
        player.placeBets()
        winningBin = self.wheel.next()
        for bet in self.table:
            if bet.outcome in winningBin.outcomes:
                player.win(bet)
            else:
                player.lose(bet)
            self.table.bets.remove(bet)
