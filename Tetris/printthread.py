import threading
import time


class PrintThread(threading.Thread):
    """"""

    def __init__(self, world_map, threadlock):
        threading.Thread.__init__(self)
        self.world_map = world_map
        self.maplock = threadlock

    def run(self):
        print("Starting" + self.name)
        while True:
            self.print_map()
            time.sleep(1)

    def print_map(self):
        """Create map of game with squares."""
        for row in self.world_map:
            for cell in row:
                print(cell, end="")
            print()
