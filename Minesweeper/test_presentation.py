import random


class Minesweeper:

    def __init__(self, rows, columns):

        self.rows = rows
        self.columns = columns
        self.mine_count = 4
        self.pointer_coords = [0, 0]
        self.mark_count = 0  # how many potential mines the player has marked

        self.user_view = self.blank_map("-")  # creating a map shown to the user
        self.game_map = self.create_map()  # creating a map with all game data
        self.game()  # calling the game() function as part of creating an instance of this class

    def game(self):

        while True:
            # printing a map to the user before every move
            self.print_map()

            # handling the move based on user input
            handled = self.handle_input(input())

            # checks if a winning or losing condition has been met
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

        # saving the coords into separate variables - basically the same as:
        # pointer_row = self.pointer_coords[0]
        # pointer_col = self.pointer_coords[1]
        pointer_row, pointer_col = self.pointer_coords[:]

        # finding the new pointer coords based on user direction
        if given == "w":
            pointer_row -= 1
        elif given == "s":
            pointer_row += 1
        elif given == "a":
            pointer_col -= 1
        elif given == "d":
            pointer_col += 1
        # clicking on the cell where the pointer is
        elif given == "":
            cell = self.game_map[pointer_row][pointer_col]
            # if the cell is not a mine
            if cell != "*":
                self.user_view[pointer_row][pointer_col] = cell
            # else the cell is a mine; return false to indicate losing
            else:
                self.user_view = self.game_map
                return False
        # let user mark a cell as a location of a potential mine, mark that cell with '='
        elif given == "e":
            cell = self.user_view[pointer_row][pointer_col]
            if cell != "=" and not cell.isdigit() and cell != " ":
                self.user_view[pointer_row][pointer_col] = "="
                self.mark_count += 1
            elif cell == "=":
                self.user_view[pointer_row][pointer_col] = "-"
                self.mark_count -= 1

        # check if all the mines have been marked correctly and other fields have been revealed
        if self.mark_count == self.mine_count and self.equal_maps():
            self.user_view = self.game_map
            # return True to indicate winning
            return True

        # if the user inputted a direction key, check if the new pointer coords were on the game field
        if self.are_in_bounds((pointer_row, pointer_col)):
            self.pointer_coords = pointer_row, pointer_col
        else:
            print("Wrong entry.")

    def equal_maps(self):
        """
        Check if view_copy and game_map are considered equal.

        view_copy is the same as game_map if the mines have been marked and everything else is revealed.
        :return:
        """
        view_copy = []

        for row in self.user_view:
            copy_row = []
            for cell in row:
                copy_row.append(cell if cell != "=" else "*")
            view_copy.append(copy_row)

        return view_copy == self.game_map

    def are_in_bounds(self, coords):
        """
        Check if the coords are on the game field.

        :param coords:
        :return:
        """
        return 0 <= coords[0] < self.rows and 0 <= coords[1] < self.columns

    def blank_map(self, char):
        """
        Return a blank map with the instance's dimensions:

        :param char:
        :return:
        """
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
        """
        Create a map filled with game data.

        :return:
        """

        # create an empty template
        gamefield = self.blank_map(" ")

        # place the mines in the template and calculate the adjacent cell numbers
        # for each mine there is in all mine coords
        for mine in self.get_mine_coords():
            mine_row, mine_col = mine

            # mark the mine with '*'
            gamefield[mine_row][mine_col] = "*"

            # check each adjacent cell to correct their mine count
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
        """
        Get random placement for all mines.

        :return: list of all mine coords
        """

        mine_coords = []

        # while there are fewer mine coordinates than mines, add more coordinates
        while len(mine_coords) < self.mine_count:
            mine_row = random.randint(0, self.rows - 1)
            mine_col = random.randint(0, self.columns - 1)
            mine_coord = mine_row, mine_col

            if mine_coord not in mine_coords:
                mine_coords.append(mine_coord)

        return mine_coords

    def print_map(self):
        """
        Print the user_view ~aesthetically~ and show the pointer on it.

        :return:
        """

        for i, row_list in enumerate(self.user_view):  # https://docs.python.org/3/library/functions.html#enumerate

            pointer_row, pointer_col = self.pointer_coords

            # how we want our pointer look when it's surrounding a cell:
            # <->

            # the row with the pointer has to be printed a little differently
            if i == pointer_row:

                row = []

                for j, cell in enumerate(row_list):

                    if j == pointer_col:
                        row.append(f"<{cell}>")
                    else:
                        row.append(f" {cell} ")
                print("".join(row))
            # print the normal row
            else:
                print(" " + "  ".join(row_list) + " ")

# https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    sweeper = Minesweeper(4, 5)
