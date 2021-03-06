from functools import reduce


class Calc:

    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        if not args:
            raise Exception('At least one input is required')
        return reduce(lambda x, y: x*y, args)
    
    def div(self, a, b):
        if b == 0:
            return 'inf'
        return a/b

    def avg(self, l):
        return sum(l)/len(l)