import os
import random


class Minesweeper:

    def __init__(self, rows, columns):

        self.rows = rows
        self.columns = columns
        self.mine_count = 4
        self.pointer_coords = [0, 0]
        self.mark_count = 0

        self.user_view = self.blank_map("-")
        self.game_map = self.create_map()
        self.game()

    def game(self):

        while True:
            self.print_map()

            handled = self.handle_input(input())

            if handled:
                self.print_map()
                print("You have won!")
                break
            elif handled is None:
                continue
            else:
                self.print_map()
                print("You've lost!")
                break

    def handle_input(self, given):

        pointer_row, pointer_col = self.pointer_coords[:]

        if given == "w":
            pointer_row -= 1
        elif given == "s":
            pointer_row += 1
        elif given == "a":
            pointer_col -= 1
        elif given == "d":
            pointer_col += 1
        elif given == "":
            cell = self.game_map[pointer_row][pointer_col]
            if cell != "*":
                self.user_view[pointer_row][pointer_col] = cell
            else:
                self.user_view = self.game_map
                return False
        elif given == "e":
            cell = self.user_view[pointer_row][pointer_col]
            if cell != "=" and not cell.isdigit() and cell != " ":
                self.user_view[pointer_row][pointer_col] = "="
                self.mark_count += 1
            elif cell == "=":
                self.user_view[pointer_row][pointer_col] = "-"
                self.mark_count -= 1
            if self.mark_count == self.mine_count and self.equal_maps():
                self.user_view = self.game_map
                return True

        if self.are_in_bounds((pointer_row, pointer_col)):
            self.pointer_coords = pointer_row, pointer_col
        else:
            print("Wrong entry.")

    def equal_maps(self):
        view_copy = []

        for row in self.user_view:
            copy_row = []
            for cell in row:
                copy_row.append(cell if cell != "=" else "*")
            view_copy.append(copy_row)

        return view_copy == self.game_map




    def are_in_bounds(self, coords):
        return 0 <= coords[0] < self.rows and 0 <= coords[1] < self.columns

    def blank_map(self, char):
        blank_map = []

        for row in range(self.rows):

            # Make row_list to hold all fields
            row_list = []
            for col in range(self.columns):

                # Append one field to row_list
                row_list.append(char)

            # Append row to blank_map
            blank_map.append(row_list)
        return blank_map

    def create_map(self):

        gamefield = self.blank_map(" ")

        for mine in self.get_mine_coords():
            mine_row, mine_col = mine

            gamefield[mine_row][mine_col] = "*"

            for row_diff in [-1, 0, 1]:
                for col_diff in [-1, 0, 1]:

                    adjacent_row = mine_row + row_diff
                    adjacent_col = mine_col + col_diff

                    if not self.are_in_bounds((adjacent_row, adjacent_col)):
                        continue

                    cell = gamefield[adjacent_row][adjacent_col]

                    if cell == " ":
                        gamefield[adjacent_row][adjacent_col] = "1"
                    elif cell.isdigit():
                        gamefield[adjacent_row][adjacent_col] = str(int(cell) + 1)
        return gamefield

    def get_mine_coords(self):

        mine_coords = []

        while len(mine_coords) < self.mine_count:
            mine_row = random.randint(0, self.rows - 1)
            mine_col = random.randint(0, self.columns - 1)
            mine_coord = mine_row, mine_col

            if mine_coord not in mine_coords:
                mine_coords.append(mine_coord)

        return mine_coords

    def print_map(self):

        for i, row_list in enumerate(self.user_view):

            pointer_row, pointer_col = self.pointer_coords

            # <->

            if i == pointer_row:

                row = []

                for j, cell in enumerate(row_list):

                    if j == pointer_col:
                        row.append(f"<{cell}>")
                    else:
                        row.append(f" {cell} ")
                print("".join(row))

            else:
                print(" " + "  ".join(row_list) + " ")


if __name__ == "__main__":
    sweeper = Minesweeper(1, 4)

