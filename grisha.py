class A:
    s = {}
    def __init__(self):
        pass
    def f(self):
        for key,val in self.s.items():
            if Arena.type == key:
                Arena.mode += val

class B(A):
    s = {"fire": 1.8, 'water': -1.5}
    def __init__(self):
        pass
