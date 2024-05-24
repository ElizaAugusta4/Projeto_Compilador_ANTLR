from antlr4 import *
from CalcLexer import CalcLexer
from CalcParser import CalcParser
from CalcVisitor import CalcVisitor

class EvalVisitor(CalcVisitor):
    def __init__(self):
        self.memory = {}

    def visitVarDeclaration(self, ctx):
        var_name = ctx.ID().getText()
        if var_name in self.memory:
            raise Exception(f"Variable '{var_name}' already declared")
        value = self.visit(ctx.expr())
        self.memory[var_name] = value
        return value

    def visitExpression(self, ctx):
        return self.visit(ctx.expr())

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.getChild(1).getText() == '*':
            return left * right
        else:  # '/'
            return left / right

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.getChild(1).getText() == '+':
            return left + right
        else:  # '-'
            return left - right

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitVar(self, ctx):
        var_name = ctx.ID().getText()
        if var_name in self.memory:
            return self.memory[var_name]
        else:
            raise Exception(f"Undefined variable: {var_name}")

    def visitInt(self, ctx):
        return int(ctx.INT().getText())

    def visitTernary(self, ctx):
        cond = self.visit(ctx.expr(0))
        if cond:
            return self.visit(ctx.expr(1))
        else:
            return self.visit(ctx.expr(2))

def main():
    lexer = CalcLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = CalcParser(stream)
    tree = parser.prog()

    visitor = EvalVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()
