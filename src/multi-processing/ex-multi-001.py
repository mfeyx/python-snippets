import multiprocessing as mp
from multiprocessing import Process, Lock
import time

def f(l, i):
    # l.acquire()
    try:
        print('hello world', i)
        # time.sleep(0.5)
        # l.release()
    finally:
        return

if __name__ == '__main__':
    # default = "spawn" --> results in: FileNotFoundError: [Errno 2] No such file or directory
    mp.set_start_method("fork")
    lock = Lock()
    for num in range(20):
        Process(target=f, args=(lock, num)).start()
