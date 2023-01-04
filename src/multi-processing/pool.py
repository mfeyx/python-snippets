import time

import multiprocessing
from multiprocessing import Pool


work = (["A", 5], ["B", 2], ["C", 1], ["D", 3])


def work_log(work_data):
    print(" Process %s waiting %s seconds" % (work_data[0], work_data[1]))
    time.sleep(int(work_data[1]))
    print(" Process %s Finished." % work_data[0])


def pool_handler():
    num_cpu = multiprocessing.cpu_count()
    num_work_units = len(work)
    workers = num_work_units if num_work_units < num_cpu else num_cpu

    print(f"Number of Workers: {workers}")
    p = Pool(workers)
    p.map(work_log, work)


if __name__ == '__main__':
    pool_handler()
