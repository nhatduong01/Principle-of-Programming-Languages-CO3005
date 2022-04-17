import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """
        Class Program
        {
            main ()
            {
            Var Num: Int = 1 + 3;
            System.out.printLn(Num);
            }
        }""" 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(Num),IntType,BinaryOp(+,IntLit(1),IntLit(3))),Call(FieldAccess(Id(System),Id(out)),Id(printLn),[Id(Num)])]))])])"""
        self.assertTrue(TestAST.test(input,expect,310))
   