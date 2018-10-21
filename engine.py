from Symbols import Symbols
import re

def make_tokens(string):
    remove_space = re.compile(r'\s+')
    no_space_string = re.sub(remove_space, '', string)
    value = [i for i in re.split(r'(\(.*?\)|\d+|(\w+))', no_space_string) if i]
    return value

def make_symbols(token_list):
    
    symbol_list = []
    t = 0
    while t < len(token_list):
        if is_expression(token_list[t]):
            symbol_list.append(make_expression(token_list[t]))

        #special case for - incase of negative numbers
        elif token_list[t] == '-':
            if symbol_list:
                last_added_symbol=symbol_list[-1]
            else: 
                last_added_symbol=False
            
            if  isinstance(last_added_symbol, Symbols.Term):
                symbol_list.append(Symbols.Operator(token_list[t]))
            else:
                symbol_list.append(Symbols.Term(token_list[t]+token_list[t+1]))
                t = t+1
        
        elif isOperator(token_list[t]):
            symbol_list.append(Symbols.Operator(token_list[t]))

        
        elif isDigit(token_list[t]):
                symbol_list.append(Symbols.Term(token_list[t]))   

        else:
            #return uknown symbol
            pass          
        t = t+1

    return Symbols.Expression(symbol_list)

def evaluate_expression(expression):
    print(expression)
    print(expression.length())
    if expression.length() > 3:
        print("in here")
        index = next((s for s, item in enumerate(expression.get()) if item.value == '+'), -1)
        new_liste = expression.get()[index-1:index+1]
        return expression.replace(index, evaluate_expression(Symbols.Expression(new_liste)))
    elif expression.length == 3:
        return evaluate_operator(*expression.get())
    elif expression.length == 1:
        return evaluate_symbol(expression.get_first())

    
def evaluate_operator(t1, op, t2):
    if Symbols.Operator.value == '+':
        return evaluate_symbol(t1) + evaluate_symbol(t2)
    elif Symbols.Operator.value == '-':
        return evaluate_symbol(t1) - evaluate_symbol(t2)
    elif Symbols.Operator.value == '*':
        return evaluate_symbol(t1) * evaluate_symbol(t2)
    elif Symbols.Operator.value == '/':
        return evaluate_symbol(t1) / evaluate_symbol(t2)

def evaluate_symbol(symbol):
    if isinstance(symbol, Symbols.Term):
        return symbol.value
    if isinstance(symbol, Symbols.Expression): 
        return evaluate_expression(symbol)
   

def make_expression(s):
    new_expression_string = s[1:-1]
    expression_tokens = make_tokens(new_expression_string)
    new_symbol_list = make_symbols(expression_tokens)
    return Symbols.Expression(new_symbol_list)


def isDigit(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def isOperator(s):
    if any(x in s for x in ('+', '-', '*', '/')):
        return True
    else:
        return False
 
def is_expression(s):
    if s.startswith('('):
        return True
    else:
        return False

if __name__ == "__main__":
    calc_string = '-2 + -66 + (3/3-2)'
    tokens = make_tokens(calc_string)
    symbols_sequence = make_symbols(tokens)
    print(evaluate_expression(symbols_sequence))

