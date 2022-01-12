grammar BKIT;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : EOF ;
// UNDERSCORE : '_' -> skip ; 
PHPNUM: [0]
	  | [1-9]+([0-9]| '_')*;



ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;