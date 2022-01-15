import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    # def test_INTLIT(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("1234 0123 0x1A 0b11111111 1__234_567","Float,<EOF>",101))
    # def test_FLOATLIT(self):
    #     self.assertTrue(TestLexer.test("1.234  1.2e3 7E-10 0.0 0 1_2345.562E-10002","aCBbdc,<EOF>",102))
    # def test_STRINGLIT(self):
    #     self.assertTrue(TestLexer.test("\"This is a string containing tab \t\" \"He asked me: '\"Where is John?'\"\" \"abc\\\\h def\"\"abc\\h def\"","aAsVN,3,<EOF>",103))
    # def test_special_keywords(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.test("Var Break Class Var True == && Continue If","123,a,123,<EOF>",104))
    # def test_comment(self):
    #     self.assertTrue(TestLexer.test("##This is a comment##  ##\"Another Comment\"##Var $x, $y : Int = 0,0","non",105))
    # def test_long_programm1(self):
    #     self.assertTrue(TestLexer.test("Class Program { main () { Out.printInt(Shape::$numOfShape);##I want to print the how many shapes##}}","non",106))
    def test_sepecial_float(self):
        self.assertTrue(TestLexer.test("123e-56 .123e-12 123.45 123_56.895e-200 0.0 0 0123 123_561","Non", 107))