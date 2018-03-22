class Passenger57(object):

    """Docstring for Passenger57. """
    __slots__ = ['black', 'table']
    def __init__(self, table, wheel):
        """TODO: to be defined1. """
        self.wheel = wheel
        self.table = table
        self.black = self.wheel.getOutcome("Black")

    def placeBets(self):

        
