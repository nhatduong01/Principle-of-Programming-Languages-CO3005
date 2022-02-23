grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
} 

program: exp EOF;

exp: (term ASSIGN)* term; // Why this is right associativity

term: factor COMPARE factor | factor;

factor: operand (ANDOR operand)* ; // Why this is left assocuativity

operand: ID | INTLIT | BOOLIT | LB exp RB;

INTLIT: [0-9]+ ;

BOOLIT: 'True' | 'False' ;

LB: '(' ;

RB: ')' ;

ANDOR: 'and' | 'or' ;

ASSIGN: '+=' | '-=' | '&=' | '|=' | ':=' ;

COMPARE: '=' | '<>' | '>=' | '<=' | '<' | '>' ;

ID: [a-z]+ ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .;
