from Symbols import Symbols
import re
import json
from flask import abort

# Store recent expression request history here
history = []

# Split expression string into a list of tokens
def make_tokens(string):
    remove_space = re.compile(r'\s+')
    no_space_string = re.sub(remove_space, '', string)
    
    token_list = [i for i in re.split(r'(\(.*?\)|\d+|.)', no_space_string) if i]
    return token_list

def check_syntax(symbol_list):
    even_symbols = symbol_list[::2]
    odd_symbols = symbol_list[1::2]

    # Check for empy expressions
    if not symbol_list:
        abort(400, description="Empty Expression.")
        
    
    # Check for expressions that are of even length
    if len(symbol_list) % 2 == 0:
        abort(400, description="Expression is of an even length.")
        

    # Check for wronly placed Operators
    if any(isinstance(x, Symbols.Operator) for x in even_symbols):
        abort(400, description="Wrong Operator position.")
        
    
    # Check for wronly placed terms or expressions
    if any(isinstance(symbol, Symbols.Term) or isinstance(symbol, Symbols.Expression) for symbol in odd_symbols):
        abort(400, description="Wrong Term og Expression position.")
        
    
    # check parantheses expressions for syntax error too
    expression = next((symbol for symbol in symbol_list if isinstance(symbol, Symbols.Expression)), False)
    if expression:
        return check_syntax(expression.get())

    return True

# Make a list of Symbols from tokens
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
            #return unkown symbol
            pass          
        t = t+1
    return Symbols.Expression(symbol_list)

def make_expression(s):
    # Strip "()" from string
    new_expression_string = s[1:-1]
    expression_token_list = make_tokens(new_expression_string)
    new_symbol_list = make_symbols(expression_token_list)
    return new_symbol_list


def get_precedence_index(expression):
    # The order in which to process operators
    operator_precedence = ['/','*','+','-']
    for i in operator_precedence:
        # find next instance of operator i in experssion
        index = next((s for s, item in enumerate(expression.get()) if item.value == i), False)
        if index:
            return index
    return EnvironmentError


def evaluate_expression(expression):
    if expression.length() > 3:
        # get next index
        index = get_precedence_index(expression)
        # get the sourounding terms
        new_liste = expression.get()[index-1:index+2]
        expression.replace(index, evaluate_expression(Symbols.Expression(new_liste)))
        return evaluate_expression(expression)
    elif expression.length() == 3:
        return evaluate_operator(*expression.get())
    elif expression.length() == 1:
        return evaluate_symbol(expression.get_first())
    
def evaluate_operator(t1, op, t2):
    if op.value == '+':
        sum = evaluate_symbol(t1) + evaluate_symbol(t2)
    elif op.value == '-':
        sum = evaluate_symbol(t1) - evaluate_symbol(t2)
    elif op.value == '*':
        sum = evaluate_symbol(t1) * evaluate_symbol(t2)
    elif op.value == '/':
        sum = evaluate_symbol(t1) / evaluate_symbol(t2)
    return Symbols.Term(sum) 

# Takes a symbol and returns a Term
def evaluate_symbol(symbol):
    if isinstance(symbol, Symbols.Term):
        return symbol.value
    if isinstance(symbol, Symbols.Expression):
        return evaluate_symbol(evaluate_expression(symbol))
   

def isDigit(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def isOperator(s):
    if any(x in s for x in ('/', '*', '-', '+')):
        return True
    else:
        return False
 
def is_expression(s):
    if s.startswith('('):
        return True
    else:
        return False

def calc_json_expression(json_expression):
    tokens = make_tokens(json_expression)
    symbols_sequence = make_symbols(tokens)
    if not check_syntax(symbols_sequence.get()):
        pass
        #raise SyntaxError("test it")
        #return "syntax error", 404

    result_str = evaluate_expression(symbols_sequence).value
    result = { "result" : result_str}
    add_history_item(json_expression, result_str)
    return result

def add_history_item(expression, result):
    item = {}
    item['expression'] = expression
    item['result'] = result
    history.append(item)

def get_history():
    return history

