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

exp: exp| funcall | INTLIT;

funcall: ID LB exp? RB;

assignment: ID ASSIGN exp;

condition: NEGATE exp
         | exp AND exp
         | exp OR exp;




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
UNTERMINATED_COMMENT:  '##' ('#' ~'/' | ~'#')*? EOF;

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

// Primitive type


INTTYPE: 'Int';
FLOATTYPE: 'Float';
STRINGTYPE: 'String';
BOOLEANTYPE: 'Boolean';
ARRAYTYPE: 'Array';
VOIDTYPE: 'void';

// Literal
//float
fragment DECIMALPART: '.'[0-9]+[0-9_]*;
fragment EXPONENTPART: [eE][+-]?[1-9]+[0-9_]*
                     | [Ee][+-]?[0];
//FLOATLIT: ('0'|([1-9]+[0-9_]*))?(DECIMALPART |EXPONENTPART | (DECIMALPART EXPONENTPART)) {self.text = self.text.replace("_","")};
FLOATLIT: DEC DECIMALPART EXPONENTPART{self.text = self.text.replace("_","")}
        | DEC EXPONENTPART {self.text = self.text.replace("_","")}
        | DECIMALPART EXPONENTPART {self.text = self.text.replace("_","")}
        | DEC DECIMALPART {self.text = self.text.replace("_","")};
// Int
// hai gach lien tiep
fragment OCT: '0'[1-7]+[0-7_]*;
fragment HEX: ('0x'|'0X')[1-9A-F]+[0-9A-F_]*;
fragment BIN: ('0b'|'0B')'1'+[01_]*;
fragment DEC: '0'|([1-9]+[0-9_]*);
INTLIT: (OCT|HEX|BIN|DEC) {self.text = self.text.replace("_", "")};
//INTLIT: [1-9_]+ {self.text = self.text.replace("_", "")};
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
// Boolean
BOOLEANLIT: ('False'| 'True');
// String
ILLEGAL_ESCAPE: '"' ('\\' ~[btnfr"'\\] | ~'\\')*{raise IllegalEscape(self.text)};
fragment EscapeSequence: ('\\b'|'\\f'|'\\r'|'\\n'|'\\t'|'\\\''|'\\\\'| '\'"');
STRINGLIT: '"'(EscapeSequence |~["])*'"';
UNCLOSE_STRING: '"'(EscapeSequence |~["])* EOF {raise UncloseString(self.text[1:])};
ID: [a-zA-Z_]+[a-zA-Z0-9_]*;
DOT: '.';
ERROR_CHAR: . {raise ErrorToken(self.text)};
//{raise UncloseString(self.text[1:])}