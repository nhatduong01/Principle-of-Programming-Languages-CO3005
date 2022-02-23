
from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program([eachVarDecl for vardecllist in ctx.vardecl() for eachVarDecl in self.visit(vardecllist)])

    def visitVardecl(self,ctx:MPParser.VardeclContext):
        return [VarDecl(myId, self.visit(ctx.mptype())) for myId in self.visit(ctx.ids())]

    def visitMptype(self,ctx:MPParser.MptypeContext): 
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()

    def visitIds(self,ctx:MPParser.IdsContext):
        return [Id(myId.getText()) for myId in ctx.ID()]
  
    

        

