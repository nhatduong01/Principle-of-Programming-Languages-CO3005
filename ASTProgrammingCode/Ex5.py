class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):

        return self.visit(ctx.mptype())

    def visitMptype(self,ctx:MPParser.MptypeContext):
        if ctx.primtype():
            return self.visit(ctx.primtype())
        elif ctx.arraytype():
            return self.visit(ctx.arraytype())
    def auxilaryVisitArrayType(self, ctx):
        dimList = [self.visit(ctx.dimen())]
        if ctx.primtype():
            return dimList +  [self.visit(ctx.primtype())]
        else:
            return dimList + self.auxilaryVisitArrayType(ctx.arraytype()) 
    
    def visitArraytype(self,ctx:MPParser.ArraytypeContext):
        if ctx.primtype():
            return ArrayType(self.visit(ctx.dimen()), self.visit(ctx.primtype()))
        else:
            allList = [self.visit(ctx.dimen())]+ self.auxilaryVisitArrayType(ctx.arraytype())
            primitiveType = allList[-1]
            allList = allList[:-1]
            allList = allList[::-1]
            unionType = reduce(lambda x, y: UnionType(x,y), allList[1:], allList[0])
            return ArrayType(unionType, primitiveType)


    def visitPrimtype(self,ctx:MPParser.PrimtypeContext): 
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()

    def visitDimen(self,ctx:MPParser.DimenContext):
        return RangeType(self.visit(ctx.num(0)), self.visit(ctx.num(1)))

    def visitNum(self,ctx:MPParser.DimenContext):
        return ctx.INTLIT().getText() if ctx.getChildCount() == 1 else '-' + ctx.INTLIT().getText()