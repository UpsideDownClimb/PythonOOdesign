from outcomeClass import Outcome

class BinBuilder(object):

    """Docstring for BinBuilder. """

    STRAIGHT_VALUE = 35
    SPLIT_VALUE    = 17
    STREET_VALUE   = 11
    CORNER_VALUE   = 8
    LINE_VALUE     = 5
    DOZEN_VALUE    = 2
    COLUMN_VALUE   = 2
    EVEN_VALUE     = 1

    def __init__(self):
        """TODO: to be defined1. """

    def buildBins(self, wheel):
        """
        :wheel: Wheel class to build bins for
        """
        self.wheel = wheel
        self._addStraightBets()
        self._addSplitBets()
        self._addStreetBets()
        self._addCornerBets()
        self._addLineBets()
        self._addDozenBets()
        self._addColumnBets()
        self._addEvenBets()

    def _addStraightBets(self):
        for binIndex in range(37):
            self.wheel.addOutcome(binIndex, Outcome(str(binIndex), self.STRAIGHT_VALUE))

        self.wheel.addOutcome(37, Outcome('00', self.STRAIGHT_VALUE))

    def _createOutputName(*args):
        return(', '.join(str(x) for x in args))

    def _addToWheel(self, binIndex, betValue, *offsets):
        positions = [binIndex] + [binIndex + i for i in offsets]
        splitName = self._createOutputName(*positions)

        for binIndex in positions:
            self.wheel.addOutcome(binIndex, Outcome(splitName, betValue))

    def _addSplitBets(self):
        "This could be replaced with itertools.chain"
        twoColumns = list(range(1, 37, 3)) + list(range(2, 37, 3))
        elevenRows = range(1, 33)

        for binIndex in twoColumns:
            self._addToWheel(binIndex, self.SPLIT_VALUE, 1)
        for binIndex in elevenRows:
            self._addToWheel(binIndex, self.SPLIT_VALUE, 3)

    def _addStreetBets(self):
        firstColumn = range(1, 37, 3)

        for binIndex in firstColumn:
            self._addToWheel(binIndex, self.STREET_VALUE, 1, 2)

    def _addCornerBets(self):
        twoColumns  = list(range(1, 34, 3)) + list(range(2, 34, 3))

        for binIndex in twoColumns:
            self._addToWheel(binIndex, self.CORNER_VALUE, 1, 3, 4)

    def _addLineBets(self):
        twoColumns  = range(1, 34, 3)

        for binIndex in twoColumns:
            self._addToWheel(binIndex, self.LINE_VALUE, 1, 2, 3, 4, 5)

    def _addDozenBets(self):
        for dozen in range(1, 3):
            outcomeName = str(dozen) + '-' + str(dozen*12)
            outcome = Outcome(outcomeName, self.DOZEN_VALUE)
            offset = 12 * (dozen - 1)
            for binIndex in range(12):
                self.wheel.addOutcome(binIndex + offset, outcome)

    def _addColumnBets(self):
        for column in range(1, 3):
            outcomeName = 'Column ' + str(column)
            outcome = Outcome(outcomeName, self.COLUMN_VALUE)

            for row in range(12):
                binIndex = 3 * row + column
                self.wheel.addOutcome(binIndex, outcome)

    def _addEvenBets(self):
        value = self.EVEN_VALUE
        redIndexes = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        blackIndexes = (x for x in range(1,37) if x not in redIndexes)
        rangesDict = {"Even":range(2, 37, 2),
                      "Odd":range(1, 37, 2),
                      "Low":range(1, 19),
                      "High":range(19, 37),
                      "Red":redIndexes,
                      "Black":blackIndexes}

        for outcomeName, outcomeRange in rangesDict.items():
            outcome = Outcome(outcomeName, value)
            for binIndex in outcomeRange:
                self.wheel.addOutcome(binIndex, outcome)
