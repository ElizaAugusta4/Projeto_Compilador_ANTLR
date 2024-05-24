import unittest
from io import StringIO
from antlr4 import InputStream, CommonTokenStream
from CalcLexer import CalcLexer
from CalcParser import CalcParser
from main import EvalVisitor

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.lexer = CalcLexer()
        self.parser = CalcParser(None)
        self.visitor = EvalVisitor()

    def test_variable_declaration(self):
        input_stream = InputStream("let x = 5; let y = 10; x + y;")
        self.lexer.inputStream = input_stream
        token_stream = CommonTokenStream(self.lexer)
        self.parser.setTokenStream(token_stream)
        tree = self.parser.prog()
        result = self.visitor.visit(tree)
        self.assertEqual(result, 15)

    def test_undefined_variable(self):
        input_stream = InputStream("x + 5;")
        self.lexer.inputStream = input_stream
        token_stream = CommonTokenStream(self.lexer)
        self.parser.setTokenStream(token_stream)
        tree = self.parser.prog()
        with self.assertRaises(Exception):
            self.visitor.visit(tree)

    def test_variable_redeclaration(self):
        input_stream = InputStream("let x = 5; let x = 10;")
        self.lexer.inputStream = input_stream
        token_stream = CommonTokenStream(self.lexer)
        self.parser.setTokenStream(token_stream)
        tree = self.parser.prog()
        with self.assertRaises(Exception):
            self.visitor.visit(tree)

    def test_ternary_expression(self):
        input_stream = InputStream("let x = 5; let y = 10; (x > y) ? x : y;")
        self.lexer.inputStream = input_stream
        token_stream = CommonTokenStream(self.lexer)
        self.parser.setTokenStream(token_stream)
        tree = self.parser.prog()
        result = self.visitor.visit(tree)
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()