from roulette.bet import Bet

class Player:

    __slots__    = ['stake', 'roundsToGo', 'table']
    STAKE_AMOUNT = 100
    DEFAULT_ROUNDS_TO_GO = 100

    def __init__(self, table):

        self.table = table
        self.stake = self.STAKE_AMOUNT
        self.roundsToGo = self.DEFAULT_ROUNDS_TO_GO

    def isPlaying(self):
        return self.stake > 0 and self.roundsToGo > 0

    def placeBets(self):
        self.roundsToGo -= 1

    def win(self, bet):
        wonAmount = bet.winAmount()
        self.stake += wonAmount

    def lose(self, bet):
        pass

    def setStake(self, stake):
        self.stake = stake

    def setRounds(self, rounds):
        self.roundsToGo = rounds


class Passenger57(Player):

    BET_AMOUNT = 10

    def __init__(self, table):
        super().__init__(table)
        self.table = table
        self.black = self.table.wheel.getOutcome("Black")
        self.winnings = []
        self.losses   = []

    def placeBets(self):
        super().placeBets()
        betToPlace = Bet(self.BET_AMOUNT, self.black)
        self.table.placeBet(betToPlace)

    def win(self, bet):
        super().win(bet)
        self.winnings.append(bet.winAmount())

    def lose(self, bet):
        super().lose(bet)
        self.losses.append(bet.loseAmount())

class Martingale(Player):

    def __init__(self, table):
        super().__init__(table)
        self.lossCount   = 0
        self.betMultiple = 1
        self.initialBet   = 2

    def placeBets(self):
        "Ideally the black should not be hardcoded but taken from some variable"
        super().placeBets()
        betAmount = self.initialBet * self.betMultiple
        self.stake -= betAmount
        blackOutcome = self.table.wheel.getOutcome("Black")
        blackBet = Bet(betAmount, blackOutcome)
        self.table.placeBet(blackBet)

    def _resetLossCount(self):
        self.lossCount = 0

    def _increaseLossCount(self):
        self.lossCount += 1

    def _doubleBetMultiple(self):
        self.betMultiple *= 2

    def win(self, bet):
        super().win(bet)
        self._resetLossCount()

    def lose(self, bet):
        super().lose(bet)
        self._increaseLossCount()
        self._doubleBetMultiple()
