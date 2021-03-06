import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_1(self):
        input = """
        Class Program {
               main() {
    
               }
            }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test_2(self):
        input = """
        Class Program
        {
            foo(a: Int ; b: Float)
            {
                
            }
            main()
            {

            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 501))
