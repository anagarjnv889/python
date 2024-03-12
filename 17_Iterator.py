# Iterator

class cube:
    def __init__(self, number):
        self.number =  number

    def __iter__(self):
        self.ele = 0
        return self

    def __next__(self):
        if self.ele <= self.number:
            result = self.ele**3
            self.ele += 1
            return result
        else:
            raise StopIteration

cn = cube(5)
my_iter = cn.__iter__()
nect = cn.__next__()
print(my_iter)
print(nect)
nect = cn.__next__()
print(nect)
nect = cn.__next__()
print(nect)