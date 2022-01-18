# Generated from c:\Users\ADMIN\Desktop\Learning\Principle of Programming Languages\Code\Code\Assignment 1\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u0242\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u010f\n\34\f\34\16")
        buf.write("\34\u0112\13\34\3\34\3\34\3\35\3\35\3\35\3\35\7\35\u011a")
        buf.write("\n\35\f\35\16\35\u011d\13\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3")
        buf.write("$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3*\3")
        buf.write("+\3+\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\66\3\66\6\66\u0178\n\66\r\66\16\66\u0179\3\66")
        buf.write("\7\66\u017d\n\66\f\66\16\66\u0180\13\66\3\67\3\67\5\67")
        buf.write("\u0184\n\67\3\67\6\67\u0187\n\67\r\67\16\67\u0188\3\67")
        buf.write("\7\67\u018c\n\67\f\67\16\67\u018f\13\67\3\67\3\67\5\67")
        buf.write("\u0193\n\67\3\67\5\67\u0196\n\67\38\38\38\38\38\38\38")
        buf.write("\38\38\38\38\38\38\38\38\38\38\58\u01a9\n8\39\39\69\u01ad")
        buf.write("\n9\r9\169\u01ae\39\79\u01b2\n9\f9\169\u01b5\139\3:\3")
        buf.write(":\3:\3:\5:\u01bb\n:\3:\6:\u01be\n:\r:\16:\u01bf\3:\7:")
        buf.write("\u01c3\n:\f:\16:\u01c6\13:\3;\3;\3;\3;\5;\u01cc\n;\3;")
        buf.write("\6;\u01cf\n;\r;\16;\u01d0\3;\7;\u01d4\n;\f;\16;\u01d7")
        buf.write("\13;\3<\3<\6<\u01db\n<\r<\16<\u01dc\3<\7<\u01e0\n<\f<")
        buf.write("\16<\u01e3\13<\5<\u01e5\n<\3=\3=\3=\3=\5=\u01eb\n=\3=")
        buf.write("\3=\3>\6>\u01f0\n>\r>\16>\u01f1\3>\3>\3?\3?\3?\3?\3?\3")
        buf.write("?\3?\3?\3?\5?\u01ff\n?\3@\3@\3@\3@\7@\u0205\n@\f@\16@")
        buf.write("\u0208\13@\3@\3@\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3")
        buf.write("A\3A\3A\3A\5A\u021c\nA\3B\3B\3B\7B\u0221\nB\fB\16B\u0224")
        buf.write("\13B\3B\3B\3C\3C\3C\7C\u022b\nC\fC\16C\u022e\13C\3C\3")
        buf.write("C\3C\3D\6D\u0234\nD\rD\16D\u0235\3D\7D\u0239\nD\fD\16")
        buf.write("D\u023c\13D\3E\3E\3F\3F\3F\4\u0110\u011b\2G\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\2m\2o\67q\2s\2u\2w\2")
        buf.write("y8{9}:\177;\u0081\2\u0083<\u0085=\u0087>\u0089?\u008b")
        buf.write("@\3\2\25\3\2\61\61\3\2%%\3\2\62;\4\2\62;aa\4\2GGgg\4\2")
        buf.write("--//\3\2\63;\3\2\62\62\3\2\639\4\2\629aa\4\2\63;CH\5\2")
        buf.write("\62;CHaa\4\2\62\63aa\5\2\13\f\17\17\"\"\n\2$$))^^ddhh")
        buf.write("ppttvv\3\2^^\3\2$$\5\2C\\aac|\6\2\62;C\\aac|\2\u0266\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2o\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}")
        buf.write("\3\2\2\2\2\177\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2")
        buf.write("\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\3\u008d")
        buf.write("\3\2\2\2\5\u0092\3\2\2\2\7\u0094\3\2\2\2\t\u0096\3\2\2")
        buf.write("\2\13\u0098\3\2\2\2\r\u009a\3\2\2\2\17\u009c\3\2\2\2\21")
        buf.write("\u009e\3\2\2\2\23\u00a0\3\2\2\2\25\u00a6\3\2\2\2\27\u00af")
        buf.write("\3\2\2\2\31\u00b2\3\2\2\2\33\u00b9\3\2\2\2\35\u00be\3")
        buf.write("\2\2\2\37\u00c6\3\2\2\2!\u00c9\3\2\2\2#\u00d0\3\2\2\2")
        buf.write("%\u00d5\3\2\2\2\'\u00db\3\2\2\2)\u00df\3\2\2\2+\u00e3")
        buf.write("\3\2\2\2-\u00ef\3\2\2\2/\u00fa\3\2\2\2\61\u00fe\3\2\2")
        buf.write("\2\63\u0101\3\2\2\2\65\u0106\3\2\2\2\67\u0108\3\2\2\2")
        buf.write("9\u0115\3\2\2\2;\u0123\3\2\2\2=\u0125\3\2\2\2?\u0127\3")
        buf.write("\2\2\2A\u0129\3\2\2\2C\u012b\3\2\2\2E\u012d\3\2\2\2G\u012f")
        buf.write("\3\2\2\2I\u0132\3\2\2\2K\u0135\3\2\2\2M\u0138\3\2\2\2")
        buf.write("O\u013a\3\2\2\2Q\u013d\3\2\2\2S\u013f\3\2\2\2U\u0142\3")
        buf.write("\2\2\2W\u0144\3\2\2\2Y\u0147\3\2\2\2[\u014b\3\2\2\2]\u014e")
        buf.write("\3\2\2\2_\u0151\3\2\2\2a\u0155\3\2\2\2c\u015b\3\2\2\2")
        buf.write("e\u0162\3\2\2\2g\u016a\3\2\2\2i\u0170\3\2\2\2k\u0175\3")
        buf.write("\2\2\2m\u0195\3\2\2\2o\u01a8\3\2\2\2q\u01aa\3\2\2\2s\u01ba")
        buf.write("\3\2\2\2u\u01cb\3\2\2\2w\u01e4\3\2\2\2y\u01ea\3\2\2\2")
        buf.write("{\u01ef\3\2\2\2}\u01fe\3\2\2\2\177\u0200\3\2\2\2\u0081")
        buf.write("\u021b\3\2\2\2\u0083\u021d\3\2\2\2\u0085\u0227\3\2\2\2")
        buf.write("\u0087\u0233\3\2\2\2\u0089\u023d\3\2\2\2\u008b\u023f\3")
        buf.write("\2\2\2\u008d\u008e\7o\2\2\u008e\u008f\7c\2\2\u008f\u0090")
        buf.write("\7k\2\2\u0090\u0091\7p\2\2\u0091\4\3\2\2\2\u0092\u0093")
        buf.write("\7*\2\2\u0093\6\3\2\2\2\u0094\u0095\7+\2\2\u0095\b\3\2")
        buf.write("\2\2\u0096\u0097\7}\2\2\u0097\n\3\2\2\2\u0098\u0099\7")
        buf.write("\177\2\2\u0099\f\3\2\2\2\u009a\u009b\7=\2\2\u009b\16\3")
        buf.write("\2\2\2\u009c\u009d\7.\2\2\u009d\20\3\2\2\2\u009e\u009f")
        buf.write("\7<\2\2\u009f\22\3\2\2\2\u00a0\u00a1\7D\2\2\u00a1\u00a2")
        buf.write("\7t\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4\7c\2\2\u00a4\u00a5")
        buf.write("\7m\2\2\u00a5\24\3\2\2\2\u00a6\u00a7\7E\2\2\u00a7\u00a8")
        buf.write("\7q\2\2\u00a8\u00a9\7p\2\2\u00a9\u00aa\7v\2\2\u00aa\u00ab")
        buf.write("\7k\2\2\u00ab\u00ac\7p\2\2\u00ac\u00ad\7w\2\2\u00ad\u00ae")
        buf.write("\7g\2\2\u00ae\26\3\2\2\2\u00af\u00b0\7K\2\2\u00b0\u00b1")
        buf.write("\7h\2\2\u00b1\30\3\2\2\2\u00b2\u00b3\7G\2\2\u00b3\u00b4")
        buf.write("\7n\2\2\u00b4\u00b5\7u\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7")
        buf.write("\7k\2\2\u00b7\u00b8\7h\2\2\u00b8\32\3\2\2\2\u00b9\u00ba")
        buf.write("\7G\2\2\u00ba\u00bb\7n\2\2\u00bb\u00bc\7u\2\2\u00bc\u00bd")
        buf.write("\7g\2\2\u00bd\34\3\2\2\2\u00be\u00bf\7H\2\2\u00bf\u00c0")
        buf.write("\7q\2\2\u00c0\u00c1\7t\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3")
        buf.write("\7c\2\2\u00c3\u00c4\7e\2\2\u00c4\u00c5\7j\2\2\u00c5\36")
        buf.write("\3\2\2\2\u00c6\u00c7\7K\2\2\u00c7\u00c8\7p\2\2\u00c8 ")
        buf.write("\3\2\2\2\u00c9\u00ca\7T\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc")
        buf.write("\7v\2\2\u00cc\u00cd\7w\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf")
        buf.write("\7p\2\2\u00cf\"\3\2\2\2\u00d0\u00d1\7P\2\2\u00d1\u00d2")
        buf.write("\7w\2\2\u00d2\u00d3\7n\2\2\u00d3\u00d4\7n\2\2\u00d4$\3")
        buf.write("\2\2\2\u00d5\u00d6\7E\2\2\u00d6\u00d7\7n\2\2\u00d7\u00d8")
        buf.write("\7c\2\2\u00d8\u00d9\7u\2\2\u00d9\u00da\7u\2\2\u00da&\3")
        buf.write("\2\2\2\u00db\u00dc\7X\2\2\u00dc\u00dd\7c\2\2\u00dd\u00de")
        buf.write("\7n\2\2\u00de(\3\2\2\2\u00df\u00e0\7X\2\2\u00e0\u00e1")
        buf.write("\7c\2\2\u00e1\u00e2\7t\2\2\u00e2*\3\2\2\2\u00e3\u00e4")
        buf.write("\7E\2\2\u00e4\u00e5\7q\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7")
        buf.write("\7u\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9\7t\2\2\u00e9\u00ea")
        buf.write("\7w\2\2\u00ea\u00eb\7e\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed")
        buf.write("\7q\2\2\u00ed\u00ee\7t\2\2\u00ee,\3\2\2\2\u00ef\u00f0")
        buf.write("\7F\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2\7u\2\2\u00f2\u00f3")
        buf.write("\7v\2\2\u00f3\u00f4\7t\2\2\u00f4\u00f5\7w\2\2\u00f5\u00f6")
        buf.write("\7e\2\2\u00f6\u00f7\7v\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9")
        buf.write("\7t\2\2\u00f9.\3\2\2\2\u00fa\u00fb\7P\2\2\u00fb\u00fc")
        buf.write("\7g\2\2\u00fc\u00fd\7y\2\2\u00fd\60\3\2\2\2\u00fe\u00ff")
        buf.write("\7D\2\2\u00ff\u0100\7{\2\2\u0100\62\3\2\2\2\u0101\u0102")
        buf.write("\7U\2\2\u0102\u0103\7g\2\2\u0103\u0104\7n\2\2\u0104\u0105")
        buf.write("\7h\2\2\u0105\64\3\2\2\2\u0106\u0107\7&\2\2\u0107\66\3")
        buf.write("\2\2\2\u0108\u0109\7%\2\2\u0109\u010a\7%\2\2\u010a\u0110")
        buf.write("\3\2\2\2\u010b\u010c\7%\2\2\u010c\u010f\n\2\2\2\u010d")
        buf.write("\u010f\n\3\2\2\u010e\u010b\3\2\2\2\u010e\u010d\3\2\2\2")
        buf.write("\u010f\u0112\3\2\2\2\u0110\u0111\3\2\2\2\u0110\u010e\3")
        buf.write("\2\2\2\u0111\u0113\3\2\2\2\u0112\u0110\3\2\2\2\u0113\u0114")
        buf.write("\7\2\2\3\u01148\3\2\2\2\u0115\u0116\7%\2\2\u0116\u0117")
        buf.write("\7%\2\2\u0117\u011b\3\2\2\2\u0118\u011a\13\2\2\2\u0119")
        buf.write("\u0118\3\2\2\2\u011a\u011d\3\2\2\2\u011b\u011c\3\2\2\2")
        buf.write("\u011b\u0119\3\2\2\2\u011c\u011e\3\2\2\2\u011d\u011b\3")
        buf.write("\2\2\2\u011e\u011f\7%\2\2\u011f\u0120\7%\2\2\u0120\u0121")
        buf.write("\3\2\2\2\u0121\u0122\b\35\2\2\u0122:\3\2\2\2\u0123\u0124")
        buf.write("\7-\2\2\u0124<\3\2\2\2\u0125\u0126\7/\2\2\u0126>\3\2\2")
        buf.write("\2\u0127\u0128\7,\2\2\u0128@\3\2\2\2\u0129\u012a\7\61")
        buf.write("\2\2\u012aB\3\2\2\2\u012b\u012c\7\'\2\2\u012cD\3\2\2\2")
        buf.write("\u012d\u012e\7#\2\2\u012eF\3\2\2\2\u012f\u0130\7(\2\2")
        buf.write("\u0130\u0131\7(\2\2\u0131H\3\2\2\2\u0132\u0133\7~\2\2")
        buf.write("\u0133\u0134\7~\2\2\u0134J\3\2\2\2\u0135\u0136\7?\2\2")
        buf.write("\u0136\u0137\7?\2\2\u0137L\3\2\2\2\u0138\u0139\7?\2\2")
        buf.write("\u0139N\3\2\2\2\u013a\u013b\7#\2\2\u013b\u013c\7?\2\2")
        buf.write("\u013cP\3\2\2\2\u013d\u013e\7@\2\2\u013eR\3\2\2\2\u013f")
        buf.write("\u0140\7>\2\2\u0140\u0141\7?\2\2\u0141T\3\2\2\2\u0142")
        buf.write("\u0143\7>\2\2\u0143V\3\2\2\2\u0144\u0145\7@\2\2\u0145")
        buf.write("\u0146\7?\2\2\u0146X\3\2\2\2\u0147\u0148\7?\2\2\u0148")
        buf.write("\u0149\7?\2\2\u0149\u014a\7\60\2\2\u014aZ\3\2\2\2\u014b")
        buf.write("\u014c\7-\2\2\u014c\u014d\7\60\2\2\u014d\\\3\2\2\2\u014e")
        buf.write("\u014f\7<\2\2\u014f\u0150\7<\2\2\u0150^\3\2\2\2\u0151")
        buf.write("\u0152\7K\2\2\u0152\u0153\7p\2\2\u0153\u0154\7v\2\2\u0154")
        buf.write("`\3\2\2\2\u0155\u0156\7H\2\2\u0156\u0157\7n\2\2\u0157")
        buf.write("\u0158\7q\2\2\u0158\u0159\7c\2\2\u0159\u015a\7v\2\2\u015a")
        buf.write("b\3\2\2\2\u015b\u015c\7U\2\2\u015c\u015d\7v\2\2\u015d")
        buf.write("\u015e\7t\2\2\u015e\u015f\7k\2\2\u015f\u0160\7p\2\2\u0160")
        buf.write("\u0161\7i\2\2\u0161d\3\2\2\2\u0162\u0163\7D\2\2\u0163")
        buf.write("\u0164\7q\2\2\u0164\u0165\7q\2\2\u0165\u0166\7n\2\2\u0166")
        buf.write("\u0167\7g\2\2\u0167\u0168\7c\2\2\u0168\u0169\7p\2\2\u0169")
        buf.write("f\3\2\2\2\u016a\u016b\7C\2\2\u016b\u016c\7t\2\2\u016c")
        buf.write("\u016d\7t\2\2\u016d\u016e\7c\2\2\u016e\u016f\7{\2\2\u016f")
        buf.write("h\3\2\2\2\u0170\u0171\7x\2\2\u0171\u0172\7q\2\2\u0172")
        buf.write("\u0173\7k\2\2\u0173\u0174\7f\2\2\u0174j\3\2\2\2\u0175")
        buf.write("\u0177\7\60\2\2\u0176\u0178\t\4\2\2\u0177\u0176\3\2\2")
        buf.write("\2\u0178\u0179\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u017a")
        buf.write("\3\2\2\2\u017a\u017e\3\2\2\2\u017b\u017d\t\5\2\2\u017c")
        buf.write("\u017b\3\2\2\2\u017d\u0180\3\2\2\2\u017e\u017c\3\2\2\2")
        buf.write("\u017e\u017f\3\2\2\2\u017fl\3\2\2\2\u0180\u017e\3\2\2")
        buf.write("\2\u0181\u0183\t\6\2\2\u0182\u0184\t\7\2\2\u0183\u0182")
        buf.write("\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0186\3\2\2\2\u0185")
        buf.write("\u0187\t\b\2\2\u0186\u0185\3\2\2\2\u0187\u0188\3\2\2\2")
        buf.write("\u0188\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018d\3")
        buf.write("\2\2\2\u018a\u018c\t\5\2\2\u018b\u018a\3\2\2\2\u018c\u018f")
        buf.write("\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e")
        buf.write("\u0196\3\2\2\2\u018f\u018d\3\2\2\2\u0190\u0192\t\6\2\2")
        buf.write("\u0191\u0193\t\7\2\2\u0192\u0191\3\2\2\2\u0192\u0193\3")
        buf.write("\2\2\2\u0193\u0194\3\2\2\2\u0194\u0196\t\t\2\2\u0195\u0181")
        buf.write("\3\2\2\2\u0195\u0190\3\2\2\2\u0196n\3\2\2\2\u0197\u0198")
        buf.write("\5w<\2\u0198\u0199\5k\66\2\u0199\u019a\5m\67\2\u019a\u019b")
        buf.write("\b8\3\2\u019b\u01a9\3\2\2\2\u019c\u019d\5w<\2\u019d\u019e")
        buf.write("\5m\67\2\u019e\u019f\b8\4\2\u019f\u01a9\3\2\2\2\u01a0")
        buf.write("\u01a1\5k\66\2\u01a1\u01a2\5m\67\2\u01a2\u01a3\b8\5\2")
        buf.write("\u01a3\u01a9\3\2\2\2\u01a4\u01a5\5w<\2\u01a5\u01a6\5k")
        buf.write("\66\2\u01a6\u01a7\b8\6\2\u01a7\u01a9\3\2\2\2\u01a8\u0197")
        buf.write("\3\2\2\2\u01a8\u019c\3\2\2\2\u01a8\u01a0\3\2\2\2\u01a8")
        buf.write("\u01a4\3\2\2\2\u01a9p\3\2\2\2\u01aa\u01ac\7\62\2\2\u01ab")
        buf.write("\u01ad\t\n\2\2\u01ac\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2")
        buf.write("\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b3\3")
        buf.write("\2\2\2\u01b0\u01b2\t\13\2\2\u01b1\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b5\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2")
        buf.write("\u01b4r\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b6\u01b7\7\62\2")
        buf.write("\2\u01b7\u01bb\7z\2\2\u01b8\u01b9\7\62\2\2\u01b9\u01bb")
        buf.write("\7Z\2\2\u01ba\u01b6\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb")
        buf.write("\u01bd\3\2\2\2\u01bc\u01be\t\f\2\2\u01bd\u01bc\3\2\2\2")
        buf.write("\u01be\u01bf\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3")
        buf.write("\2\2\2\u01c0\u01c4\3\2\2\2\u01c1\u01c3\t\r\2\2\u01c2\u01c1")
        buf.write("\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4")
        buf.write("\u01c5\3\2\2\2\u01c5t\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7")
        buf.write("\u01c8\7\62\2\2\u01c8\u01cc\7d\2\2\u01c9\u01ca\7\62\2")
        buf.write("\2\u01ca\u01cc\7D\2\2\u01cb\u01c7\3\2\2\2\u01cb\u01c9")
        buf.write("\3\2\2\2\u01cc\u01ce\3\2\2\2\u01cd\u01cf\7\63\2\2\u01ce")
        buf.write("\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01ce\3\2\2\2")
        buf.write("\u01d0\u01d1\3\2\2\2\u01d1\u01d5\3\2\2\2\u01d2\u01d4\t")
        buf.write("\16\2\2\u01d3\u01d2\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5")
        buf.write("\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6v\3\2\2\2\u01d7")
        buf.write("\u01d5\3\2\2\2\u01d8\u01e5\7\62\2\2\u01d9\u01db\t\b\2")
        buf.write("\2\u01da\u01d9\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01da")
        buf.write("\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01e1\3\2\2\2\u01de")
        buf.write("\u01e0\t\5\2\2\u01df\u01de\3\2\2\2\u01e0\u01e3\3\2\2\2")
        buf.write("\u01e1\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e5\3")
        buf.write("\2\2\2\u01e3\u01e1\3\2\2\2\u01e4\u01d8\3\2\2\2\u01e4\u01da")
        buf.write("\3\2\2\2\u01e5x\3\2\2\2\u01e6\u01eb\5q9\2\u01e7\u01eb")
        buf.write("\5s:\2\u01e8\u01eb\5u;\2\u01e9\u01eb\5w<\2\u01ea\u01e6")
        buf.write("\3\2\2\2\u01ea\u01e7\3\2\2\2\u01ea\u01e8\3\2\2\2\u01ea")
        buf.write("\u01e9\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01ed\b=\7\2")
        buf.write("\u01edz\3\2\2\2\u01ee\u01f0\t\17\2\2\u01ef\u01ee\3\2\2")
        buf.write("\2\u01f0\u01f1\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f1\u01f2")
        buf.write("\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f4\b>\2\2\u01f4")
        buf.write("|\3\2\2\2\u01f5\u01f6\7H\2\2\u01f6\u01f7\7c\2\2\u01f7")
        buf.write("\u01f8\7n\2\2\u01f8\u01f9\7u\2\2\u01f9\u01ff\7g\2\2\u01fa")
        buf.write("\u01fb\7V\2\2\u01fb\u01fc\7t\2\2\u01fc\u01fd\7w\2\2\u01fd")
        buf.write("\u01ff\7g\2\2\u01fe\u01f5\3\2\2\2\u01fe\u01fa\3\2\2\2")
        buf.write("\u01ff~\3\2\2\2\u0200\u0206\7$\2\2\u0201\u0202\7^\2\2")
        buf.write("\u0202\u0205\n\20\2\2\u0203\u0205\n\21\2\2\u0204\u0201")
        buf.write("\3\2\2\2\u0204\u0203\3\2\2\2\u0205\u0208\3\2\2\2\u0206")
        buf.write("\u0204\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0209\3\2\2\2")
        buf.write("\u0208\u0206\3\2\2\2\u0209\u020a\b@\b\2\u020a\u0080\3")
        buf.write("\2\2\2\u020b\u020c\7^\2\2\u020c\u021c\7d\2\2\u020d\u020e")
        buf.write("\7^\2\2\u020e\u021c\7h\2\2\u020f\u0210\7^\2\2\u0210\u021c")
        buf.write("\7t\2\2\u0211\u0212\7^\2\2\u0212\u021c\7p\2\2\u0213\u0214")
        buf.write("\7^\2\2\u0214\u021c\7v\2\2\u0215\u0216\7^\2\2\u0216\u021c")
        buf.write("\7)\2\2\u0217\u0218\7^\2\2\u0218\u021c\7^\2\2\u0219\u021a")
        buf.write("\7)\2\2\u021a\u021c\7$\2\2\u021b\u020b\3\2\2\2\u021b\u020d")
        buf.write("\3\2\2\2\u021b\u020f\3\2\2\2\u021b\u0211\3\2\2\2\u021b")
        buf.write("\u0213\3\2\2\2\u021b\u0215\3\2\2\2\u021b\u0217\3\2\2\2")
        buf.write("\u021b\u0219\3\2\2\2\u021c\u0082\3\2\2\2\u021d\u0222\7")
        buf.write("$\2\2\u021e\u0221\5\u0081A\2\u021f\u0221\n\22\2\2\u0220")
        buf.write("\u021e\3\2\2\2\u0220\u021f\3\2\2\2\u0221\u0224\3\2\2\2")
        buf.write("\u0222\u0220\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0225\3")
        buf.write("\2\2\2\u0224\u0222\3\2\2\2\u0225\u0226\7$\2\2\u0226\u0084")
        buf.write("\3\2\2\2\u0227\u022c\7$\2\2\u0228\u022b\5\u0081A\2\u0229")
        buf.write("\u022b\n\22\2\2\u022a\u0228\3\2\2\2\u022a\u0229\3\2\2")
        buf.write("\2\u022b\u022e\3\2\2\2\u022c\u022a\3\2\2\2\u022c\u022d")
        buf.write("\3\2\2\2\u022d\u022f\3\2\2\2\u022e\u022c\3\2\2\2\u022f")
        buf.write("\u0230\7\2\2\3\u0230\u0231\bC\t\2\u0231\u0086\3\2\2\2")
        buf.write("\u0232\u0234\t\23\2\2\u0233\u0232\3\2\2\2\u0234\u0235")
        buf.write("\3\2\2\2\u0235\u0233\3\2\2\2\u0235\u0236\3\2\2\2\u0236")
        buf.write("\u023a\3\2\2\2\u0237\u0239\t\24\2\2\u0238\u0237\3\2\2")
        buf.write("\2\u0239\u023c\3\2\2\2\u023a\u0238\3\2\2\2\u023a\u023b")
        buf.write("\3\2\2\2\u023b\u0088\3\2\2\2\u023c\u023a\3\2\2\2\u023d")
        buf.write("\u023e\7\60\2\2\u023e\u008a\3\2\2\2\u023f\u0240\13\2\2")
        buf.write("\2\u0240\u0241\bF\n\2\u0241\u008c\3\2\2\2%\2\u010e\u0110")
        buf.write("\u011b\u0179\u017e\u0183\u0188\u018d\u0192\u0195\u01a8")
        buf.write("\u01ae\u01b3\u01ba\u01bf\u01c4\u01cb\u01d0\u01d5\u01dc")
        buf.write("\u01e1\u01e4\u01ea\u01f1\u01fe\u0204\u0206\u021b\u0220")
        buf.write("\u0222\u022a\u022c\u0235\u023a\13\b\2\2\38\2\38\3\38\4")
        buf.write("\38\5\3=\6\3@\7\3C\b\3F\t")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    LB = 2
    RB = 3
    LP = 4
    RP = 5
    SEMI = 6
    COMMA = 7
    COLON = 8
    BREAK = 9
    CONTINUE = 10
    IF = 11
    ELSEIF = 12
    ELSE = 13
    FOREACH = 14
    IN = 15
    RETURN = 16
    NULL = 17
    CLASS = 18
    VAL = 19
    VAR = 20
    CONSTRUCTOR = 21
    DESTRUCTOR = 22
    NEW = 23
    BY = 24
    SELF = 25
    DOLLAR = 26
    UNTERMINATED_COMMENT = 27
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
    STRINCONCAT = 45
    STATIC_ACCESS = 46
    INTTYPE = 47
    FLOATTYPE = 48
    STRINGTYPE = 49
    BOOLEANTYPE = 50
    ARRAYTYPE = 51
    VOIDTYPE = 52
    FLOATLIT = 53
    INTLIT = 54
    WS = 55
    BOOLEANLIT = 56
    ILLEGAL_ESCAPE = 57
    STRINGLIT = 58
    UNCLOSE_STRING = 59
    ID = 60
    DOT = 61
    ERROR_CHAR = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'('", "')'", "'{'", "'}'", "';'", "','", "':'", "'Break'", 
            "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", "'In'", 
            "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", "'Constructor'", 
            "'Destructor'", "'New'", "'By'", "'Self'", "'$'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", 
            "'>'", "'<='", "'<'", "'>='", "'==.'", "'+.'", "'::'", "'Int'", 
            "'Float'", "'String'", "'Boolean'", "'Array'", "'void'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "LB", "RB", "LP", "RP", "SEMI", "COMMA", "COLON", "BREAK", "CONTINUE", 
            "IF", "ELSEIF", "ELSE", "FOREACH", "IN", "RETURN", "NULL", "CLASS", 
            "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "SELF", 
            "DOLLAR", "UNTERMINATED_COMMENT", "BlockComment", "PLUS", "MINUS", 
            "MULTIPLY", "DIVIDE", "MODULO", "NEGATE", "AND", "OR", "EQUAL", 
            "ASSIGN", "DIFFERENT", "GREATER", "LESSTHANEQUAL", "LESSER", 
            "GREATERTHANEQUAL", "STRINGCOMPARE", "STRINCONCAT", "STATIC_ACCESS", 
            "INTTYPE", "FLOATTYPE", "STRINGTYPE", "BOOLEANTYPE", "ARRAYTYPE", 
            "VOIDTYPE", "FLOATLIT", "INTLIT", "WS", "BOOLEANLIT", "ILLEGAL_ESCAPE", 
            "STRINGLIT", "UNCLOSE_STRING", "ID", "DOT", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "LB", "RB", "LP", "RP", "SEMI", "COMMA", "COLON", 
                  "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                  "IN", "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", 
                  "DESTRUCTOR", "NEW", "BY", "SELF", "DOLLAR", "UNTERMINATED_COMMENT", 
                  "BlockComment", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", 
                  "MODULO", "NEGATE", "AND", "OR", "EQUAL", "ASSIGN", "DIFFERENT", 
                  "GREATER", "LESSTHANEQUAL", "LESSER", "GREATERTHANEQUAL", 
                  "STRINGCOMPARE", "STRINCONCAT", "STATIC_ACCESS", "INTTYPE", 
                  "FLOATTYPE", "STRINGTYPE", "BOOLEANTYPE", "ARRAYTYPE", 
                  "VOIDTYPE", "DECIMALPART", "EXPONENTPART", "FLOATLIT", 
                  "OCT", "HEX", "BIN", "DEC", "INTLIT", "WS", "BOOLEANLIT", 
                  "ILLEGAL_ESCAPE", "EscapeSequence", "STRINGLIT", "UNCLOSE_STRING", 
                  "ID", "DOT", "ERROR_CHAR" ]

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
            actions[54] = self.FLOATLIT_action 
            actions[59] = self.INTLIT_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
            actions[65] = self.UNCLOSE_STRING_action 
            actions[68] = self.ERROR_CHAR_action 
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
     

        if actionIndex == 3:
            self.text = self.text.replace("_","")
     

    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text.replace("_", "")
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise IllegalEscape(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise UncloseString(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            raise ErrorToken(self.text)
     


