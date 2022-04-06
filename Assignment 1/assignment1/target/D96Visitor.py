# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp.
    def visitExp(self, ctx:D96Parser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relational_operations.
    def visitRelational_operations(self, ctx:D96Parser.Relational_operationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#logical_operations.
    def visitLogical_operations(self, ctx:D96Parser.Logical_operationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#adding_operations.
    def visitAdding_operations(self, ctx:D96Parser.Adding_operationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multiplying_operations.
    def visitMultiplying_operations(self, ctx:D96Parser.Multiplying_operationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#logical_negate_operation.
    def visitLogical_negate_operation(self, ctx:D96Parser.Logical_negate_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#sign_operations.
    def visitSign_operations(self, ctx:D96Parser.Sign_operationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_operations.
    def visitIndex_operations(self, ctx:D96Parser.Index_operationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#intance_access_operarion.
    def visitIntance_access_operarion(self, ctx:D96Parser.Intance_access_operarionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_access_operation.
    def visitStatic_access_operation(self, ctx:D96Parser.Static_access_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#object_create_operation.
    def visitObject_create_operation(self, ctx:D96Parser.Object_create_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parenthesis_operations.
    def visitParenthesis_operations(self, ctx:D96Parser.Parenthesis_operationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#string_operators.
    def visitString_operators(self, ctx:D96Parser.String_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relational_operators.
    def visitRelational_operators(self, ctx:D96Parser.Relational_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#logical_and_or.
    def visitLogical_and_or(self, ctx:D96Parser.Logical_and_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#adding_operators.
    def visitAdding_operators(self, ctx:D96Parser.Adding_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multiplying_operators.
    def visitMultiplying_operators(self, ctx:D96Parser.Multiplying_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#element_expression.
    def visitElement_expression(self, ctx:D96Parser.Element_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_operators.
    def visitIndex_operators(self, ctx:D96Parser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_lit.
    def visitArray_lit(self, ctx:D96Parser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_statements.
    def visitIf_statements(self, ctx:D96Parser.If_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_ifList.
    def visitElse_ifList(self, ctx:D96Parser.Else_ifListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#the_rest_else_if.
    def visitThe_rest_else_if(self, ctx:D96Parser.The_rest_else_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_if.
    def visitElse_if(self, ctx:D96Parser.Else_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_statements.
    def visitElse_statements(self, ctx:D96Parser.Else_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assignment_statements.
    def visitAssignment_statements(self, ctx:D96Parser.Assignment_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lhs.
    def visitLhs(self, ctx:D96Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assignment_static_access.
    def visitAssignment_static_access(self, ctx:D96Parser.Assignment_static_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#foreach_statements.
    def visitForeach_statements(self, ctx:D96Parser.Foreach_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_statements.
    def visitBreak_statements(self, ctx:D96Parser.Break_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_statements.
    def visitContinue_statements(self, ctx:D96Parser.Continue_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_statements.
    def visitReturn_statements(self, ctx:D96Parser.Return_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invocations.
    def visitMethod_invocations(self, ctx:D96Parser.Method_invocationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_statements.
    def visitBlock_statements(self, ctx:D96Parser.Block_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_statement.
    def visitList_statement(self, ctx:D96Parser.List_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#the_rest_statements.
    def visitThe_rest_statements(self, ctx:D96Parser.The_rest_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variable_constant_declaration.
    def visitVariable_constant_declaration(self, ctx:D96Parser.Variable_constant_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variableList.
    def visitVariableList(self, ctx:D96Parser.VariableListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#single_statement.
    def visitSingle_statement(self, ctx:D96Parser.Single_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_declaration.
    def visitClass_declaration(self, ctx:D96Parser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attributes_methods_declarations.
    def visitAttributes_methods_declarations(self, ctx:D96Parser.Attributes_methods_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#the_rest_attributes_methods_declarations.
    def visitThe_rest_attributes_methods_declarations(self, ctx:D96Parser.The_rest_attributes_methods_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayDeclaration.
    def visitArrayDeclaration(self, ctx:D96Parser.ArrayDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_declaration.
    def visitAttribute_declaration(self, ctx:D96Parser.Attribute_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attributesList.
    def visitAttributesList(self, ctx:D96Parser.AttributesListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#iDlist.
    def visitIDlist(self, ctx:D96Parser.IDlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expList.
    def visitExpList(self, ctx:D96Parser.ExpListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#theRestExp.
    def visitTheRestExp(self, ctx:D96Parser.TheRestExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitive_type.
    def visitPrimitive_type(self, ctx:D96Parser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_declaration.
    def visitMethod_declaration(self, ctx:D96Parser.Method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_parameters.
    def visitList_parameters(self, ctx:D96Parser.List_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#the_rest_parameters_declarations.
    def visitThe_rest_parameters_declarations(self, ctx:D96Parser.The_rest_parameters_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameters_declaration.
    def visitParameters_declaration(self, ctx:D96Parser.Parameters_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#same_type_parameters.
    def visitSame_type_parameters(self, ctx:D96Parser.Same_type_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#the_rest_ID.
    def visitThe_rest_ID(self, ctx:D96Parser.The_rest_IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return self.visitChildren(ctx)



del D96Parser