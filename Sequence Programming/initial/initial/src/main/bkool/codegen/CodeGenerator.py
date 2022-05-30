'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from AST import *
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
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                Symbol("putInt", MType([IntType()],
                       VoidType()), CName(self.libName)),
                Symbol("putIntLn", MType([IntType()],
                       VoidType()), CName(self.libName)),
                Symbol("putFloat", MType(
                    [FloatType()], VoidType()), CName(self.libName))
                ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

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
        #cname: String
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
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value


class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value


class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "BKOOLClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(
            self.className, "java.lang.Object"))
        e = SubBody(None, self.env)
        for x in ast.decl:
            e = self.visit(x, e)
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), None, Block(
            list(), list())), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame

        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(
            consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else list()
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(
            methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
                self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(
                StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR(
                "this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any

        subctxt = o
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, subctxt.sym, frame)
        return SubBody(None, [Symbol(ast.name, MType(list(), ast.returnType), CName(self.className))] + subctxt.sym)

    def visitCallExpr(self, ast, o):
        #ast: CallExpr
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value

        ctype = sym.mtype

        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(
            cname + "/" + ast.method.name, ctype, frame))

    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast, o):
        #ast: FloatLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitBinOP(self, ctx: BinOP, o):
        # Exercise 5 Prgramming Code
        myOp = ctx.op
        value1, type1 = self.visit(ctx.e1, o)
        value2, type2 = self.visit(ctx.e2, o)
        if type(type1) != type(type2):
            if type(type1) == IntType:
                value1 = value1 + self.emit.emitI2F(o.frame)
                type1 = FloatType()
            else:
                value2 = value2 + self.emit.emitI2F(o.frame)
                type2 = FloatType()
        if myOp in ['+', '-']:
            return value1 + value2 + self.emit.emitADDOP(myOp, type1, o.frame), type1
        elif myOp in ['/', '*']:
            if myOp == '/':
                print("Type 1", type(type1))
                print("Type 2", type(type2))
                return value1 + value2 + self.emit.emitMULOP(myOp, type1, o.frame) + self.emit.emitI2F(o.frame), FloatType()
            else:
                return value1 + value2 + self.emit.emitMULOP(myOp, type1, o.frame), type1
        else:
            return value1 + value2 + self.emit.emitREOP(myOp, type1, o.frame), BoolType()

    def visitBinExpr(self, ctx, o):
        # Exercise 3 Programing Code
        #ast: BinOP
        #o: Any
        valueE1, typeE1 = self.visit(ctx.e1, o)
        valueE2, typeE2 = self.visit(ctx.e2, o)
        myFrame = o.frame
        myOp = ctx.op
        returnType = IntType()
        if isinstance(typeE1, FloatType) or isinstance(typeE2, FloatType):
            returnType = FloatType()
        if myOp in ["+", "+."]:
            return valueE1 + valueE2 + self.emit.emitADDOP('+', returnType, myFrame), returnType
        elif myOp in ["-", "-."]:
            return valueE1 + valueE2 + self.emit.emitADDOP('-', returnType, myFrame), returnType
        elif myOp in ['*', '*.']:
            return valueE1 + valueE2 + self.emit.emitMULOP('*', returnType, myFrame), returnType
        else:
            return valueE1 + valueE2 + self.emit.emitMULOP('/', returnType, myFrame), returnType

    # def visitId(self, ctx: Id, o):
    #     # Exercise 4 Programming Code
    #     symbolList = o.sym
    #     myFrame = o.frame
    #     for eachSymbol in symbolList:
    #         if eachSymbol.name == ctx.name:
    #             myIndex = eachSymbol.value.value
    #             if type(myIndex) == str:
    #                 return self.emit.emitGETSTATIC(myIndex + '.' + eachSymbol.name, eachSymbol.mtype, myFrame), eachSymbol.mtype
    #             return self.emit.emitREADVAR(eachSymbol.name, eachSymbol.mtype, myIndex, myFrame), eachSymbol.mtype

    def visitBinExpr2(self, ctx, o):
        myOp = ctx.op
        value1, type1 = self.visit(ctx.e1, o)
        value2, type2 = self.visit(ctx.e2, o)
        if type(type1) != type(type2):
            if type(type1) == IntType:
                value1 = value1 + self.emit.emitI2F(o.frame)
                type1 = FloatType()
            else:
                value2 = value2 + self.emit.emitI2F(o.frame)
                type2 = FloatType()
        if myOp in ['+', '-']:
            return value1 + value2 + self.emit.emitADDOP(myOp, type1, o.frame), type1
        elif myOp in ['/', '*']:
            if myOp == '/':
                return value1 + value2 + self.emit.emitMULOP(myOp, type1, o.frame), type1
        else:
            return value1 + value2 + self.emit.emitREOP(myOp, type1, o.frame), BoolType()

    def visitVarDecl(self, ctx, o):
        # Exercise 6 Programming Code
        myFrame = o.frame
        if myFrame is None:
            emittedStr = self.emit.emitATTRIBUTE(ctx.name, ctx.typ, None)
            self.emit.printout(emittedStr)
            return Symbol(ctx.name, ctx.typ, CName("MCClass"))
        else:
            # myFrame.enterScope(True)
            emittedStr = self.emit.emitVAR(myFrame.getCurrIndex(
            ), ctx.name, ctx.typ, myFrame.getStartLabel(), myFrame.getEndLabel())
            self.emit.printout(emittedStr)
            # myFrame.exitScope()
            result = Symbol(ctx.name, ctx.typ, Index(myFrame.getNewIndex()))
            return result

    def visitId(self, ctx: Id, o):
        # Exercise 1
        symbolList = o.sym
        myFrame = o.frame
        isLeft = o.isLeft
        for eachSymbol in symbolList:
            if eachSymbol.name == ctx.name:
                myIndex = eachSymbol.value.value
                if type(myIndex) == str:
                    if not isLeft:
                        return self.emit.emitGETSTATIC(myIndex + '.' + eachSymbol.name, eachSymbol.mtype, myFrame), eachSymbol.mtype
                    return self.emit.emitPUTSTATIC(myIndex + '.' + eachSymbol.name, eachSymbol.mtype, myFrame), eachSymbol.mtype
                if not isLeft:
                    return self.emit.emitREADVAR(eachSymbol.name, eachSymbol.mtype, myIndex, myFrame), eachSymbol.mtype
                return self.emit.emitWRITEVAR(eachSymbol.name, eachSymbol.mtype, myIndex, myFrame), eachSymbol.mtype

    def visitAssign(self, ctx, param):
        # Exercise 2
        rhs = self.visit(ctx.rhs, Access(param.frame, param.sym, False))
        result = rhs[0] + self.visit(ctx.lhs,
                                     Access(param.frame, param.sym, True))[0]
        self.emit.printout(result)

    def visitIf(self, ctx, o):
        # Exercise 3
        falseLabel = o.frame.getNewLabel()
        exitLabel = o.frame.getNewLabel()
        expr = self.visit(ctx.expr, Access(o.frame, o.sym, False))[0]
        label1 = expr + self.emit.emitIFFALSE(falseLabel, o.frame)
        self.emit.printout(label1)
        self.visit(ctx.tstmt, o)
        label1 = self.emit.emitGOTO(exitLabel, o.frame)
        self.emit.printout(label1)
        label1 = self.emit.emitLABEL(falseLabel, o.frame)
        self.emit.printout(label1)
        if ctx.estmt:
            self.visit(ctx.estmt, o)
        label1 = self.emit.emitLABEL(exitLabel, o.frame)
        self.emit.printout(label1)

    def visitWhile(self, ctx, o):
        # Exercise 4
        o.frame.enterLoop()
        enterLabel = o.frame.getBreakLabel()
        outLabel = o.frame.getContinueLabel()
        currCommand = self.emit.emitLABEL(enterLabel, o.frame)
        self.emit.printout(currCommand)
        exp = self.visit(ctx.expr, Access(o.frame, o.sym, False))[0]
        currCommand = exp + self.emit.emitIFFALSE(outLabel, o.frame)
        self.emit.printout(currCommand)
        self.visit(ctx.stmt, Access(o.frame, o.sym, False))
        currCommand = self.emit.emitGOTO(enterLabel, o.frame)
        self.emit.printout(currCommand)
        currCommand = self.emit.emitLABEL(outLabel, o.frame)
        self.emit.printout(currCommand)
        o.frame.exitLoop()

    def visitFuncDecl(self, ctx, o):
        paraType = list(map(lambda x: x.typ, ctx.param))
        funcType = MType(paraType, ctx.returnType)
        self.emit.printout(self.emit.emitMETHOD(ctx.name, funcType, True))
        message = SubBody(Frame(ctx.name, ctx.returnType), o.sym.copy())
        message.frame.enterScope(True)
        paraSymbolList = list(
            map(lambda x: x.accept(self, message), ctx.param))
        message.sym[:0] = paraSymbolList[::-1]
        varSymbolList = list(
            map(lambda x: x.accept(self, message), ctx.body[0]))
        message.sym[:0] = varSymbolList[::-1]
        self.emit.printout(self.emit.emitLABEL(
            message.frame.getStartLabel(), message.frame))
        list(map(lambda b: b.accept(self, message), ctx.body[1]))
        self.emit.printout(self.emit.emitLABEL(
            message.frame.getEndLabel(), message.frame))
        self.emit.printout(self.emit.emitENDMETHOD(message.frame))
        return Symbol(ctx.name, funcType, CName(self.className))

    def visitBinExpr(self, ctx, o):
        ast = ctx
        frame = o.frame
        (code, _) = ast.e1.accept(self, o)
        code += self.emit.emitDUP(frame)
        if ast.op == "&&":
            false_label = frame.getNewLabel()
            code += self.emit.emitIFFALSE(false_label, frame)
            (_code, _) = ast.e2.accept(self, o)
            code += _code
            code += self.emit.emitANDOP(frame)
            end_bin = frame.getNewLabel()
            code += self.emit.emitGOTO(end_bin, frame)
            code += self.emit.emitLABEL(false_label, frame)
            code += self.emit.emitPOP(frame)
            code += self.emit.emitPUSHICONST("false", frame)
            code += self.emit.emitLABEL(end_bin, frame)
        else:
            true_label = frame.getNewLabel()
            code += self.emit.emitIFTRUE(true_label, frame)
            (_code, _) = ast.e2.accept(self, o)
            code += _code
            code += self.emit.emitOROP(frame)
            end_bin = frame.getNewLabel()
            code += self.emit.emitGOTO(end_bin, frame)
            code += self.emit.emitLABEL(true_label, frame)
            code += self.emit.emitPOP(frame)
            code += self.emit.emitPUSHICONST("true", frame)
            code += self.emit.emitLABEL(end_bin, frame)
        return code, BoolType()
