class Term:
    def __init__(self, value):
        self.value = value
    
    def  __add__(self, other):
        return self.value + other
    def  __sub__(self, other):
        return self.value - other

    def  __mul__(self, other):
        return self.value * other

    def  __floordiv__(self, other):
        return self.value / other

class Operator:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
         return self.value

class Expression:
    def __init__(self, *args):
        self.symbols = args
    
    def get(self):
        return self.symbols


