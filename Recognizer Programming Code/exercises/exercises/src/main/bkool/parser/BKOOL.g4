grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}
// eX1
// program  : vardecl | funcdecl;
// vardecl: 'vardecl' ;

// funcdecl: 'funcdecl' ;
// ex2
// program: declarations EOF;
// declarations: singleDeclarationg declarationsList ;
// declarationsList: singleDeclarationg declarationsList | ;
// singleDeclarationg: variable_declare | function_declare;
// variable_declare: mptype listOfID SEMI;
// listOfID: ID theRestIDList;
// theRestIDList: COMMA ID theRestIDList| ;
// function_declare:mptype ID LB parameters  RB body;
// parameters: parameter theRestParameterList |;
// parameter: mptype listOfID ;
// theRestParameterList: SEMI parameter theRestParameterList |;
// body: 'body';

// ex3
// program: declarations EOF;
// declarations: singleDeclarationg declarationsList ;
// declarationsList: singleDeclarationg declarationsList | ;
// singleDeclarationg: variable_declare | function_declare;
// variable_declare: mptype listOfID SEMI;
// listOfID: ID theRestIDList;
// theRestIDList: COMMA ID theRestIDList| ;
// function_declare:mptype ID LB parameters  RB body;
// parameters: parameter theRestParameterList |;
// parameter: mptype listOfID ;
// theRestParameterList: SEMI parameter theRestParameterList |;
// mptype: INTTYPE | FLOATTYPE;
// body: LP command RP;
// command: single_command theRestCommand |;
// theRestCommand: single_command theRestCommand|;
// single_command: variable_declare | statement;
// statement: ID '=' expr SEMI
// 		 | ID LB listofExp RB SEMI
// 		 | 'return' expr SEMI;
// listofExp: expr theRestExp | ;
// theRestExp: COMMA expr theRestExp | ;
// exp4 
program: declarations EOF;
declarations: singleDeclarationg declarationsList ;
declarationsList: singleDeclarationg declarationsList | ;
singleDeclarationg: variable_declare | function_declare;
variable_declare: mptype listOfID SEMI;
listOfID: ID theRestIDList;
theRestIDList: COMMA ID theRestIDList| ;
function_declare:mptype ID LB parameters  RB body;
parameters: parameter theRestParameterList |;
parameter: mptype listOfID ;
theRestParameterList: SEMI parameter theRestParameterList |;
mptype: INTTYPE | FLOATTYPE;
body: LP command RP;
command: single_command theRestCommand |;
theRestCommand: single_command theRestCommand|;
single_command: variable_declare | statement;
statement: ID '=' expr SEMI
		 | ID LB listofExp RB SEMI
		 | 'return' expr SEMI;
listofExp: expr theRestExp | ;
theRestExp: COMMA expr theRestExp | ;
//body: funcall SEMI;
expr: sub_expr '+' expr | sub_expr;
sub_expr: div_mul_expr '-' div_mul_expr | div_mul_expr;
div_mul_expr: div_mul_expr '/' blacket_expr | div_mul_expr '*' blacket_expr | blacket_expr;
blacket_expr: LB expr RB | INTLIT | FLOATLIT | ID | ID LB listofExp RB;


exp: funcall | INTLIT ;

funcall: ID LB exp? RB ;

INTTYPE: 'int' ;

FLOATTYPE: 'float';

VOIDTYPE: 'void'  ;

ID: [a-zA-Z]+ ;

INTLIT: [0-9]+;
FLOATLIT:INTLIT '.' INTLIT;
LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SEMI: ';' ;
COMMA: ','; 

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;