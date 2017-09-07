def num_range(start, stop, step):

    while start < stop:
        yield start
        start += step

for i in num_range(0.5, 1.0, 0.1):
        print(i)
