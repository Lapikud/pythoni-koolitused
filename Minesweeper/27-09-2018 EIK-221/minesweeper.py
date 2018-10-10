import random


class Minesweeper:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.mine_count = 4

        self.gamemap = self.create_map()
        self.pointer_coords = [0, 0]
        self.game()

    def game(self):

        while True:
            self.print_map()
            print()
            move = input()

            self.handle_input(move)

    def handle_input(self, move):

        pointer_row, pointer_col = self.pointer_coords

        if move == "w":
            pointer_row -= 1
        elif move == "s":
            pointer_row += 1
        elif move == "a":
            pointer_col -= 1
        elif move == "d":
            pointer_col += 1

        if self.in_bounds(pointer_row, pointer_col):
            self.pointer_coords = pointer_row, pointer_col

    def in_bounds(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.columns

    def create_map(self):
        gamefield = self.blank_map(" ")

        for mine_coord in self.get_mine_coords():
            mine_row, mine_col = mine_coord

            gamefield[mine_row][mine_col] = "*"

            for row_diff in [-1, 0, 1]:
                for col_diff in [-1, 0, 1]:

                    cell_row = mine_row + row_diff
                    cell_col = mine_col + col_diff

                    # the "not" wasn't on the board the last time!
                    if not self.in_bounds(cell_row, cell_col):
                        continue

                    cell = gamefield[cell_row][cell_col]

                    if cell == " ":
                        gamefield[cell_row][cell_col] = "1"
                    elif cell.isdigit() and len(cell) == 1:
                        gamefield[cell_row][cell_col] = str(int(cell) + 1)

        return gamefield

    def get_mine_coords(self):

        mine_coords = []

        while len(mine_coords) < self.mine_count:
            mine_row = random.randint(0, self.rows - 1)
            mine_col = random.randint(0, self.columns - 1)
            if (mine_row, mine_col) not in mine_coords:  # the condition wasn't added on the board the last time!
                mine_coords.append((mine_row, mine_col))

        return mine_coords

    def blank_map(self, character):

        gamemap = []

        for row in range(self.rows):
            row_list = []
            for column in range(self.columns):
                row_list.append(character)
            gamemap.append(row_list)
        return gamemap

    def print_map(self):

        pointer_row, pointer_col = self.pointer_coords

        for i, row in enumerate(self.gamemap):

            if i == pointer_row:

                row_string = []

                for j, cell in enumerate(row):
                    if j == pointer_col:
                        row_string.append(f"<{cell}>")
                    else:
                        row_string.append(f" {cell} ")
                print("".join(row_string))
            else:
                print(" " + "  ".join(row) + " ")

if __name__ == "__main__":
    sweeper = Minesweeper(4, 5)
    sweeper.print_map()
