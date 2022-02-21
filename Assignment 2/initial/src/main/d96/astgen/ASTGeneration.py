from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *

### TODO:
"""
1) SIKind is ID ?
"""

class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        # classList = []
        # for eachClass in ctx.class_declaration():
        #     processed_class = self.visit(eachClass)
        #     classList.append(processed_class)
        # return Program(classList)
        return Program([self.visit(x) for x in ctx.class_declaration()])
    def visitClass_declaration(self, ctx: D96Parser.Class_declarationContext):
        classID = Id(ctx.ID(0).getText())
        parentClass = Id(ctx.ID(1).getText()) if len(ctx.ID()) == 2 else None
        memberList = self.visit(ctx.attributes_methods_declarations())
        return ClassDecl(classID, memberList, parentClass)

    def visitAttributes_methods_declarations(self,ctx: D96Parser.Attributes_methods_declarationsContext):
        memberList : List[MemDecl] = []
        if (ctx.attribute_declaration()):
            memberList.append(self.visit(ctx.attribute_declaration()))
            return memberList + self.visit(ctx.the_rest_attributes_methods_declarations())
        elif (ctx.method_declaration()):
            memberList.append(self.visit(ctx.method_declaration()))
            return memberList + self.visit(ctx.the_rest_attributes_methods_declarations())

    def visitThe_rest_attributes_methods_declarations(self,ctx: D96Parser.The_rest_attributes_methods_declarationsContext):
        memberList : List[MemDecl] = []
        if (ctx.attribute_declaration()):
            memberList.append(self.visit(ctx.attribute_declaration()))
            return memberList + self.visit(ctx.the_rest_attributes_methods_declarations())
        elif (ctx.method_declaration()):
            memberList.append(self.visit(ctx.method_declaration()))
            return memberList + self.visit(ctx.the_rest_attributes_methods_declarations())

    def visitAttribute_declaration(self, ctx: D96Parser.Attribute_declarationContext):
        decl = self.visit(ctx.getChild(0))
        kind = self.visit(ctx.attributesList())
        return AttributeDecl(kind, decl)
    
    def visitAttributesList(self, ctx: D96Parser.AttributesListContext):
        ### NOTE #### : We are mixing Static and instance attribute here
        attributelist = []
        if ctx.getChild(0).getText()[0] == '$':
            attributelist.append(Static(ctx.getChild(0)))
        else:
            attributelist.append(Instance(ctx.getChild(0)))
        return attributelist + self.visit(ctx.iDlist())
    
    def visitIDlist(self, ctx: D96Parser.IDlistContext):
        if ctx.getChildCount() == 3:
            attributelist = []
            if ctx.getChild(1).getText()[0] == '$':
                attributelist.append(Static(ctx.getChild(1)))
            else:
                attributelist.append(Instance(ctx.getChild(1)))
            return attributelist + self.visit(ctx.iDlist())
        else: return []
    
    def visitMethod_declaration(self,ctx: D96Parser.Method_declarationContext):
        if ctx.getChildCount() == 5:
            kind = Static(ctx.getChild(0)) if ctx.getChild(0).getText()[0] == '$' else Instance(ctx.getChild(0))
            name = Id(ctx.getChild(0).getText())
            param = self.visit(ctx.list_parameters())
            body = self.visit(ctx.block_statements())
            return MethodDecl(kind, name, param, body)
        elif ctx.getChildCount() == 1:
            if ctx.constructor():
                return self.visit(ctx.constructor())
            elif ctx.destructor():
                return self.visit(ctx.destructor())
    
    def visitDestructor(self, ctx: D96Parser.DestructorContext):
        pass
    
    def visitConstructor(self, ctx: D96Parser.ConstructorContext):
        pass
    
    def visitList_parameters(self, ctx: D96Parser.List_parametersContext):
        if ctx.getChildCount() == 2:
            paraList = []
            paraList.append(self.visit(ctx.parameters_declaration()))
            return paraList + self.visit(ctx.the_rest_parameters_declarations())
        else: return []

    def visitThe_rest_parameters_declarations(self, ctx: D96Parser.The_rest_parameters_declarationsContext):
        if ctx.getChildCount() == 4:
            paraList = []
            paraList.append(self.visit(ctx.parameters_declaration()))
            return paraList + self.visit(ctx.the_rest_parameters_declarations())
        else: return []
    
    def visitParameters_declaration(self,ctx: D96Parser.Parameters_declarationContext):
        paramList =[]
        idlist = self.visit(ctx.same_type_parameters())
        primitive_type = self.visit(ctx.primitive_type())
        for eachId in idlist:
            paramList.append(VarDecl(eachId,primitive_type))
        return paramList
    
    def visitSame_type_parameters(self, ctx: D96Parser.Same_type_parametersContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            idList = []
            idList.append(Id(ctx.ID().getText()))
            return idList + self.visit(ctx.the_rest_ID())

    def visitThe_rest_ID(self, ctx: D96Parser.The_rest_IDContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            idList = []
            idList.append(Id(ctx.ID().getText()))
            return idList + self.visit(ctx.the_rest_ID())
    
    def visitPrimitive_type(self, ctx: D96Parser.Primitive_typeContext):
        if ctx.BOOLEANTYPE():
            return BoolType()
        elif ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.STRINGTYPE():
            return StringType()
        elif ctx.ID():
            return ClassType(Id(ctx.ID().getText()))
        elif ctx.arrayDeclaration():
            return self.visit(ctx.arrayDeclaration())
    
    def visitArrayDeclaration(self,ctx: D96Parser.ArrayDeclarationContext):
        eleType = self.visit(ctx.primitive_type())
        size = int(ctx.INTLIT().getText())
        # NOTE: Do we use int or INTLIT for size
        return ArrayType(size, eleType)
    
    def visitBlock_statements(self,ctx: D96Parser.Block_statementsContext):
        lstStm  = []
        return lstStm + self.visit(ctx.list_statement())
    
    def visitList_statement(self, ctx: D96Parser.List_statementContext):
        if ctx.getChildCount() == 2:
            lstStm = []
            lstStm.append(self.visit(ctx.single_statement()))
            return lstStm + self.visit(ctx.the_rest_statements())
        else:
            return []
    
    def visitThe_rest_statements(self, ctx: D96Parser.The_rest_statementsContext):
        if ctx.getChildCount() == 2:
            lstStm = []
            lstStm.append(self.visit(ctx.single_statement()))
            return lstStm + self.visit(ctx.the_rest_statements())
        else:
            return []
    
    def visitSingle_statement(self, ctx: D96Parser.Single_statementContext):
        if ctx.if_statements():
            return self.visit(ctx.if_statements())
        elif ctx.assignment_statements():
            return self.vist(ctx.assignment_statements())
        elif ctx.foreach_statements():
            return self.visit(ctx.foreach_statements())
        elif ctx.break_statements():
            return self.visit(ctx.break_statements())
        elif ctx.continue_statements():
            return self.visit(ctx.continue_statements())
        elif ctx.return_statements():
            return self.visit(ctx.return_statements())
        elif ctx.method_invocations():
            return self.visit(ctx.method_invocations())
        elif ctx.variable_constant_declaration():
            return self.visit(ctx.variable_constant_declaration())
    
    def visitIf_statements(self, ctx : D96Parser.If_statementsContext):
        # NOTE: After If is a block statements not a single statement
        expr  = self.visit(ctx.exp())
        # NOTE: Where is ELSEIF STATEMENT
        thenStmt = self.visit(ctx.block_statements())
        elseStmt = self.visitArrayDeclaration(ctx.else_statements()) if ctx.else_statements() else None
        return If(expr, thenStmt, elseStmt)
    
    def visitAssignment_statements(self, ctx: D96Parser.Assignment_statementsContext):
        lhs = self.visit(ctx.lhs())
        exp = self.visit(ctx.exp())
        return Assign(lhs, exp)
    
    def visitLhs(self, ctx: D96Parser.LhsContext):
        if(ctx.getChildCount() == 3):
            lhs = self.visit(ctx.lhs())
            fieldName = self.visit(ctx.assignment_static_access())
            return FieldAccess(lhs,fieldName)
        elif (ctx.getChildCount() == 1):
            return self.visit(ctx.assignment_static_access())
    
    def visitAssignment_static_access(self, ctx: D96Parser.Assignment_static_accessContext):
        if ctx.getChildCount() == 3:
            if ctx.element_expression():
                obj = self.visit(ctx.element_expression())
                fieldName = Id(ctx.DOLLARID().getText)
                return FieldAccess(obj, fieldName)
            elif ctx.ID():
                obj = Id(ctx.ID().getText())
                fieldName = Id(ctx.DOLLARID().getText)
                return FieldAccess(obj, fieldName)
            elif ctx.SELF():
                obj = SelfLiteral()
                fieldName = Id(ctx.DOLLARID().getText)
                return FieldAccess(obj, fieldName)
        else:
            if ctx.element_expression():
                return self.visit(ctx.element_expression())
            elif ctx.ID():
                return Id(ctx.ID().getText())
            elif ctx.SELF():
                return SelfLiteral()
    
    def visitElement_expression(self, ctx: D96Parser.Element_expressionContext):
        exp = ctx.exp()
        idx = self.visit(ctx.index_operators())
        return ArrayCell(exp, idx)
    
    def visitIndex_operators(self, ctx: D96Parser.Index_operatorsContext):
        if ctx.getChildCount() == 3:
            return ctx.visit(ctx.exp())
        else:
            expList = []
            expList.append(self.visit(ctx.exp()))
            return expList + self.visit(ctx.index_operators())

    def visitForeach_statements(self, ctx: D96Parser.Foreach_statementsContext):
        # NOTE: Where is the BY expression
        id = Id(ctx.ID().getText())
        expr1 = ctx.exp(0)
        expr2 = ctx.exp(1)
        up = None  # TODO: Fix this problem
        loop = ctx.block_statements()
        return For(id, expr1, expr2, up, loop)
    
    def visitBreak_statements(self, ctx: D96Parser.Break_statementsContext):
        # NOTE: DO we need to use CTX
        return Break()
    
    def visitcontinue_statements(self, ctx: D96Parser.Continue_statementsContext):
        # NOTE: DO we need to use CTX
        return Continue()
    
    def visitReturn_statements(self, ctx: D96Parser.Return_statementsContext):
        expr = self.visit(ctx.exp()) if ctx.exp() else None
        return Return(expr)
    
    def visitMethod_invocations(self, ctx: D96Parser.Method_invocationsContext):
        if ctx.exp():
            if ctx.getChildCount() == 4:
                expr = self.visit(ctx.exp())
                id = Id(ctx.ID().getText())
                return FieldAccess(expr, id)
            else:
                expr = self.visit(ctx.exp())
                id = Id(ctx.ID().getText())
                expList = self.visit(ctx.expList()) if ctx.expList() else []
                return CallStmt(expr, id, expList)
        else:
            # NOTE: In the grammar you write ID not exp
            # NOTE: In the grammar tou wirite Dollar ID
            if ctx.LB():
                expr = self.visit(ctx.ID())
                id = Id(ctx.DOLLARID().getText())
                expList = self.visit(ctx.expList()) if ctx.expList() else []
                return CallStmt(expr, id, expList)
            else:
                expr = self.visit(ctx.ID())
                id = Id(ctx.DOLLARID().getText())
                return FieldAccess(expr, id)
    
    def visitVariable_constant_declaration(self, ctx: D96Parser.Variable_constant_declarationContext):
        idList = self.visit(ctx.variableList())
        mytype = self.visit(ctx.primitive_type())
        if ctx.VAL():
            if ctx.expList():
                expList = self.visit(ctx.expList())
                return [ConstDecl(id, mytype, value) for id, value in zip(idList, expList)]
            else:
                return [ConstDecl(id, mytype, None) for id in idList] 
        elif ctx.VAR():
            if ctx.expList():
                expList = self.visit(ctx.expList())
                return [VarDecl(id, mytype, value) for id, value in zip(idList, expList)]
            else:
                return [VarDecl(id, mytype, None) for id in idList]
    
    def visitVariableList(self, ctx: D96Parser.VariableListContext):
        idList = []
        idList.append(Id(ctx.ID().getText()))
        return idList + self.visit(ctx.iDlist())

    def visitExpList(self, ctx: D96Parser.ExpListContext):
        expList = []
        expList.append(self.visit(ctx.exp()))
        return expList + self.visit(ctx.theRestExp())
    
    def visitTheRestExp(self, ctx: D96Parser.TheRestExpContext):
        if ctx.getChildCount() == 3:
            expList = []
            expList.append(self.visit(ctx.exp()))
            return expList + self.visit(ctx.theRestExp())
        else:
            return []
    
    # Expression
    def visitExp(self, ctx: D96Parser.ExpContext):
        if ctx.getChildCount() == 3:
            leff = self.visit(ctx.relational_operations(0))
            right = self.visit(ctx.relational_operations(1))
            op = self.visit(ctx.string_operators())
            return BinaryOp(op, leff, right)
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.relational_operations(0))
    
    def visitString_operators(self, ctx: D96Parser.String_operatorsContext):
        if ctx.STRINGCOMPARE():
            return ctx.STRINGCOMPARE().getText()
        elif ctx.STRINGCONCAT():
            return ctx.STRINGCONCAT().getText()
    
    def visitRelational_operations(self, ctx: D96Parser.Relational_operationsContext):
        if ctx.getChildCount() == 3:
            leff = self.visit(ctx.logical_operations(0))
            right = self.visit(ctx.logical_operations(1))
            op = self.visit(ctx.relational_operators())
            return BinaryOp(op, leff, right)
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.logical_operations(0))
    
    def visitRelational_operators(self, ctx: D96Parser.Relational_operatorsContext):
        if ctx.EQUAL():
            return ctx.EQUAL().getText()
        elif ctx.DIFFERENT():
            return ctx.DIFFERENT().getText()
        elif ctx.LESSER():
            return ctx.LESSER().getText()
        elif ctx.LESSTHANEQUAL():
            return ctx.LESSTHANEQUAL().getText()
        elif ctx.GREATER():
            return ctx.GREATER().getText()
        elif ctx.GREATERTHANEQUAL():
            return  ctx.GREATERTHANEQUAL().getText()
    
    def visitLogical_operations(self, ctx: D96Parser.Logical_operationsContext):
        if ctx.getChildCount() == 3:
            leff = self.visit(ctx.logical_operations())
            right = self.visit(ctx.adding_operations())
            op = self.visit(ctx.logical_and_or())
            return BinaryOp(op, leff, right)
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.adding_operations())
    
    def visitLogical_and_or(self, ctx: D96Parser.Logical_and_orContext):
        if ctx.AND():
            return ctx.AND().getText()
        elif ctx.OR():
            return ctx.OR().getText()
    
    def visitAdding_operations(self, ctx: D96Parser.Adding_operationsContext):
        if ctx.getChildCount() == 3:
            leff = self.visit(ctx.adding_operations())
            right = self.visit(ctx.multiplying_operations())
            op = self.visit(ctx.adding_operators())
            return BinaryOp(op, leff, right)
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.multiplying_operations())
    
    def visitAdding_operators(self, ctx: D96Parser.Adding_operatorsContext):
        if ctx.PLUS():
            return ctx.PLUS().getText()
        elif ctx.MINUS():
            return ctx.MINUS().getText()
    
    def visitMultiplying_operations(self, ctx: D96Parser.Multiplying_operationsContext):
        if ctx.getChildCount() == 3:
            leff = self.visit(ctx.multiplying_operations())
            right = self.visit(ctx.logical_negate_operation())
            op = self.visit(ctx.multiplying_operators())
            return BinaryOp(op, leff, right)
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.logical_negate_operation())
    
    def visitMultiplying_operator(self, ctx: D96Parser.Multiplying_operatorsContext):
        if ctx.MULTIPLY():
            return ctx.MULTIPLY().getText()
        elif ctx.DIVIDE():
            return ctx.DIVIDE().getText()
        elif ctx.MODULO():
            return ctx.MODULO().getText()
    
    def visitLogical_negate_operation(self, ctx: D96Parser.Logical_negate_operationContext):
        if ctx.getChildCount() == 2:
            body = self.visit(ctx.logical_negate_operation())
            op = ctx.NEGATE().getText()
            return UnaryOp(op, body)
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.sign_operations())
    
    def visitSign_operations(self, ctx: D96Parser.Sign_operationsContext):
        if ctx.getChildCount() == 2:
            body = self.visit(ctx.sign_operations())
            op = ctx.MINUS().getText()
            return UnaryOp(op, body)
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.index_operations())
    
    def visitIndex_operations(self, ctx: D96Parser.Index_operationsContext):
        if ctx.getChildCount() == 2:
            body = self.visit(ctx.index_operations())
            op = self.visit(ctx.index_operators())
            return UnaryOp(op, body)
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.intance_access_operarion())
    
    def visitIntance_access_operarion(self, ctx: D96Parser.Intance_access_operarionContext):
        if ctx.getChildCount() == 3:
            obj = self.visit(ctx.intance_access_operarion())
            fieldName = self.visit(ctx.static_access_operation())
            return FieldAccess(obj,fieldName)
        elif ctx.LB():
            obj = self.visit(ctx.intance_access_operarion())
            method = self.visit(ctx.static_access_operation())
            param = self.visit(ctx.expList()) if ctx.expList() else []
            return CallExpr(obj, method, param)
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.static_access_operation())
        
    def visitStatic_access_operation(self, ctx : D96Parser.Static_access_operationContext):
        if ctx.getChildCount() == 3:
            obj = self.visit(ctx.object_create_operation())
            fieldName = self.visit(ctx.DOLLARID().getText())
            return FieldAccess(obj,Id(fieldName))
        elif ctx.LB():
            obj = self.visit(ctx.object_create_operation())
            method = self.visit(ctx.DOLLARID().getText())
            param = self.visit(ctx.expList()) if ctx.expList() else []
            return CallExpr(obj, Id(method), param)
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.object_create_operation())
    
    def visitObject_create_operation(self, ctx: D96Parser.Object_create_operationContext):
        if ctx.NEW():
            className = self.visit(ctx.object_create_operation())
            idx = self.visit(ctx.expList()) if ctx.expList() else []
            return NewExpr(className, idx)
        elif ctx.parenthesis_operations():
            return self.visit(ctx.parenthesis_operations())
    
    def visitParenthesis_operations(self, ctx: D96Parser.Parenthesis_operationsContext):
        if ctx.exp():
            return self.visit(ctx.exp())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.BOOLEANLIT():
            return BooleanLiteral(ctx.BOOLEANLIT().getText() == 'True')
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.array_lit():
            return self.visit(ctx.array_lit())
        elif ctx.SELF():
            return SelfLiteral()
        elif ctx.NULL():
            return NullLiteral()
    
    def visitArray_lit(self, ctx: D96Parser.Array_litContext):
        literralList = self.visit(ctx.expList())
        return ArrayLiteral(literralList)










