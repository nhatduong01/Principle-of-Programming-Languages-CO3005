class Exp:
    def __init__(self):
        pass
    def eval():
        pass
class BinExp(Exp):
    def __init__(self, operand1, operator, operand2):
        self.operand1 = operand1
        self.operator = operator
        self.operand2 = operand2
    def eval(self):
        if self.operator == '+':
            return self.operand1.eval() + self.operand2.eval()
        elif self.operator == '-' : 
            return self.operand1.eval() - self.operand2.eval()
        elif self.operator == '*' : 
            return self.operand1.eval() * self.operand2.eval()
        elif self.operator == '/' : 
            return self.operand1.eval() / self.operand2.eval()
class UnExp(Exp):
    def __init__(self, operator, value):
        if operator == '-':
            self.value =  0 - value.value
        else:
            self.value =  value.value
    def eval(self):
        return self.value
class IntLit(Exp):
    def __init__(self, value):
        assert type(value) == int
        self.value = value
    def eval(self):
        return self.value
class FloatLit(Exp):
    def __init__(self, value):
        assert type(value) == float
        self.value = value
    def eval(self):
        return self.value
intlit1 = IntLit(4)
a = UnExp('-', intlit1)
intlit2 = IntLit(3)
intlit3 = IntLit(2)
exp1 = BinExp(intlit2, '*', intlit3)
exp2 = BinExp(a,'+', exp1)
print(exp2.eval())