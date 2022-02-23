import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """
        Class Duong
        {
            main()
            {
                
            }
        }
        """
        expect = "aada"
        self.assertTrue(TestAST.test(input,expect,300))

   