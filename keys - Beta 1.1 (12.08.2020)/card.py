class Card:

    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def get_rank(self):
        return self._rank

    def get_suit(self):
        return self._suit

    def get_all(self):
        return str(self._rank) + str(self._suit)
