import sys
import time
from player import Player
from dealer import Dealer
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow

# Create app
app = QtWidgets.QApplication(sys.argv)

# init
Dialog = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(Dialog)
Dialog.show()

player = None
bot = None
d = None

a = None  # откуда карта
b = None  # куда карта
c = []  # кто победил


def update_card():
    '''Update UI card's'''
    global player
    i = 0
    objects = [ui.p1, ui.p2, ui.p3, ui.p4, ui.p5]
    for object_name in objects:
        card = player.get_player_cards()[i]
        if card.get_rank() == '11':
            object_name.setText(f"J{ card.get_suit() }")
        elif card.get_rank() == '12':
            object_name.setText(f"Q{card.get_suit()}")
        elif card.get_rank() == '13':
            object_name.setText(f"K{card.get_suit()}")
        elif card.get_rank() == '14':
            object_name.setText(f"A{card.get_suit()}")
        else:
            object_name.setText(card.get_all())
        if player.get_player_cards()[i].get_suit() == "♥":
            object_name.setStyleSheet("color: red;")
        elif player.get_player_cards()[i].get_suit() == "♦":
            object_name.setStyleSheet("color: red;")
        else:
            object_name.setStyleSheet("color: black;")
        i += 1


def update_card_bot():
    '''Update UI card's'''
    global bot
    i = 0
    objects = [ui.b1, ui.b2, ui.b4, ui.b3, ui.b5]
    for object_name in objects:
        card = bot.get_player_cards()[i]
        if card.get_rank() == '11':
            object_name.setText(f"J{card.get_suit()}")
        elif card.get_rank() == '12':
            object_name.setText(f"Q{card.get_suit()}")
        elif card.get_rank() == '13':
            object_name.setText(f"K{card.get_suit()}")
        elif card.get_rank() == '14':
            object_name.setText(f"A{card.get_suit()}")
        else:
            object_name.setText(card.get_all())

        if bot.get_player_cards()[i].get_suit() == "♥":
            object_name.setStyleSheet("color: red;")
        elif bot.get_player_cards()[i].get_suit() == "♦":
            object_name.setStyleSheet("color: red;")
        else:
            object_name.setStyleSheet("color: black;")
        i += 1


def null_card():
    objects = [ui.b1, ui.b2, ui.b3, ui.b4, ui.b5]
    for object_name in objects:
        object_name.setText("X")
        object_name.setStyleSheet("")
    ui.who_win.setText("")

# game play


def new_game():
    global player
    global bot
    global d
    player = Player()
    d = Dealer()
    player.add_cards(d.distribution_of_cards(5))
    bot = Player()
    bot.add_cards(d.distribution_of_cards(5))
    null_card()
    update_card()
    is_valid()

    ui.is_valid.setEnabled(True)
    ui.check.setEnabled(True)
    ui.e1.setEnabled(True)
    ui.e2.setEnabled(True)
    ui.e3.setEnabled(True)
    ui.e4.setEnabled(True)
    ui.e5.setEnabled(True)
    ui.i1.setEnabled(True)
    ui.i2.setEnabled(True)
    ui.i3.setEnabled(True)
    ui.i4.setEnabled(True)
    ui.i5.setEnabled(True)


def edit_serial_card():
    '''Change the order of the cards'''
    global player
    global d
    global a
    global b
    player.player_cards[a], player.player_cards[b] = player.player_cards[b], player.player_cards[a]
    update_card()


def is_valid():
    global c
    '''Check wins in round'''
    c = []
    scores = d.comparator_cards(player, bot)
    objects = [ui.r1, ui.r2, ui.r3, ui.r4, ui.r5]
    i = 0
    for object_name in objects:
        if scores[i] == "player1":
            object_name.setText("+")
            object_name.setStyleSheet("color: green;")
            c.append("+")
        elif scores[i] == "player2":
            object_name.setText("-")
            object_name.setStyleSheet("color: red;")
            c.append("-")
        else:
            object_name.setText("=")
            object_name.setStyleSheet("color: blue;")
            c.append("=")
        i += 1


def check():
    global c
    '''Choice winner'''
    is_valid()
    if c.count('+') > c.count('-'):
        ui.who_win.setText("You win!")
    elif c.count('+') < c.count('-'):
        ui.who_win.setText("Bot win!")
    else:
        ui.who_win.setText("Nobody win!")
    update_card_bot()

    ui.is_valid.setEnabled(False)
    ui.check.setEnabled(False)
    # set export/import
    ui.e1.setEnabled(False)
    ui.e2.setEnabled(False)
    ui.e3.setEnabled(False)
    ui.e4.setEnabled(False)
    ui.e5.setEnabled(False)
    ui.i1.setEnabled(False)
    ui.i2.setEnabled(False)
    ui.i3.setEnabled(False)
    ui.i4.setEnabled(False)
    ui.i5.setEnabled(False)


def active_1(x):
    global a
    a = x


def active_2(x):
    global b
    b = x
    edit_serial_card()


# set usually func
ui.new_game.clicked.connect(new_game)
ui.is_valid.clicked.connect(is_valid)
ui.check.clicked.connect(check)
# set export/import
ui.e1.clicked.connect(lambda: active_1(0))
ui.e2.clicked.connect(lambda: active_1(1))
ui.e3.clicked.connect(lambda: active_1(2))
ui.e4.clicked.connect(lambda: active_1(3))
ui.e5.clicked.connect(lambda: active_1(4))
ui.i1.clicked.connect(lambda: active_2(0))
ui.i2.clicked.connect(lambda: active_2(1))
ui.i3.clicked.connect(lambda: active_2(2))
ui.i4.clicked.connect(lambda: active_2(3))
ui.i5.clicked.connect(lambda: active_2(4))
# Main loop
new_game()
sys.exit(app.exec_())
