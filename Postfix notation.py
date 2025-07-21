
'''
Postfix notation is an unambiguous way of writing an arithmetic expression 
without parentheses. It is defined so that if “(exp1)op(exp2)” is a
normal, fully parenthesized expression whose operation is op, the postfix
version of this is “pexp1 pexp2 op”, where pexp1 is the postfix version of
exp1 and pexp2 is the postfix version of exp2. The postfix version of a 
single number or variable is just that number or variable. For example, the
postfix version of “((5+ 2)∗(8 − 3))/4” is “5 2 + 8 3 − ∗ 4 /”. Develope
a nonrecursive way of evaluating an expression in postfix notation.
'''

class Empty(Exception):
    pass


class MyStack():
    def __init__(self):
        self._data = []        
    def __len__(self):
        return len(self._data)    
    def is_empty(self):
        return len(self._data) == 0
    def push(self, e):
        self._data.append(e)
    def top(self):
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
    
import operator

class prefix_notation_assessment():
    OPERATORS = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul,
                 '/': operator.truediv,
                 '^': operator.pow,
                 '**': operator.pow}
    
    def __init__(self):
        self._S = MyStack()  #Relying on Stack from available resources of the course
    
    
    def _is_empty(self):
        return self._S.is_empty()
    
    def _pop(self):
        if self._S.is_empty():
            raise Empty('No value available')
        else:
            return self._S.pop()
        
    def _push(self, e):
        self._S.push(e)
    
    def _evaluate(self, operator):
        pexp2 = self._pop()
        pexp1 = self._pop()
        
        self._push(self.OPERATORS[operator](pexp1, pexp2)) #Adding the result back to the stack as a new element
        
    
    def __call__(self, operation):
        self._S  = MyStack()  #Refreshing the stack for the next operation
        for i in operation:
            if i in self.OPERATORS:
                self._evaluate(i)
            elif isinstance(i, int) or isinstance(i, float):
                self._push(i)
        
        result = self._pop() #Popping the last Element which is the result of the operation
        if self._is_empty(): return result
        else: raise AdditionalValues('Invalid Expression: Wrong value numbers for the available operators')
            
pf_assess = prefix_notation_assessment()

"""Performing some Examples for the code"""
exps = [[5,2,'+',8,3,'-','*',4,'/'],
        [5,2,3,'+',8,3,'-','*',4,'/', '^'],
        [6,7, 4,'+'],[10,5,'-','*',6,'/'],
        [11,3,'+',6,1,'-','*',16,'-', '+']        
       ]

for exp in exps:
    try: 
        print(exp, '=', pf_assess(exp))
    except Exception as e:
        print (exp, 'Failed with the following exception:', e)