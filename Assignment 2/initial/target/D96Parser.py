# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
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
        buf.write("\u022f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("\3\r\3\r\5\r\u00ec\n\r\3\r\3\r\5\r\u00f0\n\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16")
        buf.write("\u00fe\n\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3")
        buf.write("\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\5\25\u0116\n\25\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0123\n\27\3\27")
        buf.write("\5\27\u0126\n\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\5")
        buf.write("\31\u012f\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\7\35\u0145\n\35\f\35\16\35\u0148\13\35\3\36\3\36")
        buf.write("\3\36\5\36\u014d\n\36\3\36\3\36\3\36\3\36\3\36\5\36\u0154")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37")
        buf.write("\u015f\n\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\5")
        buf.write("\"\u016c\n\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\3#\3#\3#\5#\u017e\n#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u0188")
        buf.write("\n#\3#\3#\5#\u018c\n#\3$\3$\3$\3$\3%\3%\3%\3%\5%\u0196")
        buf.write("\n%\3&\3&\3&\3&\5&\u019c\n&\3\'\3\'\3\'\3\'\3\'\3\'\5")
        buf.write("\'\u01a4\n\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)")
        buf.write("\3)\5)\u01b4\n)\3*\3*\3*\3*\5*\u01ba\n*\3*\3*\3*\3*\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\5+\u01c7\n+\3,\3,\3,\3,\3,\3,\3,\5")
        buf.write(",\u01d0\n,\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\5.\u01df")
        buf.write("\n.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\60\5\60\u01ea\n\60")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\5\62\u01f4\n")
        buf.write("\62\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u01fc\n\63\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u0206\n\64\3")
        buf.write("\65\3\65\3\65\3\65\5\65\u020c\n\65\3\66\3\66\3\66\3\66")
        buf.write("\3\66\5\66\u0213\n\66\3\67\3\67\3\67\3\67\38\38\38\58")
        buf.write("\u021c\n8\39\39\39\39\59\u0222\n9\3:\3:\3:\3:\3:\3:\3")
        buf.write(";\3;\3;\3;\3;\3;\2\b\b\n\f\22\248<\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhjlnprt\2\t\3\2./\4\2\'\')-\3\2%&\3\2\37 \3")
        buf.write("\2!#\3\2\27\30\3\2?@\2\u023c\2w\3\2\2\2\4\u0082\3\2\2")
        buf.write("\2\6\u0089\3\2\2\2\b\u008b\3\2\2\2\n\u0097\3\2\2\2\f\u00a3")
        buf.write("\3\2\2\2\16\u00b2\3\2\2\2\20\u00b7\3\2\2\2\22\u00b9\3")
        buf.write("\2\2\2\24\u00c3\3\2\2\2\26\u00e5\3\2\2\2\30\u00ef\3\2")
        buf.write("\2\2\32\u00fd\3\2\2\2\34\u00ff\3\2\2\2\36\u0101\3\2\2")
        buf.write("\2 \u0103\3\2\2\2\"\u0105\3\2\2\2$\u0107\3\2\2\2&\u0109")
        buf.write("\3\2\2\2(\u0115\3\2\2\2*\u0117\3\2\2\2,\u011c\3\2\2\2")
        buf.write(".\u0127\3\2\2\2\60\u012e\3\2\2\2\62\u0130\3\2\2\2\64\u0136")
        buf.write("\3\2\2\2\66\u0139\3\2\2\28\u013e\3\2\2\2:\u0153\3\2\2")
        buf.write("\2<\u0155\3\2\2\2>\u0163\3\2\2\2@\u0166\3\2\2\2B\u0169")
        buf.write("\3\2\2\2D\u018b\3\2\2\2F\u018d\3\2\2\2H\u0195\3\2\2\2")
        buf.write("J\u019b\3\2\2\2L\u019d\3\2\2\2N\u01a7\3\2\2\2P\u01b3\3")
        buf.write("\2\2\2R\u01b5\3\2\2\2T\u01c6\3\2\2\2V\u01cf\3\2\2\2X\u01d1")
        buf.write("\3\2\2\2Z\u01d8\3\2\2\2\\\u01e2\3\2\2\2^\u01e9\3\2\2\2")
        buf.write("`\u01eb\3\2\2\2b\u01f3\3\2\2\2d\u01fb\3\2\2\2f\u0205\3")
        buf.write("\2\2\2h\u020b\3\2\2\2j\u0212\3\2\2\2l\u0214\3\2\2\2n\u021b")
        buf.write("\3\2\2\2p\u0221\3\2\2\2r\u0223\3\2\2\2t\u0229\3\2\2\2")
        buf.write("vx\5R*\2wv\3\2\2\2xy\3\2\2\2yw\3\2\2\2yz\3\2\2\2z{\3\2")
        buf.write("\2\2{|\7\2\2\3|\3\3\2\2\2}~\5\6\4\2~\177\5\34\17\2\177")
        buf.write("\u0080\5\6\4\2\u0080\u0083\3\2\2\2\u0081\u0083\5\6\4\2")
        buf.write("\u0082}\3\2\2\2\u0082\u0081\3\2\2\2\u0083\5\3\2\2\2\u0084")
        buf.write("\u0085\5\b\5\2\u0085\u0086\5\36\20\2\u0086\u0087\5\b\5")
        buf.write("\2\u0087\u008a\3\2\2\2\u0088\u008a\5\b\5\2\u0089\u0084")
        buf.write("\3\2\2\2\u0089\u0088\3\2\2\2\u008a\7\3\2\2\2\u008b\u008c")
        buf.write("\b\5\1\2\u008c\u008d\5\n\6\2\u008d\u0094\3\2\2\2\u008e")
        buf.write("\u008f\f\4\2\2\u008f\u0090\5 \21\2\u0090\u0091\5\n\6\2")
        buf.write("\u0091\u0093\3\2\2\2\u0092\u008e\3\2\2\2\u0093\u0096\3")
        buf.write("\2\2\2\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\t")
        buf.write("\3\2\2\2\u0096\u0094\3\2\2\2\u0097\u0098\b\6\1\2\u0098")
        buf.write("\u0099\5\f\7\2\u0099\u00a0\3\2\2\2\u009a\u009b\f\4\2\2")
        buf.write("\u009b\u009c\5\"\22\2\u009c\u009d\5\f\7\2\u009d\u009f")
        buf.write("\3\2\2\2\u009e\u009a\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0")
        buf.write("\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\13\3\2\2\2\u00a2")
        buf.write("\u00a0\3\2\2\2\u00a3\u00a4\b\7\1\2\u00a4\u00a5\5\16\b")
        buf.write("\2\u00a5\u00ac\3\2\2\2\u00a6\u00a7\f\4\2\2\u00a7\u00a8")
        buf.write("\5$\23\2\u00a8\u00a9\5\16\b\2\u00a9\u00ab\3\2\2\2\u00aa")
        buf.write("\u00a6\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2")
        buf.write("\u00ac\u00ad\3\2\2\2\u00ad\r\3\2\2\2\u00ae\u00ac\3\2\2")
        buf.write("\2\u00af\u00b0\7$\2\2\u00b0\u00b3\5\16\b\2\u00b1\u00b3")
        buf.write("\5\20\t\2\u00b2\u00af\3\2\2\2\u00b2\u00b1\3\2\2\2\u00b3")
        buf.write("\17\3\2\2\2\u00b4\u00b5\7 \2\2\u00b5\u00b8\5\20\t\2\u00b6")
        buf.write("\u00b8\5\22\n\2\u00b7\u00b4\3\2\2\2\u00b7\u00b6\3\2\2")
        buf.write("\2\u00b8\21\3\2\2\2\u00b9\u00ba\b\n\1\2\u00ba\u00bb\5")
        buf.write("\24\13\2\u00bb\u00c0\3\2\2\2\u00bc\u00bd\f\4\2\2\u00bd")
        buf.write("\u00bf\5(\25\2\u00be\u00bc\3\2\2\2\u00bf\u00c2\3\2\2\2")
        buf.write("\u00c0\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\23\3\2")
        buf.write("\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00c4\b\13\1\2\u00c4\u00c5")
        buf.write("\5\26\f\2\u00c5\u00d4\3\2\2\2\u00c6\u00c7\f\5\2\2\u00c7")
        buf.write("\u00c8\7\61\2\2\u00c8\u00d3\5\26\f\2\u00c9\u00ca\f\4\2")
        buf.write("\2\u00ca\u00cb\7\61\2\2\u00cb\u00cc\5\26\f\2\u00cc\u00ce")
        buf.write("\7\6\2\2\u00cd\u00cf\5`\61\2\u00ce\u00cd\3\2\2\2\u00ce")
        buf.write("\u00cf\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1\7\7\2\2")
        buf.write("\u00d1\u00d3\3\2\2\2\u00d2\u00c6\3\2\2\2\u00d2\u00c9\3")
        buf.write("\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5")
        buf.write("\3\2\2\2\u00d5\25\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00d8")
        buf.write("\5\30\r\2\u00d8\u00d9\7\60\2\2\u00d9\u00da\7?\2\2\u00da")
        buf.write("\u00dc\7\6\2\2\u00db\u00dd\5`\61\2\u00dc\u00db\3\2\2\2")
        buf.write("\u00dc\u00dd\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00df\7")
        buf.write("\7\2\2\u00df\u00e6\3\2\2\2\u00e0\u00e1\5\30\r\2\u00e1")
        buf.write("\u00e2\7\60\2\2\u00e2\u00e3\7?\2\2\u00e3\u00e6\3\2\2\2")
        buf.write("\u00e4\u00e6\5\30\r\2\u00e5\u00d7\3\2\2\2\u00e5\u00e0")
        buf.write("\3\2\2\2\u00e5\u00e4\3\2\2\2\u00e6\27\3\2\2\2\u00e7\u00e8")
        buf.write("\7\33\2\2\u00e8\u00e9\7@\2\2\u00e9\u00eb\7\6\2\2\u00ea")
        buf.write("\u00ec\5`\61\2\u00eb\u00ea\3\2\2\2\u00eb\u00ec\3\2\2\2")
        buf.write("\u00ec\u00ed\3\2\2\2\u00ed\u00f0\7\7\2\2\u00ee\u00f0\5")
        buf.write("\32\16\2\u00ef\u00e7\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0")
        buf.write("\31\3\2\2\2\u00f1\u00f2\7\6\2\2\u00f2\u00f3\5\4\3\2\u00f3")
        buf.write("\u00f4\7\7\2\2\u00f4\u00fe\3\2\2\2\u00f5\u00fe\79\2\2")
        buf.write("\u00f6\u00fe\7=\2\2\u00f7\u00fe\7;\2\2\u00f8\u00fe\78")
        buf.write("\2\2\u00f9\u00fe\7@\2\2\u00fa\u00fe\5*\26\2\u00fb\u00fe")
        buf.write("\7\35\2\2\u00fc\u00fe\7\25\2\2\u00fd\u00f1\3\2\2\2\u00fd")
        buf.write("\u00f5\3\2\2\2\u00fd\u00f6\3\2\2\2\u00fd\u00f7\3\2\2\2")
        buf.write("\u00fd\u00f8\3\2\2\2\u00fd\u00f9\3\2\2\2\u00fd\u00fa\3")
        buf.write("\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe\33")
        buf.write("\3\2\2\2\u00ff\u0100\t\2\2\2\u0100\35\3\2\2\2\u0101\u0102")
        buf.write("\t\3\2\2\u0102\37\3\2\2\2\u0103\u0104\t\4\2\2\u0104!\3")
        buf.write("\2\2\2\u0105\u0106\t\5\2\2\u0106#\3\2\2\2\u0107\u0108")
        buf.write("\t\6\2\2\u0108%\3\2\2\2\u0109\u010a\5\4\3\2\u010a\u010b")
        buf.write("\5(\25\2\u010b\'\3\2\2\2\u010c\u010d\7\3\2\2\u010d\u010e")
        buf.write("\5\4\3\2\u010e\u010f\7\4\2\2\u010f\u0110\5(\25\2\u0110")
        buf.write("\u0116\3\2\2\2\u0111\u0112\7\3\2\2\u0112\u0113\5\4\3\2")
        buf.write("\u0113\u0114\7\4\2\2\u0114\u0116\3\2\2\2\u0115\u010c\3")
        buf.write("\2\2\2\u0115\u0111\3\2\2\2\u0116)\3\2\2\2\u0117\u0118")
        buf.write("\7\66\2\2\u0118\u0119\7\6\2\2\u0119\u011a\5`\61\2\u011a")
        buf.write("\u011b\7\7\2\2\u011b+\3\2\2\2\u011c\u011d\7\17\2\2\u011d")
        buf.write("\u011e\7\6\2\2\u011e\u011f\5\4\3\2\u011f\u0120\7\7\2\2")
        buf.write("\u0120\u0122\5F$\2\u0121\u0123\5.\30\2\u0122\u0121\3\2")
        buf.write("\2\2\u0122\u0123\3\2\2\2\u0123\u0125\3\2\2\2\u0124\u0126")
        buf.write("\5\64\33\2\u0125\u0124\3\2\2\2\u0125\u0126\3\2\2\2\u0126")
        buf.write("-\3\2\2\2\u0127\u0128\5\62\32\2\u0128\u0129\5\60\31\2")
        buf.write("\u0129/\3\2\2\2\u012a\u012b\5\62\32\2\u012b\u012c\5\60")
        buf.write("\31\2\u012c\u012f\3\2\2\2\u012d\u012f\3\2\2\2\u012e\u012a")
        buf.write("\3\2\2\2\u012e\u012d\3\2\2\2\u012f\61\3\2\2\2\u0130\u0131")
        buf.write("\7\20\2\2\u0131\u0132\7\6\2\2\u0132\u0133\5\4\3\2\u0133")
        buf.write("\u0134\7\7\2\2\u0134\u0135\5F$\2\u0135\63\3\2\2\2\u0136")
        buf.write("\u0137\7\21\2\2\u0137\u0138\5F$\2\u0138\65\3\2\2\2\u0139")
        buf.write("\u013a\58\35\2\u013a\u013b\7(\2\2\u013b\u013c\5\4\3\2")
        buf.write("\u013c\u013d\7\n\2\2\u013d\67\3\2\2\2\u013e\u013f\b\35")
        buf.write("\1\2\u013f\u0140\5:\36\2\u0140\u0146\3\2\2\2\u0141\u0142")
        buf.write("\f\4\2\2\u0142\u0143\7\61\2\2\u0143\u0145\5:\36\2\u0144")
        buf.write("\u0141\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2")
        buf.write("\u0146\u0147\3\2\2\2\u01479\3\2\2\2\u0148\u0146\3\2\2")
        buf.write("\2\u0149\u014d\7@\2\2\u014a\u014d\5\22\n\2\u014b\u014d")
        buf.write("\7\35\2\2\u014c\u0149\3\2\2\2\u014c\u014a\3\2\2\2\u014c")
        buf.write("\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u014f\7\60\2")
        buf.write("\2\u014f\u0154\7?\2\2\u0150\u0154\7@\2\2\u0151\u0154\5")
        buf.write("\22\n\2\u0152\u0154\7\35\2\2\u0153\u014c\3\2\2\2\u0153")
        buf.write("\u0150\3\2\2\2\u0153\u0151\3\2\2\2\u0153\u0152\3\2\2\2")
        buf.write("\u0154;\3\2\2\2\u0155\u0156\7\22\2\2\u0156\u0157\7\6\2")
        buf.write("\2\u0157\u0158\7@\2\2\u0158\u0159\7\23\2\2\u0159\u015a")
        buf.write("\5\4\3\2\u015a\u015b\7\5\2\2\u015b\u015e\5\4\3\2\u015c")
        buf.write("\u015d\7\34\2\2\u015d\u015f\5\4\3\2\u015e\u015c\3\2\2")
        buf.write("\2\u015e\u015f\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0161")
        buf.write("\7\7\2\2\u0161\u0162\5F$\2\u0162=\3\2\2\2\u0163\u0164")
        buf.write("\7\r\2\2\u0164\u0165\7\n\2\2\u0165?\3\2\2\2\u0166\u0167")
        buf.write("\7\16\2\2\u0167\u0168\7\n\2\2\u0168A\3\2\2\2\u0169\u016b")
        buf.write("\7\24\2\2\u016a\u016c\5\4\3\2\u016b\u016a\3\2\2\2\u016b")
        buf.write("\u016c\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016e\7\n\2\2")
        buf.write("\u016eC\3\2\2\2\u016f\u0170\5\4\3\2\u0170\u0171\7\61\2")
        buf.write("\2\u0171\u0172\7@\2\2\u0172\u0173\7\n\2\2\u0173\u018c")
        buf.write("\3\2\2\2\u0174\u0175\7@\2\2\u0175\u0176\7\60\2\2\u0176")
        buf.write("\u0177\7?\2\2\u0177\u018c\7\n\2\2\u0178\u0179\5\4\3\2")
        buf.write("\u0179\u017a\7\61\2\2\u017a\u017b\7@\2\2\u017b\u017d\7")
        buf.write("\6\2\2\u017c\u017e\5`\61\2\u017d\u017c\3\2\2\2\u017d\u017e")
        buf.write("\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0180\7\7\2\2\u0180")
        buf.write("\u0181\7\n\2\2\u0181\u018c\3\2\2\2\u0182\u0183\7@\2\2")
        buf.write("\u0183\u0184\7\60\2\2\u0184\u0185\7?\2\2\u0185\u0187\7")
        buf.write("\6\2\2\u0186\u0188\5`\61\2\u0187\u0186\3\2\2\2\u0187\u0188")
        buf.write("\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a\7\7\2\2\u018a")
        buf.write("\u018c\7\n\2\2\u018b\u016f\3\2\2\2\u018b\u0174\3\2\2\2")
        buf.write("\u018b\u0178\3\2\2\2\u018b\u0182\3\2\2\2\u018cE\3\2\2")
        buf.write("\2\u018d\u018e\7\b\2\2\u018e\u018f\5H%\2\u018f\u0190\7")
        buf.write("\t\2\2\u0190G\3\2\2\2\u0191\u0192\5P)\2\u0192\u0193\5")
        buf.write("J&\2\u0193\u0196\3\2\2\2\u0194\u0196\3\2\2\2\u0195\u0191")
        buf.write("\3\2\2\2\u0195\u0194\3\2\2\2\u0196I\3\2\2\2\u0197\u0198")
        buf.write("\5P)\2\u0198\u0199\5J&\2\u0199\u019c\3\2\2\2\u019a\u019c")
        buf.write("\3\2\2\2\u019b\u0197\3\2\2\2\u019b\u019a\3\2\2\2\u019c")
        buf.write("K\3\2\2\2\u019d\u019e\t\7\2\2\u019e\u019f\5N(\2\u019f")
        buf.write("\u01a0\7\f\2\2\u01a0\u01a3\5d\63\2\u01a1\u01a2\7(\2\2")
        buf.write("\u01a2\u01a4\5`\61\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3")
        buf.write("\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a6\7\n\2\2\u01a6M")
        buf.write("\3\2\2\2\u01a7\u01a8\7@\2\2\u01a8\u01a9\5^\60\2\u01a9")
        buf.write("O\3\2\2\2\u01aa\u01b4\5,\27\2\u01ab\u01b4\5\66\34\2\u01ac")
        buf.write("\u01b4\5<\37\2\u01ad\u01b4\5> \2\u01ae\u01b4\5@!\2\u01af")
        buf.write("\u01b4\5B\"\2\u01b0\u01b4\5D#\2\u01b1\u01b4\5L\'\2\u01b2")
        buf.write("\u01b4\5F$\2\u01b3\u01aa\3\2\2\2\u01b3\u01ab\3\2\2\2\u01b3")
        buf.write("\u01ac\3\2\2\2\u01b3\u01ad\3\2\2\2\u01b3\u01ae\3\2\2\2")
        buf.write("\u01b3\u01af\3\2\2\2\u01b3\u01b0\3\2\2\2\u01b3\u01b1\3")
        buf.write("\2\2\2\u01b3\u01b2\3\2\2\2\u01b4Q\3\2\2\2\u01b5\u01b6")
        buf.write("\7\26\2\2\u01b6\u01b9\7@\2\2\u01b7\u01b8\7\f\2\2\u01b8")
        buf.write("\u01ba\7@\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2")
        buf.write("\u01ba\u01bb\3\2\2\2\u01bb\u01bc\7\b\2\2\u01bc\u01bd\5")
        buf.write("T+\2\u01bd\u01be\7\t\2\2\u01beS\3\2\2\2\u01bf\u01c0\5")
        buf.write("Z.\2\u01c0\u01c1\5V,\2\u01c1\u01c7\3\2\2\2\u01c2\u01c3")
        buf.write("\5f\64\2\u01c3\u01c4\5V,\2\u01c4\u01c7\3\2\2\2\u01c5\u01c7")
        buf.write("\3\2\2\2\u01c6\u01bf\3\2\2\2\u01c6\u01c2\3\2\2\2\u01c6")
        buf.write("\u01c5\3\2\2\2\u01c7U\3\2\2\2\u01c8\u01c9\5Z.\2\u01c9")
        buf.write("\u01ca\5V,\2\u01ca\u01d0\3\2\2\2\u01cb\u01cc\5f\64\2\u01cc")
        buf.write("\u01cd\5V,\2\u01cd\u01d0\3\2\2\2\u01ce\u01d0\3\2\2\2\u01cf")
        buf.write("\u01c8\3\2\2\2\u01cf\u01cb\3\2\2\2\u01cf\u01ce\3\2\2\2")
        buf.write("\u01d0W\3\2\2\2\u01d1\u01d2\7\66\2\2\u01d2\u01d3\7\3\2")
        buf.write("\2\u01d3\u01d4\5d\63\2\u01d4\u01d5\7\13\2\2\u01d5\u01d6")
        buf.write("\79\2\2\u01d6\u01d7\7\4\2\2\u01d7Y\3\2\2\2\u01d8\u01d9")
        buf.write("\t\7\2\2\u01d9\u01da\5\\/\2\u01da\u01db\7\f\2\2\u01db")
        buf.write("\u01de\5d\63\2\u01dc\u01dd\7(\2\2\u01dd\u01df\5`\61\2")
        buf.write("\u01de\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e0\3")
        buf.write("\2\2\2\u01e0\u01e1\7\n\2\2\u01e1[\3\2\2\2\u01e2\u01e3")
        buf.write("\t\b\2\2\u01e3\u01e4\5^\60\2\u01e4]\3\2\2\2\u01e5\u01e6")
        buf.write("\7\13\2\2\u01e6\u01e7\t\b\2\2\u01e7\u01ea\5^\60\2\u01e8")
        buf.write("\u01ea\3\2\2\2\u01e9\u01e5\3\2\2\2\u01e9\u01e8\3\2\2\2")
        buf.write("\u01ea_\3\2\2\2\u01eb\u01ec\5\4\3\2\u01ec\u01ed\5b\62")
        buf.write("\2\u01eda\3\2\2\2\u01ee\u01ef\7\13\2\2\u01ef\u01f0\5\4")
        buf.write("\3\2\u01f0\u01f1\5b\62\2\u01f1\u01f4\3\2\2\2\u01f2\u01f4")
        buf.write("\3\2\2\2\u01f3\u01ee\3\2\2\2\u01f3\u01f2\3\2\2\2\u01f4")
        buf.write("c\3\2\2\2\u01f5\u01fc\7\65\2\2\u01f6\u01fc\7\62\2\2\u01f7")
        buf.write("\u01fc\7\63\2\2\u01f8\u01fc\7\64\2\2\u01f9\u01fc\5X-\2")
        buf.write("\u01fa\u01fc\7@\2\2\u01fb\u01f5\3\2\2\2\u01fb\u01f6\3")
        buf.write("\2\2\2\u01fb\u01f7\3\2\2\2\u01fb\u01f8\3\2\2\2\u01fb\u01f9")
        buf.write("\3\2\2\2\u01fb\u01fa\3\2\2\2\u01fce\3\2\2\2\u01fd\u01fe")
        buf.write("\t\b\2\2\u01fe\u01ff\7\6\2\2\u01ff\u0200\5h\65\2\u0200")
        buf.write("\u0201\7\7\2\2\u0201\u0202\5F$\2\u0202\u0206\3\2\2\2\u0203")
        buf.write("\u0206\5r:\2\u0204\u0206\5t;\2\u0205\u01fd\3\2\2\2\u0205")
        buf.write("\u0203\3\2\2\2\u0205\u0204\3\2\2\2\u0206g\3\2\2\2\u0207")
        buf.write("\u0208\5l\67\2\u0208\u0209\5j\66\2\u0209\u020c\3\2\2\2")
        buf.write("\u020a\u020c\3\2\2\2\u020b\u0207\3\2\2\2\u020b\u020a\3")
        buf.write("\2\2\2\u020ci\3\2\2\2\u020d\u020e\7\n\2\2\u020e\u020f")
        buf.write("\5l\67\2\u020f\u0210\5j\66\2\u0210\u0213\3\2\2\2\u0211")
        buf.write("\u0213\3\2\2\2\u0212\u020d\3\2\2\2\u0212\u0211\3\2\2\2")
        buf.write("\u0213k\3\2\2\2\u0214\u0215\5n8\2\u0215\u0216\7\f\2\2")
        buf.write("\u0216\u0217\5d\63\2\u0217m\3\2\2\2\u0218\u0219\7@\2\2")
        buf.write("\u0219\u021c\5p9\2\u021a\u021c\3\2\2\2\u021b\u0218\3\2")
        buf.write("\2\2\u021b\u021a\3\2\2\2\u021co\3\2\2\2\u021d\u021e\7")
        buf.write("\13\2\2\u021e\u021f\7@\2\2\u021f\u0222\5p9\2\u0220\u0222")
        buf.write("\3\2\2\2\u0221\u021d\3\2\2\2\u0221\u0220\3\2\2\2\u0222")
        buf.write("q\3\2\2\2\u0223\u0224\7\31\2\2\u0224\u0225\7\6\2\2\u0225")
        buf.write("\u0226\5h\65\2\u0226\u0227\7\7\2\2\u0227\u0228\5F$\2\u0228")
        buf.write("s\3\2\2\2\u0229\u022a\7\32\2\2\u022a\u022b\7\6\2\2\u022b")
        buf.write("\u022c\7\7\2\2\u022c\u022d\5F$\2\u022du\3\2\2\2/y\u0082")
        buf.write("\u0089\u0094\u00a0\u00ac\u00b2\u00b7\u00c0\u00ce\u00d2")
        buf.write("\u00d4\u00dc\u00e5\u00eb\u00ef\u00fd\u0115\u0122\u0125")
        buf.write("\u012e\u0146\u014c\u0153\u015e\u016b\u017d\u0187\u018b")
        buf.write("\u0195\u019b\u01a3\u01b3\u01b9\u01c6\u01cf\u01de\u01e9")
        buf.write("\u01f3\u01fb\u0205\u020b\u0212\u021b\u0221")
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
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_operations" ):
                return visitor.visitRelational_operations(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_operations" ):
                return visitor.visitLogical_operations(self)
            else:
                return visitor.visitChildren(self)



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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding_operations" ):
                return visitor.visitAdding_operations(self)
            else:
                return visitor.visitChildren(self)



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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying_operations" ):
                return visitor.visitMultiplying_operations(self)
            else:
                return visitor.visitChildren(self)



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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_negate_operation" ):
                return visitor.visitLogical_negate_operation(self)
            else:
                return visitor.visitChildren(self)




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
            elif token in [D96Parser.LB, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.ARRAYTYPE, D96Parser.FLOATLIT, D96Parser.INTLIT, D96Parser.BOOLEANLIT, D96Parser.STRINGLIT, D96Parser.ID]:
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_operations" ):
                return visitor.visitSign_operations(self)
            else:
                return visitor.visitChildren(self)




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
            elif token in [D96Parser.LB, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.ARRAYTYPE, D96Parser.FLOATLIT, D96Parser.INTLIT, D96Parser.BOOLEANLIT, D96Parser.STRINGLIT, D96Parser.ID]:
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operations" ):
                return visitor.visitIndex_operations(self)
            else:
                return visitor.visitChildren(self)



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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntance_access_operarion" ):
                return visitor.visitIntance_access_operarion(self)
            else:
                return visitor.visitChildren(self)



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
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LB) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.MINUS) | (1 << D96Parser.NEGATE) | (1 << D96Parser.ARRAYTYPE) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.INTLIT) | (1 << D96Parser.BOOLEANLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID))) != 0):
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_create_operation(self):
            return self.getTypedRuleContext(D96Parser.Object_create_operationContext,0)


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
            return D96Parser.RULE_static_access_operation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_access_operation" ):
                return visitor.visitStatic_access_operation(self)
            else:
                return visitor.visitChildren(self)




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
                self.match(D96Parser.DOLLARID)
                self.state = 216
                self.match(D96Parser.LB)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LB) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.MINUS) | (1 << D96Parser.NEGATE) | (1 << D96Parser.ARRAYTYPE) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.INTLIT) | (1 << D96Parser.BOOLEANLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID))) != 0):
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
                self.match(D96Parser.DOLLARID)
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_create_operation" ):
                return visitor.visitObject_create_operation(self)
            else:
                return visitor.visitChildren(self)




    def object_create_operation(self):

        localctx = D96Parser.Object_create_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_object_create_operation)
        self._la = 0 # Token type
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.match(D96Parser.NEW)
                self.state = 230
                self.match(D96Parser.ID)
                self.state = 231
                self.match(D96Parser.LB)
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LB) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.MINUS) | (1 << D96Parser.NEGATE) | (1 << D96Parser.ARRAYTYPE) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.INTLIT) | (1 << D96Parser.BOOLEANLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID))) != 0):
                    self.state = 232
                    self.expList()


                self.state = 235
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.LB, D96Parser.NULL, D96Parser.SELF, D96Parser.ARRAYTYPE, D96Parser.FLOATLIT, D96Parser.INTLIT, D96Parser.BOOLEANLIT, D96Parser.STRINGLIT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
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
        __slots__ = 'parser'

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


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_parenthesis_operations

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis_operations" ):
                return visitor.visitParenthesis_operations(self)
            else:
                return visitor.visitChildren(self)




    def parenthesis_operations(self):

        localctx = D96Parser.Parenthesis_operationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parenthesis_operations)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.match(D96Parser.LB)
                self.state = 240
                self.exp()
                self.state = 241
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 244
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.BOOLEANLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 245
                self.match(D96Parser.BOOLEANLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 246
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 247
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.ARRAYTYPE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 248
                self.array_lit()
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 8)
                self.state = 249
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 9)
                self.state = 250
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGCOMPARE(self):
            return self.getToken(D96Parser.STRINGCOMPARE, 0)

        def STRINGCONCAT(self):
            return self.getToken(D96Parser.STRINGCONCAT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_string_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_operators" ):
                return visitor.visitString_operators(self)
            else:
                return visitor.visitChildren(self)




    def string_operators(self):

        localctx = D96Parser.String_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_string_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_operators" ):
                return visitor.visitRelational_operators(self)
            else:
                return visitor.visitChildren(self)




    def relational_operators(self):

        localctx = D96Parser.Relational_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_relational_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_logical_and_or

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_and_or" ):
                return visitor.visitLogical_and_or(self)
            else:
                return visitor.visitChildren(self)




    def logical_and_or(self):

        localctx = D96Parser.Logical_and_orContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_logical_and_or)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(D96Parser.PLUS, 0)

        def MINUS(self):
            return self.getToken(D96Parser.MINUS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_adding_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding_operators" ):
                return visitor.visitAdding_operators(self)
            else:
                return visitor.visitChildren(self)




    def adding_operators(self):

        localctx = D96Parser.Adding_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_adding_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying_operators" ):
                return visitor.visitMultiplying_operators(self)
            else:
                return visitor.visitChildren(self)




    def multiplying_operators(self):

        localctx = D96Parser.Multiplying_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_multiplying_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_element_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_expression" ):
                return visitor.visitElement_expression(self)
            else:
                return visitor.visitChildren(self)




    def element_expression(self):

        localctx = D96Parser.Element_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_element_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.exp()
            self.state = 264
            self.index_operators()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = D96Parser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_index_operators)
        try:
            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(D96Parser.T__0)
                self.state = 267
                self.exp()
                self.state = 268
                self.match(D96Parser.T__1)
                self.state = 269
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.match(D96Parser.T__0)
                self.state = 272
                self.exp()
                self.state = 273
                self.match(D96Parser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = D96Parser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(D96Parser.ARRAYTYPE)
            self.state = 278
            self.match(D96Parser.LB)
            self.state = 279
            self.expList()
            self.state = 280
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statements" ):
                return visitor.visitIf_statements(self)
            else:
                return visitor.visitChildren(self)




    def if_statements(self):

        localctx = D96Parser.If_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_if_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(D96Parser.IF)
            self.state = 283
            self.match(D96Parser.LB)
            self.state = 284
            self.exp()
            self.state = 285
            self.match(D96Parser.RB)
            self.state = 286
            self.block_statements()
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSEIF:
                self.state = 287
                self.else_ifList()


            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 290
                self.else_statements()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_ifListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_if(self):
            return self.getTypedRuleContext(D96Parser.Else_ifContext,0)


        def the_rest_else_if(self):
            return self.getTypedRuleContext(D96Parser.The_rest_else_ifContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_ifList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_ifList" ):
                return visitor.visitElse_ifList(self)
            else:
                return visitor.visitChildren(self)




    def else_ifList(self):

        localctx = D96Parser.Else_ifListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_else_ifList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.else_if()
            self.state = 294
            self.the_rest_else_if()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class The_rest_else_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_if(self):
            return self.getTypedRuleContext(D96Parser.Else_ifContext,0)


        def the_rest_else_if(self):
            return self.getTypedRuleContext(D96Parser.The_rest_else_ifContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_the_rest_else_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThe_rest_else_if" ):
                return visitor.visitThe_rest_else_if(self)
            else:
                return visitor.visitChildren(self)




    def the_rest_else_if(self):

        localctx = D96Parser.The_rest_else_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_the_rest_else_if)
        try:
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.else_if()
                self.state = 297
                self.the_rest_else_if()
                pass
            elif token in [D96Parser.LB, D96Parser.LP, D96Parser.RP, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.ELSE, D96Parser.FOREACH, D96Parser.RETURN, D96Parser.NULL, D96Parser.VAL, D96Parser.VAR, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.NEGATE, D96Parser.ARRAYTYPE, D96Parser.FLOATLIT, D96Parser.INTLIT, D96Parser.BOOLEANLIT, D96Parser.STRINGLIT, D96Parser.ID]:
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if" ):
                return visitor.visitElse_if(self)
            else:
                return visitor.visitChildren(self)




    def else_if(self):

        localctx = D96Parser.Else_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_else_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(D96Parser.ELSEIF)
            self.state = 303
            self.match(D96Parser.LB)
            self.state = 304
            self.exp()
            self.state = 305
            self.match(D96Parser.RB)
            self.state = 306
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statements" ):
                return visitor.visitElse_statements(self)
            else:
                return visitor.visitChildren(self)




    def else_statements(self):

        localctx = D96Parser.Else_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_else_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(D96Parser.ELSE)
            self.state = 309
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statements" ):
                return visitor.visitAssignment_statements(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statements(self):

        localctx = D96Parser.Assignment_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assignment_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.lhs(0)
            self.state = 312
            self.match(D96Parser.ASSIGN)
            self.state = 313
            self.exp()
            self.state = 314
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)



    def lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.LhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.assignment_static_access()
            self._ctx.stop = self._input.LT(-1)
            self.state = 324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.LhsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                    self.state = 319
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 320
                    self.match(D96Parser.DOT)
                    self.state = 321
                    self.assignment_static_access() 
                self.state = 326
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC_ACCESS(self):
            return self.getToken(D96Parser.STATIC_ACCESS, 0)

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def index_operations(self):
            return self.getTypedRuleContext(D96Parser.Index_operationsContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assignment_static_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_static_access" ):
                return visitor.visitAssignment_static_access(self)
            else:
                return visitor.visitChildren(self)




    def assignment_static_access(self):

        localctx = D96Parser.Assignment_static_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_assignment_static_access)
        try:
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 327
                    self.match(D96Parser.ID)
                    pass

                elif la_ == 2:
                    self.state = 328
                    self.index_operations(0)
                    pass

                elif la_ == 3:
                    self.state = 329
                    self.match(D96Parser.SELF)
                    pass


                self.state = 332
                self.match(D96Parser.STATIC_ACCESS)
                self.state = 333
                self.match(D96Parser.DOLLARID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 335
                self.index_operations(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 336
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForeach_statements" ):
                return visitor.visitForeach_statements(self)
            else:
                return visitor.visitChildren(self)




    def foreach_statements(self):

        localctx = D96Parser.Foreach_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_foreach_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(D96Parser.FOREACH)
            self.state = 340
            self.match(D96Parser.LB)
            self.state = 341
            self.match(D96Parser.ID)
            self.state = 342
            self.match(D96Parser.IN)
            self.state = 343
            self.exp()
            self.state = 344
            self.match(D96Parser.T__2)
            self.state = 345
            self.exp()
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 346
                self.match(D96Parser.BY)
                self.state = 347
                self.exp()


            self.state = 350
            self.match(D96Parser.RB)
            self.state = 351
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statements" ):
                return visitor.visitBreak_statements(self)
            else:
                return visitor.visitChildren(self)




    def break_statements(self):

        localctx = D96Parser.Break_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_break_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(D96Parser.BREAK)
            self.state = 354
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statements" ):
                return visitor.visitContinue_statements(self)
            else:
                return visitor.visitChildren(self)




    def continue_statements(self):

        localctx = D96Parser.Continue_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_continue_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.match(D96Parser.CONTINUE)
            self.state = 357
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statements" ):
                return visitor.visitReturn_statements(self)
            else:
                return visitor.visitChildren(self)




    def return_statements(self):

        localctx = D96Parser.Return_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_return_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(D96Parser.RETURN)
            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LB) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.MINUS) | (1 << D96Parser.NEGATE) | (1 << D96Parser.ARRAYTYPE) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.INTLIT) | (1 << D96Parser.BOOLEANLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID))) != 0):
                self.state = 360
                self.exp()


            self.state = 363
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocationsContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocations" ):
                return visitor.visitMethod_invocations(self)
            else:
                return visitor.visitChildren(self)




    def method_invocations(self):

        localctx = D96Parser.Method_invocationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_method_invocations)
        self._la = 0 # Token type
        try:
            self.state = 393
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.exp()
                self.state = 366
                self.match(D96Parser.DOT)
                self.state = 367
                self.match(D96Parser.ID)
                self.state = 368
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.match(D96Parser.ID)
                self.state = 371
                self.match(D96Parser.STATIC_ACCESS)
                self.state = 372
                self.match(D96Parser.DOLLARID)
                self.state = 373
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 374
                self.exp()
                self.state = 375
                self.match(D96Parser.DOT)
                self.state = 376
                self.match(D96Parser.ID)
                self.state = 377
                self.match(D96Parser.LB)
                self.state = 379
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LB) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.MINUS) | (1 << D96Parser.NEGATE) | (1 << D96Parser.ARRAYTYPE) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.INTLIT) | (1 << D96Parser.BOOLEANLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID))) != 0):
                    self.state = 378
                    self.expList()


                self.state = 381
                self.match(D96Parser.RB)
                self.state = 382
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 384
                self.match(D96Parser.ID)
                self.state = 385
                self.match(D96Parser.STATIC_ACCESS)
                self.state = 386
                self.match(D96Parser.DOLLARID)
                self.state = 387
                self.match(D96Parser.LB)
                self.state = 389
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LB) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.MINUS) | (1 << D96Parser.NEGATE) | (1 << D96Parser.ARRAYTYPE) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.INTLIT) | (1 << D96Parser.BOOLEANLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID))) != 0):
                    self.state = 388
                    self.expList()


                self.state = 391
                self.match(D96Parser.RB)
                self.state = 392
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statements" ):
                return visitor.visitBlock_statements(self)
            else:
                return visitor.visitChildren(self)




    def block_statements(self):

        localctx = D96Parser.Block_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_block_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(D96Parser.LP)
            self.state = 396
            self.list_statement()
            self.state = 397
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_statement(self):
            return self.getTypedRuleContext(D96Parser.Single_statementContext,0)


        def the_rest_statements(self):
            return self.getTypedRuleContext(D96Parser.The_rest_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement" ):
                return visitor.visitList_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_statement(self):

        localctx = D96Parser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_list_statement)
        try:
            self.state = 403
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB, D96Parser.LP, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.RETURN, D96Parser.NULL, D96Parser.VAL, D96Parser.VAR, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.NEGATE, D96Parser.ARRAYTYPE, D96Parser.FLOATLIT, D96Parser.INTLIT, D96Parser.BOOLEANLIT, D96Parser.STRINGLIT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.single_statement()
                self.state = 400
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_statement(self):
            return self.getTypedRuleContext(D96Parser.Single_statementContext,0)


        def the_rest_statements(self):
            return self.getTypedRuleContext(D96Parser.The_rest_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_the_rest_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThe_rest_statements" ):
                return visitor.visitThe_rest_statements(self)
            else:
                return visitor.visitChildren(self)




    def the_rest_statements(self):

        localctx = D96Parser.The_rest_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_the_rest_statements)
        try:
            self.state = 409
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB, D96Parser.LP, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.RETURN, D96Parser.NULL, D96Parser.VAL, D96Parser.VAR, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.NEGATE, D96Parser.ARRAYTYPE, D96Parser.FLOATLIT, D96Parser.INTLIT, D96Parser.BOOLEANLIT, D96Parser.STRINGLIT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.single_statement()
                self.state = 406
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_constant_declaration" ):
                return visitor.visitVariable_constant_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_constant_declaration(self):

        localctx = D96Parser.Variable_constant_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_variable_constant_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 412
            self.variableList()
            self.state = 413
            self.match(D96Parser.COLON)
            self.state = 414
            self.primitive_type()
            self.state = 417
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 415
                self.match(D96Parser.ASSIGN)
                self.state = 416
                self.expList()


            self.state = 419
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def iDlist(self):
            return self.getTypedRuleContext(D96Parser.IDlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_variableList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableList" ):
                return visitor.visitVariableList(self)
            else:
                return visitor.visitChildren(self)




    def variableList(self):

        localctx = D96Parser.VariableListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_variableList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(D96Parser.ID)
            self.state = 422
            self.iDlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_statementContext(ParserRuleContext):
        __slots__ = 'parser'

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


        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_single_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle_statement" ):
                return visitor.visitSingle_statement(self)
            else:
                return visitor.visitChildren(self)




    def single_statement(self):

        localctx = D96Parser.Single_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_single_statement)
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.if_statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                self.assignment_statements()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 426
                self.foreach_statements()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 427
                self.break_statements()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 428
                self.continue_statements()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 429
                self.return_statements()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 430
                self.method_invocations()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 431
                self.variable_constant_declaration()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 432
                self.block_statements()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declaration" ):
                return visitor.visitClass_declaration(self)
            else:
                return visitor.visitChildren(self)




    def class_declaration(self):

        localctx = D96Parser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(D96Parser.CLASS)
            self.state = 436
            self.match(D96Parser.ID)
            self.state = 439
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 437
                self.match(D96Parser.COLON)
                self.state = 438
                self.match(D96Parser.ID)


            self.state = 441
            self.match(D96Parser.LP)
            self.state = 442
            self.attributes_methods_declarations()
            self.state = 443
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attributes_methods_declarationsContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributes_methods_declarations" ):
                return visitor.visitAttributes_methods_declarations(self)
            else:
                return visitor.visitChildren(self)




    def attributes_methods_declarations(self):

        localctx = D96Parser.Attributes_methods_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_attributes_methods_declarations)
        try:
            self.state = 452
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
                self.attribute_declaration()
                self.state = 446
                self.the_rest_attributes_methods_declarations()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.DOLLARID, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.method_declaration()
                self.state = 449
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThe_rest_attributes_methods_declarations" ):
                return visitor.visitThe_rest_attributes_methods_declarations(self)
            else:
                return visitor.visitChildren(self)




    def the_rest_attributes_methods_declarations(self):

        localctx = D96Parser.The_rest_attributes_methods_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_the_rest_attributes_methods_declarations)
        try:
            self.state = 461
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 454
                self.attribute_declaration()
                self.state = 455
                self.the_rest_attributes_methods_declarations()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.DOLLARID, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
                self.method_declaration()
                self.state = 458
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDeclaration" ):
                return visitor.visitArrayDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def arrayDeclaration(self):

        localctx = D96Parser.ArrayDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_arrayDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.match(D96Parser.ARRAYTYPE)
            self.state = 464
            self.match(D96Parser.T__0)
            self.state = 465
            self.primitive_type()
            self.state = 466
            self.match(D96Parser.COMMA)
            self.state = 467
            self.match(D96Parser.INTLIT)
            self.state = 468
            self.match(D96Parser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_declaration" ):
                return visitor.visitAttribute_declaration(self)
            else:
                return visitor.visitChildren(self)




    def attribute_declaration(self):

        localctx = D96Parser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 471
            self.attributesList()
            self.state = 472
            self.match(D96Parser.COLON)
            self.state = 473
            self.primitive_type()
            self.state = 476
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 474
                self.match(D96Parser.ASSIGN)
                self.state = 475
                self.expList()


            self.state = 478
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributesListContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributesList" ):
                return visitor.visitAttributesList(self)
            else:
                return visitor.visitChildren(self)




    def attributesList(self):

        localctx = D96Parser.AttributesListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_attributesList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            _la = self._input.LA(1)
            if not(_la==D96Parser.DOLLARID or _la==D96Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 481
            self.iDlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IDlistContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIDlist" ):
                return visitor.visitIDlist(self)
            else:
                return visitor.visitChildren(self)




    def iDlist(self):

        localctx = D96Parser.IDlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_iDlist)
        self._la = 0 # Token type
        try:
            self.state = 487
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 483
                self.match(D96Parser.COMMA)
                self.state = 484
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOLLARID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 485
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def theRestExp(self):
            return self.getTypedRuleContext(D96Parser.TheRestExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpList" ):
                return visitor.visitExpList(self)
            else:
                return visitor.visitChildren(self)




    def expList(self):

        localctx = D96Parser.ExpListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.exp()
            self.state = 490
            self.theRestExp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TheRestExpContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTheRestExp" ):
                return visitor.visitTheRestExp(self)
            else:
                return visitor.visitChildren(self)




    def theRestExp(self):

        localctx = D96Parser.TheRestExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_theRestExp)
        try:
            self.state = 497
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 492
                self.match(D96Parser.COMMA)
                self.state = 493
                self.exp()
                self.state = 494
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = D96Parser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_primitive_type)
        try:
            self.state = 505
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLEANTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                self.match(D96Parser.BOOLEANTYPE)
                pass
            elif token in [D96Parser.INTTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 500
                self.match(D96Parser.INTTYPE)
                pass
            elif token in [D96Parser.FLOATTYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 501
                self.match(D96Parser.FLOATTYPE)
                pass
            elif token in [D96Parser.STRINGTYPE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 502
                self.match(D96Parser.STRINGTYPE)
                pass
            elif token in [D96Parser.ARRAYTYPE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 503
                self.arrayDeclaration()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 504
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declaration" ):
                return visitor.visitMethod_declaration(self)
            else:
                return visitor.visitChildren(self)




    def method_declaration(self):

        localctx = D96Parser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.state = 515
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.DOLLARID, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 507
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOLLARID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 508
                self.match(D96Parser.LB)
                self.state = 509
                self.list_parameters()
                self.state = 510
                self.match(D96Parser.RB)
                self.state = 511
                self.block_statements()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 513
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 514
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameters_declaration(self):
            return self.getTypedRuleContext(D96Parser.Parameters_declarationContext,0)


        def the_rest_parameters_declarations(self):
            return self.getTypedRuleContext(D96Parser.The_rest_parameters_declarationsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_parameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_parameters" ):
                return visitor.visitList_parameters(self)
            else:
                return visitor.visitChildren(self)




    def list_parameters(self):

        localctx = D96Parser.List_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_list_parameters)
        try:
            self.state = 521
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 517
                self.parameters_declaration()
                self.state = 518
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThe_rest_parameters_declarations" ):
                return visitor.visitThe_rest_parameters_declarations(self)
            else:
                return visitor.visitChildren(self)




    def the_rest_parameters_declarations(self):

        localctx = D96Parser.The_rest_parameters_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_the_rest_parameters_declarations)
        try:
            self.state = 528
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SEMI]:
                self.enterOuterAlt(localctx, 1)
                self.state = 523
                self.match(D96Parser.SEMI)
                self.state = 524
                self.parameters_declaration()
                self.state = 525
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters_declaration" ):
                return visitor.visitParameters_declaration(self)
            else:
                return visitor.visitChildren(self)




    def parameters_declaration(self):

        localctx = D96Parser.Parameters_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_parameters_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.same_type_parameters()
            self.state = 531
            self.match(D96Parser.COLON)
            self.state = 532
            self.primitive_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Same_type_parametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def the_rest_ID(self):
            return self.getTypedRuleContext(D96Parser.The_rest_IDContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_same_type_parameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSame_type_parameters" ):
                return visitor.visitSame_type_parameters(self)
            else:
                return visitor.visitChildren(self)




    def same_type_parameters(self):

        localctx = D96Parser.Same_type_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_same_type_parameters)
        try:
            self.state = 537
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 534
                self.match(D96Parser.ID)
                self.state = 535
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThe_rest_ID" ):
                return visitor.visitThe_rest_ID(self)
            else:
                return visitor.visitChildren(self)




    def the_rest_ID(self):

        localctx = D96Parser.The_rest_IDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_the_rest_ID)
        try:
            self.state = 543
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 539
                self.match(D96Parser.COMMA)
                self.state = 540
                self.match(D96Parser.ID)
                self.state = 541
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 546
            self.match(D96Parser.LB)
            self.state = 547
            self.list_parameters()
            self.state = 548
            self.match(D96Parser.RB)
            self.state = 549
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor" ):
                return visitor.visitDestructor(self)
            else:
                return visitor.visitChildren(self)




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 551
            self.match(D96Parser.DESTRUCTOR)
            self.state = 552
            self.match(D96Parser.LB)
            self.state = 553
            self.match(D96Parser.RB)
            self.state = 554
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
         




