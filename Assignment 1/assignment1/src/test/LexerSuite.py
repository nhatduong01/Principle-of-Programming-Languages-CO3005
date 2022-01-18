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
    # def test_sepecial_float(self):
    #     self.assertTrue(TestLexer.test("123e-56 .123e-12 123.45 123_56.895e-200 0.0 0 0123 123_561","Non", 107))
    # def test_long_programm2(self):
    #     self.assertTrue(TestLexer.test("""Class Shape { Val $numOfShape: Int = 0; Val immutableAttribute: Int = 0; Var length, width: Int; }
    #     $getNumofShape() {
    #         this.lenght = 200_5000e-1123;
    #         return $numOfShape;
    #     }""","non",107))
    # def test_float1(self):
    #     self.assertTrue(TestLexer.test("0.27  2.73  0.1  2.  1e1  1e0  1.e10  20.e+22","0.27,2.73,0.1,2.,1e1,1e0,1.e10,20.e+22,<EOF>",108))
    #def test_float2(self):
    #    self.assertTrue(TestLexer.test("2_73.2E-3  27.73e5  2.e0   456_321.0e-123  1_0.001e-5  .3e4 .1e12","273.2E-3,27.73e5,2.e0,456321.0e-123,10.001e-5,.3e4,.1e12,<EOF>",109))

    # def test_integer1(self):
    #     """test integers1"""
    #     self.assertTrue(TestLexer.test("0x11_1 29_34 1_23 0xA_AACD 0b0_111 0_0_112 0b100_100_1001 234_456_789 0XABC_DEF1_2345_6789 0101_123_456_7","0x111,2934,123,0xAAACD,0b0111,00112,0b1001001001,234456789,0XABCDEF123456789,01011234567,<EOF>",110))
    def test_unclosedString(self):
        """test integers1"""
        self.assertTrue(TestLexer.test("0x11_1 29_34 1_23 0xA_AACD 0b0_111 0_0_112 0b100_100_1001 234_456_789 0XABC_DEF1_2345_6789 0101_123_456_7","0x111,2934,123,0xAAACD,0b0111,00112,0b1001001001,234456789,0XABCDEF123456789,01011234567,<EOF>",110))