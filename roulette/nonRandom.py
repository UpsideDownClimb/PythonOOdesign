import random

class NonRandom(random.Random):
    __slots__ = ['value']

    def __init__(self):
        self.value = None

    def setSeed(self, seed):
        """TODO: Docstring for .
        :seed: Non-random value to be set
        """
        self.value = seed

    def choice(self, sequence):
        """TODO: Docstring for choice.
        :sequence: sequence type object
        :returns: Value at sequence index set by seed
        """
        return(sequence[self.value])
