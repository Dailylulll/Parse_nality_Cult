# Generated from PyParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,31,225,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,1,0,1,0,1,1,5,1,51,8,1,10,1,12,1,54,
        9,1,1,1,4,1,57,8,1,11,1,12,1,58,1,1,5,1,62,8,1,10,1,12,1,65,9,1,
        5,1,67,8,1,10,1,12,1,70,9,1,1,2,1,2,1,2,1,2,3,2,76,8,2,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,89,8,4,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,3,5,98,8,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,126,
        8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,136,8,10,1,10,1,
        10,1,10,1,10,5,10,142,8,10,10,10,12,10,145,9,10,1,11,1,11,1,12,1,
        12,1,13,1,13,1,13,3,13,154,8,13,1,14,1,14,1,14,1,14,5,14,160,8,14,
        10,14,12,14,163,9,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,3,15,
        173,8,15,1,15,1,15,1,15,5,15,178,8,15,10,15,12,15,181,9,15,1,16,
        1,16,3,16,185,8,16,1,17,1,17,1,17,1,17,1,17,3,17,192,8,17,1,18,1,
        18,3,18,196,8,18,1,19,1,19,1,19,1,19,1,20,1,20,3,20,204,8,20,1,20,
        3,20,207,8,20,1,21,1,21,5,21,211,8,21,10,21,12,21,214,9,21,1,22,
        1,22,5,22,218,8,22,10,22,12,22,221,9,22,1,22,1,22,1,22,0,2,20,30,
        23,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,0,1,2,0,6,6,23,24,231,0,46,1,0,0,0,2,68,1,0,0,0,4,75,1,0,0,0,
        6,77,1,0,0,0,8,81,1,0,0,0,10,90,1,0,0,0,12,99,1,0,0,0,14,104,1,0,
        0,0,16,110,1,0,0,0,18,125,1,0,0,0,20,135,1,0,0,0,22,146,1,0,0,0,
        24,148,1,0,0,0,26,153,1,0,0,0,28,155,1,0,0,0,30,172,1,0,0,0,32,184,
        1,0,0,0,34,191,1,0,0,0,36,195,1,0,0,0,38,197,1,0,0,0,40,206,1,0,
        0,0,42,208,1,0,0,0,44,215,1,0,0,0,46,47,3,2,1,0,47,48,5,0,0,1,48,
        1,1,0,0,0,49,51,5,3,0,0,50,49,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,
        0,52,53,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,55,57,3,4,2,0,56,55,
        1,0,0,0,57,58,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,63,1,0,0,0,
        60,62,5,2,0,0,61,60,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,
        0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,66,52,1,0,0,0,67,70,1,0,0,0,68,
        66,1,0,0,0,68,69,1,0,0,0,69,3,1,0,0,0,70,68,1,0,0,0,71,76,3,6,3,
        0,72,76,3,8,4,0,73,76,3,14,7,0,74,76,3,16,8,0,75,71,1,0,0,0,75,72,
        1,0,0,0,75,73,1,0,0,0,75,74,1,0,0,0,76,5,1,0,0,0,77,78,3,24,12,0,
        78,79,5,4,0,0,79,80,3,26,13,0,80,7,1,0,0,0,81,82,5,15,0,0,82,83,
        3,20,10,0,83,84,5,13,0,0,84,85,5,2,0,0,85,88,3,2,1,0,86,89,3,10,
        5,0,87,89,3,12,6,0,88,86,1,0,0,0,88,87,1,0,0,0,88,89,1,0,0,0,89,
        9,1,0,0,0,90,91,5,16,0,0,91,92,3,20,10,0,92,93,5,13,0,0,93,94,5,
        2,0,0,94,97,3,2,1,0,95,98,3,10,5,0,96,98,3,12,6,0,97,95,1,0,0,0,
        97,96,1,0,0,0,97,98,1,0,0,0,98,11,1,0,0,0,99,100,5,17,0,0,100,101,
        5,13,0,0,101,102,5,2,0,0,102,103,3,2,1,0,103,13,1,0,0,0,104,105,
        5,19,0,0,105,106,3,20,10,0,106,107,5,13,0,0,107,108,5,2,0,0,108,
        109,3,2,1,0,109,15,1,0,0,0,110,111,5,18,0,0,111,112,3,24,12,0,112,
        113,5,21,0,0,113,114,3,18,9,0,114,115,5,13,0,0,115,116,5,2,0,0,116,
        117,3,2,1,0,117,17,1,0,0,0,118,126,3,24,12,0,119,120,5,20,0,0,120,
        121,5,9,0,0,121,122,5,26,0,0,122,123,5,11,0,0,123,124,5,26,0,0,124,
        126,5,10,0,0,125,118,1,0,0,0,125,119,1,0,0,0,126,19,1,0,0,0,127,
        128,6,10,-1,0,128,129,5,9,0,0,129,130,3,20,10,0,130,131,5,10,0,0,
        131,136,1,0,0,0,132,133,5,22,0,0,133,136,3,20,10,2,134,136,3,32,
        16,0,135,127,1,0,0,0,135,132,1,0,0,0,135,134,1,0,0,0,136,143,1,0,
        0,0,137,138,10,4,0,0,138,139,3,22,11,0,139,140,3,20,10,5,140,142,
        1,0,0,0,141,137,1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,
        1,0,0,0,144,21,1,0,0,0,145,143,1,0,0,0,146,147,7,0,0,0,147,23,1,
        0,0,0,148,149,5,28,0,0,149,25,1,0,0,0,150,154,3,32,16,0,151,154,
        3,30,15,0,152,154,3,28,14,0,153,150,1,0,0,0,153,151,1,0,0,0,153,
        152,1,0,0,0,154,27,1,0,0,0,155,156,5,7,0,0,156,161,3,26,13,0,157,
        158,5,11,0,0,158,160,3,26,13,0,159,157,1,0,0,0,160,163,1,0,0,0,161,
        159,1,0,0,0,161,162,1,0,0,0,162,164,1,0,0,0,163,161,1,0,0,0,164,
        165,5,8,0,0,165,29,1,0,0,0,166,167,6,15,-1,0,167,173,3,32,16,0,168,
        169,5,9,0,0,169,170,3,30,15,0,170,171,5,10,0,0,171,173,1,0,0,0,172,
        166,1,0,0,0,172,168,1,0,0,0,173,179,1,0,0,0,174,175,10,3,0,0,175,
        176,5,5,0,0,176,178,3,30,15,4,177,174,1,0,0,0,178,181,1,0,0,0,179,
        177,1,0,0,0,179,180,1,0,0,0,180,31,1,0,0,0,181,179,1,0,0,0,182,185,
        5,28,0,0,183,185,3,34,17,0,184,182,1,0,0,0,184,183,1,0,0,0,185,33,
        1,0,0,0,186,192,3,36,18,0,187,192,3,38,19,0,188,192,5,27,0,0,189,
        192,5,30,0,0,190,192,5,29,0,0,191,186,1,0,0,0,191,187,1,0,0,0,191,
        188,1,0,0,0,191,189,1,0,0,0,191,190,1,0,0,0,192,35,1,0,0,0,193,196,
        5,26,0,0,194,196,3,38,19,0,195,193,1,0,0,0,195,194,1,0,0,0,196,37,
        1,0,0,0,197,198,5,26,0,0,198,199,5,12,0,0,199,200,5,26,0,0,200,39,
        1,0,0,0,201,204,3,42,21,0,202,204,3,44,22,0,203,201,1,0,0,0,203,
        202,1,0,0,0,204,207,1,0,0,0,205,207,1,0,0,0,206,203,1,0,0,0,206,
        205,1,0,0,0,207,41,1,0,0,0,208,212,5,14,0,0,209,211,5,31,0,0,210,
        209,1,0,0,0,211,214,1,0,0,0,212,210,1,0,0,0,212,213,1,0,0,0,213,
        43,1,0,0,0,214,212,1,0,0,0,215,219,5,25,0,0,216,218,5,31,0,0,217,
        216,1,0,0,0,218,221,1,0,0,0,219,217,1,0,0,0,219,220,1,0,0,0,220,
        222,1,0,0,0,221,219,1,0,0,0,222,223,5,25,0,0,223,45,1,0,0,0,21,52,
        58,63,68,75,88,97,125,135,143,153,161,172,179,184,191,195,203,206,
        212,219
    ]

