"""A game of Tetris."""
import os
import time
from pynput.keyboard import Listener, Key


class Tetris:

    def __init__(self, shape_list, height, width):

        self.shapes = shape_list
        self.height = height
        self.width = width
        self.flatten = lambda l: [item for sublist in l for item in sublist]
        self.game()

    def game(self):

        with Listener(
            on_press=Tetris.on_press,
            on_release=Tetris.on_release
        ) as listener:
            listener.join()

        while True:
            self.print_map()
            time.sleep(0.5)
            self.move_all_down()

    def on_press(key):
        print('{0} pressed'.format(
            key))

    def on_release(key):
        print('{0} release'.format(
            key))
        if key == Key.esc:
            # Stop listener
            return False

    def print_map(self):
        """Create map of game with squares."""
        startend = (self.width + 4) * "-"
        line_list = []
        for x in range(self.height)[::-1]:
            line = ""
            for y in range(self.width):
                if (x, y) in self.flatten(self.shapes):
                    line += "X"
                else:
                    line += "_"
            line_list.append(line)

        print(startend)
        print("\n".join(line_list))
        print()
        print(startend)


    def move_all_down(self):
        """Moves down the required shapes."""
        for shape in self.shapes:
            if self.for_loop(shape):
                self.move_shape_down(shape)

    def for_loop(self, shape):
        """FORLOOPDURH."""
        for block in shape:
            test = (block[0] - 1, block[1])
            if test in shape:
                continue
            else:
                if test in self.flatten(self.shapes) or test[0] < 0:
                    return False
        return True

    def move_shape_down(self, shape_list):
        """Moves the blocks down by 1."""
        for i, coords in enumerate(shape_list):
            shape_list[i] = (coords[0] - 1, coords[1])




if __name__ == '__main__':
    h = Tetris([[(8, 1), (8, 2), (8, 3), (8, 4)],
                       [(1, 1), (1, 2), (0, 1), (0, 2)]
                       ], 8, 10)


