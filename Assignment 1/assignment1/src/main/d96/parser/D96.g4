grammar D96;
// 1952638
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

// assignment: ID ASSIGN exp;

// condition: NEGATE exp
//          | exp AND exp
//          | exp OR exp;




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
DOLLAR: '$';
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
STRINCONCAT: '+.';
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
ID: [a-zA-Z_]+[a-zA-Z0-9_]*;
ERROR_CHAR: . {raise ErrorToken(self.text)};
//{raise UncloseString(self.text[1:])}