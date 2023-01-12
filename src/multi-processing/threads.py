import time
import threading
from threading import Thread

sleeps = [1, 2, 3, 4, 5]

def do_work(n: int = 1) -> None:
    print("Starting work for {0} seconds...".format(n))
    time.sleep(n)
    print("Finished ({0}).".format(n))

for i in sleeps:
    t = Thread(target=do_work, args=(i, ))
    t.start()

    # active = threading.active_count()
    # print(f"Active Threads: {active}")

    # t.join()

    # with t.join()
    """
    Starting work for 1 seconds...
    Finished (1).
    Starting work for 2 seconds...
    Finished (2).
    Starting work for 3 seconds...
    Finished (3).
    Starting work for 4 seconds...
    Finished (4).
    Starting work for 5 seconds...
    Finished (5).
    Done.
    """

    # without join
    """
    Starting work for 1 seconds...
    Starting work for 2 seconds...
    Starting work for 3 seconds...
    Starting work for 4 seconds...
    Starting work for 5 seconds...
    Done.
    Finished (1).
    Finished (2).
    Finished (3).
    Finished (4).
    Finished (5).
    """

print("Done.")
