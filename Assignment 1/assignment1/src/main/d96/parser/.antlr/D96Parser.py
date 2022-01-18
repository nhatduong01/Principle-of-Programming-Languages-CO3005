# Generated from c:\Users\ADMIN\Desktop\Learning\Principle of Programming Languages\Code\Code\Assignment 1\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3>")
        buf.write("(\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\5\2\23\n\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\5\3\5\5\5\37\n\5\3\6\3\6\3\6\5\6$\n\6\3\6\3\6\3\6")
        buf.write("\2\2\7\2\4\6\b\n\2\3\4\2//\64\64\2%\2\f\3\2\2\2\4\27\3")
        buf.write("\2\2\2\6\31\3\2\2\2\b\36\3\2\2\2\n \3\2\2\2\f\r\5\4\3")
        buf.write("\2\r\16\7\3\2\2\16\17\7\4\2\2\17\20\7\5\2\2\20\22\7\6")
        buf.write("\2\2\21\23\5\6\4\2\22\21\3\2\2\2\22\23\3\2\2\2\23\24\3")
        buf.write("\2\2\2\24\25\7\7\2\2\25\26\7\2\2\3\26\3\3\2\2\2\27\30")
        buf.write("\t\2\2\2\30\5\3\2\2\2\31\32\5\n\6\2\32\33\7\b\2\2\33\7")
        buf.write("\3\2\2\2\34\37\5\n\6\2\35\37\7\66\2\2\36\34\3\2\2\2\36")
        buf.write("\35\3\2\2\2\37\t\3\2\2\2 !\7:\2\2!#\7\4\2\2\"$\5\b\5\2")
        buf.write("#\"\3\2\2\2#$\3\2\2\2$%\3\2\2\2%&\7\5\2\2&\13\3\2\2\2")
        buf.write("\5\22\36#")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'('", "')'", "'{'", "'}'", 
                     "';'", "','", "':'", "'Break'", "'Continue'", "'If'", 
                     "'Elseif'", "'Else'", "'Foreach'", "'In'", "'Return'", 
                     "'Null'", "'Class'", "'Val'", "'Var'", "'Constructor'", 
                     "'Destructor'", "'New'", "'By'", "'$'", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'='", "'!='", "'>'", "'<='", "'<'", "'>='", 
                     "'==.'", "'+.'", "'::'", "'Int'", "'Float'", "'String'", 
                     "'Boolean'", "'Array'", "'void'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "LB", "RB", "LP", "RP", 
                      "SEMI", "COMMA", "COLON", "BREAK", "CONTINUE", "IF", 
                      "ELSEIF", "ELSE", "FOREACH", "IN", "RETURN", "NULL", 
                      "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
                      "NEW", "BY", "DOLLAR", "BlockComment", "PLUS", "MINUS", 
                      "MULTIPLY", "DIVIDE", "MODULO", "NEGATE", "AND", "OR", 
                      "EQUAL", "ASSIGN", "DIFFERENT", "GREATER", "LESSTHANEQUAL", 
                      "LESSER", "GREATERTHANEQUAL", "STRINGCOMPARE", "STRINCONCAT", 
                      "STATIC_ACCESS", "INTTYPE", "FLOATTYPE", "STRINGTYPE", 
                      "BOOLEANTYPE", "ARRAYTYPE", "VOIDTYPE", "FLOATLIT", 
                      "INTLIT", "WS", "BOOLEANLIT", "STRINGLIT", "ID", "DOT", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_mptype = 1
    RULE_body = 2
    RULE_exp = 3
    RULE_funcall = 4

    ruleNames =  [ "program", "mptype", "body", "exp", "funcall" ]

    EOF = Token.EOF
    T__0=1
    LB=2
    RB=3
    LP=4
    RP=5
    SEMI=6
    COMMA=7
    COLON=8
    BREAK=9
    CONTINUE=10
    IF=11
    ELSEIF=12
    ELSE=13
    FOREACH=14
    IN=15
    RETURN=16
    NULL=17
    CLASS=18
    VAL=19
    VAR=20
    CONSTRUCTOR=21
    DESTRUCTOR=22
    NEW=23
    BY=24
    DOLLAR=25
    BlockComment=26
    PLUS=27
    MINUS=28
    MULTIPLY=29
    DIVIDE=30
    MODULO=31
    NEGATE=32
    AND=33
    OR=34
    EQUAL=35
    ASSIGN=36
    DIFFERENT=37
    GREATER=38
    LESSTHANEQUAL=39
    LESSER=40
    GREATERTHANEQUAL=41
    STRINGCOMPARE=42
    STRINCONCAT=43
    STATIC_ACCESS=44
    INTTYPE=45
    FLOATTYPE=46
    STRINGTYPE=47
    BOOLEANTYPE=48
    ARRAYTYPE=49
    VOIDTYPE=50
    FLOATLIT=51
    INTLIT=52
    WS=53
    BOOLEANLIT=54
    STRINGLIT=55
    ID=56
    DOT=57
    ERROR_CHAR=58
    UNCLOSE_STRING=59
    ILLEGAL_ESCAPE=60

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def body(self):
            return self.getTypedRuleContext(D96Parser.BodyContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.mptype()
            self.state = 11
            self.match(D96Parser.T__0)
            self.state = 12
            self.match(D96Parser.LB)
            self.state = 13
            self.match(D96Parser.RB)
            self.state = 14
            self.match(D96Parser.LP)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 15
                self.body()


            self.state = 18
            self.match(D96Parser.RP)
            self.state = 19
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MptypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(D96Parser.INTTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(D96Parser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_mptype




    def mptype(self):

        localctx = D96Parser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mptype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            _la = self._input.LA(1)
            if not(_la==D96Parser.INTTYPE or _la==D96Parser.VOIDTYPE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_body




    def body(self):

        localctx = D96Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.funcall()
            self.state = 24
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exp)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.funcall()
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(D96Parser.INTLIT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_funcall




    def funcall(self):

        localctx = D96Parser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(D96Parser.ID)
            self.state = 31
            self.match(D96Parser.LB)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.INTLIT or _la==D96Parser.ID:
                self.state = 32
                self.exp()


            self.state = 35
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





