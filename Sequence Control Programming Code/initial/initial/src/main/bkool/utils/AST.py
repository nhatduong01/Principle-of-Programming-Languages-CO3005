from abc import ABC, abstractmethod, ABCMeta
from Visitor import Visitor


class AST(ABC):
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)

class Program(AST):
    #decl:list(Decl)
    def __init__(self, decl):
        self.decl = decl
    
    def __str__(self):
        return "Program(List(" + ','.join(str(i) for i in self.decl) + "))"
    
    def accept(self, v: Visitor, param):
        return v.visitProgram(self, param)

class Decl(AST):
    __metaclass__ = ABCMeta
    pass

class FuncDecl(Decl):
    #name: Id
    #param: list(VarDecl)
    #returnType: Type
    #body: Block
    def __init__(self, name, param, returnType, body):
        self.name = name
        self.param = param
        self.returnType = returnType
        self.body = body

    def __str__(self):
        return "FuncDecl(" + str(self.name) + ",List(" +  ','.join(str(i) for i in self.param) + ")," + str(self.returnType) + "," + str(self.body) + ")"
    
    def accept(self, v, param):
        return v.visitFuncDecl(self, param)

class Type(AST):
    __metaclass__ = ABCMeta
    pass

class IntType(Type):
    def __str__(self):
        return "IntType"

    def accept(self, v, param):
        return v.visitIntType(self, param)

class FloatType(Type):
    def __str__(self):
        return "FloatType"

    def accept(self, v, param):
        return v.visitFloatType(self, param)

class BoolType(Type):
    def __str__(self):
        return "BoolType"

    def accept(self, v, param):
        return v.visitFloatType(self, param)

class VoidType(Type):
    def __str__(self):
        return "VoidType"

    def accept(self, v, param):
        return v.visitVoidType(self, param)

class Stmt(AST):
    __metaclass__ = ABCMeta
    pass

class Expr(Stmt):
    __metaclass__ = ABCMeta
    pass

class CallExpr(Expr):
    #method:Id
    #param:list(Expr)
    def __init__(self, method, param):
        self.method = method
        self.param = param

    def __str__(self):
        return "CallExpr(" + str(self.method) + ",List(" +  ','.join(str(i) for i in self.param) + "))"

    def accept(self, v, param):
        return v.visitCallExpr(self, param)



class LHS(Expr):
    __metaclass__ = ABCMeta
    pass

class Id(LHS):
    #name:string
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Id(" + self.name + ")"

    def accept(self, v, param):
        return v.visitId(self, param)

class Block(Stmt):
    #decl:list(VarDecl)
    #stmt:list(Stmt)
    def __init__(self, decl, stmt):
        self.decl = decl
        self.stmt = stmt

    def __str__(self):
        return "Block(List(" + ','.join(str(i) for i in self.decl) + "),List(" + ','.join(str(i) for i in self.stmt) + "))"

    def accept(self, v, param):
        return v.visitBlock(self, param)


class Literal(Expr):
    __metaclass__ = ABCMeta
    pass

class IntLiteral(Literal):
    #value:int
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "IntLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitIntLiteral(self, param)
class FloatLiteral(Literal):
    #value:float
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "FloatLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitFloatLiteral(self, param)

class BinOP(Expr):
    def __init__(self, op, e1, e2):
        self.op = op
        self.e1 = e1
        self.e2 = e2
    
    def accept(self, v, param):
        return v.visitBinOP(self, param)

    def __str__(self):
        return "BinOp(" + self.op + ", " + str(self.e1) + ", " + str(self.e2) + ")" 