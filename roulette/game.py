class RouletteGame(object):

    def __init__(self, wheel, table):
        self.wheel = wheel
        self.table = table

    def _isPlayerPlaying(self, player):
        return player.isPlaying()

    def cycle(self, player):
        if self._isPlayerPlaying(player):
            player.placeBets()

        winningBin = self.wheel.next()

        for bet in self.table:
            if bet.outcome in winningBin.outcomes:
                player.win(bet)
            else:
                player.lose(bet)
            self.table.bets.remove(bet)
