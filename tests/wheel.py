from roulette.bin import Bin
from roulette.outcome import Outcome
from roulette.wheel import Wheel
from roulette.nonRandom import NonRandom
import unittest

class WheelTests(unittest.TestCase):

    def setUp(self):
        self.outcome1 = Outcome("Red", 2)
        self.outcome2 = Outcome("Red", 2)
        self.outcome3 = Outcome("Black", 2)
        self.outcome4 = Outcome("Black", 3)

        self.bin1 = Bin(self.outcome1)
        self.bin2 = Bin(self.outcome1, self.outcome2)
        self.bin3 = Bin(self.outcome1, self.outcome3)

    def testNonRandomCreation(self):
        self.nonrandomOne = NonRandom()
        self.nonrandomOne.setSeed(1)
        self.nonrandomTwo = NonRandom()
        self.nonrandomTwo.setSeed(2)

    def testWheelCreation(self):
        self.testNonRandomCreation()
        self.wheelOne = Wheel(self.nonrandomOne)
        self.wheelTwo = Wheel(self.nonrandomTwo)

    def testBinModification(self):
        self.testWheelCreation();
        self.wheelOne.addOutcome(1, self.outcome1)
        self.assertEqual(self.wheelOne.next(), self.wheelOne.get(1),
                "Wheel returned different bin")
