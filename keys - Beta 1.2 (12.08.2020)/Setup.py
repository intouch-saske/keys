import sys
import os
import xml.etree.ElementTree as xml
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
values = []
i = 1
v = 3
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
            object_name.setText(f"J{card.get_suit()}")
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
    is_valid('auto')

    ui.nex_lvl.setEnabled(False)
    ui.is_valid.setEnabled(True)
    ui.check.setEnabled(True)
    ui.p1.setEnabled(True)
    ui.p2.setEnabled(True)
    ui.p3.setEnabled(True)
    ui.p4.setEnabled(True)
    ui.p5.setEnabled(True)


def edit_serial_card(a, b):
    '''Change the order of the cards'''
    global player
    global d
    player.player_cards[a], player.player_cards[b] = player.player_cards[b], player.player_cards[a]
    update_card()


def is_valid(mode="user"):
    global c
    global v
    '''Check wins in round'''
    if mode == "user":
        if v > 0:
            v -= 1
        else:
            return 0
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
    ui.edit_num.setText(str(v))


def check():
    global c
    global v
    global i
    '''Choice winner'''
    win = 0
    is_valid('auto')
    if c.count('+') > c.count('-'):
        ui.who_win.setText("You win!")
        win += 1
        i += 1
    elif c.count('+') < c.count('-'):
        ui.who_win.setText("Bot win!")
        i = 1
    else:
        ui.who_win.setText("Nobody win!")
    update_card_bot()

    ui.is_valid.setEnabled(False)
    ui.check.setEnabled(False)
    ui.nex_lvl.setEnabled(True)
    # set export/import
    ui.p1.setEnabled(False)
    ui.p2.setEnabled(False)
    ui.p3.setEnabled(False)
    ui.p4.setEnabled(False)
    ui.p5.setEnabled(False)
    if v <= 3 and win == 1:
        v += 3
    else:
        v = 3


def exp_imp(x):
    global values
    global player
    if len(values) == 0:
        values.append(x)
    elif len(values) == 1:
        values.append(x)
        player.player_cards[values[0]], player.player_cards[values[1]] = player.player_cards[values[1]], \
                                                                         player.player_cards[values[0]]
        update_card()
    else:
        values = []
        exp_imp(x)


def next_lvl():
    global i
    new_game()
    ui.lvl_num.setText(str(i))


def reference():
    os.startfile('Как играть.txt')


def about_program():
    os.startfile('Что нового.txt')

# mods


def lm():
    global Dialog
    Dialog.setStyleSheet("background-color: #606060; color: #ffa550;")
    update_card()
    is_valid()


def nm():
    global Dialog
    Dialog.setStyleSheet("background-color: #303030; color: #ffa550;")
    update_card()
    is_valid()


def bm():
    global Dialog
    Dialog.setStyleSheet("background-color: #101010; color: #ffa550;")
    оbjects = [ui.b1, ui.b2, ui.b3, ui.b4, ui.b5, ui.p1, ui.p2, ui.p3, ui.p4, ui.p5,
               ui.r1, ui.r2, ui.r3, ui.r4, ui.r5]

    for object_name in оbjects:
        object_name.setStyleSheet("")


def rus():
    pass


def eng():
    pass


def inf_val():
    global v
    v = 1000


def open_file():
    pass


def save_file(is_as=False):
    global v
    global i
    root = xml.Element("game")

    valid = xml.SubElement(root, "valid")
    valid.text = v

    level = xml.SubElement(root, "level")
    level.text = i

    tree = xml.ElementTree(root)
    with open('filename.xml', "w") as fh:
        tree.write(fh)


# set usually func
ui.nex_lvl.clicked.connect(next_lvl)
ui.is_valid.clicked.connect(lambda: is_valid('user'))
ui.check.clicked.connect(check)

# set func on action
ui.actionSave.triggered.connect(save_file)
ui.actionInfinity_valid.triggered.connect(inf_val)
ui.actionReferense.triggered.connect(reference)
ui.actionAbout_program.triggered.connect(about_program)
ui.actionLight_mode.triggered.connect(lm)
ui.actionNight_mode.triggered.connect(nm)
ui.actionBlack_mode.triggered.connect(bm)
ui.actionNewGame.triggered.connect(new_game)
ui.actionExit.triggered.connect(exit)
# set export/import
ui.p1.clicked.connect(lambda: exp_imp(0))
ui.p2.clicked.connect(lambda: exp_imp(1))
ui.p3.clicked.connect(lambda: exp_imp(2))
ui.p4.clicked.connect(lambda: exp_imp(3))
ui.p5.clicked.connect(lambda: exp_imp(4))
# Main loop
new_game()
sys.exit((app.exec_()))
