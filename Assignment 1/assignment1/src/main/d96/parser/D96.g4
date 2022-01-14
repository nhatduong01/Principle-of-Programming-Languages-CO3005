grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: mptype 'main' LB RB LP body? RP EOF;

mptype: INTTYPE | VOIDTYPE;

body: funcall SEMI;

exp: funcall | INTLIT;

funcall: ID LB exp? RB;





LB: '(';

RB: ')';

LP: '{';

RP: '}';

SEMI: ';';

// Key words
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
TRUE: 'True';
FALSE: 'False';
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
DOLLAR: '$';
// Comment skipping
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
STRINCONCAT: '+.';
DOT: '.';
STATIC_ACCESS: '::';

// Primitive type
INTTYPE: 'Int';
FLOATTYPE: 'Float';
STRINGTYPE: 'String';
BOOLEANTYPE: 'Boolean';
ARRAYTYPE: 'Array';
VOIDTYPE: 'void';

// Literal
//float
fragment DECIMALPART: '.'[0-9_]?;
fragment EXPONENTPART: [eE][+-][1-9]+[0-9_]*;
FLOATLIT: ([1-9]+[0-9_]*)?(DECIMALPART |EXPONENTPART | (DECIMALPART EXPONENTPART)) {self.text = self.text.replace("_","")};
// Int
// hai gach lien tiep
fragment OCT: '0'[1-7]+[0-7_]*;
fragment HEX: ('0x'|'0X')[1-9A-F]+[0-9A-F_]*;
fragment BIN: ('0b'|'0B')'1'+[01_]*;
fragment DEC: '0'|([1-9]+[0-9_]*);
INTLIT: (OCT|HEX|BIN|DEC) {self.text = self.text.replace("_", "")};

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
// Boolean
BOOLEANLIT: ('False'| 'True');
// String
fragment EscapeSequence: ('\b'|'\f'|'\r'|'\n'|'\t'|'\''|'\\'| '\'"');
STRINGLIT: '"'(EscapeSequence |~('"'))*'"';
ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
ID: [a-zA-Z_]+[a-zA-Z0-9_]*;