def nums(limit=10):
    i = 0
    while i < limit:
        yield i
        i += 1

n = nums()

i = n.__next__()
print(i)
i = next(n)
print(i)
i = next(n)
print(i)
