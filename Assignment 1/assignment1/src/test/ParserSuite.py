import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_1_very_simple_program (self):
        input = """
        Class Program
        {
            main()
            {
                System.out.printLn("Hello World");
            }
        }
        """ 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,200))
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Class main {
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
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_multi_dimension_array(self):
        """More complex program"""
        input = """
        Class Program
        {
            main ()
            {
                Var a: Array[Array[Array[Int,1],2],2] = Array(
                    Array(Array(1), Array(1)),
                    Array(Array(1), Array(1))
                );
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_small_program(self):
        """Miss ) int main( {}"""
        input = """        
        Class Program {
            main() {
            Var a, b, c: Int;
            Val d, e, f: Float = 2.2, 3e3, 4.4e4;
            Var arr: Array[Int, 7];
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    def test_many_classes (self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;
            
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        
        Class Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }""" 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,204))

    def test_single_main (self):
        input = """
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
                why.why();
            }
        }""" 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,205))

    def test_6_many_classes_2 (self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;
            
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        
        Class Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }

        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
                why.why();
            }
        }""" 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,206))

    def test_7_parenthesis (self):
        input = """
        Class Program
        {
            main()
            {

            }
            foo()
            {
                Val a: Int = (3+5) + (1 + 2);
                Return a;
            }
        }""" 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,207))

    def test_8_member_access (self):
        input = """
        Class Program
        {
            main()
            {

            }
            foo()
            {
                Val a: Int = (Self.newValue() + 2) + (1 + 2);
                Return a;
            }
        }""" 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,208))

    def test_9_member_Access (self):
        input = """
        Class Program
        {
            main()
            {

            }
            foo()
            {
                Val a: Int = Self.newValue() ;
                Return a;
            }
        }""" 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,209))

    def test_10_member_access (self):
        input = """
        Class Program
        {
            main()
            {

            }
            foo()
            {
                Val a: Int = Self.newValue() + 2;
                Return a;
            }
        }""" 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,210))

    def test_11_associativity (self):
        input = """
        Class Program
        {
            main()
            {

            }
            foo() {
                Val a: Boolean = (a.b.c.e() > 6) + (1 + 2);
                Return "Why\n'"\b";
            }

        }""" 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,211))

    def test_12_index_Array (self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;
            Val arr: Array[Array[Int, 2], 1] = Array(Array(1,2));
            
            $getNumOfShape() {
                Return $numOfShape;
            }
            
            getArr() {
                Return arr[1-1][1*1];
            }
        }""" 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,212))

    def test_13_index_operations (self):
        input = """
        Class Program
        {
            $getValue()
            {
                Return 0;
            }
            main ()
            {
                Var a: Array[Array[Array[Int,3],2],2] = Array(
                    Array(Array(1,3,4), Array(1,5,6)),
                    Array(Array(1,7,8), Array(1,9,10))
                );

                Var b: Int = a[1+5*9][0][Self.$getValue()];
            }
        }""" 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,213))

    def test_14_for_in (self):
        input = """
        Class Program {
            main() {
                Var rect: Int = New Rectangle();
                Out.printInt(Shape::$numOfShape);
                Self.foo(Self.foo(), 2);
                rect = Shape::$numOfShape;
                rect = rect.length;
                Foreach (i In 1 .. 100 By 2) {
                    Out.printInt(i);
                }
                If (i == 1) {
                    Foreach (i In 1 .. 100 By 2) {
                        Out.printInt(i);
                    }
                }
                Elseif (i == 2) {
                    Foreach (i In 2 .. 100) {
                        Out.printInt(i);
                    }
                }
                Else {
                    Foreach (i In 3 .. 100 By 2) {
                        Out.printInt(Self.foo() +. "lul");
                    }
                }
            }
            foo() {
                Val a: Boolean = (a.b.c.e() > 6) + (1 + 2);
                Return "Why\n'"\b";
            }
        }
        """ 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,214))

    def test_15_If_block2 (self):
        input = """
        Class Program
        {
            recursion(a:Int)
            {
                If((a == 0) || (a== 1))
                    {
                        Return 1;
                    }
                Else
                    {
                        Return Self.recursion(a - 1);
                    }
            }
            main()
            {
                Var a: Int = Self.recursion(6);
                System.out.printLn(a);
            }
        }""" 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,215))

    def test_16_sum (self):
        input = """
        Class Program
        {
            main()
            {
                Val my_array: Array[Int, 6] = Array(2,3,1,4,5,6,7,8);
                Var my_sum : Int = 0;
                Foreach (my_index In 1 .. 8)
                {
                    my_sum = my_sum + my_array[my_index];
                }
                Return my_sum;
            }
        }
        """ 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,216))

    def test_17_sum_odd (self):
        input = """
        Class Program
        {
            main()
            {
                Val my_array: Array[Int, 6] = Array(2,3,1,4,5,6,7,8);
                Var my_sum_odd : Int = 0;
                Var my_sum_even: Int = 0;
                Foreach (my_index In 1 .. 8)
                {
                    If(my_array[my_index] % 2 == 0)
                    {
                        my_sum_even  = my_sum_even + my_array[my_index];
                    }
                    Else
                    {
                        my_sum_odd  = my_sum_odd + my_array[my_index];
                    }
                }
                If (my_sum_even > my_sum_odd)
                {
                    Return True;
                }
                Else
                {
                    Return False;
                }
            }
        }""" 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,217))

    def test_18_error (self):
        input = """
        Class Program
        {
            main()
            {
                a.$foo();
            }
        }""" 
        expect = """Error on line 6 col 24: ;"""
        self.assertTrue(TestParser.test(input,expect,218))

    def test_19_circle (self):
        input = """
        Class Circle
        {
            Var radius:Int;
            Circle (Radius: Int)
            {
                self.radisu = Radius;
            }
            getArea()
            {
                Return Self.radius * 3.14;
            }
        }
        Class Program
        {
            main()
            {
                Var radius: Float = 5.26;
                Var my_circle : Int = New Circle(5.26);
                System.Out.printLn(my_circle.getArea());
            }
        }""" 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,219))

    def test_20_fibonacci (self):
        input = """
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
        }
        """ 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,220))

    def test_21_recursion (self):
        input = """
        Class Program
        {
            main()
            {
                a.a.b.c();
            }
        }""" 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,221))

    def test_22_wrong (self):
        input = """
        Class Program
        {
            fibonacci(myNum:Int)
            {
                If(myNum == 0 || myNum == 1)
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
        }
        """ 
        expect = """Error on line 6 col 39: =="""
        self.assertTrue(TestParser.test(input,expect,222))

    def test_23_for_each (self):
        input = """
        Class Program
        {
            main()
            {
                Val myArray: Array[Int, 5] = Array(1,2,3,4,5);
                Val sum: Int = 0;
                Foreach (index In 1 .. 5)
                {
                    sum = sum + myArray[index];
                    If(index == 4)
                    {
                        Break;
                    }
                }
            }
        }""" 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,223))

    def test_24_inheritance (self):
        input = """
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
        }""" 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,224))

    def test_25_constructor (self):
        input = """
        Class BaseClass 
        {
            Var $numOfObjs: Int = 0;
            Constructor() 
            {
                BaseClass::$numOfObjs = BaseClass::$numOfObjs + 1;
            }
        }""" 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,225))

    def test_26_inheritance (self):
        input = """
                Class BaseClass {
            Var $numOfObjs: Int = 0;
            Constructor() {
                BaseClass::$numOfObjs = BaseClass::$numOfObjs + 1;
            }
            Destructor() {
                BaseClass::$numOfObjs = BaseClass::$numOfObjs - 1;
                Out.printLn("Can\'t even be free for a day huh");
            }
            $staticMethod() {
                Out.printLn(Program.gcd(123_456,46*75%3));
            }
        }
        Class DerivedClass : BaseClass {
            Var UUID: Int;
        }
    """ 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,226))

    def test_27_long_program (self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;
            Val arr: Array[Array[Int, 2], 1] = Array(Array(1,2));
            
            $getNumOfShape() {
                Return $numOfShape;
            }
            
            getArr() {
                Return arr[1-1][1*1];
            }
        }
        
        Class Rectangle: Shape {
            Constructor() {
                Self.length = 3;
                Self.width = 2;
            }
            getArea() {
                Return Self.length * Self.width;
            }
        }

        Class Program {
            main() {
                Var rect: Int = New Rectangle();
                Out.printInt(Shape::$numOfShape);
                Self.foo(Self.foo(), 2);
                rect = Shape::$numOfShape;
                rect = rect.length;
                Foreach (i In 1 .. 100 By 2) {
                    Out.printInt(i);
                }
                If (i == 1) {
                    Foreach (i In 1 .. 100 By 2) {
                        Out.printInt(i);
                    }
                }
                Elseif (i == 2) {
                    Foreach (i In 2 .. 100) {
                        Out.printInt(i);
                    }
                }
                Else {
                    Foreach (i In 3 .. 100 By 2) {
                        Out.printInt(Self.foo() +. "lul");
                    }
                }
            }
            foo() {
                Val a: Boolean = (a.b.c.e() > 6) + (1 + 2);
                Return "Why\n'"\b";
            }
        }
""" 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,227))

    def test_28_long_main (self):
        input = """
        Class Program
        {
            main()
            {
                Var c: Int = New Creeper();
                If (c.height < -2.)
                { ##ALLAHU AKBAR## 
                    System.out.printLn("Is that a short joke?");
                }
                ##CHECK IT GEE##
                ##UGG##
                Val dolls: Array[String, 9] = Array("Shanhai","Hourai","France","Holland","Tibet","Kyoto","London","Russia","Orlean");
                System.out.printLn("But then again, yesterday wasn't all that easy lol "); ##^_^##
                Var obj: Int = New DerivedClass();
                Var array: Array[Int, 4] = Array(1,2,3,4);
                Var darray: Array[Array[Int, 1], 4] = Array(Array(1_12), Array(OxD_2), Array(0776_5_6), Array(0B111));
                Var exp: Int = (0XDD + (Self.gcd(12, 52) / 6 % 5) * darray[3][1] - BaseClass::$numOfObjs * array[obj.UUID]) / .e0;
                Var b: Boolean = !Self.megazord();
                Foreach(array[1] In darray[1][1] .. Self.gcd(4,28) By (c.height * BaseClass::$numOfObjs)) 
                {
                    BaseClass::$staticMethod();
                }

            }
        }""" 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,228))

    def test_29_full_class (self):
        input = """
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
        """ 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,229))

    def test_30_many_escape (self):
        input = r"""
        Class BaseClass {
            Var $numOfObjs: Int = 0;
        }
        Class DerivedClass : BaseClass {
            Var UUID: Int;
        }
        Class Program {
            main() {
                Var obj: Int = New DerivedClass();
                Var array: Array[Int, 4] = Array(1,2,3,4);
                Var darray: Array[Array[Int, 1], 4] = Array(Array(1), Array(2), Array(3), Array(4));
                Var exp: Int = 0XDD + (Self.gcd(12, 52) / 6 % 5) * darray[3][1] - BaseClass::$numOfObjs * array[obj.UUID];
                Var b: Boolean = !Self.megazord();
            }
            megazord() {
                Val goodAdvice: String = "This is pointless";
                Return !(!True || False && (goodAdvice ==. "This is pointless\n\t\r\f\b'"\'\\"));
            }
            gcd(a, b: Int) {
                If (a == 0) {Return b;}
                Return Self.gcd(b % a, a);
            }
        }
        """ 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,230))

    def test_31_linked_list (self):
        input = """
        Class Program
        {
            addNewNode(newNode,head: Int)
            {
                newNode.next_node = head;
                head = new_node;
            }
            deleteNode(position,head: Int)
            {
                If(head == 0)
                {
                    head = head.next_node;
                }
                Else
                {
                    Var curr: Int = head.next.next;
                    Var prev: Int = curr;
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,231))

    def test_32_class_linked_list (self):
        input = """
        Class LinkedList
        {
            LinkedList()
            {
                Self.value = 0;
                Self.next_node = Null;
            }
            LinkedList(new_value: Int; nextNode: Int)
            {
                Self.value = new_value;
                Self.next_node = nextNode;
            }
            Val value:Int;
            Val next_node: Boolean;
        }""" 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,232))

    def test_33_circle_radius (self):
        input = """
        Class Circle""" 
        expect = """"""
        self.assertTrue(TestParser.test(input,expect,233))

    # def test34 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,234))

    # def test35 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,235))

    # def test36 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,236))

    # def test37 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,237))

    # def test38 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,238))

    # def test39 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,239))

    # def test40 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,240))

    # def test41 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,241))

    # def test42 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,242))

    # def test43 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,243))

    # def test44 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,244))

    # def test45 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,245))

    # def test46 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,246))

    # def test47 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,247))

    # def test48 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,248))

    # def test49 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,249))

    # def test50 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,250))

    # def test51 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,251))

    # def test52 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,252))

    # def test53 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,253))

    # def test54 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,254))

    # def test55 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,255))

    # def test56 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,256))

    # def test57 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,257))

    # def test58 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,258))

    # def test59 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,259))

    # def test60 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,260))

    # def test61 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,261))

    # def test62 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,262))

    # def test63 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,263))

    # def test64 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,264))

    # def test65 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,265))

    # def test66 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,266))

    # def test67 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,267))

    # def test68 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,268))

    # def test69 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,269))

    # def test70 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,270))

    # def test71 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,271))

    # def test72 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,272))

    # def test73 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,273))

    # def test74 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,274))

    # def test75 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,275))

    # def test76 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,276))

    # def test77 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,277))

    # def test78 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,278))

    # def test79 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,279))

    # def test80 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,280))

    # def test81 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,281))

    # def test82 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,282))

    # def test83 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,283))

    # def test84 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,284))

    # def test85 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,285))

    # def test86 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,286))

    # def test87 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,287))

    # def test88 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,288))

    # def test89 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,289))

    # def test90 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,290))

    # def test91 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,291))

    # def test92 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,292))

    # def test93 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,293))

    # def test94 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,294))

    # def test95 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,295))

    # def test96 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,296))

    # def test97 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,297))

    # def test98 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,298))

    # def test99 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestParser.test(input,expect,299))
