from colorist import Color

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.face_up = False

    def turn_over(self):
        self.face_up = not self.face_up

    def get_display(self):
        '''Get string representation when displayed on board'''
        if not self.face_up:
            return f"{Color.CYAN}XXX{Color.OFF}"
        color = Color.WHITE
        if self.suit in ["♦️", "♥️"]:
            color = Color.RED
        return f"{color}{self.value}{self.suit}{Color.OFF}".rjust(13, " ")
    
    def __repr__(self) -> str:
        '''Get string representation when debugging'''
        color = Color.WHITE
        if self.suit in ["♦️", "♥️"]:
            color = Color.RED
        return f"{color}{self.value}{self.suit}{Color.OFF}"