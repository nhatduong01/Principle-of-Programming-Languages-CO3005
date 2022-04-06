class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        idList = [x.name for x in ctx.decl]
        myDict = dict(map(lambda x: (x, ""), idList))
        [self.visit(x, myDict) for x in ctx.stmts]

    def visitVarDecl(self,ctx:VarDecl,o): pass

    def visitAssign(self,ctx:Assign,o): pass

    def visitBinOp(self,ctx:BinOp,o): pass

    def visitUnOp(self,ctx:UnOp,o):
        op = ctx.op
        typeExp = self.visit(ctx.e, o)
        if typeExp == '':
            raise TypeCannotBeInferred(ctx)
        if op in ['-', 'i2f']:
            if typeExp != 'int':
                raise TypeMismatchInExpression(ctx)
            elif op == '-':
                return 'int'
            else:
                return 'float'
        elif op in ['-.', 'floor']:
            if typeExp != "float":
                raise TypeMismatchInExpression(ctx)
            elif op == '-.':
                return "float"
            else:
                return "int"
        else:
            if typeExp != 'bool':
                raise TypeMismatchInExpression(ctx)
            else:
                return "bool"

    def visitIntLit(self,ctx:IntLit,o): 
        return 'int'

    def visitFloatLit(self,ctx,o): 
        return 'float'

    def visitBoolLit(self,ctx,o): 
        return 'bool'

    def visitId(self,ctx,o): 
        if o.get(ctx.name) == None:
            raise UndeclaredIdentifier(ctx.name)
        elif o.get(ctx.name) == '':
            return ''
        else:
            return o.get(ctx.name)