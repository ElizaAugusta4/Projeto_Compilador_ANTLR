# Generated from Calc.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalcParser import CalcParser
else:
    from CalcParser import CalcParser

# This class defines a complete generic visitor for a parse tree produced by CalcParser.

class CalcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalcParser#prog.
    def visitProg(self, ctx:CalcParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#VarDeclaration.
    def visitVarDeclaration(self, ctx:CalcParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#Expression.
    def visitExpression(self, ctx:CalcParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#Ternary.
    def visitTernary(self, ctx:CalcParser.TernaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#MulDiv.
    def visitMulDiv(self, ctx:CalcParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#AddSub.
    def visitAddSub(self, ctx:CalcParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#Parens.
    def visitParens(self, ctx:CalcParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#Var.
    def visitVar(self, ctx:CalcParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#Int.
    def visitInt(self, ctx:CalcParser.IntContext):
        return self.visitChildren(ctx)



del CalcParser