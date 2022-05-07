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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\6\69\n\6\r\6\16\6:\3\7\6\7>\n\7\r\7\16\7")
        buf.write("?\3\b\6\bC\n\b\r\b\16\bD\3\b\3\b\6\bI\n\b\r\b\16\bJ\3")
        buf.write("\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\6\16X\n")
        buf.write("\16\r\16\16\16Y\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21")
        buf.write("\2\2\22\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\20\37\21!\22\3\2\5\4\2C\\c|\3\2\62")
        buf.write(";\5\2\13\f\17\17\"\"\2g\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\3#\3\2\2\2\5(\3\2\2\2\7,\3\2\2\2\t\61\3\2\2")
        buf.write("\2\138\3\2\2\2\r=\3\2\2\2\17B\3\2\2\2\21L\3\2\2\2\23N")
        buf.write("\3\2\2\2\25P\3\2\2\2\27R\3\2\2\2\31T\3\2\2\2\33W\3\2\2")
        buf.write("\2\35]\3\2\2\2\37_\3\2\2\2!a\3\2\2\2#$\7o\2\2$%\7c\2\2")
        buf.write("%&\7k\2\2&\'\7p\2\2\'\4\3\2\2\2()\7k\2\2)*\7p\2\2*+\7")
        buf.write("v\2\2+\6\3\2\2\2,-\7x\2\2-.\7q\2\2./\7k\2\2/\60\7f\2\2")
        buf.write("\60\b\3\2\2\2\61\62\7h\2\2\62\63\7n\2\2\63\64\7q\2\2\64")
        buf.write("\65\7c\2\2\65\66\7v\2\2\66\n\3\2\2\2\679\t\2\2\28\67\3")
        buf.write("\2\2\29:\3\2\2\2:8\3\2\2\2:;\3\2\2\2;\f\3\2\2\2<>\t\3")
        buf.write("\2\2=<\3\2\2\2>?\3\2\2\2?=\3\2\2\2?@\3\2\2\2@\16\3\2\2")
        buf.write("\2AC\t\3\2\2BA\3\2\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2\2E")
        buf.write("F\3\2\2\2FH\7\60\2\2GI\t\3\2\2HG\3\2\2\2IJ\3\2\2\2JH\3")
        buf.write("\2\2\2JK\3\2\2\2K\20\3\2\2\2LM\7*\2\2M\22\3\2\2\2NO\7")
        buf.write("+\2\2O\24\3\2\2\2PQ\7}\2\2Q\26\3\2\2\2RS\7\177\2\2S\30")
        buf.write("\3\2\2\2TU\7=\2\2U\32\3\2\2\2VX\t\4\2\2WV\3\2\2\2XY\3")
        buf.write("\2\2\2YW\3\2\2\2YZ\3\2\2\2Z[\3\2\2\2[\\\b\16\2\2\\\34")
        buf.write("\3\2\2\2]^\13\2\2\2^\36\3\2\2\2_`\13\2\2\2` \3\2\2\2a")
        buf.write("b\13\2\2\2b\"\3\2\2\2\b\2:?DJY\3\b\2\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    VOIDTYPE = 3
    FLOATTYPE = 4
    ID = 5
    INTLIT = 6
    FLOATLIT = 7
    LB = 8
    RB = 9
    LP = 10
    RP = 11
    SEMI = 12
    WS = 13
    ERROR_CHAR = 14
    UNCLOSE_STRING = 15
    ILLEGAL_ESCAPE = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'float'", "'('", "')'", "'{'", 
            "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "FLOATTYPE", "ID", "INTLIT", "FLOATLIT", 
            "LB", "RB", "LP", "RP", "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "FLOATTYPE", "ID", "INTLIT", 
                  "FLOATLIT", "LB", "RB", "LP", "RP", "SEMI", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


