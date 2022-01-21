grammar D96;
// 1952638
@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
// Default setting
program: class_declaration+ EOF;





// Expression 

exp: relational_operations string_operators relational_operations | relational_operations ;

relational_operations: logical_operations relational_operators logical_operations | logical_operations;

logical_operations: logical_operations logical_and_or adding_operations | adding_operations;

adding_operations: adding_operations adding_operators multiplying_operations | multiplying_operations;

multiplying_operations: multiplying_operations multiplying_operators logical_negate_operation | logical_negate_operation;

logical_negate_operation: NEGATE logical_negate_operation | sign_operations;

sign_operations: MINUS sign_operations | index_operations;

index_operations: index_operations index_operators | member_access_operarion;

member_access_operarion: member_access_operarion DOT object_create_operation
                       | member_access_operarion STATIC_ACCESS  object_create_operation
                       | member_access_operarion DOT object_create_operation LB expList RB
                       | member_access_operarion STATIC_ACCESS  object_create_operation LB expList RB
                       | object_create_operation;


object_create_operation: NEW object_create_operation LB expList RB| parenthesis_operations;

parenthesis_operations: LB exp RB
                      |INTLIT | STRINGLIT | BOOLEANLIT | FLOATLIT | ID | array_lit | DOLLARID; 

// ArrayLIT dau


string_operators: STRINGCOMPARE | STRINGCONCAT;

relational_operators: EQUAL | DIFFERENT | LESSER | LESSTHANEQUAL | GREATER | GREATERTHANEQUAL;

logical_and_or: AND | OR;

adding_operators: PLUS | MINUS;

multiplying_operators: MULTIPLY | DIVIDE | MODULO;

element_expression : exp index_operators;

index_operators : '[' exp ']'
                | '[' exp ']' index_operators;

// Array Literature
array_lit: ARRAYTYPE LB expList RB;



// If statement

if_statements: IF LB exp RB block_statements else_ifList? else_statements?;

else_ifList:  else_if the_rest_else_if;

the_rest_else_if: else_if the_rest_else_if |;

else_if: ELSEIF LB exp RB block_statements; 

else_statements: ELSE block_statements;

// Assignment statement;

assignment_statements: (ID | element_expression) ASSIGN exp SEMI;

// For/In

foreach_statements: FOREACH LB ID IN  exp '..' exp (BY exp)? RB block_statements;

// break statements

break_statements: BREAK SEMI;

// Continue statements

continue_statements: CONTINUE SEMI;

// return statements

return_statements: RETURN exp SEMI;

// Method invocation

method_invocations: ID STATIC_ACCESS DOLLARID LB RB SEMI;

block_statements: LP  list_statement RP;

list_statement: single_statement the_rest_statements |;

the_rest_statements: single_statement the_rest_statements |;

// Variable and Constant Declaration Statement
variable_constant_declaration: (VAR | VAL) variableList COLON primitive_type ( ASSIGN expList)? SEMI;

variableList:ID iDlist;

single_statement: if_statements 
                | assignment_statements 
                | foreach_statements 
                | break_statements 
                | continue_statements 
                | return_statements
                | method_invocations
                | variable_constant_declaration;










// class declaration
class_declaration:CLASS  ID (COLON ID)? LP  attributes_methods_declarations RP;

attributes_methods_declarations: attribute_declaration the_rest_attributes_methods_declarations
                               | method_declaration the_rest_attributes_methods_declarations
                               |;

the_rest_attributes_methods_declarations: attribute_declaration the_rest_attributes_methods_declarations
                                        | method_declaration the_rest_attributes_methods_declarations
                                        |;
/// the IDlist's length is not equal to the assignment list
arrayDeclaration: ARRAYTYPE  '[' primitive_type COMMA INTLIT ']';

attribute_declaration: (VAR | VAL) attributesList COLON primitive_type ( ASSIGN expList)? SEMI;
// assignment: ID ASSIGN exp;
attributesList: (DOLLARID| ID) iDlist;

iDlist: COMMA (DOLLARID | ID) iDlist |;

expList: exp theRestExp;

theRestExp: COMMA exp theRestExp |;

primitive_type: BOOLEANTYPE | INTTYPE| FLOATTYPE | STRINGTYPE | arrayDeclaration;

