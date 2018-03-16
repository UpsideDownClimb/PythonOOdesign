class Outcome():

    """Docstring for MyClass. """

    __slots__ = ['name', 'odds']

    def __init__(self, name, odds):
        """TODO: to be defined1. """
        self.name = name
        self.odds = odds
    """Class Methods"""

    def winAmount(self, amount):
        return(self.odds * amount)

    def __eq__(self, other):
        """TODO: Docstring for __eq__.
        :returns: True if this name matches the other name
        """
        return(self.name == other.name)

    def __ne__(self, other):
        """TODO: Docstring for __ne__.

        :returns: True if this name does not match the other name

        """
        return(self.name != other.name)

    def __str__(self):
        """TODO: Docstring for __str__.
        :returns: TODO

        """
        return "%s (%d:1)" % ( self.name, self.odds )
