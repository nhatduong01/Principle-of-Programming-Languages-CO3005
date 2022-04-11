class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):

        return 1 + self.visit(ctx.vardecls())

    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return 1 + self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        # Tail is always internal node because it has empty node as it child
        return 1 if ctx.getChildCount() == 0 else 1 + self.visit(ctx.vardecltail()) + self.visit(ctx.vardecl())

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return 1 + self.visit(ctx.mptype()) + self.visit(ctx.ids())

    def visitMptype(self,ctx:MPParser.MptypeContext):

        return 1

    def visitIds(self,ctx:MPParser.IdsContext):

        return 1 if ctx.getChildCount() == 1 else 1 + self.visit(ctx.ids())

