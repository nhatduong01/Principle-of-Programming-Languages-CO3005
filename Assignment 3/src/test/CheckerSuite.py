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
        expect = """Type Mismatch In Statement: VarDecl(Id($maxHeight),IntType,FloatLit(189.5))"""
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
        expect = """Type Mismatch In Statement: Return(Id(myArea))"""
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
        expect = """Type Mismatch In Statement: Return(Id(b))"""
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
                Var $score : Array[Float, 3] = Array(1,2, 3.4, 5);

        }
        """
        expect = """Type Mismatch In Statement: VarDecl(Id($score),ArrayType(3,FloatType),[IntLit(1),IntLit(2),FloatLit(3.4),IntLit(5)])"""
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_41(self):
        input = """
        Class Program
        {
            main()
            {
                Var b: Array[Boolean, 3] = Array(True, False, True);
                Var a: Array[Int, 2] = Array(True, False);
            }
        }"""
        expect = """Type Mismatch In Statement: VarDecl(Id(a),ArrayType(2,IntType),[BooleanLit(True),BooleanLit(False)])"""
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
        expect = """Type Mismatch In Statement: Return(Id(a))"""
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
                Var myArray : Array[Int, 5] = Array(1,2,3,4, True);
            }
        }"""
        expect = """Illegal Array Literal: [IntLit(1),IntLit(2),IntLit(3),IntLit(4),BooleanLit(True)]"""
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_45(self):
        input = """
        Class Program
        {
            Var $myArray: Array[Array[Array[Int,5],2],2] = Array(
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
        expect = """Type Mismatch In Statement: VarDecl(Id($myArray),ArrayType(2,ArrayType(2,ArrayType(5,IntType))),[[[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]],[[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]]])"""
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
        expect = """Type Mismatch In Statement: VarDecl(Id($myArray),ArrayType(3,ArrayType(2,ArrayType(4,IntType))),[[[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]],[[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]]])"""
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
        expect = """Illegal Array Literal: [[[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(5),IntLit(6),IntLit(7),IntLit(8)]],[[UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(2)),UnaryOp(-,IntLit(3)),UnaryOp(-,IntLit(4))],[UnaryOp(-,IntLit(5)),UnaryOp(-,IntLit(6)),UnaryOp(-,IntLit(7)),BooleanLit(False)]]]"""
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
        expect = """Type Mismatch In Statement: [[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(5),IntLit(6),IntLit(7),IntLit(8)]]"""
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_50(self):
        input = """
        Class Student
        {
            Var $numStudent: Int = 0;
            $getNumStudent()
            {
                Return 0;
            }
        }
        Class Program
        {
            main()
            {
                Var myStudent: Student;
                Val currSize: Int = myStudent::$getNumStudent();
            }
        }"""
        expect = """Illegal Member Access: CallExpr(Id(myStudent),Id($getNumStudent),[])"""
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_51(self):
        input = """
        Class Foo
        {
            $foo()
            {

            }
        }
        Class Program
        {
            main()
            {
                Var myFoo : Foo;
                myFoo::$foo();
            }
        }
        """
        expect = """Illegal Member Access: Call(Id(myFoo),Id($foo),[])"""
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_52(self):
        input = """
        Class Flower
        {
            Var height: Float;
            Var width: Float;
            getPrice( height, width: Float)
            {
                Return height * width;
            }
        }
        Class Program
        {
            main()
            {
                Var myPrice: Float = Flower.getPrice(5,4);
            }
        }"""
        expect = """Illegal Member Access: CallExpr(Id(Flower),Id(getPrice),[IntLit(5),IntLit(4)])"""
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_53(self):
        input = """
        Class SonTungMTP
        {
            Val isCopied: Boolean = True;
            compose()
            {
            }
        }
        Class Program
        {
        main()
        {
            SonTungMTP.compose();
        }
        }"""
        expect = """Illegal Member Access: Call(Id(SonTungMTP),Id(compose),[])"""
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_54(self):
        input = """
        Class Base
        {
            $foo(a, b: Int)
            {
                Return a * b;
            }
        }
        Class Derived: Base
        {

        }
        Class Program
        {
            main()
            {
                Var value: Int = Derived::$foo(4,5);
                Return value;
            }
        }"""
        expect = """Type Mismatch In Statement: Return(Id(value))"""
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_55(self):
        input = """
        Class Person
        {
            $goSleep()
            {

            }
        }
        Class Student : Person
        {

        }
        Class Program
        {
            main()
            {
            Student::$goSleep();
            Student::$goPooing();
            }
        }"""
        expect = """Undeclared Method: $goPooing"""
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_56(self):
        input = """
        Class Program
        {
            main()
            {
                Var a: Int = 5;
                Var b: Int = a.maxSize;
            }
        }"""
        expect = """Type Mismatch In Statement: FieldAccess(Id(a),Id(maxSize))"""
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_57(self):
        input = """
        Class Rectangle
        {
            Var height: Float;
            Var weight: Float;
            getArea()
            {
                Return Self.height * Self.weight;
            }
        }
        Class Program
        {
            main()
            {
                Var myShape : Rectangle ;
                Var b: Int = myShape.getArea();
            }

        }"""
        expect = """Type Mismatch In Statement: VarDecl(Id(b),IntType,CallExpr(Id(myShape),Id(getArea),[]))"""
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_58(self):
        input = """
        Class Butterfly
        {
            Val $maxPrice: Float = 1020.9;
            Var color: String;
            Var name: String;
            isHigh()
            {
                Return Self.color ==. "Red";
            }
        }
        Class Program
        {
            main()
            {
                Var myButterfly : Butterfly;
                Var isHigh: Boolean = myButterfly.isHigh();
                Var maxPrice: Float = myButterfly::$maxPrice;
            }
        }"""
        expect = """Illegal Member Access: FieldAccess(Id(myButterfly),Id($maxPrice))"""
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_59(self):
        input = """
        Class Animal
        {
            Var limbs: Int;
            Var hasWings: Boolean;
        }
        Class Human: Animal
        {
            Var name:String;
            create()
            {
                Var b: String = Self.limbs + Self.hasWings;
            }
        }"""
        expect = """Type Mismatch In Expression: BinaryOp(+,FieldAccess(Self(),Id(limbs)),FieldAccess(Self(),Id(hasWings)))"""
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_60(self):
        input = """
        Class Student
        {
            Var $Size: Int = 0;
            Var name: String;
        }
        Class Program
        {
            main()
            {
                Val currSize : Float = Student::$Size;
                Val name: String = Student.name;
            }
        }"""
        expect = """Illegal Constant Expression: FieldAccess(Id(Student),Id($Size))"""
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_61(self):
        input = """
        Class People
        {
            Var $maxHeight : Float;
            Var name: String;
            $getMaxHeight()
            {
                Return People::$maxHeight;
            }
            getName()
            {
                Return Self.name;
            }
        }
        Class Program
        {
            main()
            {
            Var maxHeight : Float = People::$getMaxHeight();
            Var myPeople : People;
            Val herName : String = myPeople.name;
            }
        }"""
        expect = """Illegal Constant Expression: FieldAccess(Id(myPeople),Id(name))"""
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_62(self):
        input = """
        Class Student
        {
            Var id: Int;
            Var name: String;
            Constructor(newId : Int ; newName: Float)
            {
                Self.id  = newId;
                Self.name = newName;
            }
        }"""
        expect = """Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(name)),Id(newName))"""
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_63(self):
        input = """
        Class Program
        {
            main()
            {
                Val sizeOfPeople: Int = 10;
                Val sizeofAnimals: Int = sizeOfPeople * 2;
                sizeOfPeople = 6;
            }
        }"""
        expect = """Cannot Assign To Constant: AssignStmt(Id(sizeOfPeople),IntLit(6))"""
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_64(self):
        input = """
        Class Cities
        {
            Val $numCities: Int = 100;
            Var name: String;
            Var population : Int;
            Constructor(newName : String; newPopulation:Int)
            {
                Self.name = newName;
                Self.population = newPopulation;
            }
        }
        Class Program
        {
            main()
            {
                Val currentSize : Int = Cities::$numCities;
                Cities::$numCities = Cities::$numCities + 1;
            }
        }"""
        expect = """Cannot Assign To Constant: AssignStmt(FieldAccess(Id(Cities),Id($numCities)),BinaryOp(+,FieldAccess(Id(Cities),Id($numCities)),IntLit(1)))"""
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_65(self):
        input = """
        Class Student
        {
            Var ID:Int;
            Var GPA: Float;
        }
        Class Program
        {
            main()
            {
                Var myStudent : Student;
                myStudent.ID = 1952638;
                myStudent.height = 1.87;
            }
        }"""
        expect = """Undeclared Attribute: height"""
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_66(self):
        input = """
        Class Student
        {
            Var name: String;
            Var ID: Int;
            Constructor(newName: String; newID : Int)
            {
                Self.name = newName;
                Self.ID = newID;
            }
        }
        Class Program
        {
            main()
            {
                Var myStudent: Student = New Student ();
            }
        }"""
        expect = """Type Mismatch In Expression: NewExpr(Id(Student),[])"""
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_67(self):
        input = """
        Class Program
        {
            main()
            {
                Var a: Int = 10;
                If(a  + 12)
                    {
                        a = a + 1;
                    }
            }
        }"""
        expect = """Type Mismatch In Statement: If(BinaryOp(+,Id(a),IntLit(12)),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))]))"""
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_68(self):
        input = """
        Class Program
        {
            main()
            {
                Val num: Int = 10;
                If (num >=0)
                {
                    Val num : Int = 12;
                    {
                        Var num: String = "duong";
                    }
                }
                Else
                {
                    Val num: Int = 13;
                }
                num = num * 10;
            }
        }"""
        expect = """Cannot Assign To Constant: AssignStmt(Id(num),BinaryOp(*,Id(num),IntLit(10)))"""
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_69(self):
        input = """
        Class Program
        {
            main()
            {
                Var a: Int = 5;
                If(a == 5)
                {
                    {}
                    Var a: String = "Hiii";
                }
                Elseif(a == 6)
                {
                    {
                        Var a : Boolean = True;
                    }
                }
                Elseif(a == 7)
                {
                    {}
                }
                Else
                {
                    {}
                }
                Var a : Float = 1.2;
            }
        }"""
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_70(self):
        input = """
        Class Program
        {
            main()
            {
                Var a: Int = 6;
                Foreach (i In 1 .. a By True)
                {
                    Var a:Boolean = True;
                }
            }
        }"""
        expect = """Type Mismatch In Statement: For(Id(i),IntLit(1),Id(a),BooleanLit(True),Block([VarDecl(Id(a),BoolType,BooleanLit(True))])])"""
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_71(self):
        input = """
        Class Program
        {
            main()
            {
                Var counter : Int = 0;
                Var my_index: Int;
                Foreach (my_index In 1 .. 8)
                {
                    counter = counter + 1;
                    Var a: Int = 9;
                }
                Val a: Int = counter + 2;
            }
        }"""
        expect = """Illegal Constant Expression: BinaryOp(+,Id(counter),IntLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_72(self):
        input = """
        Class Program
        {
            main()
            {
                Var i : Int;
                Foreach(i In 1 .. 100)
                {
                    {
                        Var i : Int = 10;
                        i = i + 1;
                    }
                }
                Var i : String = "Hello";
                Return i;
            }
        }"""
        expect = """Redeclared Variable: i"""
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_73(self):
        input = """
        Class Program
        {
            main()
            {
                Val i : Int = 10;
                Foreach(i In 1 .. 100)
                {
                }
            }
        }"""
        expect = """Cannot Assign To Constant: AssignStmt(Id(i),IntLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_74(self):
        input = """
        Class Program
        {
            main()
            {
                Val a : Int = 10;
                Val b : Int = 20;
                Var c: Int = 30;
                Val d: Int = a*c + b;
            }
        }"""
        expect = """Illegal Constant Expression: BinaryOp(+,BinaryOp(*,Id(a),Id(c)),Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_75(self):
        input = """
        Class Program
        {
            main()
            {
                Var sum: Int = 0;
                Var myArray: Array[Int, 5] = Array(1,2,3,4,5);
                Var i:Int;
                Foreach(i In 1 .. 5)
                {
                    If(sum >= 5)
                    {
                        Break;
                    }
                    Else
                    {
                        Continue;
                    }
                }
                Val result: Int = sum * 2;
            }
        }"""
        expect = """Illegal Constant Expression: BinaryOp(*,Id(sum),IntLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_76(self):
        input = """
        Class Program
        {
            main()
            {
                Var i: Int;
                Foreach (i In 1 .. 100)
                {
                    Foreach(i In 1 .. 5)
                    {
                        Break;
                    }
                    Break;
                }
                Break;
            }
        }"""
        expect = """Break Not In Loop"""
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_77(self):
        input = """
        Class Animal
        {
            Var name: String;
            Var age: Int;
            Var $maxAge: Int = 0;
            Constructor(newName : String ; newAge : Int)
            {
                If(newAge > Animal::$maxAge)
                {
                    Animal::$maxAge = newAge;
                }
                Self.name = newName;
                Self.age = newAge;
            }
        }
        Class Program
        {
            main()
            {
                Var myPig : Animal = New Animal ("Pig", 5);
                Var myOwl : Animal = New Animal ("Owl", 5.6);
            }
        }"""
        expect = """Type Mismatch In Expression: NewExpr(Id(Animal),[StringLit(Owl),FloatLit(5.6)])"""
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_78(self):
        input = """
        Class Animal
        {
            Var name: String;
            Var age: Int;
            Constructor(newName : String ; newAge : Int)
            {
                Self.name = newName;
                Self.age = newAge;
            }
            getName()
            {
                Return Self.name;
            }
        }
        Class People
        {
            Var name: String;
            Var $favoriteAnimal : Animal = New Animal("Dog", 5);
            Constructor(newName : String)
            {
                Self.name = newName;
            }
        }
        Class Program
        {
            main()
            {
                Var BorrisJohnson: People = New People ("Johnson");
                Var favoriteAnimal: String = People::$favoriteAnimal.getName();
                Var JoeBiden : People = New People ("Biden", "Capitalism");
            }
        }"""
        expect = """Type Mismatch In Expression: NewExpr(Id(People),[StringLit(Biden),StringLit(Capitalism)])"""
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_79(self):
        input = """
        Class Program
        {
            main()
            {
                Var myArray : Array[Int, 4] = Array(1,2,3,4);
                Var myFloat : Float = myArray[1];
                Val result : Float = myFloat;
            }
        }"""
        expect = """Illegal Constant Expression: Id(myFloat)"""
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_80(self):
        input = """
        Class Colors
        {
            Val $colors : Array[String, 4] = Array("Red", "Blue", "Green", "Yellow");
        }
        Class Program
        {
            main()
            {
                Var myColor : String = Colors::$colors[1];
                Var myNextColor : String = Colors::$colors[1][2];
            }
        }"""
        expect = """Type Mismatch In Expression: ArrayCell(FieldAccess(Id(Colors),Id($colors)),[IntLit(1),IntLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_81(self):
        input = """
        Class Program
        {
            main()
            {
                Var myArray: Array[Array[Int, 2], 2] = Array(
                    Array(1,2),
                    Array(3,4)
                );
                Var myInt : Int = myArray[1][1];
                Var nextInt : Int = myArray[2];
            }
        }
        """
        expect = """Type Mismatch In Statement: VarDecl(Id(nextInt),IntType,ArrayCell(Id(myArray),[IntLit(2)]))"""
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_82(self):
        input = """
        Class Program
        {
            main()
            {
                Var myList : Array [String, 3] = Array ("I", "support", "Ukraine");
                myList[3] = "Russia";
                Val myArray: Array[Float, 3] = Array(1.0, 3.4, 5.6);
                myArray[1] = 5;
            }
        }"""
        expect = """Cannot Assign To Constant: AssignStmt(ArrayCell(Id(myArray),[IntLit(1)]),IntLit(5))"""
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_83(self):
        input = """
        Class Program
        {
            Val $myAnimal : Array[String, 3] = Array("Cow", "Bird", "Alligator");
            main()
            {
                Var favoriteAnimal : String = Program::$myAnimal[1];
                Program::$myAnimal[1] = "Parrot";
            }
        }"""
        expect = """Cannot Assign To Constant: AssignStmt(ArrayCell(FieldAccess(Id(Program),Id($myAnimal)),[IntLit(1)]),StringLit(Parrot))"""
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_84(self):
        input = """
        Class Program
        {
            main()
            {
                Var firstArray : Array[Array[Int ,2], 3] = Array(
                    Array(1,2),
                    Array(3,4),
                    Array(5,6)
                );
                Var secondArray : Array[Int , 2] = firstArray[1];
                Var thirdArray : Array[Int, 2] = firstArray;
            }
        }"""
        expect = """Type Mismatch In Statement: VarDecl(Id(thirdArray),ArrayType(2,IntType),Id(firstArray))"""
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_85(self):
        input = """
        Class Program
        {
            main ()
            {
                Var myArray: Array[Array[Array[Int,4],2],2] = Array(
                        Array(
                            Array(1,2,3,4),
                            Array(1,2,3,4)
                        ),
                        Array(
                            Array(1,2,3,4),
                            Array(1,2,3,4)
                        )
                    );
                Var nextArray : Array[Array[Int,4],2] = myArray[1];
                Var value : Int = myArray[1][1][1];
                If (value)
                {
                    Var value : Boolean = True;
                }
            }
        }"""
        expect = """Type Mismatch In Statement: If(Id(value),Block([VarDecl(Id(value),BoolType,BooleanLit(True))]))"""
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_86(self):
        input = """
                    Class C{
                        e(){
                            Var c:Float = --------1.22;
                            Var d:Boolean = !((("abc" +. "def") ==. "ghi") || False);
                            Var e:Float = !!!!--1.22;
                        }
                    }"""
        expect = "Type Mismatch In Expression: UnaryOp(!,UnaryOp(-,UnaryOp(-,FloatLit(1.22))))"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_87(self):
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class C{
                            e(){
                                Var a:B;
                                Var d:Float = a.c(1,2);
                                Var e:String = a.c(1.1,2);
                            }
                        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(a),Id(c),[FloatLit(1.1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_88(self):
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(x:Int; y:Float; z:String){}
                        }
                        Class A{}
                        Class C{
                            e(){
                                Var a:B = New B();
                                a = New A();
                            }
                        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),NewExpr(Id(A),[]))"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_89(self):
        input = """
                        Class C{
                            e(){
                                Var a:Int = 1;
                                Var b:Int = 1;
                                If (True){
                                    Var a:Int = 2;
                                }
                                Elseif(True){
                                    Var a:Int = 2;
                                }
                                Else{
                                    Var a:Int = 2;
                                }
                                Var b:Int = 2 ;
                            }
                        }"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_90(self):
        input = """
                        Class C{
                            e(){
                                Var i:Int = 0;
                                Foreach(i In 1 .. 10 By 1){
                                    Var a:Int = 1;
                                    Break;
                                    If (True){
                                        Var a:Int = 1;
                                        Continue;
                                    }
                                }
                                Continue;
                            }
                        }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_91(self):
        input = """
        Class A{
            Var $a:Int = 5;
            Var b:Int = 4;
        }
        Class B{
        func(){
            Var b:Int = A::$a;
            b = A.b;
        }
        }"""
        expect = "Illegal Member Access: FieldAccess(Id(A),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_92(self):
        input = """
                        Class A{
                            $a(){
                                Return 1;
                            }
                            b(){
                                Return 1;
                            }
                        }
                        Class B{
                        func(){
                            Var b:A = New A();
                            Var c:Int = A::$a();
                            c = b.b();
                            c = b::$a();
                        }
                        }"""
        expect = "Illegal Member Access: CallExpr(Id(b),Id($a),[])"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_93(self):
        input = """
        Class B{
        Var x:Int = 1;
        foo(){
            Return 1;
        }
        func (){
            Var a:Int = Self.x;
            a = Self.foo();
            Var b:String = Self.foo();
        }
        } """
        expect = "Type Mismatch In Statement: VarDecl(Id(b),StringType,CallExpr(Self(),Id(foo),[]))"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_94(self):
        input = """
        Class A {
            Var a:Int = 1;
            foo(){
                Return 1;
            }
        }
        Class B{
            Var b:A = New A();
            foo(){
                Return New A();
            }
        }
        Class C{
            foo(){
                Var c:B = New B();
                Var e:Int = c.b.a;
                e = c.b.foo();
                e = c.foo().a;
                e = c.foo().foo();
                Var f:Int = c.foo();
            }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(f),IntType,CallExpr(Id(c),Id(foo),[]))"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_95(self):
        input = """
        Class A {
            Var a:Int = 1;
            fooExp(x:Float; y:String){
                Return 1;
            }
            fooCall(x:Float; y:String){}
        }
        Class B{
            Var b:A = New A();
            foo(){
                Return New A();
            }
            foo2(){
                Var e:Int = Self.b.a;
                e = Self.b.fooExp(1, "a");
                e = Self.foo().a;
                e = Self.foo().fooExp(1, "a");
                Self.b.fooCall(1, "a");
                Self.foo().fooCall(1, "a");
                Self.g().fooCall(1, "a");
            }
        }"""
        expect = "Undeclared Method: g"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_96(self):
        input = """
            Class A {
                Var a:Int = 1;
                $fooExp1(x:Float; y:String){
                    Return Self.a;
                }
                $fooExp2(x:Float; y:String){
                    Return x;
                }
                $fooExp3(x:Float; y:String){
                    Return y;
                }
            }
            Class B{
                foo2(){
                    Var e:Float = (New A()).a;
                    e = A::$fooExp1(1, "a");
                    e = A::$fooExp2(1, "a");
                    Var f:String = A::$fooExp3(1, "a");
                    Var g:Float = A::$fooExp3(1, "a");
                }
            }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(g),FloatType,CallExpr(Id(A),Id($fooExp3),[IntLit(1),StringLit(a)]))"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_97(self):
        input = """
        Class A {
           $fooExp1(){
                Var a: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1));
                a[1] = Array(1,1);
                a[1][1] = 1;
                a = 1;
           }
        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_98(self):
        input = """     
        Class A {
            Var a:Int = 1;
            $fooExp1(x:Float; y:String){
                    Return Self.a;
            } 
            $fooExp2(x:Float; y:String){
                    Return x;
            }  
            $fooExp3(x:Float; y:String){
                    Return y;
            }               
            }                        
            Class BB{
                foo2(){
                    Var e:Float = (New A()).a - 7;
                    e = A::$fooExp1(1, "a") +2 - -----5;
                    e = A::$fooExp2(1, "a") + 1;
                    Var f:String = A::$fooExp3(1, "a") +. "abc";
                    Var g:String = A::$fooExp3(1, "a") + 1;
                }
            }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,CallExpr(Id(A),Id($fooExp3),[IntLit(1),StringLit(a)]),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 484))
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_99(self):
        input = """     
        Class A {
            Var a:Int = 1;
            fooExp(x:Float; y:String){
                Return 1;
            }  
            fooCall(x:Float; y:String){}                    
        }                        
        Class B{ 
            Var b:A = New A();
            foo(){
                Return New A();
            }
            foo2(){
                Var e:Int = Self.b.a;
                e = Self.b.fooExp(1, "a");
                e = Self.foo().a;
                e = Self.foo().fooExp(1, "a");
                Self.b.fooCall(1, "a");
                Self.foo().fooCall(1, "a");
                Self.g().fooCall(1, "a");
            }
        }"""
        expect = "Undeclared Method: g"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_100(self):
        input = """     
        Class A {
            Var a:Int = 1;
            fooExp(x:Float; y:String){
                Return 1;
            }  
            fooCall(x:Float; y:String){}                    
        }                        
        Class B{ 
            Var b:A = New A();
            foo(){
                Return New A();
            }
            foo2(){
                Var e:Int = Self.b.a;
                e = Self.b.fooExp(1, "a");
                e = Self.foo().a;
                e = Self.foo().fooExp(1, "a");
                Self.b.fooCall(1, "a");
                Self.foo().fooCall(1, "a");
                Self.g().fooCall(1, "a");
            }
        }"""
        expect = "Undeclared Method: g"
        self.assertTrue(TestChecker.test(input, expect, 499))
