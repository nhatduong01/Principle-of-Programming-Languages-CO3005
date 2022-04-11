
class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):

        return self.visit(ctx.mptype())

    def visitMptype(self,ctx:MPParser.MptypeContext):
        if ctx.primtype():
            return self.visit(ctx.primtype())
        elif ctx.arraytype():
            return self.visit(ctx.arraytype())

    def visitArraytype(self,ctx:MPParser.ArraytypeContext):
        primType = self.visit(ctx.primtype())
        indexType = self.visit(ctx.dimens())
        return ArrayType(indexType, primType)

    def visitPrimtype(self,ctx:MPParser.PrimtypeContext): 
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
            
    def visitDimens(self,ctx:MPParser.DimensContext):
        myDims = ctx.dimen()
        return reduce(lambda x,y: UnionType(x,self.visit(y)), myDims[1:], self.visit(myDims[0]))

    def visitDimen(self,ctx:MPParser.DimenContext):
        return RangeType(self.visit(ctx.num(0)), self.visit(ctx.num(1)))

    def visitNum(self,ctx:MPParser.DimenContext):
        return ctx.INTLIT().getText() if ctx.getChildCount() == 1 else '-' + ctx.INTLIT().getText() 