import random


class Shuffler:
    """
    Defines a Shuffler class which will be used to shuffle the elements of a tuple.
    """

    def __init__(self, tuple1):
        self.tuple1 = tuple1

    def randomize_tuple(self):
        """creates a random list from the elements of the tuple and casts it back to tuple."""
        return tuple(random.sample(self.tuple1, len(self.tuple1)))
