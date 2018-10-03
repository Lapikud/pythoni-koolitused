import os
import sys
from random import randint


class Minesweeper:

    def __init__(self):

        self.rows = 5
        self.columns = 6
        self.mine_count = 4

        self.game_field = self.create_map()
        self.user_view = self.get_blank_map()
        self.pointer = (0, 0)
        self.message = ""

        self.moves = {"w": (-1, 0),
                      "s": (1, 0),
                      "d": (0, 1),
                      "a": (0, -1)}

        self.game()

    def game(self):

        while True:
            os.system("clear")
            self.print_map()
            print(self.message)
            self.message = ""
            user_input = self.wait_for_key()
            pointer_content = self.game_field[self.pointer[0]][self.pointer[1]]

            if user_input in self.moves.keys():
                diff = self.moves[user_input]
                new_coords = (self.pointer[0] + diff[0], self.pointer[1] + diff[1])

                if self.are_in_bounds(new_coords):
                    self.pointer = new_coords
                else:
                    self.message = "Nowhere to go."

            elif user_input == " ":
                if pointer_content == "*":
                    self.user_view = self.game_field
                    os.system("clear")
                    break
                elif pointer_content == " ":
                    for coord in self.get_open_area_coords(self.game_field, self.pointer):
                        self.show_coord(coord)
                else:
                    self.show_coord(self.pointer)

            elif user_input == "e":
                # mark mine
                pass

            else:
                self.message = "Come again?"

    def show_coord(self, coord):
        coord_row, coord_col = coord
        self.user_view[coord_row][coord_col] = self.game_field[coord_row][coord_col]

    def are_in_bounds(self, coords):
        return 0 <= coords[0] < self.rows and 0 <= coords[1] < self.columns

    def create_map(self):

        field = []

        for i in range(self.rows):
            field.append([" " for j in range(self.columns)])

        for mine_coord in self.get_all_mine_coords():

            mine_row, mine_col = mine_coord
            field[mine_row][mine_col] = "*"

            for row_diff in [-1, 0, 1]:
                for col_diff in [-1, 0, 1]:

                    one_up_row = mine_row + row_diff
                    one_up_col = mine_col + col_diff
                    if not self.are_in_bounds((one_up_row, one_up_col)):
                        continue

                    cell = field[one_up_row][one_up_col]
                    if cell not in (" ", "*"):
                        field[one_up_row][one_up_col] += 1
                    elif cell == " ":
                        field[one_up_row][one_up_col] = 1
        return field

    def get_blank_map(self):
        return [['-' for j in range(self.columns)] for i in range(self.rows)]

    def get_open_area_coords(self, game_field, start_coord):
        start_row, start_col = start_coord

        start = game_field[start_row][start_col]

        if start != " ":
            raise Exception(f"Start coordinates {start_coord} are not open: expected ' ', got {start}")

        open_area_coords = {start_coord}
        self.get_open_area_coords_recursively(game_field, start_coord, open_area_coords)
        return open_area_coords

    def get_open_area_coords_recursively(self, game_field, cur_coords, coords_set):
        cur_coord_row, cur_coord_col = cur_coords

        for row_diff in (-1, 0, 1):
            for col_diff in (-1, 0, 1):
                coord = (cur_coord_row + row_diff, cur_coord_col + col_diff)

                if self.are_in_bounds(coord) and coord not in coords_set:

                    coord_row, coord_col = coord
                    if game_field[coord_row][coord_col] != " ":
                        coords_set.add(coord)
                    else:
                        coords_set.add(coord)
                        self.get_open_area_coords_recursively(game_field, coord, coords_set)

    def get_all_mine_coords(self):

        mine_coords = {0}
        mine_coords.clear()

        while len(mine_coords) < self.mine_count:
            mine_coord = (randint(0, self.rows - 1), randint(0, self.columns - 1))
            mine_coords.add(mine_coord)

        return mine_coords

    def print_map(self, debug=False):

        game_field = self.game_field if debug else self.user_view

        row_count = len(game_field)
        col_count = len(game_field[0])
        pointer_row, pointer_col = self.pointer

        if not pointer_row < row_count:
            raise Exception(f"Pointer out of bounds: field has {row_count} rows, pointer is at index {pointer_row}.")
        if not pointer_col < col_count:
            raise Exception(f"Pointer out of bounds: field has {col_count} columns, pointer is at index {pointer_col}.")

        for row_index, row in enumerate(game_field):

            row_elements = list(map(str, game_field[row_index]))

            if row_index == pointer_row and pointer_col != 0:
                print(f" {'  '.join(row_elements[:pointer_col])}" + \
                      f" <{row_elements[pointer_col]}> " + \
                      '  '.join(row_elements[pointer_col + 1:]))

            elif row_index == pointer_row and pointer_col == 0:
                print(f"<{row_elements[0]}> {'  '.join(row_elements[1:])}")

            else:
                print(f" {'  '.join(row_elements)}")

    def wait_for_key(self):
        ''' Wait for a key press on the console and return it. '''
        result = None
        if os.name == 'nt':
            import msvcrt
            result = msvcrt.getch()
        else:
            import termios
            fd = sys.stdin.fileno()

            oldterm = termios.tcgetattr(fd)
            newattr = termios.tcgetattr(fd)
            newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
            termios.tcsetattr(fd, termios.TCSANOW, newattr)

            try:
                result = sys.stdin.read(1)
            except IOError:
                pass
            finally:
                termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

        return result


"""
ANSI codes:
\003[im where i is:
5 blinking
1 bold
31 fg red
32 fg green
33 fg yellow
34 fg blue
35 fg violet
36 fg cyan
37 fg grey

40-47 same but bg
91-97 same but lighter
100-107 same but bg and lighter
"""

if __name__ == "__main__":
    field2 = [[" ", " ", "1"],
              [" ", "1", "1"],
              ["1", "1", "1"]]

    minesweeper = Minesweeper()
    minesweeper.print_map()


    # Row/columns error
    # print_map(field1, (5, 3))
    # print_map(field1, (4, 6))
