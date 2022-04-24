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
        if type(leftType) == type(rightType):
            return True
        elif type(leftType) == FloatType and type(rightType) == IntType:
            return True
        elif type(leftType) == ClassType and type(rightType) == ClassType:
            return self.checkSubClass(programContext, rightType.classname.name, leftType.classname.name)
        else:
            return False

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
                    symbolStack.append((eachParam.variable.name, eachParam.varType, eachParam.varInit))
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
        programContext = param[0][-1]
        className = param[1]
        attributeObject = programContext[className][ast.variable.name]
        if type(attributeObject.kind) is Static:
            if attributeObject.decl.varInit is not None:
                typeVarInit = self.visit(attributeObject.decl.varInit, param)
                if not self.checkAssignment(programContext, ast.varType, typeVarInit):
                    raise TypeMismatchInExpression(ast)
        # TODO: If it is an instance variable but It has init value, what is
        # the error then

    def visitConstDecl(self, ast: ConstDecl, param):
        """
        I assume that:
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
            if not self.checkAssignment(programContext, ast.constType, typeValue):
                raise TypeMismatchInConstant(ast)

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

    def visitClassType(self, ast: ClassType, param):
        programContext = param[0][-1]
        if programContext.get(ast.classname.name) is None:
            raise Undeclared(Class(), ast.classname.name)

    def visitFloatType(self, ast: FloatType, param):
        return FloatType()


