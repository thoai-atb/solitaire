import random
from card import *
from board import *
from colorist import Color

def get_deck():
    '''Return 52 cards shuffled'''
    suits = ["♠️", "♥️", "♣️", "♦️"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck =  []
    for suit in suits:
        for value in values:
            card = Card(suit, value)
            deck.append(card)
    random.shuffle(deck)
    return deck

deck = get_deck()
board = Board()
board.deal(deck)
board.display()

while True:
    move = "".join(input("Input move: ").split())
    if move == "exit":
        break
    if len(move) != 2:
        print(f"{Color.RED}Wrong input! Please input again...{Color.OFF}")
        continue
    from_col = move[0]
    to_col = move[1]
    if from_col not in "abcdefg":
        print(f"{Color.RED}Wrong first column! Please input again...{Color.OFF}")
        continue
    if to_col not in "abcdefg":
        print(f"{Color.RED}Wrong second column! Please input again...{Color.OFF}")
        continue
    if from_col == to_col:
        print(f"{Color.RED}Columns cannot be the same! Please input again...{Color.OFF}")
        continue
    board.move(from_col, to_col)
    board.display()