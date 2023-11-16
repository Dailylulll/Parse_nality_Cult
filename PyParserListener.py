# Generated from PyParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PyParser import PyParser
else:
    from PyParser import PyParser

# This class defines a complete listener for a parse tree produced by PyParser.
class PyParserListener(ParseTreeListener):

    # Enter a parse tree produced by PyParser#program.
    def enterProgram(self, ctx:PyParser.ProgramContext):
        pass

    # Exit a parse tree produced by PyParser#program.
    def exitProgram(self, ctx:PyParser.ProgramContext):
        pass


    # Enter a parse tree produced by PyParser#block.
    def enterBlock(self, ctx:PyParser.BlockContext):
        pass

    # Exit a parse tree produced by PyParser#block.
    def exitBlock(self, ctx:PyParser.BlockContext):
        pass


    # Enter a parse tree produced by PyParser#iblock.
    def enterIblock(self, ctx:PyParser.IblockContext):
        pass

    # Exit a parse tree produced by PyParser#iblock.
    def exitIblock(self, ctx:PyParser.IblockContext):
        pass


    # Enter a parse tree produced by PyParser#statement.
    def enterStatement(self, ctx:PyParser.StatementContext):
        pass

    # Exit a parse tree produced by PyParser#statement.
    def exitStatement(self, ctx:PyParser.StatementContext):
        pass


    # Enter a parse tree produced by PyParser#assignment.
    def enterAssignment(self, ctx:PyParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PyParser#assignment.
    def exitAssignment(self, ctx:PyParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PyParser#if.
    def enterIf(self, ctx:PyParser.IfContext):
        pass

    # Exit a parse tree produced by PyParser#if.
    def exitIf(self, ctx:PyParser.IfContext):
        pass


    # Enter a parse tree produced by PyParser#elif.
    def enterElif(self, ctx:PyParser.ElifContext):
        pass

    # Exit a parse tree produced by PyParser#elif.
    def exitElif(self, ctx:PyParser.ElifContext):
        pass


    # Enter a parse tree produced by PyParser#else.
    def enterElse(self, ctx:PyParser.ElseContext):
        pass

    # Exit a parse tree produced by PyParser#else.
    def exitElse(self, ctx:PyParser.ElseContext):
        pass


    # Enter a parse tree produced by PyParser#while.
    def enterWhile(self, ctx:PyParser.WhileContext):
        pass

    # Exit a parse tree produced by PyParser#while.
    def exitWhile(self, ctx:PyParser.WhileContext):
        pass


    # Enter a parse tree produced by PyParser#for.
    def enterFor(self, ctx:PyParser.ForContext):
        pass

    # Exit a parse tree produced by PyParser#for.
    def exitFor(self, ctx:PyParser.ForContext):
        pass


    # Enter a parse tree produced by PyParser#iterable.
    def enterIterable(self, ctx:PyParser.IterableContext):
        pass

    # Exit a parse tree produced by PyParser#iterable.
    def exitIterable(self, ctx:PyParser.IterableContext):
        pass


    # Enter a parse tree produced by PyParser#bexpr.
    def enterBexpr(self, ctx:PyParser.BexprContext):
        pass

    # Exit a parse tree produced by PyParser#bexpr.
    def exitBexpr(self, ctx:PyParser.BexprContext):
        pass


    # Enter a parse tree produced by PyParser#logic_op.
    def enterLogic_op(self, ctx:PyParser.Logic_opContext):
        pass

    # Exit a parse tree produced by PyParser#logic_op.
    def exitLogic_op(self, ctx:PyParser.Logic_opContext):
        pass


    # Enter a parse tree produced by PyParser#lvalue.
    def enterLvalue(self, ctx:PyParser.LvalueContext):
        pass

    # Exit a parse tree produced by PyParser#lvalue.
    def exitLvalue(self, ctx:PyParser.LvalueContext):
        pass


    # Enter a parse tree produced by PyParser#rvalue.
    def enterRvalue(self, ctx:PyParser.RvalueContext):
        pass

    # Exit a parse tree produced by PyParser#rvalue.
    def exitRvalue(self, ctx:PyParser.RvalueContext):
        pass


    # Enter a parse tree produced by PyParser#list.
    def enterList(self, ctx:PyParser.ListContext):
        pass

    # Exit a parse tree produced by PyParser#list.
    def exitList(self, ctx:PyParser.ListContext):
        pass


    # Enter a parse tree produced by PyParser#expr.
    def enterExpr(self, ctx:PyParser.ExprContext):
        pass

    # Exit a parse tree produced by PyParser#expr.
    def exitExpr(self, ctx:PyParser.ExprContext):
        pass


    # Enter a parse tree produced by PyParser#value.
    def enterValue(self, ctx:PyParser.ValueContext):
        pass

    # Exit a parse tree produced by PyParser#value.
    def exitValue(self, ctx:PyParser.ValueContext):
        pass


    # Enter a parse tree produced by PyParser#literal.
    def enterLiteral(self, ctx:PyParser.LiteralContext):
        pass

    # Exit a parse tree produced by PyParser#literal.
    def exitLiteral(self, ctx:PyParser.LiteralContext):
        pass


    # Enter a parse tree produced by PyParser#number.
    def enterNumber(self, ctx:PyParser.NumberContext):
        pass

    # Exit a parse tree produced by PyParser#number.
    def exitNumber(self, ctx:PyParser.NumberContext):
        pass


    # Enter a parse tree produced by PyParser#float.
    def enterFloat(self, ctx:PyParser.FloatContext):
        pass

    # Exit a parse tree produced by PyParser#float.
    def exitFloat(self, ctx:PyParser.FloatContext):
        pass


    # Enter a parse tree produced by PyParser#comment.
    def enterComment(self, ctx:PyParser.CommentContext):
        pass

    # Exit a parse tree produced by PyParser#comment.
    def exitComment(self, ctx:PyParser.CommentContext):
        pass



del PyParser