class Board:
    def __init__(self):
        self.cols = []
        for _ in range(7):
            self.cols.append([])
    
    def __repr__(self) -> str:
        return str(self.cols)

    def display(self):
        max_len = len(max(self.cols, key=len))
        board_str = " a  |  b  |  c  |  d  |  e  |  f  |  g  |\n"
        board_str += "----|-----|-----|-----|-----|-----|-----|\n"
        for i in range(max_len):
            line = ""
            for col in self.cols:
                if i < len(col):
                    line +=  col[i].get_display() + " | "
                else:
                    line += "   " + " | "
            board_str += line + "\n"
        print(board_str)
    
    def deal(self, deck: list):
        for i in range(7):
            for j in range(i+1):
                card = deck.pop()
                if j == i:
                    card.turn_over()
                self.cols[i].append(card)

    def get_column_by_letter(self, letter):
        index = "abcdefg".find(letter)
        return self.cols[index]
    
    def move(self, from_col, dest_col):
        # DESTINATION COLUMN
        dest_col = self.get_column_by_letter(dest_col)
        dest_card = None
        if len(dest_col) != 0:
            dest_card = dest_col[-1]
            # TODO: check dest_card to get correct amount of card from the other column

        # FROM COLUMN
        from_col = self.get_column_by_letter(from_col)
        to_move_list = []
        for card in from_col:
            if not card.face_up: # facing down
                continue
            to_move_list.append(card)

        for card in to_move_list:
            from_col.remove(card)
            dest_col.append(card)
        if len(from_col) > 0:
            from_col[-1].turn_over()

