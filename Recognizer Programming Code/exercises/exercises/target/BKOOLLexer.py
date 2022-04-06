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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\30")
        buf.write("v\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\6\13Q\n\13\r\13\16\13R\3\f\6\fV\n\f\r\f\16")
        buf.write("\fW\3\r\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21")
        buf.write("\3\21\3\22\3\22\3\23\3\23\3\24\6\24k\n\24\r\24\16\24l")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\2\2\30\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30\3\2\5\4\2")
        buf.write("C\\c|\3\2\62;\5\2\13\f\17\17\"\"\2x\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\3/\3\2\2\2\5\61\3")
        buf.write("\2\2\2\78\3\2\2\2\t:\3\2\2\2\13<\3\2\2\2\r>\3\2\2\2\17")
        buf.write("@\3\2\2\2\21D\3\2\2\2\23J\3\2\2\2\25P\3\2\2\2\27U\3\2")
        buf.write("\2\2\31Y\3\2\2\2\33]\3\2\2\2\35_\3\2\2\2\37a\3\2\2\2!")
        buf.write("c\3\2\2\2#e\3\2\2\2%g\3\2\2\2\'j\3\2\2\2)p\3\2\2\2+r\3")
        buf.write("\2\2\2-t\3\2\2\2/\60\7?\2\2\60\4\3\2\2\2\61\62\7t\2\2")
        buf.write("\62\63\7g\2\2\63\64\7v\2\2\64\65\7w\2\2\65\66\7t\2\2\66")
        buf.write("\67\7p\2\2\67\6\3\2\2\289\7-\2\29\b\3\2\2\2:;\7/\2\2;")
        buf.write("\n\3\2\2\2<=\7\61\2\2=\f\3\2\2\2>?\7,\2\2?\16\3\2\2\2")
        buf.write("@A\7k\2\2AB\7p\2\2BC\7v\2\2C\20\3\2\2\2DE\7h\2\2EF\7n")
        buf.write("\2\2FG\7q\2\2GH\7c\2\2HI\7v\2\2I\22\3\2\2\2JK\7x\2\2K")
        buf.write("L\7q\2\2LM\7k\2\2MN\7f\2\2N\24\3\2\2\2OQ\t\2\2\2PO\3\2")
        buf.write("\2\2QR\3\2\2\2RP\3\2\2\2RS\3\2\2\2S\26\3\2\2\2TV\t\3\2")
        buf.write("\2UT\3\2\2\2VW\3\2\2\2WU\3\2\2\2WX\3\2\2\2X\30\3\2\2\2")
        buf.write("YZ\5\27\f\2Z[\7\60\2\2[\\\5\27\f\2\\\32\3\2\2\2]^\7*\2")
        buf.write("\2^\34\3\2\2\2_`\7+\2\2`\36\3\2\2\2ab\7}\2\2b \3\2\2\2")
        buf.write("cd\7\177\2\2d\"\3\2\2\2ef\7=\2\2f$\3\2\2\2gh\7.\2\2h&")
        buf.write("\3\2\2\2ik\t\4\2\2ji\3\2\2\2kl\3\2\2\2lj\3\2\2\2lm\3\2")
        buf.write("\2\2mn\3\2\2\2no\b\24\2\2o(\3\2\2\2pq\13\2\2\2q*\3\2\2")
        buf.write("\2rs\13\2\2\2s,\3\2\2\2tu\13\2\2\2u.\3\2\2\2\6\2RWl\3")
        buf.write("\b\2\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    INTTYPE = 7
    FLOATTYPE = 8
    VOIDTYPE = 9
    ID = 10
    INTLIT = 11
    FLOATLIT = 12
    LB = 13
    RB = 14
    LP = 15
    RP = 16
    SEMI = 17
    COMMA = 18
    WS = 19
    ERROR_CHAR = 20
    UNCLOSE_STRING = 21
    ILLEGAL_ESCAPE = 22

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'return'", "'+'", "'-'", "'/'", "'*'", "'int'", "'float'", 
            "'void'", "'('", "')'", "'{'", "'}'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "FLOATTYPE", "VOIDTYPE", "ID", "INTLIT", "FLOATLIT", 
            "LB", "RB", "LP", "RP", "SEMI", "COMMA", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "INTTYPE", 
                  "FLOATTYPE", "VOIDTYPE", "ID", "INTLIT", "FLOATLIT", "LB", 
                  "RB", "LP", "RP", "SEMI", "COMMA", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


