"""Iz the dosctrings."""

import threading

from pynput.keyboard import Key, Listener


class Listeninthread(threading.Thread):
    """ikutsunanodesuka?!?!?!?!?!?!."""

    def __init__(self, world_map, threadlock):
        threading.Thread.__init__(self)
        self.world_map = world_map
        self.threadlock = threadlock

    def run(self):
        with Listener(
                on_press=Listeninthread.on_press,
                on_release=Listeninthread.on_release) as listener:
            listener.join()

    def on_press(key):
        print(f'{key} pressed')
        if key == Key.right:
            pass
        elif key == Key.left:
            pass
        elif key == Key.up:
            print("Wrong key.")
        elif key == Key.down:
            pass

    def on_release(key):
        print(f'{key} released')
        if key == Key.esc:
            return False
