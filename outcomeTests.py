from outcomeClass import Outcome
import unittest

class OutcomeTests(unittest.TestCase):
    def setUp(self):
        self.outcome1 = Outcome("asdf", 2)
        self.outcome2 = Outcome("asdf", 2)
        self.outcome3 = Outcome("asdfh", 2)
        self.outcome4 = Outcome("asdfj", 3)

    def testEquality(self):
        self.assertEqual(self.outcome1, self.outcome2, "Unequal outcomes with the same name")
    
    def testNonEquality(self):
        self.assertNotEqual(self.outcome1, self.outcome3, "Equal outcomes with the same name")
    def testEqualHash(self):
        self.assertEqual(self.outcome1, self.outcome2, "Unequal hashes of same name outcomes")
    def testUnequalHash(self):
        self.assertNotEqual(self.outcome1, self.outcome3, "Equal hashes of same name outcomes")


    def testWinAmount(self):
        self.assertEqual(self.outcome1.winAmount(10), 20, "Win amount wrong value")
