from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *



class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program([self.visit(x) for x in ctx.class_declaration()])
    def visitClass_declaration(self, ctx: D96Parser.Class_declarationContext):
        classID = Id(ctx.ID(0).getText())
        parentClass = Id(ctx.ID(1).getText()) if len(ctx.ID()) == 2 else None
        memberList = self.visit(ctx.attributes_methods_declarations())
        return ClassDecl(classID, memberList, parentClass)

    def visitAttributes_methods_declarations(self,ctx: D96Parser.Attributes_methods_declarationsContext):
        memberList : List[MemDecl] = []
        if (ctx.attribute_declaration()):
            memberList = memberList + self.visit(ctx.attribute_declaration())
            return memberList + self.visit(ctx.the_rest_attributes_methods_declarations())
        elif (ctx.method_declaration()):
            memberList.append(self.visit(ctx.method_declaration()))
            return memberList + self.visit(ctx.the_rest_attributes_methods_declarations())
        return memberList

    def visitThe_rest_attributes_methods_declarations(self,ctx: D96Parser.The_rest_attributes_methods_declarationsContext):
        memberList : List[MemDecl] = []
        if (ctx.attribute_declaration()):
            memberList = memberList + self.visit(ctx.attribute_declaration())
            return memberList + self.visit(ctx.the_rest_attributes_methods_declarations())
        elif (ctx.method_declaration()):
            memberList.append(self.visit(ctx.method_declaration()))
            return memberList + self.visit(ctx.the_rest_attributes_methods_declarations())
        return []

    def visitAttribute_declaration(self, ctx: D96Parser.Attribute_declarationContext):
        # NOTE: If number of exps is not equal to the attribute list, then what???
        attribList = self.visit(ctx.attributesList())
        temp = self.visit(ctx.expList()) if ctx.expList() else None
        if temp:
            assert len(temp) == len(attribList), "Not enough expressions"
        expList = temp if ctx.expList() else [None] * len(attribList)
        mytype = self.visit(ctx.primitive_type())
        if isinstance(mytype, ClassType):
            if temp == None:
                expList = [NullLiteral()] * len(attribList)
        constList = [(name, mytype, value) for name, value in zip (attribList, expList)]
        if ctx.VAL():
            return [AttributeDecl(Instance(), ConstDecl(myId, myType, myValue)) if str(myId)[3] !='$' else 
                    AttributeDecl(Static(), ConstDecl(myId, myType, myValue)) for myId, myType, myValue in constList]
        elif ctx.VAR():
            return [AttributeDecl(Instance(), VarDecl(myId, myType, myValue)) if str(myId)[3] !='$' else 
                    AttributeDecl(Static(), VarDecl(myId, myType, myValue)) for myId, myType, myValue in constList]
    def visitAttributesList(self, ctx: D96Parser.AttributesListContext):
        ### NOTE #### : Do we keep dollar sign
        attributelist = [Id(ctx.getChild(0).getText())]
        return attributelist + self.visit(ctx.iDlist())
    
    def visitIDlist(self, ctx: D96Parser.IDlistContext):
        if ctx.getChildCount() == 3:
            attributelist = [Id(ctx.getChild(1).getText())]
            return attributelist + self.visit(ctx.iDlist())
        else: return []
    
    def visitMethod_declaration(self,ctx: D96Parser.Method_declarationContext):
        if ctx.getChildCount() == 5:
            kind = Static() if ctx.getChild(0).getText()[0] == '$' else Instance() 
            name = Id(ctx.getChild(0).getText())
            param = self.visit(ctx.list_parameters())
            body = self.visit(ctx.block_statements())
            if str(name) == "Id(main)" and len(param) == 0:
                temp = ctx
                while(not isinstance(temp, D96Parser.Class_declarationContext)):
                    temp = temp.parentCtx
                if temp.ID(0).getText()== 'Program':
                    kind = Static()
            return MethodDecl(kind, name, param, body)
        elif ctx.getChildCount() == 1:
            if ctx.constructor():
                return self.visit(ctx.constructor())
            elif ctx.destructor():
                return self.visit(ctx.destructor())
    
    def visitDestructor(self, ctx: D96Parser.DestructorContext):
        myID = Id('Destructor')
        param = []
        body = self.visit(ctx.block_statements())
        return MethodDecl(Instance(),myID, param, body)
    
    def visitConstructor(self, ctx: D96Parser.ConstructorContext):
            name = Id("Constructor")
            param = self.visit(ctx.list_parameters())
            body = self.visit(ctx.block_statements())
            return MethodDecl(Instance(), name, param, body)
    
    def visitList_parameters(self, ctx: D96Parser.List_parametersContext):
        if ctx.getChildCount() == 2:
            paraList =  self.visit(ctx.parameters_declaration())
            return paraList + self.visit(ctx.the_rest_parameters_declarations())
        else: return []

    def visitThe_rest_parameters_declarations(self, ctx: D96Parser.The_rest_parameters_declarationsContext):
        if ctx.getChildCount() == 3:
            paraList = self.visit(ctx.parameters_declaration())
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
        numText = ctx.INTLIT().getText()
        size = 0
        if numText == '0' or numText == '00':
            size = 0
        elif numText[0] == '0' and (numText[1] == 'x' or numText[1] == 'X'):
            size = int(numText,16)
        elif numText[0] == '0' and (numText[1] == 'B' or numText[1] == 'b'):
            size = int(numText,2)
        elif numText[0] == '0':
            size = int('0o' + numText[1:],8)
        else:
            size = int(numText)
        assert size > 0, "Size of array must be greater then 0"
        # NOTE: Do we use int or INTLIT for size
        return ArrayType(size, eleType)
    
    def visitBlock_statements(self,ctx: D96Parser.Block_statementsContext):
        lstStm  = self.visit(ctx.list_statement())
        return Block(lstStm)
    
    def visitList_statement(self, ctx: D96Parser.List_statementContext):
        if ctx.getChildCount() == 2:
            lstStm = []
            newEle = self.visit(ctx.single_statement())
            if isinstance(newEle, list):
                lstStm = newEle
            else:
                lstStm.append(newEle)
            return lstStm + self.visit(ctx.the_rest_statements())
        else:
            return []
    
    def visitThe_rest_statements(self, ctx: D96Parser.The_rest_statementsContext):
        if ctx.getChildCount() == 2:
            lstStm = []
            newEle = self.visit(ctx.single_statement())
            if isinstance(newEle, list):
                lstStm = newEle
            else:
                lstStm.append(newEle)
            return lstStm + self.visit(ctx.the_rest_statements())
        else:
            return []
    
    def visitSingle_statement(self, ctx: D96Parser.Single_statementContext):
        if ctx.if_statements():
            return self.visit(ctx.if_statements())
        elif ctx.assignment_statements():
            return self.visit(ctx.assignment_statements())
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
        elif ctx.block_statements():
            return self.visit(ctx.block_statements())
    
    def visitIf_statements(self, ctx : D96Parser.If_statementsContext): 
        expr  = self.visit(ctx.exp())
        thenStmt = self.visit(ctx.block_statements())
        if ctx.else_ifList():
            elseifList = self.visit(ctx.else_ifList())
            initValue = self.visit(ctx.else_statements()) if ctx.else_statements() else None
            elseifList[-1].elseStmt = initValue
            for i in range(len(elseifList) -2, -1, -1):
                elseifList[i].elseStmt = elseifList[i+1]
            return If(expr, thenStmt, elseifList[0])
        else:
            elseStmt = self.visit(ctx.else_statements()) if ctx.else_statements() else None
            return If(expr, thenStmt, elseStmt)

    def visitElse_ifList(self, ctx: D96Parser.Else_ifListContext):
        return [self.visit(ctx.else_if())] + self.visit(ctx.the_rest_else_if())

    def visitThe_rest_else_if(self, ctx: D96Parser.The_rest_else_ifContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return [self.visit(ctx.else_if())] + self.visit(ctx.the_rest_else_if())
    
    def visitElse_if(self, ctx: D96Parser.Else_ifContext):
        exp = self.visit(ctx.exp())
        thenStmt = self.visit(ctx.block_statements())
        return If(exp, thenStmt, None)

    def visitElse_statements(self, ctx: D96Parser.Else_statementsContext):
        return self.visit(ctx.block_statements())
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
            if ctx.index_operations():
                obj = self.visit(ctx.index_operations())
                fieldName = Id(ctx.DOLLARID().getText())
                return FieldAccess(obj, fieldName)
            elif ctx.ID():
                obj = Id(ctx.ID().getText())
                fieldName = Id(ctx.DOLLARID().getText())
                return FieldAccess(obj, fieldName)
            elif ctx.SELF():
                obj = SelfLiteral()
                fieldName = Id(ctx.DOLLARID().getText())
                return FieldAccess(obj, fieldName)
        else:
            if ctx.index_operations():
                return self.visit(ctx.index_operations())
            elif ctx.ID():
                return Id(ctx.ID().getText())
            elif ctx.SELF():
                return SelfLiteral()
    
    # def visitElement_expression(self, ctx: D96Parser.Element_expressionContext):
    #     exp = self.visit(ctx.exp())
    #     idx = self.visit(ctx.index_operators())
    #     return ArrayCell(exp, idx)
    
    def visitIndex_operators(self, ctx: D96Parser.Index_operatorsContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.exp())]
        else:
            expList = []
            expList.append(self.visit(ctx.exp()))
            return expList + self.visit(ctx.index_operators())

    def visitForeach_statements(self, ctx: D96Parser.Foreach_statementsContext):
        id = Id(ctx.ID().getText())
        expr1 = self.visit(ctx.exp(0))
        expr2 = self.visit(ctx.exp(1))
        expr3 = self.visit(ctx.exp(2)) if len(ctx.exp()) == 3 else IntLiteral(1)
        loop = self.visit(ctx.block_statements()) # NOTE: A single statement or a block
        return For(id, expr1, expr2, loop, expr3)
    
    def visitBreak_statements(self, ctx: D96Parser.Break_statementsContext):
        # NOTE: DO we need to use CTX
        return Break()
    
    def visitContinue_statements(self, ctx: D96Parser.Continue_statementsContext):
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
                expr = Id(ctx.ID().getText())
                id = Id(ctx.DOLLARID().getText())
                expList = self.visit(ctx.expList()) if ctx.expList() else []
                return CallStmt(expr, id, expList)
            else:
                expr = Id(ctx.ID().getText())
                id = Id(ctx.DOLLARID().getText())
                return FieldAccess(expr, id)
    
    def visitVariable_constant_declaration(self, ctx: D96Parser.Variable_constant_declarationContext):
        idList = self.visit(ctx.variableList())
        mytype = self.visit(ctx.primitive_type())
        if ctx.VAL():
            if ctx.expList():
                expList = self.visit(ctx.expList())
                assert len(expList) == len(idList), "Not enough expressions"
                return [ConstDecl(id, mytype, value) for id, value in zip(idList, expList)]
            else:
                return [ConstDecl(id, mytype, NullLiteral()) for id in idList] if isinstance(mytype,ClassType) else  [ConstDecl(id, mytype, None) for id in idList]
        elif ctx.VAR():
            if ctx.expList():
                expList = self.visit(ctx.expList())
                assert len(expList) == len(idList), "Not enough expressions"
                return [VarDecl(id, mytype, value) for id, value in zip(idList, expList)]
            else:
                return [VarDecl(id, mytype, NullLiteral()) for id in idList ] if isinstance(mytype,ClassType) else [VarDecl(id, mytype, None) for id in idList ]
    
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
            left = self.visit(ctx.multiplying_operations())
            right = self.visit(ctx.logical_negate_operation())
            op = self.visit(ctx.multiplying_operators())
            return BinaryOp(op, left, right)
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.logical_negate_operation())
    
    def visitMultiplying_operators(self, ctx: D96Parser.Multiplying_operatorsContext):
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
            return ArrayCell(body, op)
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
            fieldName = ctx.DOLLARID().getText()
            return FieldAccess(obj,Id(fieldName))
        elif ctx.LB():
            obj = self.visit(ctx.object_create_operation())
            method = Id(ctx.DOLLARID().getText())
            param = self.visit(ctx.expList()) if ctx.expList() else []
            return CallExpr(obj, method, param)
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.object_create_operation())
    
    def visitObject_create_operation(self, ctx: D96Parser.Object_create_operationContext):
        if ctx.NEW():
            className = Id(ctx.ID().getText())
            idx = self.visit(ctx.expList()) if ctx.expList() else []
            return NewExpr(className, idx)
        elif ctx.parenthesis_operations():
            return self.visit(ctx.parenthesis_operations())
    
    def visitParenthesis_operations(self, ctx: D96Parser.Parenthesis_operationsContext):
        if ctx.exp():
            return self.visit(ctx.exp())
        elif ctx.INTLIT():
            numText = ctx.INTLIT().getText()
            if numText == '0' or numText == '00':
                return IntLiteral(0)
            elif numText[0] == '0' and (numText[1] == 'x' or numText[1] == 'X'):
                return IntLiteral(int(numText,16))
            elif numText[0] == '0' and (numText[1] == 'B' or numText[1] == 'b'):
                return IntLiteral(int(numText,2))
            elif numText[0] == '0':
                return IntLiteral(int('0o' + numText[1:],8))
            else:
                return IntLiteral(int(numText)) 
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.BOOLEANLIT():
            return BooleanLiteral(ctx.BOOLEANLIT().getText() == 'True')
        elif ctx.FLOATLIT():
            num = ctx.FLOATLIT().getText()
            if num[0] == '.':
                num = '0' + num
            return FloatLiteral(float(num))
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.array_lit():
            return self.visit(ctx.array_lit())
        elif ctx.SELF():
            return SelfLiteral()
        elif ctx.NULL():
            return NullLiteral()
    
    def visitArray_lit(self, ctx: D96Parser.Array_litContext):
        literralList = self.visit(ctx.expList()) if ctx.expList() else []
        return ArrayLiteral(literralList)










