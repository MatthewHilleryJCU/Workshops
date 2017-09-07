def frange(start, stop, step):

    while start < stop:
        yield start
        start += step

for i in frange(0.5, 1.0, 0.1):
        print(i)
