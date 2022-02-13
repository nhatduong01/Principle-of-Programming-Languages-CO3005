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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u0232\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\3\2\6\2x\n\2\r\2\16\2y\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3\u0083\n\3\3\4\3\4\3\4\3\4\3\4\5\4\u008a\n\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\7\5\u0093\n\5\f\5\16\5\u0096\13\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u009f\n\6\f\6\16\6\u00a2")
        buf.write("\13\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u00ab\n\7\f\7\16")
        buf.write("\7\u00ae\13\7\3\b\3\b\3\b\5\b\u00b3\n\b\3\t\3\t\3\t\5")
        buf.write("\t\u00b8\n\t\3\n\3\n\3\n\3\n\3\n\7\n\u00bf\n\n\f\n\16")
        buf.write("\n\u00c2\13\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\5\13\u00cf\n\13\3\13\3\13\7\13\u00d3\n")
        buf.write("\13\f\13\16\13\u00d6\13\13\3\f\3\f\3\f\3\f\3\f\5\f\u00dd")
        buf.write("\n\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00e6\n\f\3\r\3\r")
        buf.write("\3\r\3\r\5\r\u00ec\n\r\3\r\3\r\3\r\5\r\u00f1\n\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\5\16\u0100\n\16\3\17\3\17\3\20\3\20\3\21\3\21\3")
        buf.write("\22\3\22\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\5\25\u0118\n\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0125")
        buf.write("\n\27\3\27\5\27\u0128\n\27\3\30\3\30\3\30\3\31\3\31\3")
        buf.write("\31\3\31\5\31\u0131\n\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\7\35\u0147\n\35\f\35\16\35\u014a\13\35")
        buf.write("\3\36\3\36\3\36\5\36\u014f\n\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\5\36\u0156\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\5\37\u0161\n\37\3\37\3\37\3\37\3 \3 \3 \3!")
        buf.write("\3!\3!\3\"\3\"\5\"\u016e\n\"\3\"\3\"\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u0180\n#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\5#\u018a\n#\3#\3#\5#\u018e\n#\3$\3$\3$\3$\3%\3")
        buf.write("%\3%\3%\5%\u0198\n%\3&\3&\3&\3&\5&\u019e\n&\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\5\'\u01a6\n\'\3\'\3\'\3(\3(\3(\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\5)\u01b7\n)\3*\3*\3*\3*\5*\u01bd")
        buf.write("\n*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\5+\u01ca\n+\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\5,\u01d3\n,\3-\3-\3-\3-\3-\3-\3-\3.\3")
        buf.write(".\3.\3.\3.\3.\5.\u01e2\n.\3.\3.\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\60\5\60\u01ed\n\60\3\61\3\61\3\61\3\62\3\62\3\62\3")
        buf.write("\62\3\62\5\62\u01f7\n\62\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\5\63\u01ff\n\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3")
        buf.write("\64\5\64\u0209\n\64\3\65\3\65\3\65\3\65\5\65\u020f\n\65")
        buf.write("\3\66\3\66\3\66\3\66\3\66\5\66\u0216\n\66\3\67\3\67\3")
        buf.write("\67\3\67\38\38\38\58\u021f\n8\39\39\39\39\59\u0225\n9")
        buf.write("\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\2\b\b\n\f\22\248")
        buf.write("<\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprt\2\t\3\2./\4\2\'")
        buf.write("\')-\3\2%&\3\2\37 \3\2!#\3\2\27\30\3\2?@\2\u0241\2w\3")
        buf.write("\2\2\2\4\u0082\3\2\2\2\6\u0089\3\2\2\2\b\u008b\3\2\2\2")
        buf.write("\n\u0097\3\2\2\2\f\u00a3\3\2\2\2\16\u00b2\3\2\2\2\20\u00b7")
        buf.write("\3\2\2\2\22\u00b9\3\2\2\2\24\u00c3\3\2\2\2\26\u00e5\3")
        buf.write("\2\2\2\30\u00f0\3\2\2\2\32\u00ff\3\2\2\2\34\u0101\3\2")
        buf.write("\2\2\36\u0103\3\2\2\2 \u0105\3\2\2\2\"\u0107\3\2\2\2$")
        buf.write("\u0109\3\2\2\2&\u010b\3\2\2\2(\u0117\3\2\2\2*\u0119\3")
        buf.write("\2\2\2,\u011e\3\2\2\2.\u0129\3\2\2\2\60\u0130\3\2\2\2")
        buf.write("\62\u0132\3\2\2\2\64\u0138\3\2\2\2\66\u013b\3\2\2\28\u0140")
        buf.write("\3\2\2\2:\u0155\3\2\2\2<\u0157\3\2\2\2>\u0165\3\2\2\2")
        buf.write("@\u0168\3\2\2\2B\u016b\3\2\2\2D\u018d\3\2\2\2F\u018f\3")
        buf.write("\2\2\2H\u0197\3\2\2\2J\u019d\3\2\2\2L\u019f\3\2\2\2N\u01a9")
        buf.write("\3\2\2\2P\u01b6\3\2\2\2R\u01b8\3\2\2\2T\u01c9\3\2\2\2")
        buf.write("V\u01d2\3\2\2\2X\u01d4\3\2\2\2Z\u01db\3\2\2\2\\\u01e5")
        buf.write("\3\2\2\2^\u01ec\3\2\2\2`\u01ee\3\2\2\2b\u01f6\3\2\2\2")
        buf.write("d\u01fe\3\2\2\2f\u0208\3\2\2\2h\u020e\3\2\2\2j\u0215\3")
        buf.write("\2\2\2l\u0217\3\2\2\2n\u021e\3\2\2\2p\u0224\3\2\2\2r\u0226")
        buf.write("\3\2\2\2t\u022c\3\2\2\2vx\5R*\2wv\3\2\2\2xy\3\2\2\2yw")
        buf.write("\3\2\2\2yz\3\2\2\2z{\3\2\2\2{|\7\2\2\3|\3\3\2\2\2}~\5")
        buf.write("\6\4\2~\177\5\34\17\2\177\u0080\5\6\4\2\u0080\u0083\3")
        buf.write("\2\2\2\u0081\u0083\5\6\4\2\u0082}\3\2\2\2\u0082\u0081")
        buf.write("\3\2\2\2\u0083\5\3\2\2\2\u0084\u0085\5\b\5\2\u0085\u0086")
        buf.write("\5\36\20\2\u0086\u0087\5\b\5\2\u0087\u008a\3\2\2\2\u0088")
        buf.write("\u008a\5\b\5\2\u0089\u0084\3\2\2\2\u0089\u0088\3\2\2\2")
        buf.write("\u008a\7\3\2\2\2\u008b\u008c\b\5\1\2\u008c\u008d\5\n\6")
        buf.write("\2\u008d\u0094\3\2\2\2\u008e\u008f\f\4\2\2\u008f\u0090")
        buf.write("\5 \21\2\u0090\u0091\5\n\6\2\u0091\u0093\3\2\2\2\u0092")
        buf.write("\u008e\3\2\2\2\u0093\u0096\3\2\2\2\u0094\u0092\3\2\2\2")
        buf.write("\u0094\u0095\3\2\2\2\u0095\t\3\2\2\2\u0096\u0094\3\2\2")
        buf.write("\2\u0097\u0098\b\6\1\2\u0098\u0099\5\f\7\2\u0099\u00a0")
        buf.write("\3\2\2\2\u009a\u009b\f\4\2\2\u009b\u009c\5\"\22\2\u009c")
        buf.write("\u009d\5\f\7\2\u009d\u009f\3\2\2\2\u009e\u009a\3\2\2\2")
        buf.write("\u009f\u00a2\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u00a1\3")
        buf.write("\2\2\2\u00a1\13\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3\u00a4")
        buf.write("\b\7\1\2\u00a4\u00a5\5\16\b\2\u00a5\u00ac\3\2\2\2\u00a6")
        buf.write("\u00a7\f\4\2\2\u00a7\u00a8\5$\23\2\u00a8\u00a9\5\16\b")
        buf.write("\2\u00a9\u00ab\3\2\2\2\u00aa\u00a6\3\2\2\2\u00ab\u00ae")
        buf.write("\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad")
        buf.write("\r\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b0\7$\2\2\u00b0")
        buf.write("\u00b3\5\16\b\2\u00b1\u00b3\5\20\t\2\u00b2\u00af\3\2\2")
        buf.write("\2\u00b2\u00b1\3\2\2\2\u00b3\17\3\2\2\2\u00b4\u00b5\7")
        buf.write(" \2\2\u00b5\u00b8\5\20\t\2\u00b6\u00b8\5\22\n\2\u00b7")
        buf.write("\u00b4\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\21\3\2\2\2\u00b9")
        buf.write("\u00ba\b\n\1\2\u00ba\u00bb\5\24\13\2\u00bb\u00c0\3\2\2")
        buf.write("\2\u00bc\u00bd\f\4\2\2\u00bd\u00bf\5(\25\2\u00be\u00bc")
        buf.write("\3\2\2\2\u00bf\u00c2\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0")
        buf.write("\u00c1\3\2\2\2\u00c1\23\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3")
        buf.write("\u00c4\b\13\1\2\u00c4\u00c5\5\26\f\2\u00c5\u00d4\3\2\2")
        buf.write("\2\u00c6\u00c7\f\5\2\2\u00c7\u00c8\7\61\2\2\u00c8\u00d3")
        buf.write("\5\26\f\2\u00c9\u00ca\f\4\2\2\u00ca\u00cb\7\61\2\2\u00cb")
        buf.write("\u00cc\5\26\f\2\u00cc\u00ce\7\6\2\2\u00cd\u00cf\5`\61")
        buf.write("\2\u00ce\u00cd\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0")
        buf.write("\3\2\2\2\u00d0\u00d1\7\7\2\2\u00d1\u00d3\3\2\2\2\u00d2")
        buf.write("\u00c6\3\2\2\2\u00d2\u00c9\3\2\2\2\u00d3\u00d6\3\2\2\2")
        buf.write("\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\25\3\2")
        buf.write("\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00d8\5\30\r\2\u00d8\u00d9")
        buf.write("\7\60\2\2\u00d9\u00da\5\30\r\2\u00da\u00dc\7\6\2\2\u00db")
        buf.write("\u00dd\5`\61\2\u00dc\u00db\3\2\2\2\u00dc\u00dd\3\2\2\2")
        buf.write("\u00dd\u00de\3\2\2\2\u00de\u00df\7\7\2\2\u00df\u00e6\3")
        buf.write("\2\2\2\u00e0\u00e1\5\30\r\2\u00e1\u00e2\7\60\2\2\u00e2")
        buf.write("\u00e3\5\30\r\2\u00e3\u00e6\3\2\2\2\u00e4\u00e6\5\30\r")
        buf.write("\2\u00e5\u00d7\3\2\2\2\u00e5\u00e0\3\2\2\2\u00e5\u00e4")
        buf.write("\3\2\2\2\u00e6\27\3\2\2\2\u00e7\u00e8\7\33\2\2\u00e8\u00e9")
        buf.write("\5\30\r\2\u00e9\u00eb\7\6\2\2\u00ea\u00ec\5`\61\2\u00eb")
        buf.write("\u00ea\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ed\3\2\2\2")
        buf.write("\u00ed\u00ee\7\7\2\2\u00ee\u00f1\3\2\2\2\u00ef\u00f1\5")
        buf.write("\32\16\2\u00f0\u00e7\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1")
        buf.write("\31\3\2\2\2\u00f2\u00f3\7\6\2\2\u00f3\u00f4\5\4\3\2\u00f4")
        buf.write("\u00f5\7\7\2\2\u00f5\u0100\3\2\2\2\u00f6\u0100\79\2\2")
        buf.write("\u00f7\u0100\7=\2\2\u00f8\u0100\7;\2\2\u00f9\u0100\78")
        buf.write("\2\2\u00fa\u0100\7@\2\2\u00fb\u0100\5*\26\2\u00fc\u0100")
        buf.write("\7?\2\2\u00fd\u0100\7\35\2\2\u00fe\u0100\7\25\2\2\u00ff")
        buf.write("\u00f2\3\2\2\2\u00ff\u00f6\3\2\2\2\u00ff\u00f7\3\2\2\2")
        buf.write("\u00ff\u00f8\3\2\2\2\u00ff\u00f9\3\2\2\2\u00ff\u00fa\3")
        buf.write("\2\2\2\u00ff\u00fb\3\2\2\2\u00ff\u00fc\3\2\2\2\u00ff\u00fd")
        buf.write("\3\2\2\2\u00ff\u00fe\3\2\2\2\u0100\33\3\2\2\2\u0101\u0102")
        buf.write("\t\2\2\2\u0102\35\3\2\2\2\u0103\u0104\t\3\2\2\u0104\37")
        buf.write("\3\2\2\2\u0105\u0106\t\4\2\2\u0106!\3\2\2\2\u0107\u0108")
        buf.write("\t\5\2\2\u0108#\3\2\2\2\u0109\u010a\t\6\2\2\u010a%\3\2")
        buf.write("\2\2\u010b\u010c\5\4\3\2\u010c\u010d\5(\25\2\u010d\'\3")
        buf.write("\2\2\2\u010e\u010f\7\3\2\2\u010f\u0110\5\4\3\2\u0110\u0111")
        buf.write("\7\4\2\2\u0111\u0118\3\2\2\2\u0112\u0113\7\3\2\2\u0113")
        buf.write("\u0114\5\4\3\2\u0114\u0115\7\4\2\2\u0115\u0116\5(\25\2")
        buf.write("\u0116\u0118\3\2\2\2\u0117\u010e\3\2\2\2\u0117\u0112\3")
        buf.write("\2\2\2\u0118)\3\2\2\2\u0119\u011a\7\66\2\2\u011a\u011b")
        buf.write("\7\6\2\2\u011b\u011c\5`\61\2\u011c\u011d\7\7\2\2\u011d")
        buf.write("+\3\2\2\2\u011e\u011f\7\17\2\2\u011f\u0120\7\6\2\2\u0120")
        buf.write("\u0121\5\4\3\2\u0121\u0122\7\7\2\2\u0122\u0124\5F$\2\u0123")
        buf.write("\u0125\5.\30\2\u0124\u0123\3\2\2\2\u0124\u0125\3\2\2\2")
        buf.write("\u0125\u0127\3\2\2\2\u0126\u0128\5\64\33\2\u0127\u0126")
        buf.write("\3\2\2\2\u0127\u0128\3\2\2\2\u0128-\3\2\2\2\u0129\u012a")
        buf.write("\5\62\32\2\u012a\u012b\5\60\31\2\u012b/\3\2\2\2\u012c")
        buf.write("\u012d\5\62\32\2\u012d\u012e\5\60\31\2\u012e\u0131\3\2")
        buf.write("\2\2\u012f\u0131\3\2\2\2\u0130\u012c\3\2\2\2\u0130\u012f")
        buf.write("\3\2\2\2\u0131\61\3\2\2\2\u0132\u0133\7\20\2\2\u0133\u0134")
        buf.write("\7\6\2\2\u0134\u0135\5\4\3\2\u0135\u0136\7\7\2\2\u0136")
        buf.write("\u0137\5F$\2\u0137\63\3\2\2\2\u0138\u0139\7\21\2\2\u0139")
        buf.write("\u013a\5F$\2\u013a\65\3\2\2\2\u013b\u013c\58\35\2\u013c")
        buf.write("\u013d\7(\2\2\u013d\u013e\5\4\3\2\u013e\u013f\7\n\2\2")
        buf.write("\u013f\67\3\2\2\2\u0140\u0141\b\35\1\2\u0141\u0142\5:")
        buf.write("\36\2\u0142\u0148\3\2\2\2\u0143\u0144\f\4\2\2\u0144\u0145")
        buf.write("\7\61\2\2\u0145\u0147\5:\36\2\u0146\u0143\3\2\2\2\u0147")
        buf.write("\u014a\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3\2\2\2")
        buf.write("\u01499\3\2\2\2\u014a\u0148\3\2\2\2\u014b\u014f\7@\2\2")
        buf.write("\u014c\u014f\5&\24\2\u014d\u014f\7\35\2\2\u014e\u014b")
        buf.write("\3\2\2\2\u014e\u014c\3\2\2\2\u014e\u014d\3\2\2\2\u014f")
        buf.write("\u0150\3\2\2\2\u0150\u0151\7\60\2\2\u0151\u0156\7?\2\2")
        buf.write("\u0152\u0156\7@\2\2\u0153\u0156\5&\24\2\u0154\u0156\7")
        buf.write("\35\2\2\u0155\u014e\3\2\2\2\u0155\u0152\3\2\2\2\u0155")
        buf.write("\u0153\3\2\2\2\u0155\u0154\3\2\2\2\u0156;\3\2\2\2\u0157")
        buf.write("\u0158\7\22\2\2\u0158\u0159\7\6\2\2\u0159\u015a\58\35")
        buf.write("\2\u015a\u015b\7\23\2\2\u015b\u015c\5\4\3\2\u015c\u015d")
        buf.write("\7\5\2\2\u015d\u0160\5\4\3\2\u015e\u015f\7\34\2\2\u015f")
        buf.write("\u0161\5\4\3\2\u0160\u015e\3\2\2\2\u0160\u0161\3\2\2\2")
        buf.write("\u0161\u0162\3\2\2\2\u0162\u0163\7\7\2\2\u0163\u0164\5")
        buf.write("F$\2\u0164=\3\2\2\2\u0165\u0166\7\r\2\2\u0166\u0167\7")
        buf.write("\n\2\2\u0167?\3\2\2\2\u0168\u0169\7\16\2\2\u0169\u016a")
        buf.write("\7\n\2\2\u016aA\3\2\2\2\u016b\u016d\7\24\2\2\u016c\u016e")
        buf.write("\5\4\3\2\u016d\u016c\3\2\2\2\u016d\u016e\3\2\2\2\u016e")
        buf.write("\u016f\3\2\2\2\u016f\u0170\7\n\2\2\u0170C\3\2\2\2\u0171")
        buf.write("\u0172\5\4\3\2\u0172\u0173\7\61\2\2\u0173\u0174\7@\2\2")
        buf.write("\u0174\u0175\7\n\2\2\u0175\u018e\3\2\2\2\u0176\u0177\7")
        buf.write("@\2\2\u0177\u0178\7\60\2\2\u0178\u0179\7?\2\2\u0179\u018e")
        buf.write("\7\n\2\2\u017a\u017b\5\4\3\2\u017b\u017c\7\61\2\2\u017c")
        buf.write("\u017d\7@\2\2\u017d\u017f\7\6\2\2\u017e\u0180\5`\61\2")
        buf.write("\u017f\u017e\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0181\3")
        buf.write("\2\2\2\u0181\u0182\7\7\2\2\u0182\u0183\7\n\2\2\u0183\u018e")
        buf.write("\3\2\2\2\u0184\u0185\7@\2\2\u0185\u0186\7\60\2\2\u0186")
        buf.write("\u0187\7?\2\2\u0187\u0189\7\6\2\2\u0188\u018a\5`\61\2")
        buf.write("\u0189\u0188\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018b\3")
        buf.write("\2\2\2\u018b\u018c\7\7\2\2\u018c\u018e\7\n\2\2\u018d\u0171")
        buf.write("\3\2\2\2\u018d\u0176\3\2\2\2\u018d\u017a\3\2\2\2\u018d")
        buf.write("\u0184\3\2\2\2\u018eE\3\2\2\2\u018f\u0190\7\b\2\2\u0190")
        buf.write("\u0191\5H%\2\u0191\u0192\7\t\2\2\u0192G\3\2\2\2\u0193")
        buf.write("\u0194\5P)\2\u0194\u0195\5J&\2\u0195\u0198\3\2\2\2\u0196")
        buf.write("\u0198\3\2\2\2\u0197\u0193\3\2\2\2\u0197\u0196\3\2\2\2")
        buf.write("\u0198I\3\2\2\2\u0199\u019a\5P)\2\u019a\u019b\5J&\2\u019b")
        buf.write("\u019e\3\2\2\2\u019c\u019e\3\2\2\2\u019d\u0199\3\2\2\2")
        buf.write("\u019d\u019c\3\2\2\2\u019eK\3\2\2\2\u019f\u01a0\t\7\2")
        buf.write("\2\u01a0\u01a1\5N(\2\u01a1\u01a2\7\f\2\2\u01a2\u01a5\5")
        buf.write("d\63\2\u01a3\u01a4\7(\2\2\u01a4\u01a6\5`\61\2\u01a5\u01a3")
        buf.write("\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7")
        buf.write("\u01a8\7\n\2\2\u01a8M\3\2\2\2\u01a9\u01aa\7@\2\2\u01aa")
        buf.write("\u01ab\5^\60\2\u01abO\3\2\2\2\u01ac\u01b7\5,\27\2\u01ad")
        buf.write("\u01b7\5\66\34\2\u01ae\u01b7\5<\37\2\u01af\u01b7\5> \2")
        buf.write("\u01b0\u01b7\5@!\2\u01b1\u01b7\5B\"\2\u01b2\u01b7\5D#")
        buf.write("\2\u01b3\u01b7\5L\'\2\u01b4\u01b7\5@!\2\u01b5\u01b7\5")
        buf.write("> \2\u01b6\u01ac\3\2\2\2\u01b6\u01ad\3\2\2\2\u01b6\u01ae")
        buf.write("\3\2\2\2\u01b6\u01af\3\2\2\2\u01b6\u01b0\3\2\2\2\u01b6")
        buf.write("\u01b1\3\2\2\2\u01b6\u01b2\3\2\2\2\u01b6\u01b3\3\2\2\2")
        buf.write("\u01b6\u01b4\3\2\2\2\u01b6\u01b5\3\2\2\2\u01b7Q\3\2\2")
        buf.write("\2\u01b8\u01b9\7\26\2\2\u01b9\u01bc\7@\2\2\u01ba\u01bb")
        buf.write("\7\f\2\2\u01bb\u01bd\7@\2\2\u01bc\u01ba\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01bf\7\b\2\2")
        buf.write("\u01bf\u01c0\5T+\2\u01c0\u01c1\7\t\2\2\u01c1S\3\2\2\2")
        buf.write("\u01c2\u01c3\5Z.\2\u01c3\u01c4\5V,\2\u01c4\u01ca\3\2\2")
        buf.write("\2\u01c5\u01c6\5f\64\2\u01c6\u01c7\5V,\2\u01c7\u01ca\3")
        buf.write("\2\2\2\u01c8\u01ca\3\2\2\2\u01c9\u01c2\3\2\2\2\u01c9\u01c5")
        buf.write("\3\2\2\2\u01c9\u01c8\3\2\2\2\u01caU\3\2\2\2\u01cb\u01cc")
        buf.write("\5Z.\2\u01cc\u01cd\5V,\2\u01cd\u01d3\3\2\2\2\u01ce\u01cf")
        buf.write("\5f\64\2\u01cf\u01d0\5V,\2\u01d0\u01d3\3\2\2\2\u01d1\u01d3")
        buf.write("\3\2\2\2\u01d2\u01cb\3\2\2\2\u01d2\u01ce\3\2\2\2\u01d2")
        buf.write("\u01d1\3\2\2\2\u01d3W\3\2\2\2\u01d4\u01d5\7\66\2\2\u01d5")
        buf.write("\u01d6\7\3\2\2\u01d6\u01d7\5d\63\2\u01d7\u01d8\7\13\2")
        buf.write("\2\u01d8\u01d9\79\2\2\u01d9\u01da\7\4\2\2\u01daY\3\2\2")
        buf.write("\2\u01db\u01dc\t\7\2\2\u01dc\u01dd\5\\/\2\u01dd\u01de")
        buf.write("\7\f\2\2\u01de\u01e1\5d\63\2\u01df\u01e0\7(\2\2\u01e0")
        buf.write("\u01e2\5`\61\2\u01e1\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2")
        buf.write("\u01e2\u01e3\3\2\2\2\u01e3\u01e4\7\n\2\2\u01e4[\3\2\2")
        buf.write("\2\u01e5\u01e6\t\b\2\2\u01e6\u01e7\5^\60\2\u01e7]\3\2")
        buf.write("\2\2\u01e8\u01e9\7\13\2\2\u01e9\u01ea\t\b\2\2\u01ea\u01ed")
        buf.write("\5^\60\2\u01eb\u01ed\3\2\2\2\u01ec\u01e8\3\2\2\2\u01ec")
        buf.write("\u01eb\3\2\2\2\u01ed_\3\2\2\2\u01ee\u01ef\5\4\3\2\u01ef")
        buf.write("\u01f0\5b\62\2\u01f0a\3\2\2\2\u01f1\u01f2\7\13\2\2\u01f2")
        buf.write("\u01f3\5\4\3\2\u01f3\u01f4\5b\62\2\u01f4\u01f7\3\2\2\2")
        buf.write("\u01f5\u01f7\3\2\2\2\u01f6\u01f1\3\2\2\2\u01f6\u01f5\3")
        buf.write("\2\2\2\u01f7c\3\2\2\2\u01f8\u01ff\7\65\2\2\u01f9\u01ff")
        buf.write("\7\62\2\2\u01fa\u01ff\7\63\2\2\u01fb\u01ff\7\64\2\2\u01fc")
        buf.write("\u01ff\5X-\2\u01fd\u01ff\7@\2\2\u01fe\u01f8\3\2\2\2\u01fe")
        buf.write("\u01f9\3\2\2\2\u01fe\u01fa\3\2\2\2\u01fe\u01fb\3\2\2\2")
        buf.write("\u01fe\u01fc\3\2\2\2\u01fe\u01fd\3\2\2\2\u01ffe\3\2\2")
        buf.write("\2\u0200\u0201\t\b\2\2\u0201\u0202\7\6\2\2\u0202\u0203")
        buf.write("\5h\65\2\u0203\u0204\7\7\2\2\u0204\u0205\5F$\2\u0205\u0209")
        buf.write("\3\2\2\2\u0206\u0209\5r:\2\u0207\u0209\5t;\2\u0208\u0200")
        buf.write("\3\2\2\2\u0208\u0206\3\2\2\2\u0208\u0207\3\2\2\2\u0209")
        buf.write("g\3\2\2\2\u020a\u020b\5l\67\2\u020b\u020c\5j\66\2\u020c")
        buf.write("\u020f\3\2\2\2\u020d\u020f\3\2\2\2\u020e\u020a\3\2\2\2")
        buf.write("\u020e\u020d\3\2\2\2\u020fi\3\2\2\2\u0210\u0211\7\n\2")
        buf.write("\2\u0211\u0212\5l\67\2\u0212\u0213\5j\66\2\u0213\u0216")
        buf.write("\3\2\2\2\u0214\u0216\3\2\2\2\u0215\u0210\3\2\2\2\u0215")
        buf.write("\u0214\3\2\2\2\u0216k\3\2\2\2\u0217\u0218\5n8\2\u0218")
        buf.write("\u0219\7\f\2\2\u0219\u021a\5d\63\2\u021am\3\2\2\2\u021b")
        buf.write("\u021c\7@\2\2\u021c\u021f\5p9\2\u021d\u021f\3\2\2\2\u021e")
        buf.write("\u021b\3\2\2\2\u021e\u021d\3\2\2\2\u021fo\3\2\2\2\u0220")
        buf.write("\u0221\7\13\2\2\u0221\u0222\7@\2\2\u0222\u0225\5p9\2\u0223")
        buf.write("\u0225\3\2\2\2\u0224\u0220\3\2\2\2\u0224\u0223\3\2\2\2")
        buf.write("\u0225q\3\2\2\2\u0226\u0227\7\31\2\2\u0227\u0228\7\6\2")
        buf.write("\2\u0228\u0229\5h\65\2\u0229\u022a\7\7\2\2\u022a\u022b")
        buf.write("\5F$\2\u022bs\3\2\2\2\u022c\u022d\7\32\2\2\u022d\u022e")
        buf.write("\7\6\2\2\u022e\u022f\7\7\2\2\u022f\u0230\5F$\2\u0230u")
        buf.write("\3\2\2\2/y\u0082\u0089\u0094\u00a0\u00ac\u00b2\u00b7\u00c0")
        buf.write("\u00ce\u00d2\u00d4\u00dc\u00e5\u00eb\u00f0\u00ff\u0117")
        buf.write("\u0124\u0127\u0130\u0148\u014e\u0155\u0160\u016d\u017f")
        buf.write("\u0189\u018d\u0197\u019d\u01a5\u01b6\u01bc\u01c9\u01d2")
        buf.write("\u01e1\u01ec\u01f6\u01fe\u0208\u020e\u0215\u021e\u0224")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'..'", "'('", "')'", "'{'", 
                     "'}'", "';'", "','", "':'", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'In'", 
                     "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", 
                     "'Constructor'", "'Destructor'", "'New'", "'By'", "'Self'", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
                     "'&&'", "'||'", "'=='", "'='", "'!='", "'>'", "'<='", 
                     "'<'", "'>='", "'==.'", "'+.'", "'::'", "'.'", "'Int'", 
                     "'Float'", "'String'", "'Boolean'", "'Array'", "'Void'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "LB", "RB", "LP", "RP", "SEMI", "COMMA", "COLON", 
                      "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                      "IN", "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", 
                      "DESTRUCTOR", "NEW", "BY", "SELF", "BlockComment", 
                      "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MODULO", "NEGATE", 
                      "AND", "OR", "EQUAL", "ASSIGN", "DIFFERENT", "GREATER", 
                      "LESSTHANEQUAL", "LESSER", "GREATERTHANEQUAL", "STRINGCOMPARE", 
                      "STRINGCONCAT", "STATIC_ACCESS", "DOT", "INTTYPE", 
                      "FLOATTYPE", "STRINGTYPE", "BOOLEANTYPE", "ARRAYTYPE", 
                      "VOIDTYPE", "FLOATLIT", "INTLIT", "WS", "BOOLEANLIT", 
                      "ILLEGAL_ESCAPE", "STRINGLIT", "UNCLOSE_STRING", "DOLLARID", 
                      "ID", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_exp = 1
    RULE_relational_operations = 2
    RULE_logical_operations = 3
    RULE_adding_operations = 4
    RULE_multiplying_operations = 5
    RULE_logical_negate_operation = 6
    RULE_sign_operations = 7
    RULE_index_operations = 8
    RULE_intance_access_operarion = 9
    RULE_static_access_operation = 10
    RULE_object_create_operation = 11
    RULE_parenthesis_operations = 12
    RULE_string_operators = 13
    RULE_relational_operators = 14
    RULE_logical_and_or = 15
    RULE_adding_operators = 16
    RULE_multiplying_operators = 17
    RULE_element_expression = 18
    RULE_index_operators = 19
    RULE_array_lit = 20
    RULE_if_statements = 21
    RULE_else_ifList = 22
    RULE_the_rest_else_if = 23
    RULE_else_if = 24
    RULE_else_statements = 25
    RULE_assignment_statements = 26
    RULE_lhs = 27
    RULE_assignment_static_access = 28
    RULE_foreach_statements = 29
    RULE_break_statements = 30
    RULE_continue_statements = 31
    RULE_return_statements = 32
    RULE_method_invocations = 33
    RULE_block_statements = 34
    RULE_list_statement = 35
    RULE_the_rest_statements = 36
    RULE_variable_constant_declaration = 37
    RULE_variableList = 38
    RULE_single_statement = 39
    RULE_class_declaration = 40
    RULE_attributes_methods_declarations = 41
    RULE_the_rest_attributes_methods_declarations = 42
    RULE_arrayDeclaration = 43
    RULE_attribute_declaration = 44
    RULE_attributesList = 45
    RULE_iDlist = 46
    RULE_expList = 47
    RULE_theRestExp = 48
    RULE_primitive_type = 49
    RULE_method_declaration = 50
    RULE_list_parameters = 51
    RULE_the_rest_parameters_declarations = 52
    RULE_parameters_declaration = 53
    RULE_same_type_parameters = 54
    RULE_the_rest_ID = 55
    RULE_constructor = 56
    RULE_destructor = 57

    ruleNames =  [ "program", "exp", "relational_operations", "logical_operations", 
                   "adding_operations", "multiplying_operations", "logical_negate_operation", 
                   "sign_operations", "index_operations", "intance_access_operarion", 
                   "static_access_operation", "object_create_operation", 
                   "parenthesis_operations", "string_operators", "relational_operators", 
                   "logical_and_or", "adding_operators", "multiplying_operators", 
                   "element_expression", "index_operators", "array_lit", 
                   "if_statements", "else_ifList", "the_rest_else_if", "else_if", 
                   "else_statements", "assignment_statements", "lhs", "assignment_static_access", 
                   "foreach_statements", "break_statements", "continue_statements", 
                   "return_statements", "method_invocations", "block_statements", 
                   "list_statement", "the_rest_statements", "variable_constant_declaration", 
                   "variableList", "single_statement", "class_declaration", 
                   "attributes_methods_declarations", "the_rest_attributes_methods_declarations", 
                   "arrayDeclaration", "attribute_declaration", "attributesList", 
                   "iDlist", "expList", "theRestExp", "primitive_type", 
                   "method_declaration", "list_parameters", "the_rest_parameters_declarations", 
                   "parameters_declaration", "same_type_parameters", "the_rest_ID", 
                   "constructor", "destructor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    LB=4
    RB=5
    LP=6
    RP=7
    SEMI=8
    COMMA=9
    COLON=10
    BREAK=11
    CONTINUE=12
    IF=13
    ELSEIF=14
    ELSE=15
    FOREACH=16
    IN=17
    RETURN=18
    NULL=19
    CLASS=20
    VAL=21
    VAR=22
    CONSTRUCTOR=23
    DESTRUCTOR=24
    NEW=25
    BY=26
    SELF=27
    BlockComment=28
    PLUS=29
    MINUS=30
    MULTIPLY=31
    DIVIDE=32
    MODULO=33
    NEGATE=34
    AND=35
    OR=36
    EQUAL=37
    ASSIGN=38
    DIFFERENT=39
    GREATER=40
    LESSTHANEQUAL=41
    LESSER=42
    GREATERTHANEQUAL=43
    STRINGCOMPARE=44
    STRINGCONCAT=45
    STATIC_ACCESS=46
    DOT=47
    INTTYPE=48
    FLOATTYPE=49
    STRINGTYPE=50
    BOOLEANTYPE=51
    ARRAYTYPE=52
    VOIDTYPE=53
    FLOATLIT=54
    INTLIT=55
    WS=56
    BOOLEANLIT=57
    ILLEGAL_ESCAPE=58
    STRINGLIT=59
    UNCLOSE_STRING=60
    DOLLARID=61
    ID=62
    ERROR_CHAR=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def class_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declarationContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 116
                self.class_declaration()
                self.state = 119 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 121
            self.match(D96Parser.EOF)
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

        def relational_operations(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Relational_operationsContext)
            else:
                return self.getTypedRuleContext(D96Parser.Relational_operationsContext,i)


        def string_operators(self):
            return self.getTypedRuleContext(D96Parser.String_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_exp)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.relational_operations()
                self.state = 124
                self.string_operators()
                self.state = 125
                self.relational_operations()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.relational_operations()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_operationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_operations(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Logical_operationsContext)
            else:
                return self.getTypedRuleContext(D96Parser.Logical_operationsContext,i)


        def relational_operators(self):
            return self.getTypedRuleContext(D96Parser.Relational_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_relational_operations




    def relational_operations(self):

        localctx = D96Parser.Relational_operationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_relational_operations)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.logical_operations(0)
                self.state = 131
                self.relational_operators()
                self.state = 132
                self.logical_operations(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.logical_operations(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_operationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def adding_operations(self):
            return self.getTypedRuleContext(D96Parser.Adding_operationsContext,0)


        def logical_operations(self):
            return self.getTypedRuleContext(D96Parser.Logical_operationsContext,0)


        def logical_and_or(self):
            return self.getTypedRuleContext(D96Parser.Logical_and_orContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_logical_operations



    def logical_operations(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Logical_operationsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_logical_operations, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.adding_operations(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 146
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Logical_operationsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_operations)
                    self.state = 140
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 141
                    self.logical_and_or()
                    self.state = 142
                    self.adding_operations(0) 
                self.state = 148
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Adding_operationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplying_operations(self):
            return self.getTypedRuleContext(D96Parser.Multiplying_operationsContext,0)


        def adding_operations(self):
            return self.getTypedRuleContext(D96Parser.Adding_operationsContext,0)


        def adding_operators(self):
            return self.getTypedRuleContext(D96Parser.Adding_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_adding_operations



    def adding_operations(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Adding_operationsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_adding_operations, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.multiplying_operations(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 158
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Adding_operationsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_operations)
                    self.state = 152
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 153
                    self.adding_operators()
                    self.state = 154
                    self.multiplying_operations(0) 
                self.state = 160
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplying_operationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_negate_operation(self):
            return self.getTypedRuleContext(D96Parser.Logical_negate_operationContext,0)


        def multiplying_operations(self):
            return self.getTypedRuleContext(D96Parser.Multiplying_operationsContext,0)


        def multiplying_operators(self):
            return self.getTypedRuleContext(D96Parser.Multiplying_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_multiplying_operations



    def multiplying_operations(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Multiplying_operationsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_multiplying_operations, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.logical_negate_operation()
            self._ctx.stop = self._input.LT(-1)
            self.state = 170
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Multiplying_operationsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_operations)
                    self.state = 164
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 165
                    self.multiplying_operators()
                    self.state = 166
                    self.logical_negate_operation() 
                self.state = 172
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logical_negate_operationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEGATE(self):
            return self.getToken(D96Parser.NEGATE, 0)

        def logical_negate_operation(self):
            return self.getTypedRuleContext(D96Parser.Logical_negate_operationContext,0)


        def sign_operations(self):
            return self.getTypedRuleContext(D96Parser.Sign_operationsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_logical_negate_operation




    def logical_negate_operation(self):

        localctx = D96Parser.Logical_negate_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_logical_negate_operation)
        try:
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEGATE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.match(D96Parser.NEGATE)
                self.state = 174
                self.logical_negate_operation()
                pass
            elif token in [D96Parser.LB, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.ARRAYTYPE, D96Parser.FLOATLIT, D96Parser.INTLIT, D96Parser.BOOLEANLIT, D96Parser.STRINGLIT, D96Parser.DOLLARID, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.sign_operations()
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


    class Sign_operationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(D96Parser.MINUS, 0)

        def sign_operations(self):
            return self.getTypedRuleContext(D96Parser.Sign_operationsContext,0)


        def index_operations(self):
            return self.getTypedRuleContext(D96Parser.Index_operationsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_sign_operations




    def sign_operations(self):

        localctx = D96Parser.Sign_operationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_sign_operations)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(D96Parser.MINUS)
                self.state = 179
                self.sign_operations()
                pass
            elif token in [D96Parser.LB, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.ARRAYTYPE, D96Parser.FLOATLIT, D96Parser.INTLIT, D96Parser.BOOLEANLIT, D96Parser.STRINGLIT, D96Parser.DOLLARID, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.index_operations(0)
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


    class Index_operationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def intance_access_operarion(self):
            return self.getTypedRuleContext(D96Parser.Intance_access_operarionContext,0)


        def index_operations(self):
            return self.getTypedRuleContext(D96Parser.Index_operationsContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operations



    def index_operations(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Index_operationsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_index_operations, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.intance_access_operarion(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 190
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_operationsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_operations)
                    self.state = 186
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 187
                    self.index_operators() 
                self.state = 192
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Intance_access_operarionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def static_access_operation(self):
            return self.getTypedRuleContext(D96Parser.Static_access_operationContext,0)


        def intance_access_operarion(self):
            return self.getTypedRuleContext(D96Parser.Intance_access_operarionContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expList(self):
            return self.getTypedRuleContext(D96Parser.ExpListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_intance_access_operarion



    def intance_access_operarion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Intance_access_operarionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_intance_access_operarion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.static_access_operation()
            self._ctx.stop = self._input.LT(-1)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 208
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Intance_access_operarionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_intance_access_operarion)
                        self.state = 196
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 197
                        self.match(D96Parser.DOT)
                        self.state = 198
                        self.static_access_operation()
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Intance_access_operarionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_intance_access_operarion)
                        self.state = 199
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 200
                        self.match(D96Parser.DOT)
                        self.state = 201
                        self.static_access_operation()
                        self.state = 202
                        self.match(D96Parser.LB)
                        self.state = 204
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LB) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.MINUS) | (1 << D96Parser.NEGATE) | (1 << D96Parser.ARRAYTYPE) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.INTLIT) | (1 << D96Parser.BOOLEANLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.DOLLARID) | (1 << D96Parser.ID))) != 0):
                            self.state = 203
                            self.expList()


                        self.state = 206
                        self.match(D96Parser.RB)
                        pass

             
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Static_access_operationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_create_operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Object_create_operationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Object_create_operationContext,i)


        def STATIC_ACCESS(self):
            return self.getToken(D96Parser.STATIC_ACCESS, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expList(self):
            return self.getTypedRuleContext(D96Parser.ExpListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_access_operation




    def static_access_operation(self):

        localctx = D96Parser.Static_access_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_static_access_operation)
        self._la = 0 # Token type
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.object_create_operation()
                self.state = 214
                self.match(D96Parser.STATIC_ACCESS)
                self.state = 215
                self.object_create_operation()
                self.state = 216
                self.match(D96Parser.LB)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LB) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.MINUS) | (1 << D96Parser.NEGATE) | (1 << D96Parser.ARRAYTYPE) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.INTLIT) | (1 << D96Parser.BOOLEANLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.DOLLARID) | (1 << D96Parser.ID))) != 0):
                    self.state = 217
                    self.expList()


                self.state = 220
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.object_create_operation()
                self.state = 223
                self.match(D96Parser.STATIC_ACCESS)
                self.state = 224
                self.object_create_operation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 226
                self.object_create_operation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_create_operationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def object_create_operation(self):
            return self.getTypedRuleContext(D96Parser.Object_create_operationContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expList(self):
            return self.getTypedRuleContext(D96Parser.ExpListContext,0)


        def parenthesis_operations(self):
            return self.getTypedRuleContext(D96Parser.Parenthesis_operationsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_object_create_operation




    def object_create_operation(self):

        localctx = D96Parser.Object_create_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_object_create_operation)
        self._la = 0 # Token type
        try:
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.match(D96Parser.NEW)
                self.state = 230
                self.object_create_operation()
                self.state = 231
                self.match(D96Parser.LB)
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LB) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.MINUS) | (1 << D96Parser.NEGATE) | (1 << D96Parser.ARRAYTYPE) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.INTLIT) | (1 << D96Parser.BOOLEANLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.DOLLARID) | (1 << D96Parser.ID))) != 0):
                    self.state = 232
                    self.expList()


                self.state = 235
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.LB, D96Parser.NULL, D96Parser.SELF, D96Parser.ARRAYTYPE, D96Parser.FLOATLIT, D96Parser.INTLIT, D96Parser.BOOLEANLIT, D96Parser.STRINGLIT, D96Parser.DOLLARID, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.parenthesis_operations()
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


    class Parenthesis_operationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def STRINGLIT(self):
            return self.getToken(D96Parser.STRINGLIT, 0)

        def BOOLEANLIT(self):
            return self.getToken(D96Parser.BOOLEANLIT, 0)

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def array_lit(self):
            return self.getTypedRuleContext(D96Parser.Array_litContext,0)


        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_parenthesis_operations




    def parenthesis_operations(self):

        localctx = D96Parser.Parenthesis_operationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parenthesis_operations)
        try:
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(D96Parser.LB)
                self.state = 241
                self.exp()
                self.state = 242
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 245
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.BOOLEANLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 246
                self.match(D96Parser.BOOLEANLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 247
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 248
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.ARRAYTYPE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 249
                self.array_lit()
                pass
            elif token in [D96Parser.DOLLARID]:
                self.enterOuterAlt(localctx, 8)
                self.state = 250
                self.match(D96Parser.DOLLARID)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 9)
                self.state = 251
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 10)
                self.state = 252
                self.match(D96Parser.NULL)
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


    class String_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGCOMPARE(self):
            return self.getToken(D96Parser.STRINGCOMPARE, 0)

        def STRINGCONCAT(self):
            return self.getToken(D96Parser.STRINGCONCAT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_string_operators




    def string_operators(self):

        localctx = D96Parser.String_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_string_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            _la = self._input.LA(1)
            if not(_la==D96Parser.STRINGCOMPARE or _la==D96Parser.STRINGCONCAT):
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


    class Relational_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def DIFFERENT(self):
            return self.getToken(D96Parser.DIFFERENT, 0)

        def LESSER(self):
            return self.getToken(D96Parser.LESSER, 0)

        def LESSTHANEQUAL(self):
            return self.getToken(D96Parser.LESSTHANEQUAL, 0)

        def GREATER(self):
            return self.getToken(D96Parser.GREATER, 0)

        def GREATERTHANEQUAL(self):
            return self.getToken(D96Parser.GREATERTHANEQUAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_relational_operators




    def relational_operators(self):

        localctx = D96Parser.Relational_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_relational_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUAL) | (1 << D96Parser.DIFFERENT) | (1 << D96Parser.GREATER) | (1 << D96Parser.LESSTHANEQUAL) | (1 << D96Parser.LESSER) | (1 << D96Parser.GREATERTHANEQUAL))) != 0)):
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


    class Logical_and_orContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_logical_and_or




    def logical_and_or(self):

        localctx = D96Parser.Logical_and_orContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_logical_and_or)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            _la = self._input.LA(1)
            if not(_la==D96Parser.AND or _la==D96Parser.OR):
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


    class Adding_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(D96Parser.PLUS, 0)

        def MINUS(self):
            return self.getToken(D96Parser.MINUS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_adding_operators




    def adding_operators(self):

        localctx = D96Parser.Adding_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_adding_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            _la = self._input.LA(1)
            if not(_la==D96Parser.PLUS or _la==D96Parser.MINUS):
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


    class Multiplying_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTIPLY(self):
            return self.getToken(D96Parser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(D96Parser.DIVIDE, 0)

        def MODULO(self):
            return self.getToken(D96Parser.MODULO, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_multiplying_operators




    def multiplying_operators(self):

        localctx = D96Parser.Multiplying_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_multiplying_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLY) | (1 << D96Parser.DIVIDE) | (1 << D96Parser.MODULO))) != 0)):
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


    class Element_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_element_expression




    def element_expression(self):

        localctx = D96Parser.Element_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_element_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.exp()
            self.state = 266
            self.index_operators()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operators




    def index_operators(self):

        localctx = D96Parser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_index_operators)
        try:
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.match(D96Parser.T__0)
                self.state = 269
                self.exp()
                self.state = 270
                self.match(D96Parser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.match(D96Parser.T__0)
                self.state = 273
                self.exp()
                self.state = 274
                self.match(D96Parser.T__1)
                self.state = 275
                self.index_operators()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAYTYPE(self):
            return self.getToken(D96Parser.ARRAYTYPE, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expList(self):
            return self.getTypedRuleContext(D96Parser.ExpListContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_lit




    def array_lit(self):

        localctx = D96Parser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(D96Parser.ARRAYTYPE)
            self.state = 280
            self.match(D96Parser.LB)
            self.state = 281
            self.expList()
            self.state = 282
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def else_ifList(self):
            return self.getTypedRuleContext(D96Parser.Else_ifListContext,0)


        def else_statements(self):
            return self.getTypedRuleContext(D96Parser.Else_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_statements




    def if_statements(self):

        localctx = D96Parser.If_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_if_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(D96Parser.IF)
            self.state = 285
            self.match(D96Parser.LB)
            self.state = 286
            self.exp()
            self.state = 287
            self.match(D96Parser.RB)
            self.state = 288
            self.block_statements()
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSEIF:
                self.state = 289
                self.else_ifList()


            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 292
                self.else_statements()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_ifListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_if(self):
            return self.getTypedRuleContext(D96Parser.Else_ifContext,0)


        def the_rest_else_if(self):
            return self.getTypedRuleContext(D96Parser.The_rest_else_ifContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_ifList




    def else_ifList(self):

        localctx = D96Parser.Else_ifListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_else_ifList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.else_if()
            self.state = 296
            self.the_rest_else_if()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class The_rest_else_ifContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_if(self):
            return self.getTypedRuleContext(D96Parser.Else_ifContext,0)


        def the_rest_else_if(self):
            return self.getTypedRuleContext(D96Parser.The_rest_else_ifContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_the_rest_else_if




    def the_rest_else_if(self):

        localctx = D96Parser.The_rest_else_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_the_rest_else_if)
        try:
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.else_if()
                self.state = 299
                self.the_rest_else_if()
                pass
            elif token in [D96Parser.LB, D96Parser.RP, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.ELSE, D96Parser.FOREACH, D96Parser.RETURN, D96Parser.NULL, D96Parser.VAL, D96Parser.VAR, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.NEGATE, D96Parser.ARRAYTYPE, D96Parser.FLOATLIT, D96Parser.INTLIT, D96Parser.BOOLEANLIT, D96Parser.STRINGLIT, D96Parser.DOLLARID, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)

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


    class Else_ifContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_if




    def else_if(self):

        localctx = D96Parser.Else_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_else_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(D96Parser.ELSEIF)
            self.state = 305
            self.match(D96Parser.LB)
            self.state = 306
            self.exp()
            self.state = 307
            self.match(D96Parser.RB)
            self.state = 308
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_statements




    def else_statements(self):

        localctx = D96Parser.Else_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_else_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(D96Parser.ELSE)
            self.state = 311
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assignment_statements




    def assignment_statements(self):

        localctx = D96Parser.Assignment_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assignment_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.lhs(0)
            self.state = 314
            self.match(D96Parser.ASSIGN)
            self.state = 315
            self.exp()
            self.state = 316
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_static_access(self):
            return self.getTypedRuleContext(D96Parser.Assignment_static_accessContext,0)


        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_lhs



    def lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.LhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.assignment_static_access()
            self._ctx.stop = self._input.LT(-1)
            self.state = 326
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.LhsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                    self.state = 321
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 322
                    self.match(D96Parser.DOT)
                    self.state = 323
                    self.assignment_static_access() 
                self.state = 328
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Assignment_static_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC_ACCESS(self):
            return self.getToken(D96Parser.STATIC_ACCESS, 0)

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def element_expression(self):
            return self.getTypedRuleContext(D96Parser.Element_expressionContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assignment_static_access




    def assignment_static_access(self):

        localctx = D96Parser.Assignment_static_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_assignment_static_access)
        try:
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 329
                    self.match(D96Parser.ID)
                    pass

                elif la_ == 2:
                    self.state = 330
                    self.element_expression()
                    pass

                elif la_ == 3:
                    self.state = 331
                    self.match(D96Parser.SELF)
                    pass


                self.state = 334
                self.match(D96Parser.STATIC_ACCESS)
                self.state = 335
                self.match(D96Parser.DOLLARID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 337
                self.element_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 338
                self.match(D96Parser.SELF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Foreach_statementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_foreach_statements




    def foreach_statements(self):

        localctx = D96Parser.Foreach_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_foreach_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(D96Parser.FOREACH)
            self.state = 342
            self.match(D96Parser.LB)
            self.state = 343
            self.lhs(0)
            self.state = 344
            self.match(D96Parser.IN)
            self.state = 345
            self.exp()
            self.state = 346
            self.match(D96Parser.T__2)
            self.state = 347
            self.exp()
            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 348
                self.match(D96Parser.BY)
                self.state = 349
                self.exp()


            self.state = 352
            self.match(D96Parser.RB)
            self.state = 353
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_statements




    def break_statements(self):

        localctx = D96Parser.Break_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_break_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(D96Parser.BREAK)
            self.state = 356
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_statements




    def continue_statements(self):

        localctx = D96Parser.Continue_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_continue_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(D96Parser.CONTINUE)
            self.state = 359
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_statements




    def return_statements(self):

        localctx = D96Parser.Return_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_return_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(D96Parser.RETURN)
            self.state = 363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LB) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.MINUS) | (1 << D96Parser.NEGATE) | (1 << D96Parser.ARRAYTYPE) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.INTLIT) | (1 << D96Parser.BOOLEANLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.DOLLARID) | (1 << D96Parser.ID))) != 0):
                self.state = 362
                self.exp()


            self.state = 365
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def STATIC_ACCESS(self):
            return self.getToken(D96Parser.STATIC_ACCESS, 0)

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expList(self):
            return self.getTypedRuleContext(D96Parser.ExpListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_invocations




    def method_invocations(self):

        localctx = D96Parser.Method_invocationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_method_invocations)
        self._la = 0 # Token type
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.exp()
                self.state = 368
                self.match(D96Parser.DOT)
                self.state = 369
                self.match(D96Parser.ID)
                self.state = 370
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                self.match(D96Parser.ID)
                self.state = 373
                self.match(D96Parser.STATIC_ACCESS)
                self.state = 374
                self.match(D96Parser.DOLLARID)
                self.state = 375
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 376
                self.exp()
                self.state = 377
                self.match(D96Parser.DOT)
                self.state = 378
                self.match(D96Parser.ID)
                self.state = 379
                self.match(D96Parser.LB)
                self.state = 381
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LB) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.MINUS) | (1 << D96Parser.NEGATE) | (1 << D96Parser.ARRAYTYPE) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.INTLIT) | (1 << D96Parser.BOOLEANLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.DOLLARID) | (1 << D96Parser.ID))) != 0):
                    self.state = 380
                    self.expList()


                self.state = 383
                self.match(D96Parser.RB)
                self.state = 384
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 386
                self.match(D96Parser.ID)
                self.state = 387
                self.match(D96Parser.STATIC_ACCESS)
                self.state = 388
                self.match(D96Parser.DOLLARID)
                self.state = 389
                self.match(D96Parser.LB)
                self.state = 391
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LB) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.MINUS) | (1 << D96Parser.NEGATE) | (1 << D96Parser.ARRAYTYPE) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.INTLIT) | (1 << D96Parser.BOOLEANLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.DOLLARID) | (1 << D96Parser.ID))) != 0):
                    self.state = 390
                    self.expList()


                self.state = 393
                self.match(D96Parser.RB)
                self.state = 394
                self.match(D96Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def list_statement(self):
            return self.getTypedRuleContext(D96Parser.List_statementContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_block_statements




    def block_statements(self):

        localctx = D96Parser.Block_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_block_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(D96Parser.LP)
            self.state = 398
            self.list_statement()
            self.state = 399
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_statement(self):
            return self.getTypedRuleContext(D96Parser.Single_statementContext,0)


        def the_rest_statements(self):
            return self.getTypedRuleContext(D96Parser.The_rest_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_statement




    def list_statement(self):

        localctx = D96Parser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_list_statement)
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.RETURN, D96Parser.NULL, D96Parser.VAL, D96Parser.VAR, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.NEGATE, D96Parser.ARRAYTYPE, D96Parser.FLOATLIT, D96Parser.INTLIT, D96Parser.BOOLEANLIT, D96Parser.STRINGLIT, D96Parser.DOLLARID, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.single_statement()
                self.state = 402
                self.the_rest_statements()
                pass
            elif token in [D96Parser.RP]:
                self.enterOuterAlt(localctx, 2)

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


    class The_rest_statementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_statement(self):
            return self.getTypedRuleContext(D96Parser.Single_statementContext,0)


        def the_rest_statements(self):
            return self.getTypedRuleContext(D96Parser.The_rest_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_the_rest_statements




    def the_rest_statements(self):

        localctx = D96Parser.The_rest_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_the_rest_statements)
        try:
            self.state = 411
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.RETURN, D96Parser.NULL, D96Parser.VAL, D96Parser.VAR, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.NEGATE, D96Parser.ARRAYTYPE, D96Parser.FLOATLIT, D96Parser.INTLIT, D96Parser.BOOLEANLIT, D96Parser.STRINGLIT, D96Parser.DOLLARID, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.single_statement()
                self.state = 408
                self.the_rest_statements()
                pass
            elif token in [D96Parser.RP]:
                self.enterOuterAlt(localctx, 2)

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


    class Variable_constant_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableList(self):
            return self.getTypedRuleContext(D96Parser.VariableListContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def expList(self):
            return self.getTypedRuleContext(D96Parser.ExpListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_variable_constant_declaration




    def variable_constant_declaration(self):

        localctx = D96Parser.Variable_constant_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_variable_constant_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 414
            self.variableList()
            self.state = 415
            self.match(D96Parser.COLON)
            self.state = 416
            self.primitive_type()
            self.state = 419
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 417
                self.match(D96Parser.ASSIGN)
                self.state = 418
                self.expList()


            self.state = 421
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def iDlist(self):
            return self.getTypedRuleContext(D96Parser.IDlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_variableList




    def variableList(self):

        localctx = D96Parser.VariableListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_variableList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(D96Parser.ID)
            self.state = 424
            self.iDlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_statements(self):
            return self.getTypedRuleContext(D96Parser.If_statementsContext,0)


        def assignment_statements(self):
            return self.getTypedRuleContext(D96Parser.Assignment_statementsContext,0)


        def foreach_statements(self):
            return self.getTypedRuleContext(D96Parser.Foreach_statementsContext,0)


        def break_statements(self):
            return self.getTypedRuleContext(D96Parser.Break_statementsContext,0)


        def continue_statements(self):
            return self.getTypedRuleContext(D96Parser.Continue_statementsContext,0)


        def return_statements(self):
            return self.getTypedRuleContext(D96Parser.Return_statementsContext,0)


        def method_invocations(self):
            return self.getTypedRuleContext(D96Parser.Method_invocationsContext,0)


        def variable_constant_declaration(self):
            return self.getTypedRuleContext(D96Parser.Variable_constant_declarationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_single_statement




    def single_statement(self):

        localctx = D96Parser.Single_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_single_statement)
        try:
            self.state = 436
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.if_statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 427
                self.assignment_statements()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 428
                self.foreach_statements()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 429
                self.break_statements()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 430
                self.continue_statements()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 431
                self.return_statements()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 432
                self.method_invocations()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 433
                self.variable_constant_declaration()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 434
                self.continue_statements()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 435
                self.break_statements()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def attributes_methods_declarations(self):
            return self.getTypedRuleContext(D96Parser.Attributes_methods_declarationsContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_declaration




    def class_declaration(self):

        localctx = D96Parser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(D96Parser.CLASS)
            self.state = 439
            self.match(D96Parser.ID)
            self.state = 442
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 440
                self.match(D96Parser.COLON)
                self.state = 441
                self.match(D96Parser.ID)


            self.state = 444
            self.match(D96Parser.LP)
            self.state = 445
            self.attributes_methods_declarations()
            self.state = 446
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attributes_methods_declarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_declaration(self):
            return self.getTypedRuleContext(D96Parser.Attribute_declarationContext,0)


        def the_rest_attributes_methods_declarations(self):
            return self.getTypedRuleContext(D96Parser.The_rest_attributes_methods_declarationsContext,0)


        def method_declaration(self):
            return self.getTypedRuleContext(D96Parser.Method_declarationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attributes_methods_declarations




    def attributes_methods_declarations(self):

        localctx = D96Parser.Attributes_methods_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_attributes_methods_declarations)
        try:
            self.state = 455
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 448
                self.attribute_declaration()
                self.state = 449
                self.the_rest_attributes_methods_declarations()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.DOLLARID, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
                self.method_declaration()
                self.state = 452
                self.the_rest_attributes_methods_declarations()
                pass
            elif token in [D96Parser.RP]:
                self.enterOuterAlt(localctx, 3)

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


    class The_rest_attributes_methods_declarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_declaration(self):
            return self.getTypedRuleContext(D96Parser.Attribute_declarationContext,0)


        def the_rest_attributes_methods_declarations(self):
            return self.getTypedRuleContext(D96Parser.The_rest_attributes_methods_declarationsContext,0)


        def method_declaration(self):
            return self.getTypedRuleContext(D96Parser.Method_declarationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_the_rest_attributes_methods_declarations




    def the_rest_attributes_methods_declarations(self):

        localctx = D96Parser.The_rest_attributes_methods_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_the_rest_attributes_methods_declarations)
        try:
            self.state = 464
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.attribute_declaration()
                self.state = 458
                self.the_rest_attributes_methods_declarations()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.DOLLARID, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 460
                self.method_declaration()
                self.state = 461
                self.the_rest_attributes_methods_declarations()
                pass
            elif token in [D96Parser.RP]:
                self.enterOuterAlt(localctx, 3)

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


    class ArrayDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAYTYPE(self):
            return self.getToken(D96Parser.ARRAYTYPE, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arrayDeclaration




    def arrayDeclaration(self):

        localctx = D96Parser.ArrayDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_arrayDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.match(D96Parser.ARRAYTYPE)
            self.state = 467
            self.match(D96Parser.T__0)
            self.state = 468
            self.primitive_type()
            self.state = 469
            self.match(D96Parser.COMMA)
            self.state = 470
            self.match(D96Parser.INTLIT)
            self.state = 471
            self.match(D96Parser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributesList(self):
            return self.getTypedRuleContext(D96Parser.AttributesListContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def expList(self):
            return self.getTypedRuleContext(D96Parser.ExpListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute_declaration




    def attribute_declaration(self):

        localctx = D96Parser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 474
            self.attributesList()
            self.state = 475
            self.match(D96Parser.COLON)
            self.state = 476
            self.primitive_type()
            self.state = 479
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 477
                self.match(D96Parser.ASSIGN)
                self.state = 478
                self.expList()


            self.state = 481
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributesListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iDlist(self):
            return self.getTypedRuleContext(D96Parser.IDlistContext,0)


        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attributesList




    def attributesList(self):

        localctx = D96Parser.AttributesListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_attributesList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            _la = self._input.LA(1)
            if not(_la==D96Parser.DOLLARID or _la==D96Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 484
            self.iDlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IDlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def iDlist(self):
            return self.getTypedRuleContext(D96Parser.IDlistContext,0)


        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_iDlist




    def iDlist(self):

        localctx = D96Parser.IDlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_iDlist)
        self._la = 0 # Token type
        try:
            self.state = 490
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 486
                self.match(D96Parser.COMMA)
                self.state = 487
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOLLARID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 488
                self.iDlist()
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)

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


    class ExpListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def theRestExp(self):
            return self.getTypedRuleContext(D96Parser.TheRestExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expList




    def expList(self):

        localctx = D96Parser.ExpListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.exp()
            self.state = 493
            self.theRestExp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TheRestExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def theRestExp(self):
            return self.getTypedRuleContext(D96Parser.TheRestExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_theRestExp




    def theRestExp(self):

        localctx = D96Parser.TheRestExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_theRestExp)
        try:
            self.state = 500
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.match(D96Parser.COMMA)
                self.state = 496
                self.exp()
                self.state = 497
                self.theRestExp()
                pass
            elif token in [D96Parser.RB, D96Parser.SEMI]:
                self.enterOuterAlt(localctx, 2)

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


    class Primitive_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEANTYPE(self):
            return self.getToken(D96Parser.BOOLEANTYPE, 0)

        def INTTYPE(self):
            return self.getToken(D96Parser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(D96Parser.FLOATTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(D96Parser.STRINGTYPE, 0)

        def arrayDeclaration(self):
            return self.getTypedRuleContext(D96Parser.ArrayDeclarationContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitive_type




    def primitive_type(self):

        localctx = D96Parser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_primitive_type)
        try:
            self.state = 508
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLEANTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 502
                self.match(D96Parser.BOOLEANTYPE)
                pass
            elif token in [D96Parser.INTTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 503
                self.match(D96Parser.INTTYPE)
                pass
            elif token in [D96Parser.FLOATTYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 504
                self.match(D96Parser.FLOATTYPE)
                pass
            elif token in [D96Parser.STRINGTYPE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 505
                self.match(D96Parser.STRINGTYPE)
                pass
            elif token in [D96Parser.ARRAYTYPE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 506
                self.arrayDeclaration()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 507
                self.match(D96Parser.ID)
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


    class Method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_parameters(self):
            return self.getTypedRuleContext(D96Parser.List_parametersContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def constructor(self):
            return self.getTypedRuleContext(D96Parser.ConstructorContext,0)


        def destructor(self):
            return self.getTypedRuleContext(D96Parser.DestructorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_declaration




    def method_declaration(self):

        localctx = D96Parser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.state = 518
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.DOLLARID, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 510
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOLLARID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 511
                self.match(D96Parser.LB)
                self.state = 512
                self.list_parameters()
                self.state = 513
                self.match(D96Parser.RB)
                self.state = 514
                self.block_statements()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 516
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 517
                self.destructor()
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


    class List_parametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameters_declaration(self):
            return self.getTypedRuleContext(D96Parser.Parameters_declarationContext,0)


        def the_rest_parameters_declarations(self):
            return self.getTypedRuleContext(D96Parser.The_rest_parameters_declarationsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_parameters




    def list_parameters(self):

        localctx = D96Parser.List_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_list_parameters)
        try:
            self.state = 524
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 520
                self.parameters_declaration()
                self.state = 521
                self.the_rest_parameters_declarations()
                pass
            elif token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class The_rest_parameters_declarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def parameters_declaration(self):
            return self.getTypedRuleContext(D96Parser.Parameters_declarationContext,0)


        def the_rest_parameters_declarations(self):
            return self.getTypedRuleContext(D96Parser.The_rest_parameters_declarationsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_the_rest_parameters_declarations




    def the_rest_parameters_declarations(self):

        localctx = D96Parser.The_rest_parameters_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_the_rest_parameters_declarations)
        try:
            self.state = 531
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SEMI]:
                self.enterOuterAlt(localctx, 1)
                self.state = 526
                self.match(D96Parser.SEMI)
                self.state = 527
                self.parameters_declaration()
                self.state = 528
                self.the_rest_parameters_declarations()
                pass
            elif token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class Parameters_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def same_type_parameters(self):
            return self.getTypedRuleContext(D96Parser.Same_type_parametersContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_parameters_declaration




    def parameters_declaration(self):

        localctx = D96Parser.Parameters_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_parameters_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.same_type_parameters()
            self.state = 534
            self.match(D96Parser.COLON)
            self.state = 535
            self.primitive_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Same_type_parametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def the_rest_ID(self):
            return self.getTypedRuleContext(D96Parser.The_rest_IDContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_same_type_parameters




    def same_type_parameters(self):

        localctx = D96Parser.Same_type_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_same_type_parameters)
        try:
            self.state = 540
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 537
                self.match(D96Parser.ID)
                self.state = 538
                self.the_rest_ID()
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)

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


    class The_rest_IDContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def the_rest_ID(self):
            return self.getTypedRuleContext(D96Parser.The_rest_IDContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_the_rest_ID




    def the_rest_ID(self):

        localctx = D96Parser.The_rest_IDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_the_rest_ID)
        try:
            self.state = 546
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 542
                self.match(D96Parser.COMMA)
                self.state = 543
                self.match(D96Parser.ID)
                self.state = 544
                self.the_rest_ID()
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)

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


    class ConstructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_parameters(self):
            return self.getTypedRuleContext(D96Parser.List_parametersContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 548
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 549
            self.match(D96Parser.LB)
            self.state = 550
            self.list_parameters()
            self.state = 551
            self.match(D96Parser.RB)
            self.state = 552
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554
            self.match(D96Parser.DESTRUCTOR)
            self.state = 555
            self.match(D96Parser.LB)
            self.state = 556
            self.match(D96Parser.RB)
            self.state = 557
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.logical_operations_sempred
        self._predicates[4] = self.adding_operations_sempred
        self._predicates[5] = self.multiplying_operations_sempred
        self._predicates[8] = self.index_operations_sempred
        self._predicates[9] = self.intance_access_operarion_sempred
        self._predicates[27] = self.lhs_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logical_operations_sempred(self, localctx:Logical_operationsContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def adding_operations_sempred(self, localctx:Adding_operationsContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multiplying_operations_sempred(self, localctx:Multiplying_operationsContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def index_operations_sempred(self, localctx:Index_operationsContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def intance_access_operarion_sempred(self, localctx:Intance_access_operarionContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def lhs_sempred(self, localctx:LhsContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




