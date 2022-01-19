import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_INTLIT(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1234 0123 0x1A 0b11111111 1__234_567","1234,0123,0x1A,0b11111111,1,__234_567,<EOF>",101))
    def test_FLOATLIT(self):
        self.assertTrue(TestLexer.test("1.234  1.2e3 7E-10 0.0 0 1_2345.562E-10002","1.234,1.2e3,7E-10,0.0,0,12345.562E-10002,<EOF>",102))
    def test_STRINGLIT(self):
        self.assertTrue(TestLexer.test("\"This is a string containing tab \\t\" \"He asked me: '\"Where is John?'\"\"","This is a string containing tab \\t,He asked me: '\"Where is John?'\",<EOF>",103))
    #     \"This is a string containing tab \t\" \"He asked me: '\"Where is John?'\"\"
    #     \" \"abc\\\\h def\"\"abc\\h def\"
    def test_special_keywords(self):
        """test integers"""
        self.assertTrue(TestLexer.test("Var Break Class Var True == && Continue If","Var,Break,Class,Var,True,==,&&,Continue,If,<EOF>",104))
    def test_comment(self):
        self.assertTrue(TestLexer.test("##This is a comment##  ##\"Another Co\\mment\"##Var $x, $y : Int = 0,0","Var,$,x,,,$,y,:,Int,=,0,,,0,<EOF>",105))
    def test_long_programm1(self):
        self.assertTrue(TestLexer.test("Class Program { main () { Out.printInt(Shape::$numOfShape);##I want to print the how many shapes##}}","Class,Program,{,main,(,),{,Out,.,printInt,(,Shape,::,$,numOfShape,),;,},},<EOF>",106))
    def test_sepecial_float(self):
        self.assertTrue(TestLexer.test("123e-56 .123e-12 123.45 123_56.895e-200 0.0 0 0123 123_561","123e-56,.123e-12,123.45,12356.895e-200,0.0,0,0123,123561,<EOF>", 107))
    def test_long_programm2(self):
        self.assertTrue(TestLexer.test("""Class Shape { Val $numOfShape: Int = 0; Val immutableAttribute: Int = 0; Var length, width: Int; }
        $getNumofShape() {
            this.lenght = 200_5000e-1123;
            Return $numOfShape;
        }""","Class,Shape,{,Val,$,numOfShape,:,Int,=,0,;,Val,immutableAttribute,:,Int,=,0,;,Var,length,,,width,:,Int,;,},$,getNumofShape,(,),{,this,.,lenght,=,2005000e-1123,;,Return,$,numOfShape,;,},<EOF>",108))
    def test_float1(self):
        self.assertTrue(TestLexer.test("0.27  2.73  0.1  2.  1e1  1e0  1.e10  20.e+22","0.27,2.73,0.1,2.,1e1,1e0,1.e10,20.e+22,<EOF>",109))
    def test_float2(self):
        self.assertTrue(TestLexer.test("2_73.2E-3  27.73e5  2.e0   456_321.0e-123  1_0.001e-5  .3e4 .1e12","273.2E-3,27.73e5,2.e0,456321.0e-123,10.001e-5,.3e4,.1e12,<EOF>",110))

    def test_integer1(self):
        """test integers1"""
        self.assertTrue(TestLexer.test("0x11_1 29_34 1_23 0xA_AACD 0b0_111 0b100_100_1001 234_456_789 0XABC_DEF1_2345_6789 0101_123_456_7","0x111,2934,123,0xAAACD,0b0111,0b1001001001,234456789,0XABCDEF123456789,01011234567,<EOF>",111))
    def test_STRINGLIT(self):
        self.assertTrue(TestLexer.test("\"This is a \\t string \\n containing tab \" \"He asked me: '\"Where is John?'\"\"","This is a \\t string \\n containing tab ,He asked me: '\"Where is John?'\",<EOF>",112))
    def test_STRINGLIT2(self):
        self.assertTrue(TestLexer.test("\"This is a \\t string \\n containing tab \" \"He asked \\n me: '\"Where '\"is'\" John?'\"\"","This is a \\t string \\n containing tab ,He asked \\n me: '\"Where '\"is'\" John?'\",<EOF>",113))
    def test_STRING_unclosed(self):
        self.assertTrue(TestLexer.test("\"This is a \\t string \\n containing tab \" \"He asked \\n me: '\"Where '\"is'\" John?'\"\" \"I am not closed","This is a \\t string \\n containing tab ,He asked \\n me: '\"Where '\"is'\" John?'\",Unclosed String: I am not closed",114))
    def test_STRING_unclosed(self):
        self.assertTrue(TestLexer.test("\"I have an escape sequence '\"Here it is \\n'\"\"","I have an escape sequence '\"Here it is \\n'\",<EOF>",115))
    
    def test_STRING_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("\"I have an escape sequence '\"Here it is \\n'\"\"","I have an escape sequence '\"Here it is \\n'\",<EOF>",116))
    def test_STRING_illegal_escape(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("\"I have an escape sequence '\"Here it is \\k' here it is\"\"","Illegal Escape In String: I have an escape sequence '\"Here it is \\k",117))
    def test_unclosed_string2(self):
        self.assertTrue(TestLexer.test("\"It is a unclosed \\n string", "Unclosed String: It is a unclosed \\n string", 118))
    def test_unclosed_string3(self):
        self.assertTrue(TestLexer.test("\"It is a \\k unclosed \\n string", "Illegal Escape In String: It is a \\k", 119))
    def test_long_program2(self):
        string_test = """Class Person 
        {
            Var $numPeople: Int = 0;
            Var name: String;
        }
        """
        self.assertTrue(TestLexer.test(string_test,'Class,Person,{,Var,$,numPeople,:,Int,=,0,;,Var,name,:,String,;,},<EOF>', 120))
    def test_long_program3(self):
        string_test = """Class Program
        {
            main ()
            {
                Var name: String = "Hello How are you \\n";
                Val number: Int = 10;
                Out.printInt(number); 
            }
        }"""
        expected_result = """Class,Program,{,main,(,),{,Var,name,:,String,=,Hello How are you \\n,;,Val,number,:,Int,=,10,;,Out,.,printInt,(,number,),;,},},<EOF>"""
        self.assertTrue(TestLexer.test(string_test, expected_result,121))
    def test_long_program_escape (self):
        string_test = """
        Class Program
        {
            main ()
            {
                Var name: String = "Hello How are you \\n";
                Var answer: String = "I am fine \\\\ Thank you \\'"
                Val number: Int = 10;
                Out.printInt(number); 
            }
        }""" 
        string_expected = """Class,Program,{,main,(,),{,Var,name,:,String,=,Hello How are you \\n,;,Var,answer,:,String,=,I am fine \\\\ Thank you \\',Val,number,:,Int,=,10,;,Out,.,printInt,(,number,),;,},},<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 122))
    def test_illegal_escap (self):
        string_test = """
        Class Program
        {
            main ()
            {
                Var name: String = "Hello How are you \\n";
                Var answer: String = "I am fine \\\\ Thank you \\'"
                Var $radisu: Float = 123_456.e-23
                Val number: Int = 10;
                Var new_string: String = "I am newww \\d"
                Out.printInt(number); 
            }
        }""" 
        string_expected = """Class,Program,{,main,(,),{,Var,name,:,String,=,Hello How are you \\n,;,Var,answer,:,String,=,I am fine \\\\ Thank you \\',Var,$,radisu,:,Float,=,123456.e-23,Val,number,:,Int,=,10,;,Var,new_string,:,String,=,Illegal Escape In String: I am newww \d"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 123))
    def test_unclosed_string (self):
        string_test = """
        Class Program
        {
            main ()
            {

                Var $radisu: Float = 123_456.e-23
                Val number: Int = 10;
                Out.printInt(number); 
            }
        }
        Var new_string: String = "I am newww \\n
        """ 
        string_expected = """Class,Program,{,main,(,),{,Var,$,radisu,:,Float,=,123456.e-23,Val,number,:,Int,=,10,;,Out,.,printInt,(,number,),;,},},Var,new_string,:,String,=,Unclosed String: I am newww \\n

        """
        self.assertTrue(TestLexer.test(string_test, string_expected, 124))
    def test_ID (self):
        string_test = """__ABC""" 
        string_expected = """__ABC,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 125))
    def test8_ID (self):
        string_test = """__123""" 
        string_expected = """__123,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 126))
    def test9_binary (self):
        string_test = """0b0000""" 
        string_expected = """0b0000,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 127))
    def test10 (self):
        string_test = """True""" 
        string_expected = """True,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 128))
    def test11 (self):
        string_test = """true""" 
        string_expected = """true,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 129))
    def test12 (self):
        string_test = """0B0_0""" 
        string_expected = """0B00,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 130))
    def test13 (self):
        string_test = """12e01""" 
        string_expected = """12e0,1,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 131))
    def test14 (self):
        string_test = """0B00_""" 
        string_expected = """0B00,_,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 132))
    def test15 (self):
        string_test = """0b_00""" 
        string_expected = """0,b_00,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 133))
    def test16 (self):
        string_test = """0_b00""" 
        string_expected = """0,_b00,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 134))
    def test17 (self):
        string_test = """1_.23""" 
        string_expected = """1,_,.,23,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 135))
    def test18 (self):
        string_test = """12e01""" 
        string_expected = """12e0,1,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 136))
    def test19 (self):
        string_test = """0x0123_456_789_ABC_DEF""" 
        string_expected = """0x0123456789ABCDEF,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 137))
    # def test20 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 138))
    # def test21 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 139))
    # def test22 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 140))
    # def test23 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 141))
    # def test24 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 142)
    # def test25 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 143)
    # def test26 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 144)
    # def test27 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 145)
    # def test28 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 146)
    # def test29 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 147)
    # def test30 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 148)
    # def test31 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 149)
    # def test32 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 150)
    # def test33 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 151)
    # def test34 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 152)
    # def test35 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 153)
    # def test36 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 154)
    # def test37 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 155)
    # def test38 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 156)
    # def test39 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 157)
    # def test40 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 158)
    # def test41 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 159)
    # def test42 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 160)
    # def test43 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 161)
    # def test44 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 162)
    # def test45 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 163)
    # def test46 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 164)
    # def test47 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 165)
    # def test48 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 166)
    # def test49 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 167)
    # def test50 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 168)
    # def test51 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 169)
    # def test52 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 170)
    # def test53 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 171)
    # def test54 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 172)
    # def test55 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 173)
    # def test56 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 174)
    # def test57 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 175)
    # def test58 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 176)
    # def test59 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 177)
    # def test60 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 178)
    # def test61 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 179)
    # def test62 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 180)
    # def test63 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 181)
    # def test64 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 182)
    # def test65 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 183)
    # def test66 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 184)
    # def test67 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 185)
    # def test68 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 186)
    # def test69 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 187)
    # def test70 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 188)
    # def test71 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 189)
    # def test72 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 190)
    # def test73 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 191)
    # def test74 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 192)
    # def test75 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 193)
    # def test76 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 194)
    # def test77 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 195)
    # def test78 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 196)
    # def test79 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 197)
    # def test80 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 198)
    # def test81 (self):
    #     string_test = """""" 
    #     string_expected = """"""
    #     self.assertTrue(TestLexer.test(string_test, string_expected, 199)