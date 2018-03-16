from binClass import Bin
from outcomeClass import Outcome
import unittest

class OutcomeTests(unittest.TestCase):
    def setUp(self):
        self.outcome1 = Outcome("asdf", 2)
        self.outcome2 = Outcome("asdf", 2)
        self.outcome3 = Outcome("asdfh", 2)
        self.outcome4 = Outcome("asdfj", 3)
        self.bin1 = Bin(self.outcome1)
        self.bin2 = Bin(self.outcome1, self.outcome2)
        self.bin3 = Bin(self.outcome1, self.outcome3)

    def testEquality(self):
        """
        this currently fails as we do not have equality operator defined
        and the hashes of the objects are different
        """
        self.assertEqual(self.bin1, self.bin2, "Unequal bins with the same outcome repeated")
    def testNonEquality(self):
        self.assertNotEqual(self.bin1, self.bin3, "Equal bins with different outcomes")
