from functools import reduce
from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import * 

class ASTGeneration(MPVisitor):
    def toBool(self,x):
        return x == "True"

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.exp())

    def visitExp(self,ctx:MPParser.ExpContext):
        termList = [self.visit(x) for x in ctx.term()]
        assignList = ctx.ASSIGN()
        assignList = assignList[::-1]
        rhs = termList[-1]
        termList = termList[::-1]
        return reduce(lambda acc, ele: Binary(ele[1].getText(),ele[0],acc), zip(termList[1:], assignList), rhs)
    def visitTerm(self,ctx:MPParser.TermContext): 
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.factor(0))
            right = self.visit(ctx.factor(1))
            return Binary(ctx.COMPARE().getText(), left, right)
        else:
            return self.visit(ctx.factor(0))

    def visitFactor(self,ctx:MPParser.FactorContext):
        return reduce( lambda acc, newEle: Binary(newEle[0].getText(),
        acc, self.visit(newEle[1])), zip(ctx.ANDOR(), ctx.operand()[1:]), self.visit(ctx.operand(0)))
  
    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLIT():
            return BooleanLiteral(self.toBool(ctx.BOOLIT().getText()))
        else: return self.visit(ctx.exp())
        

