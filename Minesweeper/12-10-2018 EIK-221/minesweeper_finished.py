import random


class Minesweeper:

    def __init__(self, rows, columns):
        self.mark_count = 0
        self.rows = rows
        self.columns = columns
        self.mine_count = 4

        self.user_view = self.blank_map("-")
        self.gamemap = self.create_map()
        self.pointer_coords = [0, 0]
        self.game()

    def game(self):

        while True:
            self.print_map()
            print()
            move = input()

            handled = self.handle_input(move)

            if handled is None:
                continue
            elif not handled:
                print("You've lost!")
            else:
                print("You've won!")
            self.print_map()
            break

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
        # koledasti kirjutatud "" kood, järgmine kord võiks juba eelnevalt arvestada rekursiivsuse lisamisega
        elif move == "":
            cell = self.gamemap[pointer_row][pointer_col]

            if cell == " ":
                self.open_all_empty_cells(pointer_row, pointer_col)

            if cell == "*":
                self.user_view = self.gamemap
                return False
            else:
                self.user_view[pointer_row][pointer_col] = self.gamemap[pointer_row][pointer_col]
        elif move == "e":
            cell = self.user_view[pointer_row][pointer_col]
            if cell != "=" and not cell.isdigit() and cell != " ":
                self.user_view[pointer_row][pointer_col] = "="
                self.mark_count += 1
            elif cell == "=":
                self.user_view[pointer_row][pointer_col] = "-"
                self.mark_count -= 1

        if self.mark_count == self.mine_count and self.equal_maps():
            self.user_view = self.gamemap
            return True

        if self.in_bounds(pointer_row, pointer_col):
            self.pointer_coords = pointer_row, pointer_col

    def equal_maps(self):
        view_copy = []

        for row in self.user_view:
            row_copy = []
            for cell in row:
                row_copy.append(cell if cell != "=" else "*")
            view_copy.append(row_copy)
        our_boolean = view_copy == self.gamemap
        return our_boolean

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
            if (mine_row, mine_col) not in mine_coords:
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

        for i, row in enumerate(self.user_view):

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

    def open_all_empty_cells(self, row, col):
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                adjacent_row = row + i
                adjacent_col = col + j

                if not self.in_bounds(adjacent_row, adjacent_col):
                    continue
                if self.user_view[adjacent_row][adjacent_col] == "-" and self.gamemap[adjacent_row][adjacent_col] == " ":
                    self.user_view[adjacent_row][adjacent_col] = " "
                    self.open_all_empty_cells(adjacent_row, adjacent_col)

if __name__ == "__main__":
    sweeper = Minesweeper(4, 10)
