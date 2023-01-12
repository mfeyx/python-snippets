import string
import urllib.request
import json
import time
import threading


finished_count = 0

count = { k: 0 for k in string.ascii_lowercase }
def count_letters(url: str, freq: dict) -> dict:
    res = urllib.request.urlopen(url)
    txt = str(res.read())

    for letter in txt:
        l = letter.lower()
        if l in string.ascii_lowercase:
            freq[l] += 1

    global finished_count
    finished_count += 1

    return freq


def main():

    start_total = time.perf_counter()

    N = 20
    n = 1000

    for i in range(n, n+N):
        url = f"https://www.rfc-editor.org/rfc/rfc{i}.txt"
        threading.Thread(target=count_letters, args=(url, count)).start()

    while finished_count < N:
        time.sleep(0.1)

    end_total = time.perf_counter()
    print(f"TOTAL: {end_total - start_total}")
    print(json.dumps(count, indent=4))


if __name__ == "__main__":
    main()
