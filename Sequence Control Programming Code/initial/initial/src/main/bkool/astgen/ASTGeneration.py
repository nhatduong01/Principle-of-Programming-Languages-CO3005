from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *

class ASTGeneration(BKOOLVisitor):
    def visitProgram(self,ctx:BKOOLParser.ProgramContext):
        return Program([FuncDecl(Id("main"),
                        [],
                        self.visit(ctx.mptype()),
                        Block([],[self.visit(ctx.body())] if ctx.body() else []))])

    def visitMptype(self,ctx:BKOOLParser.MptypeContext):
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        else:
            return VoidType()

    def visitBody(self,ctx:BKOOLParser.BodyContext):
        return self.visit(ctx.funcall())
  
  	
    def visitFuncall(self,ctx:BKOOLParser.FuncallContext):
        return CallExpr(Id(ctx.ID().getText()),[self.visit(ctx.exp())] if ctx.exp() else [])

    def visitExp(self,ctx:BKOOLParser.ExpContext):
        if ctx.getChildCount() == 3:
            e1 = self.visit(ctx.exp())
            e2 = self.visit(ctx.exp1())
            op = ctx.getChild(1).getText()
            return BinOP(op, e1, e2)
        else:
            return self.visit(ctx.exp1())
    def visitExp1(self,ctx:BKOOLParser.Exp1Context):
        if ctx.getChildCount() == 3:
            e1 = self.visit(ctx.exp1())
            e2 = self.visit(ctx.exp2())
            op = ctx.getChild(1).getText()
            return BinOP(op, e1, e2)
        else:
            return self.visit(ctx.exp2())
    def visitExp2(self,ctx:BKOOLParser.Exp2Context):
        if (ctx.funcall()):
            return self.visit(ctx.funcall())
        elif(ctx.FLOATLIT()):
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        else:
            return IntLiteral(int(ctx.INTLIT().getText()))


