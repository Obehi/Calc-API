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

    def  __repr__(self):
        return '{}'.format(self.value)


class Expression:
    def __init__(self, *args):
        self.value = list(args)
    
    def get(self):
        return self.value

    def get_first(self):
        if not self.value:
            return EnvironmentError
        return self.value[0]

    def length(self):
        return len(self.value)
    
    def replace(self, index, value):
        if index % 2 == 0:
            return EnvironmentError
        if index >= len(self.value):
            return EnvironmentError

        term_one = self.value[index-1]
        term_two = self.value[index+1]

        temp_list = self.value[index-1:index+2]

        del self.value[index-1:index+2]

        self.value.insert(index-1, value)

    def __repr__(self):
        return '{}'.format(self.value)
    
  
class Operator:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
         return self.value
         
    def  __repr__(self):
        return '{}'.format(self.value)

class Add(Operator):
    def __init__(self, value):
        super(Add, self).__init__(value)

class Sub(Operator):
    def __init__(self, value):
        super().__init__(value)

class Mul(Operator):
    def __init__(self, value):
        super().__init__(value)

class Div(Operator):
    def __init__(self):
        super().__init__()

