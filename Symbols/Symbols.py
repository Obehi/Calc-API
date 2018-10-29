class Term:
    def __init__(self, value):
        self.value = float(value)

    def  __repr__(self):
        return '{}'.format(self.value)
    
    def value(self):
        return float(self.value)


class Expression:
    def __init__(self, *args):
        #convert the tuple to list
        
        self.value = args[0]

    def get(self):
        return self.value

    def get_first(self):
        if not self.value:
            raise Exception('Expression: List of symbols is empty')
        return self.value[0]

    def length(self):
        return len(self.value)
    
    # replace index and sorrounding elements with value
    def replace(self, index, value):
        if index % 2 == 0:
            raise Exception('Expression: Operator is in wrong index')
        if index >= len(self.value):
            raise Exception('Expression: Operator is out of bound')

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

    def  __repr__(self):
        return '{}'.format(self.value)



