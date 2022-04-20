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

    def visitProgram(self, ast: Program, c):
        programContext = {}
        c.append(programContext)
        [self.visit(x, c) for x in ast.decl]
        return ''

    def visitClassDecl(self, ast: ClassDecl, c):
        programContext = c[-1]
        if programContext.get(ast.classname.name) is None:
            programContext[ast.classname.name] = {}
            # TODO: Deal with the parent class
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
            self.visit(ast.body, (c, symbolStack, varStack, scopeStack))
        else:
            raise Redeclared(Method(), ast.name.name)

    def visitAttributeDecl(self, ast: AttributeDecl, c):
        programContext = c[0][-1]
        className = c[1]
        if isinstance(ast.decl, VarDecl):
            if programContext[className].get(ast.decl.variable.name) is None:
                programContext[className][ast.decl.variable.name] = ast
            else:
                raise Redeclared(Attribute(), ast.decl.variable.name)
        else:
            if programContext[className].get(ast.decl.constant.name) is None:
                programContext[className][ast.decl.constant.name] = ast
            else:
                raise Redeclared(Attribute(), ast.decl.constant.name)

    def visitBlock(self, ast: Block, param):
        [self.visit(x, param) for x in ast.inst]