class PyParser ( Parser ):

    grammarFileName = "PyParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'\\n'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'['", "']'", "'('", "')'", 
                     "','", "'.'", "':'", "'#'", "'if'", "'elif'", "'else'", 
                     "'for'", "'while'", "'range'", "'in'", "'not'", "'and'", 
                     "'or'", "'''''" ]

    symbolicNames = [ "<INVALID>", "WS", "NEWLINE", "TAB", "ASSIGNMENT", 
                      "OPERATOR", "CONDITION", "LBRA", "RBRA", "LPAR", "RPAR", 
                      "COMMA", "PERIOD", "COLON", "POUND", "IF", "ELIF", 
                      "ELSE", "FOR", "WHILE", "RANGE", "IN", "NOT", "AND", 
                      "OR", "TICK3", "INT", "BOOL", "ID", "CHAR", "STRING", 
                      "CHAR_SET" ]

    RULE_program = 0
    RULE_block = 1
    RULE_statement = 2
    RULE_assignment = 3
    RULE_if = 4
    RULE_elif = 5
    RULE_else = 6
    RULE_while = 7
    RULE_for = 8
    RULE_iterable = 9
    RULE_bexpr = 10
    RULE_logic_op = 11
    RULE_lvalue = 12
    RULE_rvalue = 13
    RULE_list = 14
    RULE_expr = 15
    RULE_value = 16
    RULE_literal = 17
    RULE_number = 18
    RULE_float = 19
    RULE_comment = 20
    RULE_comment1 = 21
    RULE_comment2 = 22

    ruleNames =  [ "program", "block", "statement", "assignment", "if", 
                   "elif", "else", "while", "for", "iterable", "bexpr", 
                   "logic_op", "lvalue", "rvalue", "list", "expr", "value", 
                   "literal", "number", "float", "comment", "comment1", 
                   "comment2" ]

    EOF = Token.EOF
    WS=1
    NEWLINE=2
    TAB=3
    ASSIGNMENT=4
    OPERATOR=5
    CONDITION=6
    LBRA=7
    RBRA=8
    LPAR=9
    RPAR=10
    COMMA=11
    PERIOD=12
    COLON=13
    POUND=14
    IF=15
    ELIF=16
    ELSE=17
    FOR=18
    WHILE=19
    RANGE=20
    IN=21
    NOT=22
    AND=23
    OR=24
    TICK3=25
    INT=26
    BOOL=27
    ID=28
    CHAR=29
    STRING=30
    CHAR_SET=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(PyParser.BlockContext,0)


        def EOF(self):
            return self.getToken(PyParser.EOF, 0)

        def getRuleIndex(self):
            return PyParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = PyParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.block()
            self.state = 47
            self.match(PyParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TAB(self, i:int=None):
            if i is None:
                return self.getTokens(PyParser.TAB)
            else:
                return self.getToken(PyParser.TAB, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PyParser.StatementContext)
            else:
                return self.getTypedRuleContext(PyParser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PyParser.NEWLINE)
            else:
                return self.getToken(PyParser.NEWLINE, i)

        def getRuleIndex(self):
            return PyParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = PyParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 52
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==3:
                        self.state = 49
                        self.match(PyParser.TAB)
                        self.state = 54
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 56 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 55
                            self.statement()

                        else:
                            raise NoViableAltException(self)
                        self.state = 58 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                    self.state = 63
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 60
                            self.match(PyParser.NEWLINE) 
                        self.state = 65
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
             
                self.state = 70
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(PyParser.AssignmentContext,0)


        def if_(self):
            return self.getTypedRuleContext(PyParser.IfContext,0)


        def while_(self):
            return self.getTypedRuleContext(PyParser.WhileContext,0)


        def for_(self):
            return self.getTypedRuleContext(PyParser.ForContext,0)


        def getRuleIndex(self):
            return PyParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = PyParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.assignment()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.if_()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.while_()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 74
                self.for_()
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


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(PyParser.LvalueContext,0)


        def ASSIGNMENT(self):
            return self.getToken(PyParser.ASSIGNMENT, 0)

        def rvalue(self):
            return self.getTypedRuleContext(PyParser.RvalueContext,0)


        def getRuleIndex(self):
            return PyParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = PyParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.lvalue()
            self.state = 78
            self.match(PyParser.ASSIGNMENT)
            self.state = 79
            self.rvalue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(PyParser.IF, 0)

        def bexpr(self):
            return self.getTypedRuleContext(PyParser.BexprContext,0)


        def COLON(self):
            return self.getToken(PyParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(PyParser.NEWLINE, 0)

        def block(self):
            return self.getTypedRuleContext(PyParser.BlockContext,0)


        def elif_(self):
            return self.getTypedRuleContext(PyParser.ElifContext,0)


        def else_(self):
            return self.getTypedRuleContext(PyParser.ElseContext,0)


        def getRuleIndex(self):
            return PyParser.RULE_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)




    def if_(self):

        localctx = PyParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(PyParser.IF)
            self.state = 82
            self.bexpr(0)
            self.state = 83
            self.match(PyParser.COLON)
            self.state = 84
            self.match(PyParser.NEWLINE)
            self.state = 85
            self.block()
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 86
                self.elif_()

            elif la_ == 2:
                self.state = 87
                self.else_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(PyParser.ELIF, 0)

        def bexpr(self):
            return self.getTypedRuleContext(PyParser.BexprContext,0)


        def COLON(self):
            return self.getToken(PyParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(PyParser.NEWLINE, 0)

        def block(self):
            return self.getTypedRuleContext(PyParser.BlockContext,0)


        def elif_(self):
            return self.getTypedRuleContext(PyParser.ElifContext,0)


        def else_(self):
            return self.getTypedRuleContext(PyParser.ElseContext,0)


        def getRuleIndex(self):
            return PyParser.RULE_elif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif" ):
                listener.enterElif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif" ):
                listener.exitElif(self)




    def elif_(self):

        localctx = PyParser.ElifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_elif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(PyParser.ELIF)
            self.state = 91
            self.bexpr(0)
            self.state = 92
            self.match(PyParser.COLON)
            self.state = 93
            self.match(PyParser.NEWLINE)
            self.state = 94
            self.block()
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 95
                self.elif_()

            elif la_ == 2:
                self.state = 96
                self.else_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(PyParser.ELSE, 0)

        def COLON(self):
            return self.getToken(PyParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(PyParser.NEWLINE, 0)

        def block(self):
            return self.getTypedRuleContext(PyParser.BlockContext,0)


        def getRuleIndex(self):
            return PyParser.RULE_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse" ):
                listener.enterElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse" ):
                listener.exitElse(self)




    def else_(self):

        localctx = PyParser.ElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(PyParser.ELSE)
            self.state = 100
            self.match(PyParser.COLON)
            self.state = 101
            self.match(PyParser.NEWLINE)
            self.state = 102
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(PyParser.WHILE, 0)

        def bexpr(self):
            return self.getTypedRuleContext(PyParser.BexprContext,0)


        def COLON(self):
            return self.getToken(PyParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(PyParser.NEWLINE, 0)

        def block(self):
            return self.getTypedRuleContext(PyParser.BlockContext,0)


        def getRuleIndex(self):
            return PyParser.RULE_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)




    def while_(self):

        localctx = PyParser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(PyParser.WHILE)
            self.state = 105
            self.bexpr(0)
            self.state = 106
            self.match(PyParser.COLON)
            self.state = 107
            self.match(PyParser.NEWLINE)
            self.state = 108
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(PyParser.FOR, 0)

        def lvalue(self):
            return self.getTypedRuleContext(PyParser.LvalueContext,0)


        def IN(self):
            return self.getToken(PyParser.IN, 0)

        def iterable(self):
            return self.getTypedRuleContext(PyParser.IterableContext,0)


        def COLON(self):
            return self.getToken(PyParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(PyParser.NEWLINE, 0)

        def block(self):
            return self.getTypedRuleContext(PyParser.BlockContext,0)


        def getRuleIndex(self):
            return PyParser.RULE_for

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor" ):
                listener.enterFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor" ):
                listener.exitFor(self)




    def for_(self):

        localctx = PyParser.ForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(PyParser.FOR)
            self.state = 111
            self.lvalue()
            self.state = 112
            self.match(PyParser.IN)
            self.state = 113
            self.iterable()
            self.state = 114
            self.match(PyParser.COLON)
            self.state = 115
            self.match(PyParser.NEWLINE)
            self.state = 116
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(PyParser.LvalueContext,0)


        def RANGE(self):
            return self.getToken(PyParser.RANGE, 0)

        def LPAR(self):
            return self.getToken(PyParser.LPAR, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(PyParser.INT)
            else:
                return self.getToken(PyParser.INT, i)

        def COMMA(self):
            return self.getToken(PyParser.COMMA, 0)

        def RPAR(self):
            return self.getToken(PyParser.RPAR, 0)

        def getRuleIndex(self):
            return PyParser.RULE_iterable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterable" ):
                listener.enterIterable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterable" ):
                listener.exitIterable(self)




    def iterable(self):

        localctx = PyParser.IterableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_iterable)
        try:
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.lvalue()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.match(PyParser.RANGE)
                self.state = 120
                self.match(PyParser.LPAR)
                self.state = 121
                self.match(PyParser.INT)
                self.state = 122
                self.match(PyParser.COMMA)
                self.state = 123
                self.match(PyParser.INT)
                self.state = 124
                self.match(PyParser.RPAR)
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


    class BexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(PyParser.LPAR, 0)

        def bexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PyParser.BexprContext)
            else:
                return self.getTypedRuleContext(PyParser.BexprContext,i)


        def RPAR(self):
            return self.getToken(PyParser.RPAR, 0)

        def NOT(self):
            return self.getToken(PyParser.NOT, 0)

        def value(self):
            return self.getTypedRuleContext(PyParser.ValueContext,0)


        def logic_op(self):
            return self.getTypedRuleContext(PyParser.Logic_opContext,0)


        def getRuleIndex(self):
            return PyParser.RULE_bexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBexpr" ):
                listener.enterBexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBexpr" ):
                listener.exitBexpr(self)



    def bexpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PyParser.BexprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_bexpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.state = 128
                self.match(PyParser.LPAR)
                self.state = 129
                self.bexpr(0)
                self.state = 130
                self.match(PyParser.RPAR)
                pass
            elif token in [22]:
                self.state = 132
                self.match(PyParser.NOT)
                self.state = 133
                self.bexpr(2)
                pass
            elif token in [26, 27, 28, 29, 30]:
                self.state = 134
                self.value()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 143
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PyParser.BexprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bexpr)
                    self.state = 137
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 138
                    self.logic_op()
                    self.state = 139
                    self.bexpr(5) 
                self.state = 145
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logic_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(PyParser.OR, 0)

        def AND(self):
            return self.getToken(PyParser.AND, 0)

        def CONDITION(self):
            return self.getToken(PyParser.CONDITION, 0)

        def getRuleIndex(self):
            return PyParser.RULE_logic_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_op" ):
                listener.enterLogic_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_op" ):
                listener.exitLogic_op(self)




    def logic_op(self):

        localctx = PyParser.Logic_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_logic_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 25165888) != 0)):
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


    class LvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PyParser.ID, 0)

        def getRuleIndex(self):
            return PyParser.RULE_lvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLvalue" ):
                listener.enterLvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLvalue" ):
                listener.exitLvalue(self)




    def lvalue(self):

        localctx = PyParser.LvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_lvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(PyParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(PyParser.ValueContext,0)


        def expr(self):
            return self.getTypedRuleContext(PyParser.ExprContext,0)


        def list_(self):
            return self.getTypedRuleContext(PyParser.ListContext,0)


        def getRuleIndex(self):
            return PyParser.RULE_rvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRvalue" ):
                listener.enterRvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRvalue" ):
                listener.exitRvalue(self)




    def rvalue(self):

        localctx = PyParser.RvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_rvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 150
                self.value()
                pass

            elif la_ == 2:
                self.state = 151
                self.expr(0)
                pass

            elif la_ == 3:
                self.state = 152
                self.list_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRA(self):
            return self.getToken(PyParser.LBRA, 0)

        def rvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PyParser.RvalueContext)
            else:
                return self.getTypedRuleContext(PyParser.RvalueContext,i)


        def RBRA(self):
            return self.getToken(PyParser.RBRA, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PyParser.COMMA)
            else:
                return self.getToken(PyParser.COMMA, i)

        def getRuleIndex(self):
            return PyParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)




    def list_(self):

        localctx = PyParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(PyParser.LBRA)
            self.state = 156
            self.rvalue()
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 157
                self.match(PyParser.COMMA)
                self.state = 158
                self.rvalue()
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 164
            self.match(PyParser.RBRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(PyParser.ValueContext,0)


        def LPAR(self):
            return self.getToken(PyParser.LPAR, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PyParser.ExprContext)
            else:
                return self.getTypedRuleContext(PyParser.ExprContext,i)


        def RPAR(self):
            return self.getToken(PyParser.RPAR, 0)

        def OPERATOR(self):
            return self.getToken(PyParser.OPERATOR, 0)

        def getRuleIndex(self):
            return PyParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PyParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27, 28, 29, 30]:
                self.state = 167
                self.value()
                pass
            elif token in [9]:
                self.state = 168
                self.match(PyParser.LPAR)
                self.state = 169
                self.expr(0)
                self.state = 170
                self.match(PyParser.RPAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 179
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PyParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 174
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 175
                    self.match(PyParser.OPERATOR)
                    self.state = 176
                    self.expr(4) 
                self.state = 181
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PyParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(PyParser.LiteralContext,0)


        def getRuleIndex(self):
            return PyParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = PyParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_value)
        try:
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(PyParser.ID)
                pass
            elif token in [26, 27, 29, 30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.literal()
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


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(PyParser.NumberContext,0)


        def float_(self):
            return self.getTypedRuleContext(PyParser.FloatContext,0)


        def BOOL(self):
            return self.getToken(PyParser.BOOL, 0)

        def STRING(self):
            return self.getToken(PyParser.STRING, 0)

        def CHAR(self):
            return self.getToken(PyParser.CHAR, 0)

        def getRuleIndex(self):
            return PyParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = PyParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_literal)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.float_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 188
                self.match(PyParser.BOOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 189
                self.match(PyParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 190
                self.match(PyParser.CHAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(PyParser.INT, 0)

        def float_(self):
            return self.getTypedRuleContext(PyParser.FloatContext,0)


        def getRuleIndex(self):
            return PyParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = PyParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_number)
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.match(PyParser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.float_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(PyParser.INT)
            else:
                return self.getToken(PyParser.INT, i)

        def PERIOD(self):
            return self.getToken(PyParser.PERIOD, 0)

        def getRuleIndex(self):
            return PyParser.RULE_float

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)




    def float_(self):

        localctx = PyParser.FloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(PyParser.INT)
            self.state = 198
            self.match(PyParser.PERIOD)
            self.state = 199
            self.match(PyParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comment1(self):
            return self.getTypedRuleContext(PyParser.Comment1Context,0)


        def comment2(self):
            return self.getTypedRuleContext(PyParser.Comment2Context,0)


        def getRuleIndex(self):
            return PyParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = PyParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_comment)
        try:
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [14]:
                    self.state = 201
                    self.comment1()
                    pass
                elif token in [25]:
                    self.state = 202
                    self.comment2()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [-1]:
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


    class Comment1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POUND(self):
            return self.getToken(PyParser.POUND, 0)

        def CHAR_SET(self, i:int=None):
            if i is None:
                return self.getTokens(PyParser.CHAR_SET)
            else:
                return self.getToken(PyParser.CHAR_SET, i)

        def getRuleIndex(self):
            return PyParser.RULE_comment1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment1" ):
                listener.enterComment1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment1" ):
                listener.exitComment1(self)




    def comment1(self):

        localctx = PyParser.Comment1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_comment1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(PyParser.POUND)
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 209
                self.match(PyParser.CHAR_SET)
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comment2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TICK3(self, i:int=None):
            if i is None:
                return self.getTokens(PyParser.TICK3)
            else:
                return self.getToken(PyParser.TICK3, i)

        def CHAR_SET(self, i:int=None):
            if i is None:
                return self.getTokens(PyParser.CHAR_SET)
            else:
                return self.getToken(PyParser.CHAR_SET, i)

        def getRuleIndex(self):
            return PyParser.RULE_comment2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment2" ):
                listener.enterComment2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment2" ):
                listener.exitComment2(self)




    def comment2(self):

        localctx = PyParser.Comment2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_comment2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(PyParser.TICK3)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 216
                self.match(PyParser.CHAR_SET)
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 222
            self.match(PyParser.TICK3)
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
        self._predicates[10] = self.bexpr_sempred
        self._predicates[15] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def bexpr_sempred(self, localctx:BexprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




