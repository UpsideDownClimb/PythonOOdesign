class Bin(object):

    """Docstring for Bin class"""
    __slots__ = ['outcomes']
    def __init__(self, *outcomes):
        """TODO: to be defined. """
        self.outcomes = frozenset([outcomeElement for outcomeElement in outcomes])

    def __str__(self):
        return(', '.join(list(map(str, self.outcomes))))

    def add(self, outcome):
        """
        :outcome: An Outcome class object to be added to the set
        """
        self.outcomes |= set([outcome])
        
