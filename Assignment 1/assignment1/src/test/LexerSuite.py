import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_keywords(self):
        self.assertTrue(TestLexer.test("123_456_789","123456789,<EOF>",100))
    def test_INTLIT(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1234 0123 0x1A 0b11111111 1__234_567","1234,0123,0x1A,0b11111111,1,__234_567,<EOF>",101))
    def test_FLOATLIT(self):
        self.assertTrue(TestLexer.test("1.234  1.2e3 7E-10 0.0 0 1_2345.562E-10002","1.234,1.2e3,7E-10,0.0,0,12345.562E-10002,<EOF>",102))
    def test_STRINGLIT0(self):
        self.assertTrue(TestLexer.test("\"This is a string containing tab \\t\" \"He asked me: '\"Where is John?'\"\"","This is a string containing tab \\t,He asked me: '\"Where is John?'\",<EOF>",103))
    #     \"This is a string containing tab \t\" \"He asked me: '\"Where is John?'\"\"
    #     \" \"abc\\\\h def\"\"abc\\h def\"
    def test_special_keywords(self):
        """test integers"""
        self.assertTrue(TestLexer.test("Var Break Class Var True == && Continue If","Var,Break,Class,Var,True,==,&&,Continue,If,<EOF>",104))
    def test_comment(self):
        self.assertTrue(TestLexer.test("##This is a comment##  ##\"Another Co\\mment\"##Var $x, $y : Int = 0,0","Var,$x,,,$y,:,Int,=,0,,,0,<EOF>",105))
    def test_long_programm1(self):
        self.assertTrue(TestLexer.test("Class Program { main () { Out.printInt(Shape::$numOfShape);##I want to print the how many shapes##}}","Class,Program,{,main,(,),{,Out,.,printInt,(,Shape,::,$numOfShape,),;,},},<EOF>",106))
    def test_sepecial_float(self):
        self.assertTrue(TestLexer.test("123e-56 .123e-12 123.45 123_56.895e-200 0.0 0 0123 123_561","123e-56,.123e-12,123.45,12356.895e-200,0.0,0,0123,123561,<EOF>", 107))
    def test_long_programm2(self):
        self.assertTrue(TestLexer.test("""Class Shape { Val $numOfShape: Int = 0; Val immutableAttribute: Int = 0; Var length, width: Int; }
        $getNumofShape() {
            this.lenght = 200_5000e-1123;
            Return $numOfShape;
        }""","Class,Shape,{,Val,$numOfShape,:,Int,=,0,;,Val,immutableAttribute,:,Int,=,0,;,Var,length,,,width,:,Int,;,},$getNumofShape,(,),{,this,.,lenght,=,2005000e-1123,;,Return,$numOfShape,;,},<EOF>",108))
    def test_float1(self):
        self.assertTrue(TestLexer.test("0.27  2.73  0.1  2.  1e1  1e0  1.e10  20.e+22","0.27,2.73,0.1,2.,1e1,1e0,1.e10,20.e+22,<EOF>",109))
    def test_float2(self):
        self.assertTrue(TestLexer.test("2_73.2E-3  27.73e5  2.e0   456_321.0e-123  1_0.001e-5  .3e4 .1e12","273.2E-3,27.73e5,2.e0,456321.0e-123,10.001e-5,.3e4,.1e12,<EOF>",110))

    def test_integer1(self):
        """test integers1"""
        self.assertTrue(TestLexer.test("0x11_1 29_34 1_23 0xA_AACD 0b0_111 0b100_100_1001 234_456_789 0XABC_DEF1_2345_6789 0101_123_456_7","0x111,2934,123,0xAAACD,0b0,_111,0b1001001001,234456789,0XABCDEF123456789,01011234567,<EOF>",111))
    def test_STRINGLIT(self):
        self.assertTrue(TestLexer.test("\"This is a \\t string \\n containing tab \" \"He asked me: '\"Where is John?'\"\"","This is a \\t string \\n containing tab ,He asked me: '\"Where is John?'\",<EOF>",112))
    def test_STRINGLIT2(self):
        self.assertTrue(TestLexer.test("\"This is a \\t string \\n containing tab \" \"He asked \\n me: '\"Where '\"is'\" John?'\"\"","This is a \\t string \\n containing tab ,He asked \\n me: '\"Where '\"is'\" John?'\",<EOF>",113))
    def test_STRING_unclosed(self):
        self.assertTrue(TestLexer.test("\"This is a \\t string \\n containing tab \" \"He asked \\n me: '\"Where '\"is'\" John?'\"\" \"I am not closed","This is a \\t string \\n containing tab ,He asked \\n me: '\"Where '\"is'\" John?'\",Unclosed String: I am not closed",114))
    def test_STRING_unclosed1(self):
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
        self.assertTrue(TestLexer.test(string_test,'Class,Person,{,Var,$numPeople,:,Int,=,0,;,Var,name,:,String,;,},<EOF>', 120))
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
        string_expected = """Class,Program,{,main,(,),{,Var,name,:,String,=,Hello How are you \\n,;,Var,answer,:,String,=,I am fine \\\\ Thank you \\',Var,$radisu,:,Float,=,123456.e-23,Val,number,:,Int,=,10,;,Var,new_string,:,String,=,Illegal Escape In String: I am newww \d"""
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
        string_expected = """Class,Program,{,main,(,),{,Var,$radisu,:,Float,=,123456.e-23,Val,number,:,Int,=,10,;,Out,.,printInt,(,number,),;,},},Var,new_string,:,String,=,Unclosed String: I am newww \\n

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
        string_expected = """0b0,00,0,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 127))
    def test_10 (self):
        string_test = """True""" 
        string_expected = """True,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 128))
    def test_11 (self):
        string_test = """true""" 
        string_expected = """true,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 129))
    def test_12 (self):
        string_test = """0B0_0""" 
        string_expected = """0B0,_0,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 130))
    def test_13 (self):
        string_test = """12e01""" 
        string_expected = """12e01,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 131))
    def test_14 (self):
        string_test = """0B00_""" 
        string_expected = """0B0,0,_,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 132))
    def test_15 (self):
        string_test = """0b_00""" 
        string_expected = """0,b_00,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 133))
    def test_16 (self):
        string_test = """0_b00""" 
        string_expected = """0,_b00,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 134))
    def test_17 (self):
        string_test = """1_.23""" 
        string_expected = """1,_,.,23,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 135))
    def test_18 (self):
        string_test = """12e01""" 
        string_expected = """12e01,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 136))
    def test_19 (self):
        string_test = """0x0123_456_789_ABC_DEF""" 
        string_expected = """0x0,123456789,_ABC_DEF,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 137))
    def test_20 (self):
        string_test = """\"bao \\q\"""" 
        string_expected = """Illegal Escape In String: bao \q"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 138))
    def test_21 (self):
        string_test = """\"\\n\"""" 
        string_expected = """\\n,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 139))
    def test_22 (self):
        string_test = """
        Class Program
        {
            main()
            {
                a::$foo();
            }
        }""" 
        string_expected = """Class,Program,{,main,(,),{,a,::,$foo,(,),;,},},<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 140))
    def test_23 (self):
        string_test = """
        Class Program
        {
            main()
            {
                a::$foo();
                a = "Noooooo!!!!";
            }
        }""" 
        string_expected = """Class,Program,{,main,(,),{,a,::,$foo,(,),;,a,=,Noooooo!!!!,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 141))
    def test_24_illegal_escape (self):
        string_test = """
        ba+12+\"na\"\"md+1.2-468\lb""" 
        string_expected = """ba,+,12,+,na,Illegal Escape In String: md+1.2-468\l"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 142))
    def test_25_illegal_escape (self):
        string_test = """
        \"1.2+1.3+1.4\\o'\"123""" 
        string_expected = """Illegal Escape In String: 1.2+1.3+1.4\\o"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 143))
    def test_26_illegal_escape (self):
        string_test = """\"concaheo\\uabc""" 
        string_expected = """Illegal Escape In String: concaheo\\u"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 144))
    def test_27_long_program (self):
        string_test = r"""
                Class Entity {
            Var UUID: String;
            Var $numOfEntities: Int = 0;
            Constructor() {
                Entity::$numOfEntities = Entity::$numOfEntities + 1;
            }
            Destructor() {
                Entity::$numOfEntities = Entity::$numOfEntities - 1;
            }
        }
        Class Pig:Entity{
            Var height: Float = 0.75;
            Var width: Float = 0.8;
            Var length: Float = 1.2;
            ## Where individual liberty is nothing but a daydream ##
        }
        Class Creeper:Entity{
            Var height: Float = 1.75;
            Var width: Float = 0.8;
            Var length: Float = 0.8;
            ## The wine consumed at a banquet should amount to the blood that was spilled ##
        }
        Class Program {
            main() {
                Var c: Creeper = New Creeper();
                If (c.height < 2.){ ##ALLAHU AKBAR## 
                    System.out.printLn("Is that a short joke?\\j");
                }
                ##CHECK IT GEE##
                ##UGG##
                Val dolls: Array[String, 9] = Array("Shanhai","Hourai","France","Holland","Tibet","Kyoto","London","Russia","Orlean");
                System.out.printLn("The only easy day was yesterday");
                Val $key: Boolean = ("DAWN TO" +. "x16") ==. IOSYS.MarisaStoleThePreciousThing.Lyrics; # #Not a comment##
            }
        }""" 
        string_expected = r"""Class,Entity,{,Var,UUID,:,String,;,Var,$numOfEntities,:,Int,=,0,;,Constructor,(,),{,Entity,::,$numOfEntities,=,Entity,::,$numOfEntities,+,1,;,},Destructor,(,),{,Entity,::,$numOfEntities,=,Entity,::,$numOfEntities,-,1,;,},},Class,Pig,:,Entity,{,Var,height,:,Float,=,0.75,;,Var,width,:,Float,=,0.8,;,Var,length,:,Float,=,1.2,;,},Class,Creeper,:,Entity,{,Var,height,:,Float,=,1.75,;,Var,width,:,Float,=,0.8,;,Var,length,:,Float,=,0.8,;,},Class,Program,{,main,(,),{,Var,c,:,Creeper,=,New,Creeper,(,),;,If,(,c,.,height,<,2.,),{,System,.,out,.,printLn,(,Is that a short joke?\\j,),;,},Val,dolls,:,Array,[,String,,,9,],=,Array,(,Shanhai,,,Hourai,,,France,,,Holland,,,Tibet,,,Kyoto,,,London,,,Russia,,,Orlean,),;,System,.,out,.,printLn,(,The only easy day was yesterday,),;,Val,$key,:,Boolean,=,(,DAWN TO,+.,x16,),==.,IOSYS,.,MarisaStoleThePreciousThing,.,Lyrics,;,Error Token #"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 145))
    def test_28_unclosed_string (self):
        string_test = """\"ULxM*`~.~+C_DISD2""" 
        string_expected = """Unclosed String: ULxM*`~.~+C_DISD2"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 146))
    def test_29_unclosed_string (self):
        string_test = """##SRs##\"Nk8U;\"rA\"@Y3*\"oV\"bh1""" 
        string_expected = """Nk8U;,rA,@Y3*,oV,Unclosed String: bh1"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 147))
    def test_30_error_char (self):
        string_test = """
        o%jvhs'Ty{*(0Ay0s&n|""" 
        string_expected = """o,%,jvhs,Error Token '"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 148))
    def test_31_error_char (self):
        string_test = """(C*.=22Pta!0=&o""" 
        string_expected = """(,C,*,.,=,22,Pta,!,0,=,Error Token &"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 149))
    def test_32_error_char (self):
        string_test = """;J~%IbnQL!x-OBd""" 
        string_expected = """;,J,Error Token ~"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 150))
    def test_33_array (self):
        string_test = """Var arr : Array[Int, 4] = Array(1_2,20_3,39_2,0);""" 
        string_expected = """Var,arr,:,Array,[,Int,,,4,],=,Array,(,12,,,203,,,392,,,0,),;,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 151))
    def test_34_array (self):
        string_test = """Var arr : Array[Float, 3] = Array(3_3.2, 23_4.e0, .32e-4);""" 
        string_expected = """Var,arr,:,Array,[,Float,,,3,],=,Array,(,33.2,,,234.e0,,,.32e-4,),;,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 152))
    def test_35_float_lit (self):
        string_test = """762 762. 762.51 762e51 .762e51 0.762e51 .e0""" 
        string_expected = """762,762.,762.51,762e51,.762e51,0.762e51,.e0,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 153))
    def test_36_small_Class(self):
        string_test = r"""
        Class Animal {
            Var name: String;
        }
        Class Dog : Animal {
            bark() {
                System.out.printLn("Woof woof");
            }
        }""" 
        string_expected = r"""Class,Animal,{,Var,name,:,String,;,},Class,Dog,:,Animal,{,bark,(,),{,System,.,out,.,printLn,(,Woof woof,),;,},},<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 153))
    def test_37_float_lit (self):
        string_test = """123 12_3. 123e-4 .123e+4 1.e-234 1_2.3e4 1_2.34 0.0000 0.e-0 0.0e+0 1_2.e-0 .e0 1_2_3.e+0""" 
        string_expected = """123,123.,123e-4,.123e+4,1.e-234,12.3e4,12.34,0.0000,0.e-0,0.0e+0,12.e-0,.e0,123.e+0,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 155))
    def test_38_unterminated_comment (self):
        string_test = """##dangling # #comment here""" 
        string_expected = """Error Token #"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 156))
    def test_39_relational_ops (self):
        string_test = """>= < > <= == != = ==.""" 
        string_expected = """>=,<,>,<=,==,!=,=,==.,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 157))
    def test_40_arithmethic_ops (self):
        string_test = """+ - * / % +. || &&""" 
        string_expected = """+,-,*,/,%,+.,||,&&,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 158))
    def test_41_long_program (self):
        string_test = """
        Class Program
        {
            main()
            {
                a.a.b.c();
            }
        }""" 
        string_expected = """Class,Program,{,main,(,),{,a,.,a,.,b,.,c,(,),;,},},<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 159))
    def test_42_long_program (self):
        string_test = """
        Class Program
        {
            fibonacci(myNum:Int)
            {
                If((myNum == 0) || (myNum == 1))
                    {
                        Return 1;
                    }
                Else
                {
                    Return Self.fibonacci(myNum - 1) + Self.fibonacci(myNum - 1);
                }
            }
            main ()
            {
                Val my_num : Int = Self.fibonacci(10);
                System.Out.printLn(my_num);
            }
        }""" 
        string_expected = """Class,Program,{,fibonacci,(,myNum,:,Int,),{,If,(,(,myNum,==,0,),||,(,myNum,==,1,),),{,Return,1,;,},Else,{,Return,Self,.,fibonacci,(,myNum,-,1,),+,Self,.,fibonacci,(,myNum,-,1,),;,},},main,(,),{,Val,my_num,:,Int,=,Self,.,fibonacci,(,10,),;,System,.,Out,.,printLn,(,my_num,),;,},},<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 160))
    def test_43_illegal_escape (self):
        string_test = """
        main()
        {
            Var a: Int = 5;
            Val c: String = "I am very happy \\z"
        }""" 
        string_expected = """main,(,),{,Var,a,:,Int,=,5,;,Val,c,:,String,=,Illegal Escape In String: I am very happy \z"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 161))
    def test_44_unclosed_string (self):
        string_test = """
        Class Program
        {
            main()
            {
                System.out.printLn("Hello World\\n)}}""" 
        string_expected = """Class,Program,{,main,(,),{,System,.,out,.,printLn,(,Unclosed String: Hello World\\n)}}"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 162))
    def test_45_intfloatlit (self):
        string_test = """01245avfeece 123.e-23_56 789 0b1223""" 
        string_expected = """01245,avfeece,123.e-23,_56,789,0b1,223,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 163))
    def test_46_string (self):
        string_test = """\"I have a lot of escape sequence \\n \\t  \" 1234._446 13__562238""" 
        string_expected = """I have a lot of escape sequence \\n \\t  ,1234.,_446,13,__562238,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 164))
    def test_47_intlitID (self):
        string_test = """ I am a cat \" I am a car\" \\n \\ t""" 
        string_expected = """I,am,a,cat, I am a car,Error Token \\"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 165))
    def test_48_class (self):
        string_test = """Class //student {}""" 
        string_expected = """Class,/,/,student,{,},<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 166))
    def test_49_string (self):
        string_test = """\"I don\\'t like you \\n  ## GETOUT ##\"""" 
        string_expected = """I don\\'t like you \\n  ## GETOUT ##,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 167))
    def test_50_mix (self):
        string_test = """a = "123.___256" 123.__e-23.560""" 
        string_expected = """a,=,123.___256,123.,__e,-,23.560,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 168))
    def test_51_array (self):
        string_test = """Array(1,2,3,3.0,0.00001e-56_23, \"Heyyyy \\n \")""" 
        string_expected = """Array,(,1,,,2,,,3,,,3.0,,,0.00001e-56,_23,,,Heyyyy \\n ,),<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 169))
    def test_52_random (self):
        string_test = """bnnengwfowfmwrp
        bev ekbevwfw RR##@R#1v 2r23r3r3t3gvevsfvwv""" 
        string_expected = """bnnengwfowfmwrp,bev,ekbevwfw,RR,Error Token #"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 170))
    def test_53_string (self):
        string_test = """\"Hi Bao nhieu lau\\' chua \\'gap\" #### This is not a comment ####""" 
        string_expected = """Hi Bao nhieu lau\\' chua \\'gap,This,is,not,a,comment,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 171))
    def test_54_hexadeciam (self):
        string_test = """0x43238814.466_556e-12342_234 0xABCEvBTRBRNTNNJY 0xasadvvfbsvsvd""" 
        string_expected = """0x43238814,.,466556e-12342,_234,0xABCE,vBTRBRNTNNJY,0,xasadvvfbsvsvd,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 172))
    def test_55_condition (self):
        string_test = """True && True || False && False""" 
        string_expected = """True,&&,True,||,False,&&,False,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 173))
    def test_56_string (self):
        string_test = """e.1331664 23+566 \"I love\" +. \"You\"""" 
        string_expected = """e,.,1331664,23,+,566,I love,+.,You,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 174))
    def test_57_escape (self):
        string_test = """\" \\n \\t \\z \\' \\\\ \"""" 
        string_expected = """Illegal Escape In String:  \\n \\t \\z"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 175))
    def test_58_wrong_escape (self):
        string_test = """\" \\t \\r \\\\ \\d \\z \"""" 
        string_expected = """Illegal Escape In String:  \\t \\r \\\\ \\d"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 176))
    def test_59_ (self):
        string_test = """## \"You cannot do this \\t \" a =  \"You can do this\"""" 
        string_expected = """Error Token #"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 177))
    def test_60_if_else (self):
        string_test = """If (False) {} Elseif (True) {} Else {}""" 
        string_expected = """If,(,False,),{,},Elseif,(,True,),{,},Else,{,},<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 178))
    def test_61_numLit (self):
        string_test = """1_2 0 07_23 0xF_F 0X1_6 0b0_0_0 0B1_0 1_0.e+0 2_1.6e-9 23E+6 45E-0 .E309""" 
        string_expected = """12,0,0723,0xFF,0X16,0b0,_0_0,0B10,10.e+0,21.6e-9,23E+6,45E-0,.E309,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 179))
    def test_62_func (self):
        string_test = """
        shoot() {
            ## shoot ##
            Var bullet: Bullet = New Bullet();
            ## and ##
            bullet.travel();
            ## i'll move ##
        }""" 
        string_expected = """shoot,(,),{,Var,bullet,:,Bullet,=,New,Bullet,(,),;,bullet,.,travel,(,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 180))
    def test_63_long_program (self):
        string_test = r"""
        Class Animal {
            Var name: String;
        }
        Class Dog : Animal {
            bark() {
                System.out.printLn("Woof woof");
            }
        }
        Class Cat : Animal {
            purr() {
                System.out.printLn("*whatever sounds cats make when they purr*");
            }
        }
        Class Mouse : Animal {
            squeak() {
                System.out.printLn("Squeak squeak");
            }
        }"""
        string_expected = r"""Class,Animal,{,Var,name,:,String,;,},Class,Dog,:,Animal,{,bark,(,),{,System,.,out,.,printLn,(,Woof woof,),;,},},Class,Cat,:,Animal,{,purr,(,),{,System,.,out,.,printLn,(,*whatever sounds cats make when they purr*,),;,},},Class,Mouse,:,Animal,{,squeak,(,),{,System,.,out,.,printLn,(,Squeak squeak,),;,},},<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 181))
    def test_64_mix (self):
        string_test = """Var a: String = \"How are you? \\t I am very good\"
        Var b: Int = 0x11211_6
        Var c: Floar = 123.sdfdssdfe-23589""" 
        string_expected = """Var,a,:,String,=,How are you? \\t I am very good,Var,b,:,Int,=,0x112116,Var,c,:,Floar,=,123.,sdfdssdfe,-,23589,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 182))
    def test_65_long_program (self):
        string_test = """
        Class Hawl
        {
            Var height: Float;
            Var speed: Float;
            fly()
            {
                System.Out.printLn(\"I am flying nowwww!!\")
                Self.speed = 123.e5656;
            }
            eat()
            {
                speed = 0.0;
            }
        }""" 
        string_expected = """Class,Hawl,{,Var,height,:,Float,;,Var,speed,:,Float,;,fly,(,),{,System,.,Out,.,printLn,(,I am flying nowwww!!,),Self,.,speed,=,123.e5656,;,},eat,(,),{,speed,=,0.0,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 183))
    def test_66_forloop (self):
        string_test = """
        Foreach (i In 1..100 By 2)
        {
            If(i == 5_6)
            {
                print("How are you!!! \\n");
            }
        }""" 
        string_expected = """Foreach,(,i,In,1.,.,100,By,2,),{,If,(,i,==,56,),{,print,(,How are you!!! \\n,),;,},},<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 184))
    def test_67_mix (self):
        string_test = """\" I am pissed \\n \\t \"
        135658_52166_45621e-56 = 46.234548_561 
        \" I love PPL so much \" ## Comment##""" 
        string_expected = """ I am pissed \\n \\t ,1356585216645621e-56,=,46.234548,_561, I love PPL so much ,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 185))
    def test_68_array (self):
        string_test = """
        Var a = Array[Int,6];
        Foreach(i In 1 ..6 )
        {
            ## I want to assign ##
            a[i] = i;
        }""" 
        string_expected = """Var,a,=,Array,[,Int,,,6,],;,Foreach,(,i,In,1,..,6,),{,a,[,i,],=,i,;,},<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 186))
    def test_69_constructor (self):
        string_test = """
        Constructor()
        {
            Self.height = 0;
            Self.status = \"Hew watch out the steroids \\t \"
            ## Be careful with that ##
        }
        \"I am not joking \\t \\n \\1 \"""" 
        string_expected = r"""Constructor,(,),{,Self,.,height,=,0,;,Self,.,status,=,Hew watch out the steroids \t ,},Illegal Escape In String: I am not joking \t \n \1"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 187))
    def test_70_destructor (self):
        string_test = """
        Destructor()
        {
            ##What you gonna do with me##
            Free(Self);
            printLn(\"I am freeed\");
        }""" 
        string_expected = """Destructor,(,),{,Free,(,Self,),;,printLn,(,I am freeed,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 188))
    def test_71_long_program (self):
        string_test = """
        Class Program
        {
            gcd(a: Int, b:Int)
            {
                If (b == 0)
                {
                    Return a;
                }
                Else
                {
                    Return Self.gcd(b%a,a);
                }
            }
            main()
            {
                Var my_gcd : Int = Self.gcd(12,36);
                printLn(my_gcd)
            }
        }""" 
        string_expected = """Class,Program,{,gcd,(,a,:,Int,,,b,:,Int,),{,If,(,b,==,0,),{,Return,a,;,},Else,{,Return,Self,.,gcd,(,b,%,a,,,a,),;,},},main,(,),{,Var,my_gcd,:,Int,=,Self,.,gcd,(,12,,,36,),;,printLn,(,my_gcd,),},},<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 189))
    def test_72_mix (self):
        string_test = """
        Var a: String = \"Lorem ipsum dolor sit amet, \\t consectetur adipiscing elit\"'
        vffvsvsvefvev cnwifvea#R#%@^# %#$@#$t214r2""" 
        string_expected = """Var,a,:,String,=,Lorem ipsum dolor sit amet, \\t consectetur adipiscing elit,Error Token '"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 190))
    def test_73_mix (self):
        string_test = """
        Vestibulum vel odio eu leo pulvinar s\\agittis quis vitae est
        """ 
        string_expected = """Vestibulum,vel,odio,eu,leo,pulvinar,s,Error Token \\"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 191))
    def test_74_mix (self):
        string_test = """
        Vestibulum vel odio eu leo p1234_242413.e56ulvinar sagittis quis vitae est
        124231.dignis_sim  0xASDFGHHGF \"Aliquam sit amet lectus iaculis leo accumsan lacinia""" 
        string_expected = """Vestibulum,vel,odio,eu,leo,p1234_242413,.e56,ulvinar,sagittis,quis,vitae,est,124231.,dignis_sim,0xA,SDFGHHGF,Unclosed String: Aliquam sit amet lectus iaculis leo accumsan lacinia"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 192))
    def test_75_long_program (self):
        string_test = """
        Class Program
        {
            getMax(myArray: Array[Int, 6])
            {
                Var MaxValue = -inf_int;
                Foreach(i In 1 .. 6)
                {
                    If(MaxValue < myArray[i])
                    {
                        MaxValue = myArray[i];
                    }
                }
                Return MaxValue;
            }
            main()
            {
                Var MyArray: Array[Int, 6] = Array(1,2,3,4,5,6);
                printLn(Self.getMax(MyArray));
            }
        }
        """ 
        string_expected = """Class,Program,{,getMax,(,myArray,:,Array,[,Int,,,6,],),{,Var,MaxValue,=,-,inf_int,;,Foreach,(,i,In,1,..,6,),{,If,(,MaxValue,<,myArray,[,i,],),{,MaxValue,=,myArray,[,i,],;,},},Return,MaxValue,;,},main,(,),{,Var,MyArray,:,Array,[,Int,,,6,],=,Array,(,1,,,2,,,3,,,4,,,5,,,6,),;,printLn,(,Self,.,getMax,(,MyArray,),),;,},},<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 193))
    def test_76_mix (self):
        string_test = """
        \"Sed libero mi, pharetra at dolor \\t \\n eget, \\b \\\\ mollis mattis metus\"
        \" Nulla venenatis tempus hend\\rerit\"""" 
        string_expected = """Sed libero mi, pharetra at dolor \\t \\n eget, \\b \\\\ mollis mattis metus, Nulla venenatis tempus hend\\rerit,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 194))
    def test_77_int_lit (self):
        string_test = """
        4656 04651_4444315 465.265e--566 5989.e++46210 23..466312""" 
        string_expected = """4656,046514444315,465.265,e,-,-,566,5989.,e,+,+,46210,23.,.,466312,<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 195))
    def test_78_if_else (self):
        string_test = """
        If(a == 0)
        {
            print(\"Lorem ipsum dolor sit amet\");
        }
        Elseif (a == 1)
        {
            print(\"Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur,\\t adipisci velit...\");
        }
        Else
        {
            print(1215_461e010);
        }""" 
        string_expected = """If,(,a,==,0,),{,print,(,Lorem ipsum dolor sit amet,),;,},Elseif,(,a,==,1,),{,print,(,Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur,\\t adipisci velit...,),;,},Else,{,print,(,1215461e010,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 196))
    def test_79_mix (self):
        string_test = """
        12224341.efefewwf \"Nunc ut posuere nisl, non euismod \\metus.\"""" 
        string_expected = """12224341.,efefewwf,Illegal Escape In String: Nunc ut posuere nisl, non euismod \\m"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 197))
    def test_80_long_program (self):
        string_test = """
        Class LinkedList
        {
            LinkedList()
            {
                Self.value = 0;
                Self.next_node = Null;
            }
            LinkedList(new_value: Int, nextNode: LinkedList)
            {
                Self.value = new_value;
                Self.next_node = nextNode;
            }
            Val value:Int;
            Val next_node: LinkedList;
        }""" 
        string_expected = """Class,LinkedList,{,LinkedList,(,),{,Self,.,value,=,0,;,Self,.,next_node,=,Null,;,},LinkedList,(,new_value,:,Int,,,nextNode,:,LinkedList,),{,Self,.,value,=,new_value,;,Self,.,next_node,=,nextNode,;,},Val,value,:,Int,;,Val,next_node,:,LinkedList,;,},<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 198))
    def test_81_long_program (self):
        string_test = """
        Class Program
        {
            addNewNode(newNode: LinkedList, head: LinkedList)
            {
                newNode.next_node = head;
                head = new_node;
            }
            deleteNode(position: Int, head: LinkedList)
            {
                If(Int == 0)
                {
                    head = head.next_node;
                }
                Else
                {
                    Var curr: LinkedList = head.next.next;
                    Var prev: LinkedList = curr;
                    Foreach(i In 2 .. position)
                    {
                        prev = curr;
                        curr = curr.next_node;
                    }
                    prev.next = curr;
                    head = prev;
                }

            }
        }""" 
        string_expected = """Class,Program,{,addNewNode,(,newNode,:,LinkedList,,,head,:,LinkedList,),{,newNode,.,next_node,=,head,;,head,=,new_node,;,},deleteNode,(,position,:,Int,,,head,:,LinkedList,),{,If,(,Int,==,0,),{,head,=,head,.,next_node,;,},Else,{,Var,curr,:,LinkedList,=,head,.,next,.,next,;,Var,prev,:,LinkedList,=,curr,;,Foreach,(,i,In,2,..,position,),{,prev,=,curr,;,curr,=,curr,.,next_node,;,},prev,.,next,=,curr,;,head,=,prev,;,},},},<EOF>"""
        self.assertTrue(TestLexer.test(string_test, string_expected, 199))