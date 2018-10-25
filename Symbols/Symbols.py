class Term:
    def __init__(self, value):
        self.value = float(value)
        print('creating term - type:{}   value:{}'.format(type(self.value), self.value))
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
    
    def value(self):
        return float(self.value)


class Expression:
    def __init__(self, *args):
        #convert the tuple to list
        
        print("creating Expression args: {} ".format(args))
        print("type(args): {}".format(type(args)))
        self.value = args[0]
        print("making a list of args into value: {} ".format(self.value))
        print("type(self.value): {}".format(type(self.value)))

    def get(self):
        return self.value

    def get_first(self):
        if not self.value:
            return EnvironmentError
        return self.value[0]

    def length(self):
        return len(self.value)
    
    # replace index and sorrounding elements with value
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
        return 'Expression: {}'.format(self.value)
    
class Operator:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
         return self.value
         
    def  __repr__(self):
        return '{}'.format(self.value)



