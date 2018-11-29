"""The time of the testing has begone."""
import threading

import printthread

import changethread

world_map = [["X", "X", " "],
             [" ", " ", "X"]]

threadlock = threading.Lock()

thread1 = printthread.PrintThread(world_map, threadlock)
thread2 = changethread.Listeninthread(world_map, threadlock)
thread1.start()
thread2.start()
