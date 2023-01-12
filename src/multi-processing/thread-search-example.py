import os
from os.path import join, isdir
from threading import Thread, Lock


dir_name = "/Volumes/Coding/github/py-ml-titelbilder/images_download"
file_name = "00018"
matches = []

mutex = Lock()

def file_search(root, filename):
    print(f"Searching in: {root}")

    child_threads = []
    for file in os.listdir(root):
        full_path = join(root, file)
        if isdir(full_path):
            t = Thread(target=file_search, args=(full_path, file_name))
            t.start()
            child_threads.append(t)

        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()

    for t in child_threads:
        t.join()


def main():
    t = Thread(target=file_search, args=(dir_name, file_name))
    t.start()
    t.join()

    print(f"FOUND {len(matches)} FILES")


if __name__ == "__main__":
    main()
