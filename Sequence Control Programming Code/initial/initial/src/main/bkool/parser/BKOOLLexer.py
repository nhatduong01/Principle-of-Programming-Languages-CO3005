# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26")
        buf.write("s\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\n\6\nI\n\n\r\n\16\nJ\3\13\6")
        buf.write("\13N\n\13\r\13\16\13O\3\f\6\fS\n\f\r\f\16\fT\3\f\3\f\6")
        buf.write("\fY\n\f\r\f\16\fZ\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20")
        buf.write("\3\21\3\21\3\22\6\22h\n\22\r\22\16\22i\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\2\2\26\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26\3\2\5\4\2C\\c|\3\2\62;\5\2\13\f")
        buf.write("\17\17\"\"\2w\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\3+\3\2\2")
        buf.write("\2\5\60\3\2\2\2\7\62\3\2\2\2\t\64\3\2\2\2\13\66\3\2\2")
        buf.write("\2\r8\3\2\2\2\17<\3\2\2\2\21A\3\2\2\2\23H\3\2\2\2\25M")
        buf.write("\3\2\2\2\27R\3\2\2\2\31\\\3\2\2\2\33^\3\2\2\2\35`\3\2")
        buf.write("\2\2\37b\3\2\2\2!d\3\2\2\2#g\3\2\2\2%m\3\2\2\2\'o\3\2")
        buf.write("\2\2)q\3\2\2\2+,\7o\2\2,-\7c\2\2-.\7k\2\2./\7p\2\2/\4")
        buf.write("\3\2\2\2\60\61\7-\2\2\61\6\3\2\2\2\62\63\7/\2\2\63\b\3")
        buf.write("\2\2\2\64\65\7,\2\2\65\n\3\2\2\2\66\67\7\61\2\2\67\f\3")
        buf.write("\2\2\289\7k\2\29:\7p\2\2:;\7v\2\2;\16\3\2\2\2<=\7x\2\2")
        buf.write("=>\7q\2\2>?\7k\2\2?@\7f\2\2@\20\3\2\2\2AB\7h\2\2BC\7n")
        buf.write("\2\2CD\7q\2\2DE\7c\2\2EF\7v\2\2F\22\3\2\2\2GI\t\2\2\2")
        buf.write("HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2\2\2K\24\3\2\2\2L")
        buf.write("N\t\3\2\2ML\3\2\2\2NO\3\2\2\2OM\3\2\2\2OP\3\2\2\2P\26")
        buf.write("\3\2\2\2QS\t\3\2\2RQ\3\2\2\2ST\3\2\2\2TR\3\2\2\2TU\3\2")
        buf.write("\2\2UV\3\2\2\2VX\7\60\2\2WY\t\3\2\2XW\3\2\2\2YZ\3\2\2")
        buf.write("\2ZX\3\2\2\2Z[\3\2\2\2[\30\3\2\2\2\\]\7*\2\2]\32\3\2\2")
        buf.write("\2^_\7+\2\2_\34\3\2\2\2`a\7}\2\2a\36\3\2\2\2bc\7\177\2")
        buf.write("\2c \3\2\2\2de\7=\2\2e\"\3\2\2\2fh\t\4\2\2gf\3\2\2\2h")
        buf.write("i\3\2\2\2ig\3\2\2\2ij\3\2\2\2jk\3\2\2\2kl\b\22\2\2l$\3")
        buf.write("\2\2\2mn\13\2\2\2n&\3\2\2\2op\13\2\2\2p(\3\2\2\2qr\13")
        buf.write("\2\2\2r*\3\2\2\2\b\2JOTZi\3\b\2\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    INTTYPE = 6
    VOIDTYPE = 7
    FLOATTYPE = 8
    ID = 9
    INTLIT = 10
    FLOATLIT = 11
    LB = 12
    RB = 13
    LP = 14
    RP = 15
    SEMI = 16
    WS = 17
    ERROR_CHAR = 18
    UNCLOSE_STRING = 19
    ILLEGAL_ESCAPE = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'+'", "'-'", "'*'", "'/'", "'int'", "'void'", "'float'", 
            "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "FLOATTYPE", "ID", "INTLIT", "FLOATLIT", 
            "LB", "RB", "LP", "RP", "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "INTTYPE", "VOIDTYPE", 
                  "FLOATTYPE", "ID", "INTLIT", "FLOATLIT", "LB", "RB", "LP", 
                  "RP", "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


