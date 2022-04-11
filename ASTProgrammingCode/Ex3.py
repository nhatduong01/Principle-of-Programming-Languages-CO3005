class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program([item for x in ctx.vardecl() for item in self.visit(x)])

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        idList = self.visit(ctx.ids())
        myType = self.visit(ctx.mptype())
        return [VarDecl(myID, myType) for myID in idList]

    def visitMptype(self,ctx:MPParser.MptypeContext):
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()

    def visitIds(self,ctx:MPParser.IdsContext):
        return [Id(x.getText()) for x in ctx.ID()]