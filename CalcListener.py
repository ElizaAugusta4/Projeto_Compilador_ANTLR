# Generated from Calc.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalcParser import CalcParser
else:
    from CalcParser import CalcParser

# This class defines a complete listener for a parse tree produced by CalcParser.
class CalcListener(ParseTreeListener):

    # Enter a parse tree produced by CalcParser#prog.
    def enterProg(self, ctx:CalcParser.ProgContext):
        pass

    # Exit a parse tree produced by CalcParser#prog.
    def exitProg(self, ctx:CalcParser.ProgContext):
        pass


    # Enter a parse tree produced by CalcParser#VarDeclaration.
    def enterVarDeclaration(self, ctx:CalcParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by CalcParser#VarDeclaration.
    def exitVarDeclaration(self, ctx:CalcParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by CalcParser#Expression.
    def enterExpression(self, ctx:CalcParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CalcParser#Expression.
    def exitExpression(self, ctx:CalcParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CalcParser#Ternary.
    def enterTernary(self, ctx:CalcParser.TernaryContext):
        pass

    # Exit a parse tree produced by CalcParser#Ternary.
    def exitTernary(self, ctx:CalcParser.TernaryContext):
        pass


    # Enter a parse tree produced by CalcParser#MulDiv.
    def enterMulDiv(self, ctx:CalcParser.MulDivContext):
        pass

    # Exit a parse tree produced by CalcParser#MulDiv.
    def exitMulDiv(self, ctx:CalcParser.MulDivContext):
        pass


    # Enter a parse tree produced by CalcParser#AddSub.
    def enterAddSub(self, ctx:CalcParser.AddSubContext):
        pass

    # Exit a parse tree produced by CalcParser#AddSub.
    def exitAddSub(self, ctx:CalcParser.AddSubContext):
        pass


    # Enter a parse tree produced by CalcParser#Parens.
    def enterParens(self, ctx:CalcParser.ParensContext):
        pass

    # Exit a parse tree produced by CalcParser#Parens.
    def exitParens(self, ctx:CalcParser.ParensContext):
        pass


    # Enter a parse tree produced by CalcParser#Var.
    def enterVar(self, ctx:CalcParser.VarContext):
        pass

    # Exit a parse tree produced by CalcParser#Var.
    def exitVar(self, ctx:CalcParser.VarContext):
        pass


    # Enter a parse tree produced by CalcParser#Int.
    def enterInt(self, ctx:CalcParser.IntContext):
        pass

    # Exit a parse tree produced by CalcParser#Int.
    def exitInt(self, ctx:CalcParser.IntContext):
        pass



del CalcParser