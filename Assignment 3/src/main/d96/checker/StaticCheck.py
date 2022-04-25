"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


class StaticChecker(BaseVisitor, Utils):
    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("putIntLn", MType([IntType()], VoidType()))
    ]

    def __init__(self, ast):
        self.ast = ast
        self.isInConsDecl = False

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def checkSubClass(self, programContext, subClass, parentClass):
        if programContext[subClass]["parentClass"] is None:
            return False
        elif programContext[subClass]["parentClass"] == parentClass:
            return True
        else:
            return self.checkSubClass(programContext, programContext[subClass]["parentClass"], parentClass)

    def checkAssignment(self, programContext, leftType, rightType):
        if type(leftType) == type(rightType) and type(leftType) is ClassType:
            return self.checkSubClass(programContext, rightType.classname.name, leftType.classname.name)
        elif type(leftType) is FloatType and type(rightType) is IntType:
            return True
        elif type(leftType) == type(rightType) and type(leftType) is not ClassType:
            return True
        else:
            return False

    def lookUpSymbol(self, varStack, symbols):
        for i in range(len(varStack))[::-1]:
            if varStack[i] == symbols:
                return i
        raise Undeclared(Variable(), symbols)

    def visitProgram(self, ast: Program, c):
        programContext = {}
        c.append(programContext)
        [self.visit(x, c) for x in ast.decl]
        if programContext.get("Program") is None:
            raise NoEntryPoint()
        if programContext["Program"].get("main") is None:
            raise NoEntryPoint()
        elif type(programContext["Program"]["main"].kind) != Static or len(
                programContext["Program"]["main"].param) != 0:
            raise NoEntryPoint()
        return ''

    def visitClassDecl(self, ast: ClassDecl, c):
        programContext = c[-1]
        if programContext.get(ast.classname.name) is None:
            programContext[ast.classname.name] = {}
            if ast.parentname is not None and programContext.get(ast.parentname.name) is None:
                raise Undeclared(Class(), ast.parentname.name)
            programContext[ast.classname.name][
                "parentClass"] = ast.parentname.name if ast.parentname is not None else ast.parentname
            [self.visit(x, (c, ast.classname.name)) for x in ast.memlist]
        else:
            raise Redeclared(Class(), ast.classname.name)

    def visitMethodDecl(self, ast, c):
        programContext = c[0][-1]
        className = c[1]
        if programContext[className].get(ast.name.name) is None:
            # TODO: Here we consider if the method and attribute has the same name, we must raise it too
            programContext[className][ast.name.name] = ast
            symbolStack = []
            scopeStack = [0]
            varStack = []
            for eachParam in ast.param:
                if eachParam.variable.name in varStack:
                    raise Redeclared(Parameter(), eachParam.variable.name)
                else:
                    varStack.append(eachParam.variable.name)
                    # False because parameter is considered variable not constant
                    symbolStack.append((eachParam.variable.name, eachParam.varType, eachParam.varInit, False))
                    self.visit(eachParam.varType, c)
            self.visit(ast.body, (c, symbolStack, varStack, scopeStack))
        else:
            raise Redeclared(Method(), ast.name.name)

    def visitAttributeDecl(self, ast: AttributeDecl, c):
        programContext = c[0][-1]
        className = c[1]
        if isinstance(ast.decl, VarDecl):
            if programContext[className].get(ast.decl.variable.name) is None:
                programContext[className][ast.decl.variable.name] = ast
                self.visit(ast.decl, c)
            else:
                raise Redeclared(Attribute(), ast.decl.variable.name)
        else:
            if programContext[className].get(ast.decl.constant.name) is None:
                programContext[className][ast.decl.constant.name] = ast
                self.visit(ast.decl, c)
            else:
                raise Redeclared(Attribute(), ast.decl.constant.name)

    def visitVarDecl(self, ast: VarDecl, param):
        if len(param) == 2:
            # We are in a class
            programContext = param[0][-1]
            className = param[1]
            attributeObject = programContext[className][ast.variable.name]
            if type(attributeObject.kind) is Static:
                if attributeObject.decl.varInit is not None:
                    varType = self.visit(ast.varType, param)
                    typeVarInit = self.visit(attributeObject.decl.varInit, param)
                    if not self.checkAssignment(programContext, varType, typeVarInit):
                        raise TypeMismatchInExpression(ast)
            # TODO: If it is an instance variable but It has init value, what is
            # the error then
        elif len(param) == 4:
            # We are in a method
            programContext = param[0][0][-1]
            className = param[0][1]
            symbolStack = param[1]
            varStack = param[2]
            scopeStack = param[3]
            if ast.variable.name in varStack[scopeStack[-1]:]:
                raise Redeclared(Variable(), ast.variable.name)
            if ast.varInit is not None and type(ast.varInit) is not NullLiteral:
                varType = self.visit(ast.varType, param[0])
                varInitType = self.visit(ast.varInit, param)
                if not self.checkAssignment(programContext, varType, varInitType):
                    raise TypeMismatchInStatement(ast)
            varStack.append(ast.variable.name)
            symbolStack.append((ast.variable.name, ast.varType, ast.varInit, False))

    def visitConstDecl(self, ast: ConstDecl, param):
        self.isInConsDecl = True
        if len(param) == 2:
            """
            We are in a function, I assume that:
            1) If it does not have an init value => raise IllegalConstantExpression()
            2) If the init value does not match the type => raise TypeMismatchInConstant()
            TODO: I have not handle the case it is the combination of immutable attribute
            """
            programContext = param[0][-1]
            typeValue = ast.value
            if typeValue is None:
                raise IllegalConstantExpression(None)
            else:
                typeValue = self.visit(ast.value, param)
                constType = self.visit(ast.constType, param)
                if not self.checkAssignment(programContext, constType, typeValue):
                    raise TypeMismatchInConstant(ast)
        elif len(param) == 4:
            """
            We are in a method,
            TODO: I have not handle the case it is the combination of immutable attribute
            """
            programContext = param[0][0][-1]
            className = param[0][1]
            symbolStack = param[1]
            varStack = param[2]
            scopeStack = param[3]
            if ast.constant.name in varStack[scopeStack[-1]:]:
                raise Redeclared(Constant(), ast.constant.name)
            elif ast.value is None:
                raise IllegalConstantExpression(None)
            else:
                constType = self.visit(ast.constType, param[0])
                valueType = self.visit(ast.value, param)
                if not self.checkAssignment(programContext, constType, valueType):
                    raise TypeMismatchInConstant(ast)
            varStack.append(ast.constant.name)
            symbolStack.append((ast.constant.name, ast.constType, ast.value, True))
        self.isInConsDecl = False

    def visitBlock(self, ast: Block, param):
        [self.visit(x, param) for x in ast.inst]

    def visitBinaryOp(self, ast: BinaryOp, param):
        programContext = param[0][-1]
        symbolStack = param[1]
        varStack = param[2]
        scopeStack = param[3]

    def visitIntLiteral(self, ast: IntLiteral, param):
        return IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, param):
        return FloatType()

    def visitNullLiteral(self, ast: NullLiteral, param):
        return None

    def visitClassType(self, ast: ClassType, param):
        programContext = param[0][-1]
        if programContext.get(ast.classname.name) is None:
            raise Undeclared(Class(), ast.classname.name)
        return ast

    def visitFloatType(self, ast: FloatType, param):
        return FloatType()

    def visitIntType(self, ast: IntType, param):
        return IntType()

    def visitStringType(self, ast: StringType, param):
        return StringType()
    
    def visitId(self, ast: Id, param):
        symbolStack = param[1]
        varStack = param[2]
        symbolIdx = self.lookUpSymbol(varStack, ast.name)
        if self.isInConsDecl:
            if not symbolStack[symbolIdx][3]:
                raise IllegalConstantExpression(ast)
        return symbolStack[symbolIdx][1]
