# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#declarations.
    def visitDeclarations(self, ctx:BKOOLParser.DeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#declarationsList.
    def visitDeclarationsList(self, ctx:BKOOLParser.DeclarationsListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#singleDeclarationg.
    def visitSingleDeclarationg(self, ctx:BKOOLParser.SingleDeclarationgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#variable_declare.
    def visitVariable_declare(self, ctx:BKOOLParser.Variable_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#listOfID.
    def visitListOfID(self, ctx:BKOOLParser.ListOfIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#theRestIDList.
    def visitTheRestIDList(self, ctx:BKOOLParser.TheRestIDListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#function_declare.
    def visitFunction_declare(self, ctx:BKOOLParser.Function_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#parameters.
    def visitParameters(self, ctx:BKOOLParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#parameter.
    def visitParameter(self, ctx:BKOOLParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#theRestParameterList.
    def visitTheRestParameterList(self, ctx:BKOOLParser.TheRestParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mptype.
    def visitMptype(self, ctx:BKOOLParser.MptypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#body.
    def visitBody(self, ctx:BKOOLParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#command.
    def visitCommand(self, ctx:BKOOLParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#theRestCommand.
    def visitTheRestCommand(self, ctx:BKOOLParser.TheRestCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#single_command.
    def visitSingle_command(self, ctx:BKOOLParser.Single_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statement.
    def visitStatement(self, ctx:BKOOLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#listofExp.
    def visitListofExp(self, ctx:BKOOLParser.ListofExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#theRestExp.
    def visitTheRestExp(self, ctx:BKOOLParser.TheRestExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#sub_expr.
    def visitSub_expr(self, ctx:BKOOLParser.Sub_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#div_mul_expr.
    def visitDiv_mul_expr(self, ctx:BKOOLParser.Div_mul_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#blacket_expr.
    def visitBlacket_expr(self, ctx:BKOOLParser.Blacket_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp.
    def visitExp(self, ctx:BKOOLParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#funcall.
    def visitFuncall(self, ctx:BKOOLParser.FuncallContext):
        return self.visitChildren(ctx)



del BKOOLParser