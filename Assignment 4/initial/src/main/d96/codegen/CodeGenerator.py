'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod


class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("readInt", MType(list(), IntType()), CName(self.libName)),
                Symbol("writeInt", MType([IntType()],
                       VoidType()), CName(self.libName)),
                Symbol("readFloat", MType(list(), FloatType()),
                       CName(self.libName)),
                Symbol("writeFloat", MType([FloatType()],
                                           VoidType()), CName(self.libName)),
                Symbol("readBool", MType(list(), BoolType()),
                       CName(self.libName)),
                Symbol("writeBool", MType([BoolType()],
                       VoidType()), CName(self.libName)),
                Symbol("readStr", MType(list(), StringType()),
                       CName(self.libName)),
                Symbol("writeStr", MType([StringType()],
                       VoidType()), CName(self.libName)),
                ]

    def gen(self, ast, dir_):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)


class StringType(Type):

    def __str__(self):
        return "StringType"

    def accept(self, v, param):
        return None


class ArrayPointerType(Type):
    def __init__(self, ctype):
        # cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None


class ClassType(Type):
    def __init__(self, cname):
        self.cname = cname

    def __str__(self):
        return "Class({0})".format(str(self.cname))

    def accept(self, v, param):
        return None


class SubBody():
    def __init__(self, frame, sym):
        # frame: Frame
        # sym: List[Symbol]

        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        # frame: Frame
        # sym: List[Symbol]
        # isLeft: Boolean
        # isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        # value: Int

        self.value = value


class CName(Val):
    def __init__(self, value):
        # value: String

        self.value = value


class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        # astTree: AST
        # env: List[Symbol]
        # dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "D96Class"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast: Program, c):
        e = SubBody(None, self.env)
        for eachClass in ast.decl:
            e = self.visit(eachClass, e)
        return []

    def visitClassDecl(self, ast: ClassDecl, c):
        # TODO: I just make for only class program
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.emit.printout(self.emit.emitPROLOG(
            self.className, "java.lang.Object"))
        [self.visit(eachDecl, SubBody(None, [])) for eachDecl in ast.memlist]
        self.emit.emitEPILOG()

    def visitAttributeDecl(self, ast: AttributeDecl, c):
        name, type = self.visit(ast.decl, c)
        isStatic = True if isinstance(ast.kind, Static) else False
        self.emit.printout(self.emit.emitATTRIBUTE(name, type, isStatic))

    def visitMethodDecl(self, ast: MethodDecl, c):
        frame = Frame(ast.name.name, VoidType())
        # TODO: When it is False?
        frame.enterScope(True)
        isStatic = True if isinstance(ast.kind, Static) else False
        if ast.name.name == "main":
            mtype = MType([ArrayPointerType(StringType())], VoidType())
        else:
            inType = []
            for eachParam in ast.param:
                inType.append(self.visit(eachParam, c))
            mtype = MType(inType, VoidType())
        self.emit.printout(self.emit.emitMETHOD(
            ast.name.name, mtype, isStatic, frame))
        if ast.name.name == "main":
            self.emit.printout(self.emit.emitVAR(frame.getCurrIndex(), "arg" + str(frame.getCurrIndex()), ArrayPointerType(StringType()), frame.getStartLabel(),
                                                 frame.getEndLabel()))
        else:
            for idx in range(len(inType)):
                self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "arg" + str(frame.getCurrIndex()),
                                                     inType[idx], frame.getStartLabel(), frame.getEndLabel()))
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        # TODO: visit the body
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitVarDecl(self, ast: VarDecl, c):
        type = self.visit(ast.varType, c)
        return type

    def visitIntType(self, ast: IntType, c):
        return ast

    def visitFloatType(self, ast: FloatType, c):
        return ast
