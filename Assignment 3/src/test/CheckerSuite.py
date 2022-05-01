import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_1(self):
        """Simple program: int main() {} """
        input = """
        Class Duong
        {
        }
        """
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_2(self):
        input = """
        Class Duong
        {
        }
        Class Duong
        {
        }
        Class Program
        {

        }
        """
        expect = """Redeclared Class: Duong"""
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_3(self):
        """Simple program: int main() {} """
        input = """
        Class Duong
        {
        }
        Class Program
        {

        }
        """
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_4(self):
        input = """
        Class Program
        {
        foo(){}
        goo(){}
        foo(){}
        }"""
        expect = """Redeclared Method: foo"""
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_5(self):
        input = """
        Class Program
        {
        $foo(){}
        $foo(){}
        }"""
        expect = """Redeclared Method: $foo"""
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_6(self):
        input = """
        Class Program
        {
        goo(x,t : String){}
        goo(){}
        }"""
        expect = """Redeclared Method: goo"""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_7(self):
        input = """
        Class Program
        {
        $getArea(x,x: Float)
        {
        }
        }"""
        expect = """Redeclared Parameter: x"""
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_8(self):
        input = """
        Class Program
        {
            Var c: String = "Duong";
            Var c: Int = 1;
        }"""
        expect = """Redeclared Attribute: c"""
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_9(self):
        input = """
        Class Student
        {
            Val numStudents: Int = 0;
            Var numStudents: Int;
        }"""
        expect = """Redeclared Attribute: numStudents"""
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_10(self):
        input = """
        Class Student
        {
        Val numStudents: Int;
        }
        """
        expect = """Illegal Constant Expression: None"""
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_11(self):
        input = """
        Class Moon
        {
        Val width: Float =  3;
        Val height: Float = 10;
        }"""
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_12(self):
        input = """
        Class Student
        {
        Var $maxHeight : Int = 189.5;
        }"""
        expect = """Type Mismatch In Expression: VarDecl(Id($maxHeight),IntType,FloatLit(189.5))"""
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_13(self):
        input = """
        Class Student : Person
        {
        }"""
        expect = """Undeclared Class: Person"""
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_14(self):
        input = """
        Class Base
        {
        }
        Class Base1: Base
        {
        }
        Class Base2: Base1
        {
        getArea(height, width : Float; type: Shape)
        {}
        }"""
        expect = """Undeclared Class: Shape"""
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_15(self):
        input = """
        Class Student
        {
        Var $maxHeight : Float;
        Var height: Float;
        compareHeight(studentA, studentB : Student)
        {
        Var a: Float = 1.2;
        Var a: Int = 2;
        }
        }"""
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_16(self):
        input = """Class Program
        {
        main()
        {
        Var a: Int = 1;
        Var b: Float = a;
        Val c: Float = a;
        }
        }"""
        expect = """Illegal Constant Expression: Id(a)"""
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_17(self):
        input = """
        Class Base
        {
        }
        Class Base1: Base
        {
        }
        Class Base2: Base1
        {
        }
        Class Program
        {
        main()
        {
        Var var1 : Base2;
        Var var2: Base = var1;
        Var var3: Base2 = var2;
        }
        }"""
        expect = """Type Mismatch In Statement: VarDecl(Id(var3),ClassType(Id(Base2)),Id(var2))"""
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_18(self):
        input = """
        Class Student
        {
        foo(a, b : Int ; c: String)
        {
        Var temp: Int;
        {
        Var temp: Int;
        Var goo: Float;
        Var goo: Int;
        }
        }
        }
        """
        expect = """Redeclared Variable: goo"""
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_19(self):
        input = """
        Class Student
        {
            main()
            {
                Var a: Int;
                {
                    Var a : Int;
                    {
                        Var a: Int;
                        Var b: Int;
                    }
                    Var b: Int;
                }
            }
        }"""
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_20(self):
        input = """
        Class Program
        {
            main()
            {
                Var a: Float = 1 + 2;
                Var b: Float = a + 5;
                Var c: Boolean = a + True;
            }
        }"""
        expect = """Type Mismatch In Expression: BinaryOp(+,Id(a),BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_21(self):
        input = """
        Class Student
        {
            Var $maxHeight: Float = -1 + 80.0;
            Val $isTall: Boolean = ! True;
            Val $isShort: Int = 1 + False;
        }"""
        expect = """Type Mismatch In Expression: BinaryOp(+,IntLit(1),BooleanLit(False))"""
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_22(self):
        input = """
        Class Student
        {
            getScore()
            {
                Val a: Int = (1 + 2).getScore();
            }
        }"""
        expect = """Type Mismatch In Expression: CallExpr(BinaryOp(+,IntLit(1),IntLit(2)),Id(getScore),[])"""
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_23(self):
        input = """
        Class Flower
        {
            water()
            {
                Var isWatered: Boolean = Person::$waterFlower();
            }
        }"""
        expect = """Undeclared Class: Person"""
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_24(self):
        input = """
        Class Person
        {
            Var name: String;
        }
        Class Dog
        {
            goOut(myPerson: String)
            {
                Val owner: String = myPerson.getName();
            }
        }"""
        expect = """Type Mismatch In Expression: CallExpr(Id(myPerson),Id(getName),[])"""
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_25(self):
        input = """
        Class Person
        {
            Var name: String;
        }
        Class Student : Person
        {
            getName()
            {
                Return Person::$getName();
            }
        }"""
        expect = """Undeclared Method: $getName"""
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_26(self):
        input = """
        Class Person
        {
            Var name: String;
        }
        Class Dog
        {
            goOut(myPerson: Person)
            {
                Val owner: String = myPerson.getName();
            }
        }"""
        expect = """Undeclared Method: getName"""
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_27(self):
        input = """
        Class Flower
        {
            Var name: String;
            getName()
            {
                Return "String";
            }
        }
        Class Children
        {
            growFlower()
            {
                Var newFlower : Flower;
                Return newFlower;
            }
        }
        Class Program
        {
            main()
            {
                Var oneChild: Children;
                Var newFlower : Int = oneChild.growFlower().getName();
            }
        }
        """
        expect = """Type Mismatch In Statement: VarDecl(Id(newFlower),IntType,CallExpr(CallExpr(Id(oneChild),Id(growFlower),[]),Id(getName),[]))"""
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_28(self):
        input = """
        Class Flower
        {
            Var height: Float;
            getHeight()
            {
                Return 10.2;
            }
            getPrice()
            {
                Return 10.2 * Self.getHeight();
            }
        }
        Class Program
        {
            main()
            {
                Var myFlower: Flower;
                Var myHeight: Int = myFlower.getPrice();
            }
        }"""
        expect = """Type Mismatch In Statement: VarDecl(Id(myHeight),IntType,CallExpr(Id(myFlower),Id(getPrice),[]))"""
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_29(self):
        input = """
        Class Flower
        {
            Var height: Float;
            getHeight()
            {
                Return 10.2;
            }
            getPrice()
            {
                Return True * Self.getHeight();
            }
        }"""
        expect = """Type Mismatch In Expression: BinaryOp(*,BooleanLit(True),CallExpr(Self(),Id(getHeight),[]))"""
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_30(self):
        input = """
        Class Bird
        {
            Var name: String;
            Var age: Int;
            foo()
            {

            }
            goo()
            {
                Var a: Int = Self.foo();
            }
        }"""
        expect = """Type Mismatch In Expression: CallExpr(Self(),Id(foo),[])"""
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_31(self):
        input = """
        Class Program
        {
            getArea(a, b: Float)
            {
                Return a*b;
            }
            main()
            {
                Val myArea: Float = Self.getArea();
            }
        }"""
        expect = """Type Mismatch In Expression: CallExpr(Self(),Id(getArea),[])"""
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_32(self):
        input = """
        Class Program
        {
            getArea(a, b: Float)
            {
                Return a*b;
            }
            main()
            {
                Var height: Int = 5;
                Var width: Int = 6;
                Var myArea: Float = Self.getArea(height, width);
                Return myArea;
            }
        }"""
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_33(self):
        input = """
        Class Program
        {
            getArea(a, b: Float)
            {
                Return a*b;
            }
            main()
            {
                Var height: Int = 5;
                Var width: Boolean = True;
                Var myArea: Float = Self.getArea(height, width);
                Return myArea;
            }
        }"""
        expect = """Type Mismatch In Expression: CallExpr(Self(),Id(getArea),[Id(height),Id(width)])"""
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_34(self):
        input = """
        Class Program
        {
            foo()
            {

            }
            main()
            {
                Self.goo();
            }
        }"""
        expect = """Undeclared Method: goo"""
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_35(self):
        input = """
        Class Base
        {

        }
        Class Derived: Base
        {
            foo(myBase: Base ; a: Int)
            {
                Return a + 1;
            }
        }
        Class Program
        {
            main()
            {
                Var myInt: Int = 5;
                Var derivedClass : Derived ;
                derivedClass.foo(derivedClass, myInt);
            }
        }
        """
        expect = """Type Mismatch In Statement: Call(Id(derivedClass),Id(foo),[Id(derivedClass),Id(myInt)])"""
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_36(self):
        input = """
        Class Base
        {
            foo(a, b: Float)
            {
                Return a >= b;
            }
        }
        Class Derived: Base
        {

        }
        Class Program
        {
            main()
            {
                Var myClass: Derived;
                Var a: Int = myClass.foo(4,5);
            }
        }"""
        expect = """Type Mismatch In Statement: VarDecl(Id(a),IntType,CallExpr(Id(myClass),Id(foo),[IntLit(4),IntLit(5)]))"""
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_37(self):
        input = """
        Class Base
        {
            foo (a, b: String)
            {
                Return a ==. b;
            }
        }
        Class Derived1 : Base
        {

        }
        Class Derived2: Derived1
        {

        }
        Class Program
        {
            main()
            {
                Var a: Derived2;
                Var b: Boolean =  a.foo("Hello", "World");
                Return b;
            }
        }"""
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_38(self):
        input = """
        Class Base
        {
            hello()
            {
                Var a: Int = 6;
                {
                    Var a: Int = 7;
                }
                Return a;
            }
        }
        Class Person : Base
        {

        }
        Class Program
        {
            main()
            {
                Var myClass: Person;
                myClass.hello();
            }
        }"""
        expect = """Type Mismatch In Statement: Call(Id(myClass),Id(hello),[])"""
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_39(self):
        input = """
        Class Program
        {
            Val myArray: Array[Int, 5] = Array(1,2,3,4,5);
            Var $myArray2: Array[Boolean, 2] = Array(True, False);
        }"""
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_40(self):
        input = """
        Class Program
        {
            Val $Color : Array[String, 3] = Array("Red", "Blue", "Yellow");
            Val $score : Array[Float, 3] = Array(1,2, 3.4, 5);
        }
        """
        expect = """Illegal Array Literal: [IntLit(1),IntLit(2),FloatLit(3.4),IntLit(5)]"""
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_41(self):
        input = """
        Class Program
        {
            main()
            {
                Var b: Array[Boolean, 3] = Array(True, False. True);
                Var a: Array[Int, 2] = Array(True, False);
            }
        }"""
        expect = """Illegal Array Literal: [BooleanLit(True),FieldAccess(BooleanLit(False),BooleanLit(True))]"""
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_42(self):
        input = """
        Class Program
        {
            Var myArray : Array[Int, 5];
            main()
            {
                Val Bird: Array[String, 5] = 5;
            }
        }"""
        expect = """Type Mismatch In Constant Declaration: ConstDecl(Id(Bird),ArrayType(5,StringType),IntLit(5))"""
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_43(self):
        input = """
        Class Program
        {
            main()
            {
                Var a: Array[Array[Array[Int,4],2],2] = Array(
                    Array(
                        Array(1,2,3,4),
                        Array(1,2,3,4)
                    ),
                    Array(
                        Array(1,2,3,4),
                        Array(1,2,3,4)
                    )
                );
                Return a;
            }
        }"""
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 442))
    
    def test_44(self):
        input = """
        Class Program
        {
            main()
            {
                Var a: Array[Array[Array[Int,4],2],2] = Array(
                    Array(
                        Array(1,2,3,4),
                        Array(1,2,3,4)
                    ),
                    Array(
                        Array(1,2,3,4),
                        Array(1,2,3,4)
                    )
                );
                Return a;
            }
        }"""
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_45(self):
        input = """
        Class Program
        {
            Val $myArray: Array[Array[Array[Int,5],2],2] = Array(
                    Array(
                        Array(1,2,3,4),
                        Array(1,2,3,4)
                    ),
                    Array(
                        Array(1,2,3,4),
                        Array(1,2,3,4)
                    )
                );
        }"""
        expect = """Illegal Array Literal: [IntLit(1),IntLit(2),IntLit(3),IntLit(4)]"""
        self.assertTrue(TestChecker.test(input, expect, 444))
    
    def test_46(self):
        input = """
        Class Program
        {
            Var $myArray: Array[Array[Array[Int,4],2],3] = Array(
                    Array(
                        Array(1,2,3,4),
                        Array(1,2,3,4)
                    ),
                    Array(
                        Array(1,2,3,4),
                        Array(1,2,3,4)
                    )
                );
        }"""
        expect = """Illegal Array Literal: [[[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]],[[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]]]"""
        self.assertTrue(TestChecker.test(input, expect, 445))
    
    def test_47(self):
        input = """
        Class Program
        {
            Var $myArray: Array[Array[Array[Int,4],2],2] = Array(
                    Array(
                        Array(1,2,3,4),
                        Array(5,6,7,8)
                    ),
                    Array(
                        Array(-1,-2,-3,-4),
                        Array(-5,-6,-7, False)
                    )
                );
        }"""
        expect = """Illegal Array Literal: [UnaryOp(-,IntLit(5)),UnaryOp(-,IntLit(6)),UnaryOp(-,IntLit(7)),BooleanLit(False)]"""
        self.assertTrue(TestChecker.test(input, expect, 446))
    
    def test_48(self):
        input = """
        Class Program
        {
            Var a: Int;
            main()
            {
                Var a: Int = Array(1,2,3,4,5);
            }
        }"""
        expect = """Type Mismatch In Statement: VarDecl(Id(a),IntType,[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)])"""
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_49(self):
        input = """
        Class Program
        {
            Val $myArray : Array[Int, 2] =
            Array
            (
                Array(1,2,3,4),
                Array(5,6,7,8)
            );
        }"""
        expect = """Illegal Array Literal: [[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(5),IntLit(6),IntLit(7),IntLit(8)]]"""
        self.assertTrue(TestChecker.test(input, expect, 448))
    #
    # def test_50(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 449))
    #
    # def test_51(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 450))
    #
    # def test_52(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 451))
    #
    # def test_53(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 452))
    #
    # def test_54(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 453))
    #
    # def test_55(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 454))
    #
    # def test_56(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 455))
    #
    # def test_57(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 456))
    #
    # def test_58(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 457))
    #
    # def test_59(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 458))
    #
    # def test_60(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 459))
    #
    # def test_61(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 460))
    #
    # def test_62(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 461))
    #
    # def test_63(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 462))
    #
    # def test_64(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 463))
    #
    # def test_65(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 464))
    #
    # def test_66(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 465))
    #
    # def test_67(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 466))
    #
    # def test_68(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 467))
    #
    # def test_69(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 468))
    #
    # def test_70(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 469))
    #
    # def test_71(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 470))
    #
    # def test_72(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 471))
    #
    # def test_73(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 472))
    #
    # def test_74(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 473))
    #
    # def test_75(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 474))
    #
    # def test_76(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 475))
    #
    # def test_77(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 476))
    #
    # def test_78(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 477))
    #
    # def test_79(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 478))
    #
    # def test_80(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 479))
    #
    # def test_81(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 480))
    #
    # def test_82(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 481))
    #
    # def test_83(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 482))
    #
    # def test_84(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 483))
    #
    # def test_85(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 484))
    #
    # def test_86(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 485))
    #
    # def test_87(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 486))
    #
    # def test_88(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 487))
    #
    # def test_89(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 488))
    #
    # def test_90(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 489))
    #
    # def test_91(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 490))
    #
    # def test_92(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 491))
    #
    # def test_93(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 492))
    #
    # def test_94(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 493))
    #
    # def test_95(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 494))
    #
    # def test_96(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 495))
    #
    # def test_97(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 496))
    #
    # def test_98(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 497))
    #
    # def test_99(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 498))
    #
    # def test_100(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 499))
