class Simulator(object):

    def __init__(self, player, game):

        self.initDuration = 250
        self.initStake = 100
        self.samples = 50
        self.durations = list()
        self.maxima = list()
        self.playerClass = player
        self.game = game

    def _createPlayer(self, duration, stake):
        tableToPlayOn = self.game.table
        player = self.playerClass(tableToPlayOn)
        player.setRounds(duration)
        player.setStake(stake)
        return player

    def session(self):
        stakes = list()
        player = self._createPlayer(self.initDuration, self.initStake)
        while player.isPlaying():
            self.game.cycle(player)
            stakes.append(player.stake)
        return stakes

    def gather(self):
        for _ in range(self.samples):
            sessionResult = self.session()
            self.maxima.append(max(sessionResult))
            self.durations.append(len(sessionResult))


