import time
from threading import Thread, Lock

class StingySpendy:
    n = 20_000_000
    money = 100
    runs = 0
    stingy_runs = 0
    spendy_runs = 0

    mutex = Lock()

    def stingy(self):
        for _ in range(self.n):
            self.mutex.acquire()
            self.money += 10
            self.mutex.release()
        print("Stingy done.")

    def spendy(self):
        for _ in range(self.n):
            self.mutex.acquire()
            self.money -= 10
            self.mutex.release()
            self.spendy_runs += 1
        print("Spendy done.")

s = StingySpendy()

targets = [s.stingy, s.spendy]
for target in targets:
    t = Thread(target=target, args=())
    t.start()
    # t.join()

time.sleep(2)

print("MONEY:", s.money)
