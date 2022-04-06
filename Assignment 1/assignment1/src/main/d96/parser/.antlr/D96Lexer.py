# Generated from c:\Users\ADMIN\Desktop\Learning\Principle of Programming Languages\Code\Code\Assignment 1\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u0244\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\7\35\u010f\n\35\f\35\16")
        buf.write("\35\u0112\13\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3")
        buf.write("&\3&\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3*\3+\3+\3,\3,\3,\3")
        buf.write("-\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\67\3\67\7\67\u016f\n\67\f\67\16\67\u0172\13\67\38\3")
        buf.write("8\58\u0176\n8\38\68\u0179\n8\r8\168\u017a\39\39\39\39")
        buf.write("\39\39\39\39\39\39\39\39\39\39\39\39\59\u018d\n9\3:\3")
        buf.write(":\3:\3:\3:\7:\u0194\n:\f:\16:\u0197\13:\3:\3:\5:\u019b")
        buf.write("\n:\3;\3;\3;\3;\5;\u01a1\n;\3;\3;\3;\3;\7;\u01a7\n;\f")
        buf.write(";\16;\u01aa\13;\3;\3;\3;\3;\5;\u01b0\n;\3;\5;\u01b3\n")
        buf.write(";\3<\3<\3<\3<\5<\u01b9\n<\3<\3<\3<\3<\7<\u01bf\n<\f<\16")
        buf.write("<\u01c2\13<\3<\3<\3<\3<\5<\u01c8\n<\3<\5<\u01cb\n<\3=")
        buf.write("\3=\3=\3=\3=\7=\u01d2\n=\f=\16=\u01d5\13=\5=\u01d7\n=")
        buf.write("\3>\3>\3>\3>\5>\u01dd\n>\3>\3>\3?\6?\u01e2\n?\r?\16?\u01e3")
        buf.write("\3?\3?\3@\3@\3@\3@\3@\3@\3@\3@\3@\5@\u01f1\n@\3A\3A\3")
        buf.write("A\7A\u01f6\nA\fA\16A\u01f9\13A\3A\3A\3A\3A\5A\u01ff\n")
        buf.write("A\3A\3A\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3")
        buf.write("B\5B\u0213\nB\3C\3C\3C\7C\u0218\nC\fC\16C\u021b\13C\3")
        buf.write("C\3C\3C\3D\3D\3D\7D\u0223\nD\fD\16D\u0226\13D\3D\3D\3")
        buf.write("D\3E\3E\6E\u022d\nE\rE\16E\u022e\3E\7E\u0232\nE\fE\16")
        buf.write("E\u0235\13E\3F\6F\u0238\nF\rF\16F\u0239\3F\7F\u023d\n")
        buf.write("F\fF\16F\u0240\13F\3G\3G\3G\3\u0110\2H\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m\2o\2q8s\2u\2w\2y\2{9}:\177")
        buf.write(";\u0081<\u0083\2\u0085=\u0087>\u0089?\u008b@\u008dA\3")
        buf.write("\2\23\3\2\62;\4\2GGgg\4\2--//\3\2\639\3\2\629\3\2\62\62")
        buf.write("\4\2\63;CH\4\2\62;CH\3\2\63\63\3\2\62\63\3\2\63;\5\2\13")
        buf.write("\f\17\17\"\"\4\2$$^^\t\2))^^ddhhppttvv\3\2$$\5\2C\\aa")
        buf.write("c|\6\2\62;C\\aac|\2\u026a\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2q\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\3\u008f\3\2\2\2\5\u0091")
        buf.write("\3\2\2\2\7\u0093\3\2\2\2\t\u0096\3\2\2\2\13\u0098\3\2")
        buf.write("\2\2\r\u009a\3\2\2\2\17\u009c\3\2\2\2\21\u009e\3\2\2\2")
        buf.write("\23\u00a0\3\2\2\2\25\u00a2\3\2\2\2\27\u00a4\3\2\2\2\31")
        buf.write("\u00aa\3\2\2\2\33\u00b3\3\2\2\2\35\u00b6\3\2\2\2\37\u00bd")
        buf.write("\3\2\2\2!\u00c2\3\2\2\2#\u00ca\3\2\2\2%\u00cd\3\2\2\2")
        buf.write("\'\u00d4\3\2\2\2)\u00d9\3\2\2\2+\u00df\3\2\2\2-\u00e3")
        buf.write("\3\2\2\2/\u00e7\3\2\2\2\61\u00f3\3\2\2\2\63\u00fe\3\2")
        buf.write("\2\2\65\u0102\3\2\2\2\67\u0105\3\2\2\29\u010a\3\2\2\2")
        buf.write(";\u0118\3\2\2\2=\u011a\3\2\2\2?\u011c\3\2\2\2A\u011e\3")
        buf.write("\2\2\2C\u0120\3\2\2\2E\u0122\3\2\2\2G\u0124\3\2\2\2I\u0127")
        buf.write("\3\2\2\2K\u012a\3\2\2\2M\u012d\3\2\2\2O\u012f\3\2\2\2")
        buf.write("Q\u0132\3\2\2\2S\u0134\3\2\2\2U\u0137\3\2\2\2W\u0139\3")
        buf.write("\2\2\2Y\u013c\3\2\2\2[\u0140\3\2\2\2]\u0143\3\2\2\2_\u0146")
        buf.write("\3\2\2\2a\u0148\3\2\2\2c\u014c\3\2\2\2e\u0152\3\2\2\2")
        buf.write("g\u0159\3\2\2\2i\u0161\3\2\2\2k\u0167\3\2\2\2m\u016c\3")
        buf.write("\2\2\2o\u0173\3\2\2\2q\u018c\3\2\2\2s\u019a\3\2\2\2u\u01b2")
        buf.write("\3\2\2\2w\u01ca\3\2\2\2y\u01d6\3\2\2\2{\u01dc\3\2\2\2")
        buf.write("}\u01e1\3\2\2\2\177\u01f0\3\2\2\2\u0081\u01f2\3\2\2\2")
        buf.write("\u0083\u0212\3\2\2\2\u0085\u0214\3\2\2\2\u0087\u021f\3")
        buf.write("\2\2\2\u0089\u022a\3\2\2\2\u008b\u0237\3\2\2\2\u008d\u0241")
        buf.write("\3\2\2\2\u008f\u0090\7]\2\2\u0090\4\3\2\2\2\u0091\u0092")
        buf.write("\7_\2\2\u0092\6\3\2\2\2\u0093\u0094\7\60\2\2\u0094\u0095")
        buf.write("\7\60\2\2\u0095\b\3\2\2\2\u0096\u0097\7*\2\2\u0097\n\3")
        buf.write("\2\2\2\u0098\u0099\7+\2\2\u0099\f\3\2\2\2\u009a\u009b")
        buf.write("\7}\2\2\u009b\16\3\2\2\2\u009c\u009d\7\177\2\2\u009d\20")
        buf.write("\3\2\2\2\u009e\u009f\7=\2\2\u009f\22\3\2\2\2\u00a0\u00a1")
        buf.write("\7.\2\2\u00a1\24\3\2\2\2\u00a2\u00a3\7<\2\2\u00a3\26\3")
        buf.write("\2\2\2\u00a4\u00a5\7D\2\2\u00a5\u00a6\7t\2\2\u00a6\u00a7")
        buf.write("\7g\2\2\u00a7\u00a8\7c\2\2\u00a8\u00a9\7m\2\2\u00a9\30")
        buf.write("\3\2\2\2\u00aa\u00ab\7E\2\2\u00ab\u00ac\7q\2\2\u00ac\u00ad")
        buf.write("\7p\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af\7k\2\2\u00af\u00b0")
        buf.write("\7p\2\2\u00b0\u00b1\7w\2\2\u00b1\u00b2\7g\2\2\u00b2\32")
        buf.write("\3\2\2\2\u00b3\u00b4\7K\2\2\u00b4\u00b5\7h\2\2\u00b5\34")
        buf.write("\3\2\2\2\u00b6\u00b7\7G\2\2\u00b7\u00b8\7n\2\2\u00b8\u00b9")
        buf.write("\7u\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb\7k\2\2\u00bb\u00bc")
        buf.write("\7h\2\2\u00bc\36\3\2\2\2\u00bd\u00be\7G\2\2\u00be\u00bf")
        buf.write("\7n\2\2\u00bf\u00c0\7u\2\2\u00c0\u00c1\7g\2\2\u00c1 \3")
        buf.write("\2\2\2\u00c2\u00c3\7H\2\2\u00c3\u00c4\7q\2\2\u00c4\u00c5")
        buf.write("\7t\2\2\u00c5\u00c6\7g\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8")
        buf.write("\7e\2\2\u00c8\u00c9\7j\2\2\u00c9\"\3\2\2\2\u00ca\u00cb")
        buf.write("\7K\2\2\u00cb\u00cc\7p\2\2\u00cc$\3\2\2\2\u00cd\u00ce")
        buf.write("\7T\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0\7v\2\2\u00d0\u00d1")
        buf.write("\7w\2\2\u00d1\u00d2\7t\2\2\u00d2\u00d3\7p\2\2\u00d3&\3")
        buf.write("\2\2\2\u00d4\u00d5\7P\2\2\u00d5\u00d6\7w\2\2\u00d6\u00d7")
        buf.write("\7n\2\2\u00d7\u00d8\7n\2\2\u00d8(\3\2\2\2\u00d9\u00da")
        buf.write("\7E\2\2\u00da\u00db\7n\2\2\u00db\u00dc\7c\2\2\u00dc\u00dd")
        buf.write("\7u\2\2\u00dd\u00de\7u\2\2\u00de*\3\2\2\2\u00df\u00e0")
        buf.write("\7X\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2\7n\2\2\u00e2,\3")
        buf.write("\2\2\2\u00e3\u00e4\7X\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6")
        buf.write("\7t\2\2\u00e6.\3\2\2\2\u00e7\u00e8\7E\2\2\u00e8\u00e9")
        buf.write("\7q\2\2\u00e9\u00ea\7p\2\2\u00ea\u00eb\7u\2\2\u00eb\u00ec")
        buf.write("\7v\2\2\u00ec\u00ed\7t\2\2\u00ed\u00ee\7w\2\2\u00ee\u00ef")
        buf.write("\7e\2\2\u00ef\u00f0\7v\2\2\u00f0\u00f1\7q\2\2\u00f1\u00f2")
        buf.write("\7t\2\2\u00f2\60\3\2\2\2\u00f3\u00f4\7F\2\2\u00f4\u00f5")
        buf.write("\7g\2\2\u00f5\u00f6\7u\2\2\u00f6\u00f7\7v\2\2\u00f7\u00f8")
        buf.write("\7t\2\2\u00f8\u00f9\7w\2\2\u00f9\u00fa\7e\2\2\u00fa\u00fb")
        buf.write("\7v\2\2\u00fb\u00fc\7q\2\2\u00fc\u00fd\7t\2\2\u00fd\62")
        buf.write("\3\2\2\2\u00fe\u00ff\7P\2\2\u00ff\u0100\7g\2\2\u0100\u0101")
        buf.write("\7y\2\2\u0101\64\3\2\2\2\u0102\u0103\7D\2\2\u0103\u0104")
        buf.write("\7{\2\2\u0104\66\3\2\2\2\u0105\u0106\7U\2\2\u0106\u0107")
        buf.write("\7g\2\2\u0107\u0108\7n\2\2\u0108\u0109\7h\2\2\u01098\3")
        buf.write("\2\2\2\u010a\u010b\7%\2\2\u010b\u010c\7%\2\2\u010c\u0110")
        buf.write("\3\2\2\2\u010d\u010f\13\2\2\2\u010e\u010d\3\2\2\2\u010f")
        buf.write("\u0112\3\2\2\2\u0110\u0111\3\2\2\2\u0110\u010e\3\2\2\2")
        buf.write("\u0111\u0113\3\2\2\2\u0112\u0110\3\2\2\2\u0113\u0114\7")
        buf.write("%\2\2\u0114\u0115\7%\2\2\u0115\u0116\3\2\2\2\u0116\u0117")
        buf.write("\b\35\2\2\u0117:\3\2\2\2\u0118\u0119\7-\2\2\u0119<\3\2")
        buf.write("\2\2\u011a\u011b\7/\2\2\u011b>\3\2\2\2\u011c\u011d\7,")
        buf.write("\2\2\u011d@\3\2\2\2\u011e\u011f\7\61\2\2\u011fB\3\2\2")
        buf.write("\2\u0120\u0121\7\'\2\2\u0121D\3\2\2\2\u0122\u0123\7#\2")
        buf.write("\2\u0123F\3\2\2\2\u0124\u0125\7(\2\2\u0125\u0126\7(\2")
        buf.write("\2\u0126H\3\2\2\2\u0127\u0128\7~\2\2\u0128\u0129\7~\2")
        buf.write("\2\u0129J\3\2\2\2\u012a\u012b\7?\2\2\u012b\u012c\7?\2")
        buf.write("\2\u012cL\3\2\2\2\u012d\u012e\7?\2\2\u012eN\3\2\2\2\u012f")
        buf.write("\u0130\7#\2\2\u0130\u0131\7?\2\2\u0131P\3\2\2\2\u0132")
        buf.write("\u0133\7@\2\2\u0133R\3\2\2\2\u0134\u0135\7>\2\2\u0135")
        buf.write("\u0136\7?\2\2\u0136T\3\2\2\2\u0137\u0138\7>\2\2\u0138")
        buf.write("V\3\2\2\2\u0139\u013a\7@\2\2\u013a\u013b\7?\2\2\u013b")
        buf.write("X\3\2\2\2\u013c\u013d\7?\2\2\u013d\u013e\7?\2\2\u013e")
        buf.write("\u013f\7\60\2\2\u013fZ\3\2\2\2\u0140\u0141\7-\2\2\u0141")
        buf.write("\u0142\7\60\2\2\u0142\\\3\2\2\2\u0143\u0144\7<\2\2\u0144")
        buf.write("\u0145\7<\2\2\u0145^\3\2\2\2\u0146\u0147\7\60\2\2\u0147")
        buf.write("`\3\2\2\2\u0148\u0149\7K\2\2\u0149\u014a\7p\2\2\u014a")
        buf.write("\u014b\7v\2\2\u014bb\3\2\2\2\u014c\u014d\7H\2\2\u014d")
        buf.write("\u014e\7n\2\2\u014e\u014f\7q\2\2\u014f\u0150\7c\2\2\u0150")
        buf.write("\u0151\7v\2\2\u0151d\3\2\2\2\u0152\u0153\7U\2\2\u0153")
        buf.write("\u0154\7v\2\2\u0154\u0155\7t\2\2\u0155\u0156\7k\2\2\u0156")
        buf.write("\u0157\7p\2\2\u0157\u0158\7i\2\2\u0158f\3\2\2\2\u0159")
        buf.write("\u015a\7D\2\2\u015a\u015b\7q\2\2\u015b\u015c\7q\2\2\u015c")
        buf.write("\u015d\7n\2\2\u015d\u015e\7g\2\2\u015e\u015f\7c\2\2\u015f")
        buf.write("\u0160\7p\2\2\u0160h\3\2\2\2\u0161\u0162\7C\2\2\u0162")
        buf.write("\u0163\7t\2\2\u0163\u0164\7t\2\2\u0164\u0165\7c\2\2\u0165")
        buf.write("\u0166\7{\2\2\u0166j\3\2\2\2\u0167\u0168\7X\2\2\u0168")
        buf.write("\u0169\7q\2\2\u0169\u016a\7k\2\2\u016a\u016b\7f\2\2\u016b")
        buf.write("l\3\2\2\2\u016c\u0170\7\60\2\2\u016d\u016f\t\2\2\2\u016e")
        buf.write("\u016d\3\2\2\2\u016f\u0172\3\2\2\2\u0170\u016e\3\2\2\2")
        buf.write("\u0170\u0171\3\2\2\2\u0171n\3\2\2\2\u0172\u0170\3\2\2")
        buf.write("\2\u0173\u0175\t\3\2\2\u0174\u0176\t\4\2\2\u0175\u0174")
        buf.write("\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0178\3\2\2\2\u0177")
        buf.write("\u0179\t\2\2\2\u0178\u0177\3\2\2\2\u0179\u017a\3\2\2\2")
        buf.write("\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017bp\3\2\2")
        buf.write("\2\u017c\u017d\5y=\2\u017d\u017e\5m\67\2\u017e\u017f\5")
        buf.write("o8\2\u017f\u0180\b9\3\2\u0180\u018d\3\2\2\2\u0181\u0182")
        buf.write("\5y=\2\u0182\u0183\5o8\2\u0183\u0184\b9\4\2\u0184\u018d")
        buf.write("\3\2\2\2\u0185\u0186\5m\67\2\u0186\u0187\5o8\2\u0187\u018d")
        buf.write("\3\2\2\2\u0188\u0189\5y=\2\u0189\u018a\5m\67\2\u018a\u018b")
        buf.write("\b9\5\2\u018b\u018d\3\2\2\2\u018c\u017c\3\2\2\2\u018c")
        buf.write("\u0181\3\2\2\2\u018c\u0185\3\2\2\2\u018c\u0188\3\2\2\2")
        buf.write("\u018dr\3\2\2\2\u018e\u018f\7\62\2\2\u018f\u0195\t\5\2")
        buf.write("\2\u0190\u0194\t\6\2\2\u0191\u0192\7a\2\2\u0192\u0194")
        buf.write("\t\5\2\2\u0193\u0190\3\2\2\2\u0193\u0191\3\2\2\2\u0194")
        buf.write("\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196\3\2\2\2")
        buf.write("\u0196\u019b\3\2\2\2\u0197\u0195\3\2\2\2\u0198\u0199\7")
        buf.write("\62\2\2\u0199\u019b\t\7\2\2\u019a\u018e\3\2\2\2\u019a")
        buf.write("\u0198\3\2\2\2\u019bt\3\2\2\2\u019c\u019d\7\62\2\2\u019d")
        buf.write("\u01a1\7z\2\2\u019e\u019f\7\62\2\2\u019f\u01a1\7Z\2\2")
        buf.write("\u01a0\u019c\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1\u01a2\3")
        buf.write("\2\2\2\u01a2\u01a8\t\b\2\2\u01a3\u01a7\t\t\2\2\u01a4\u01a5")
        buf.write("\7a\2\2\u01a5\u01a7\t\t\2\2\u01a6\u01a3\3\2\2\2\u01a6")
        buf.write("\u01a4\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6\3\2\2\2")
        buf.write("\u01a8\u01a9\3\2\2\2\u01a9\u01b3\3\2\2\2\u01aa\u01a8\3")
        buf.write("\2\2\2\u01ab\u01ac\7\62\2\2\u01ac\u01b0\7z\2\2\u01ad\u01ae")
        buf.write("\7\62\2\2\u01ae\u01b0\7Z\2\2\u01af\u01ab\3\2\2\2\u01af")
        buf.write("\u01ad\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b3\t\7\2\2")
        buf.write("\u01b2\u01a0\3\2\2\2\u01b2\u01af\3\2\2\2\u01b3v\3\2\2")
        buf.write("\2\u01b4\u01b5\7\62\2\2\u01b5\u01b9\7d\2\2\u01b6\u01b7")
        buf.write("\7\62\2\2\u01b7\u01b9\7D\2\2\u01b8\u01b4\3\2\2\2\u01b8")
        buf.write("\u01b6\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01c0\t\n\2\2")
        buf.write("\u01bb\u01bf\t\13\2\2\u01bc\u01bd\7a\2\2\u01bd\u01bf\t")
        buf.write("\13\2\2\u01be\u01bb\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf")
        buf.write("\u01c2\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2")
        buf.write("\u01c1\u01cb\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3\u01c4\7")
        buf.write("\62\2\2\u01c4\u01c8\7d\2\2\u01c5\u01c6\7\62\2\2\u01c6")
        buf.write("\u01c8\7D\2\2\u01c7\u01c3\3\2\2\2\u01c7\u01c5\3\2\2\2")
        buf.write("\u01c8\u01c9\3\2\2\2\u01c9\u01cb\t\7\2\2\u01ca\u01b8\3")
        buf.write("\2\2\2\u01ca\u01c7\3\2\2\2\u01cbx\3\2\2\2\u01cc\u01d7")
        buf.write("\7\62\2\2\u01cd\u01d3\t\f\2\2\u01ce\u01d2\t\2\2\2\u01cf")
        buf.write("\u01d0\7a\2\2\u01d0\u01d2\t\2\2\2\u01d1\u01ce\3\2\2\2")
        buf.write("\u01d1\u01cf\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3\u01d1\3")
        buf.write("\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5\u01d3")
        buf.write("\3\2\2\2\u01d6\u01cc\3\2\2\2\u01d6\u01cd\3\2\2\2\u01d7")
        buf.write("z\3\2\2\2\u01d8\u01dd\5s:\2\u01d9\u01dd\5u;\2\u01da\u01dd")
        buf.write("\5w<\2\u01db\u01dd\5y=\2\u01dc\u01d8\3\2\2\2\u01dc\u01d9")
        buf.write("\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc\u01db\3\2\2\2\u01dd")
        buf.write("\u01de\3\2\2\2\u01de\u01df\b>\6\2\u01df|\3\2\2\2\u01e0")
        buf.write("\u01e2\t\r\2\2\u01e1\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2")
        buf.write("\u01e3\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e5\3")
        buf.write("\2\2\2\u01e5\u01e6\b?\2\2\u01e6~\3\2\2\2\u01e7\u01e8\7")
        buf.write("H\2\2\u01e8\u01e9\7c\2\2\u01e9\u01ea\7n\2\2\u01ea\u01eb")
        buf.write("\7u\2\2\u01eb\u01f1\7g\2\2\u01ec\u01ed\7V\2\2\u01ed\u01ee")
        buf.write("\7t\2\2\u01ee\u01ef\7w\2\2\u01ef\u01f1\7g\2\2\u01f0\u01e7")
        buf.write("\3\2\2\2\u01f0\u01ec\3\2\2\2\u01f1\u0080\3\2\2\2\u01f2")
        buf.write("\u01f7\7$\2\2\u01f3\u01f6\n\16\2\2\u01f4\u01f6\5\u0083")
        buf.write("B\2\u01f5\u01f3\3\2\2\2\u01f5\u01f4\3\2\2\2\u01f6\u01f9")
        buf.write("\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8")
        buf.write("\u01fe\3\2\2\2\u01f9\u01f7\3\2\2\2\u01fa\u01fb\7^\2\2")
        buf.write("\u01fb\u01ff\n\17\2\2\u01fc\u01fd\7)\2\2\u01fd\u01ff\n")
        buf.write("\20\2\2\u01fe\u01fa\3\2\2\2\u01fe\u01fc\3\2\2\2\u01ff")
        buf.write("\u0200\3\2\2\2\u0200\u0201\bA\7\2\u0201\u0082\3\2\2\2")
        buf.write("\u0202\u0203\7^\2\2\u0203\u0213\7d\2\2\u0204\u0205\7^")
        buf.write("\2\2\u0205\u0213\7h\2\2\u0206\u0207\7^\2\2\u0207\u0213")
        buf.write("\7t\2\2\u0208\u0209\7^\2\2\u0209\u0213\7p\2\2\u020a\u020b")
        buf.write("\7^\2\2\u020b\u0213\7v\2\2\u020c\u020d\7^\2\2\u020d\u0213")
        buf.write("\7)\2\2\u020e\u020f\7^\2\2\u020f\u0213\7^\2\2\u0210\u0211")
        buf.write("\7)\2\2\u0211\u0213\7$\2\2\u0212\u0202\3\2\2\2\u0212\u0204")
        buf.write("\3\2\2\2\u0212\u0206\3\2\2\2\u0212\u0208\3\2\2\2\u0212")
        buf.write("\u020a\3\2\2\2\u0212\u020c\3\2\2\2\u0212\u020e\3\2\2\2")
        buf.write("\u0212\u0210\3\2\2\2\u0213\u0084\3\2\2\2\u0214\u0219\7")
        buf.write("$\2\2\u0215\u0218\5\u0083B\2\u0216\u0218\n\16\2\2\u0217")
        buf.write("\u0215\3\2\2\2\u0217\u0216\3\2\2\2\u0218\u021b\3\2\2\2")
        buf.write("\u0219\u0217\3\2\2\2\u0219\u021a\3\2\2\2\u021a\u021c\3")
        buf.write("\2\2\2\u021b\u0219\3\2\2\2\u021c\u021d\7$\2\2\u021d\u021e")
        buf.write("\bC\b\2\u021e\u0086\3\2\2\2\u021f\u0224\7$\2\2\u0220\u0223")
        buf.write("\5\u0083B\2\u0221\u0223\n\16\2\2\u0222\u0220\3\2\2\2\u0222")
        buf.write("\u0221\3\2\2\2\u0223\u0226\3\2\2\2\u0224\u0222\3\2\2\2")
        buf.write("\u0224\u0225\3\2\2\2\u0225\u0227\3\2\2\2\u0226\u0224\3")
        buf.write("\2\2\2\u0227\u0228\7\2\2\3\u0228\u0229\bD\t\2\u0229\u0088")
        buf.write("\3\2\2\2\u022a\u022c\7&\2\2\u022b\u022d\t\21\2\2\u022c")
        buf.write("\u022b\3\2\2\2\u022d\u022e\3\2\2\2\u022e\u022c\3\2\2\2")
        buf.write("\u022e\u022f\3\2\2\2\u022f\u0233\3\2\2\2\u0230\u0232\t")
        buf.write("\22\2\2\u0231\u0230\3\2\2\2\u0232\u0235\3\2\2\2\u0233")
        buf.write("\u0231\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u008a\3\2\2\2")
        buf.write("\u0235\u0233\3\2\2\2\u0236\u0238\t\21\2\2\u0237\u0236")
        buf.write("\3\2\2\2\u0238\u0239\3\2\2\2\u0239\u0237\3\2\2\2\u0239")
        buf.write("\u023a\3\2\2\2\u023a\u023e\3\2\2\2\u023b\u023d\t\22\2")
        buf.write("\2\u023c\u023b\3\2\2\2\u023d\u0240\3\2\2\2\u023e\u023c")
        buf.write("\3\2\2\2\u023e\u023f\3\2\2\2\u023f\u008c\3\2\2\2\u0240")
        buf.write("\u023e\3\2\2\2\u0241\u0242\13\2\2\2\u0242\u0243\bG\n\2")
        buf.write("\u0243\u008e\3\2\2\2\'\2\u0110\u0170\u0175\u017a\u018c")
        buf.write("\u0193\u0195\u019a\u01a0\u01a6\u01a8\u01af\u01b2\u01b8")
        buf.write("\u01be\u01c0\u01c7\u01ca\u01d1\u01d3\u01d6\u01dc\u01e3")
        buf.write("\u01f0\u01f5\u01f7\u01fe\u0212\u0217\u0219\u0222\u0224")
        buf.write("\u022e\u0233\u0239\u023e\13\b\2\2\39\2\39\3\39\4\3>\5")
        buf.write("\3A\6\3C\7\3D\b\3G\t")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    LB = 4
    RB = 5
    LP = 6
    RP = 7
    SEMI = 8
    COMMA = 9
    COLON = 10
    BREAK = 11
    CONTINUE = 12
    IF = 13
    ELSEIF = 14
    ELSE = 15
    FOREACH = 16
    IN = 17
    RETURN = 18
    NULL = 19
    CLASS = 20
    VAL = 21
    VAR = 22
    CONSTRUCTOR = 23
    DESTRUCTOR = 24
    NEW = 25
    BY = 26
    SELF = 27
    BlockComment = 28
    PLUS = 29
    MINUS = 30
    MULTIPLY = 31
    DIVIDE = 32
    MODULO = 33
    NEGATE = 34
    AND = 35
    OR = 36
    EQUAL = 37
    ASSIGN = 38
    DIFFERENT = 39
    GREATER = 40
    LESSTHANEQUAL = 41
    LESSER = 42
    GREATERTHANEQUAL = 43
    STRINGCOMPARE = 44
    STRINGCONCAT = 45
    STATIC_ACCESS = 46
    DOT = 47
    INTTYPE = 48
    FLOATTYPE = 49
    STRINGTYPE = 50
    BOOLEANTYPE = 51
    ARRAYTYPE = 52
    VOIDTYPE = 53
    FLOATLIT = 54
    INTLIT = 55
    WS = 56
    BOOLEANLIT = 57
    ILLEGAL_ESCAPE = 58
    STRINGLIT = 59
    UNCLOSE_STRING = 60
    DOLLARID = 61
    ID = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "'..'", "'('", "')'", "'{'", "'}'", "';'", "','", 
            "':'", "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", 
            "'Foreach'", "'In'", "'Return'", "'Null'", "'Class'", "'Val'", 
            "'Var'", "'Constructor'", "'Destructor'", "'New'", "'By'", "'Self'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'='", "'!='", "'>'", "'<='", "'<'", "'>='", "'==.'", "'+.'", 
            "'::'", "'.'", "'Int'", "'Float'", "'String'", "'Boolean'", 
            "'Array'", "'Void'" ]

    symbolicNames = [ "<INVALID>",
            "LB", "RB", "LP", "RP", "SEMI", "COMMA", "COLON", "BREAK", "CONTINUE", 
            "IF", "ELSEIF", "ELSE", "FOREACH", "IN", "RETURN", "NULL", "CLASS", 
            "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "SELF", 
            "BlockComment", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MODULO", 
            "NEGATE", "AND", "OR", "EQUAL", "ASSIGN", "DIFFERENT", "GREATER", 
            "LESSTHANEQUAL", "LESSER", "GREATERTHANEQUAL", "STRINGCOMPARE", 
            "STRINGCONCAT", "STATIC_ACCESS", "DOT", "INTTYPE", "FLOATTYPE", 
            "STRINGTYPE", "BOOLEANTYPE", "ARRAYTYPE", "VOIDTYPE", "FLOATLIT", 
            "INTLIT", "WS", "BOOLEANLIT", "ILLEGAL_ESCAPE", "STRINGLIT", 
            "UNCLOSE_STRING", "DOLLARID", "ID", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "LB", "RB", "LP", "RP", "SEMI", 
                  "COMMA", "COLON", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                  "ELSE", "FOREACH", "IN", "RETURN", "NULL", "CLASS", "VAL", 
                  "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "SELF", 
                  "BlockComment", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", 
                  "MODULO", "NEGATE", "AND", "OR", "EQUAL", "ASSIGN", "DIFFERENT", 
                  "GREATER", "LESSTHANEQUAL", "LESSER", "GREATERTHANEQUAL", 
                  "STRINGCOMPARE", "STRINGCONCAT", "STATIC_ACCESS", "DOT", 
                  "INTTYPE", "FLOATTYPE", "STRINGTYPE", "BOOLEANTYPE", "ARRAYTYPE", 
                  "VOIDTYPE", "DECIMALPART", "EXPONENTPART", "FLOATLIT", 
                  "OCT", "HEX", "BIN", "DEC", "INTLIT", "WS", "BOOLEANLIT", 
                  "ILLEGAL_ESCAPE", "EscapeSequence", "STRINGLIT", "UNCLOSE_STRING", 
                  "DOLLARID", "ID", "ERROR_CHAR" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[55] = self.FLOATLIT_action 
            actions[60] = self.INTLIT_action 
            actions[63] = self.ILLEGAL_ESCAPE_action 
            actions[65] = self.STRINGLIT_action 
            actions[66] = self.UNCLOSE_STRING_action 
            actions[69] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_","")
     

        if actionIndex == 1:
            self.text = self.text.replace("_","")
     

        if actionIndex == 2:
            self.text = self.text.replace("_","")
     

    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text.replace("_", "")
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise IllegalEscape(self.text[1:])
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise UncloseString(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            raise ErrorToken(self.text)
     


