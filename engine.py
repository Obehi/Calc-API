
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

    return symbol_list

def evaluate(symbols):
    # if any(isinstance(x, SubclassOne) for x in symbols):
    index = next((s for s, item in enumerate(symbols) if item.value == '+'), -1)

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