method_declaration: (DOLLARID | ID) LB list_parameters RB  block_statements
                  | constructor
                  | destructor;


list_parameters: parameters_declaration the_rest_parameters_declarations |;

the_rest_parameters_declarations: SEMI parameters_declaration the_rest_parameters_declarations |;

parameters_declaration: same_type_parameters primitive_type;

same_type_parameters: ID the_rest_ID |;

the_rest_ID: COMMA ID the_rest_ID |;

constructor: CONSTRUCTOR LB list_parameters RB block_statements;

destructor: DESTRUCTOR LB RB block_statements;







LB: '(';

RB: ')';

LP: '{';

RP: '}';

SEMI: ';';

COMMA: ',';

COLON: ':';

// Key words
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
IN: 'In';
RETURN: 'Return';
NULL: 'Null';
CLASS: 'Class';
VAL: 'Val';
VAR: 'Var';
CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
NEW: 'New';
BY: 'By';
SELF: 'Self';
// Comment skipping
UNTERMINATED_COMMENT:  '##' ('#' ~'#' | ~'#')*? EOF;

BlockComment 
    : '##' .*? '##' -> skip
    ;


// Operators
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MODULO: '%';
NEGATE: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
ASSIGN: '=';
DIFFERENT: '!=';
GREATER: '>';
LESSTHANEQUAL: '<=';
LESSER: '<';
GREATERTHANEQUAL: '>=';
STRINGCOMPARE: '==.';
STRINGCONCAT: '+.';
STATIC_ACCESS: '::';
DOT: '.';
// Primitive type


INTTYPE: 'Int';
FLOATTYPE: 'Float';
STRINGTYPE: 'String';
BOOLEANTYPE: 'Boolean';
ARRAYTYPE: 'Array';
VOIDTYPE: 'Void';

// Literal
//float
fragment DECIMALPART: '.'[0-9]?([0-9]|'_'[0-9])*;
fragment EXPONENTPART: [eE][+-]?[1-9]+([0-9]|'_'[0-9])*
                     | [Ee][+-]?[0];
//FLOATLIT: ('0'|([1-9]+[0-9_]*))?(DECIMALPART |EXPONENTPART | (DECIMALPART EXPONENTPART)) {self.text = self.text.replace("_","")};
FLOATLIT: DEC DECIMALPART EXPONENTPART{self.text = self.text.replace("_","")}
        | DEC EXPONENTPART {self.text = self.text.replace("_","")}
        | DECIMALPART EXPONENTPART {self.text = self.text.replace("_","")}
        | DEC DECIMALPART {self.text = self.text.replace("_","")};
// Int
// hai gach lien tiep
fragment OCT: '0'[1-7]([0-7]|'_'[1-7])*;
fragment HEX: ('0x'|'0X')[0-9A-Z]([0-9A-Z]|'_'[0-9A-Z])*;
fragment BIN: ('0b'|'0B')[01]([01]|'_'[01])*;
fragment DEC: '0'|[1-9]([0-9]|'_'[0-9])*;
// ([1-9]+([0-9]|'_'[0-9]))
INTLIT: (OCT|HEX|BIN|DEC) {self.text = self.text.replace("_", "")};
//INTLIT: [1-9_]+ {self.text = self.text.replace("_", "")};
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
// Boolean
BOOLEANLIT: ('False'| 'True');
// String
ILLEGAL_ESCAPE: '"'(~[\\'"]| EscapeSequence)*('\\' ~[btnfr'\\] | '\'' ~'"') {raise IllegalEscape(self.text[1:])};
fragment EscapeSequence: ('\\b'|'\\f'|'\\r'|'\\n'|'\\t'|'\\\''|'\\\\'| '\'"');
STRINGLIT: '"'(EscapeSequence |~[\\'"])*'"' {self.text = self.text[1:-1]};
UNCLOSE_STRING: '"'(EscapeSequence |~[\\'"])* EOF {raise UncloseString(self.text[1:])};
DOLLARID: '$'[a-zA-Z_]+[a-zA-Z0-9_]*;
ID: [a-zA-Z_]+[a-zA-Z0-9_]*;
ERROR_CHAR: . {raise ErrorToken(self.text)};
//{raise UncloseString(self.text[1:])}