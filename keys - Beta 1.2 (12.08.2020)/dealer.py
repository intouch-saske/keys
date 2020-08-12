from random import randint
from random import choice
from card import Card


class Dealer:

    def __init__(self):
        self._deck_cards = []
        self._ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
        self._suits = ['♥', '♦', '♣', '♠']
        for i in self._ranks:
            for j in self._suits:
                self._deck_cards.append(Card(i, j))
        self._scoreboard = []

    def distribution_of_cards(self, amount):
        out_list = []
        for i in range(amount):
            elment = choice(self._deck_cards)
            out_list.append(elment)
            self._deck_cards.remove(elment)
        return out_list

    def old_comparator_cards(self, player1, player2):
        self._scoreboard = []
        player1_cards = player1.get_player_cards()
        player2_cards = player2.get_player_cards()

        player1_cards_list = []
        player2_cards_list = []
        for i in range(0, 5):
            for j in range(0, 13):
                if self._ranks[j] == player1_cards[i].get_rank():
                    player1_cards_list.append(j)
                if self._ranks[j] == player2_cards[i].get_rank():
                    player2_cards_list.append(j)

        for i in range(0, 5):
            if player1_cards_list[i] > player2_cards_list[i]:
                self._scoreboard.append("player1")
            elif player1_cards_list[i] < player2_cards_list[i]:
                self._scoreboard.append("player2")
            else:
                self._scoreboard.append('equally')

    def comparator_cards(self, player1, player2):
        self._scoreboard = []
        player1_cards = player1.get_player_cards()
        player2_cards = player2.get_player_cards()

        for i in range(0, 5):
            if int(player1_cards[i].get_rank()) > int(player2_cards[i].get_rank()):
                self._scoreboard.append("player1")
            elif int(player1_cards[i].get_rank()) < int(player2_cards[i].get_rank()):
                self._scoreboard.append("player2")
            else:
                self._scoreboard.append('equally')

        return self._scoreboard
