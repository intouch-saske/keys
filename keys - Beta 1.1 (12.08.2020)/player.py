class Player:

    def __init__(self):
        self.player_cards = []
        self._scoreboard = 0

    def add_cards(self, player_cards):
        self.player_cards = player_cards

    def get_player_cards(self):
        return self.player_cards
