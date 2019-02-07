class Calc:

    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        res = 1
        for i in args:
            res *= i
        return res
