class Outcome():

    """Docstring for MyClass. """

    __slots__ = ['name', 'odds']

    def __init__(self, name: str, odds: int):
        self.name = name
        self.odds = odds

    """Class Methods"""

    def __eq__(self, other):
        """
        :returns: True if this name matches the other name
        """
        return( self.__class__ == other.__class__ and
                self.name == other.name
        )

    def __ne__(self, other):
        """
        :returns: True if this name does not match the other name
        """
        return(
                self.__class__ != other.__class__ or 
                self.name != other.name
        )

    def __hash__(self):
        """TODO: Docstring for __hash__.
        :returns: hash of name field

        """
        return(hash(self.name))

    def __repr__(self):
        """
        :returns: Formatted string with name and odds
        """
        return "{0} ({1}:1)".format(self.name, self.odds)

    def winAmount(self, amount):
       """
       :amount: Integer value of bet amount.
       :returns: Numeric value of win amount. 
       """
       return(self.odds * amount)


