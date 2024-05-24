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
            
    def test_math_expression(self):
        input_stream = InputStream("let x = 5; let y = 10; x + y * 3;")
        self.lexer.inputStream = input_stream
        token_stream = CommonTokenStream(self.lexer)
        self.parser.setTokenStream(token_stream)
        tree = self.parser.prog()
        result = self.visitor.visit(tree)
        self.assertEqual(result, 35)
    
    # def test_ternary_expression_with_multiplication(self):
    #     input_stream = InputStream("let x = 5; let y = 10; (x > y) ? x * 2 : y * 2;")
    #     self.lexer.inputStream = input_stream
    #     token_stream = CommonTokenStream(self.lexer)
    #     self.parser.setTokenStream(token_stream)
    #     tree = self.parser.prog()
    #     result = self.visitor.visit(tree)
    #     self.assertEqual(result, 20)
        
    def test_nested_expressions(self):
        input = "(let x = 5; let y = 10; (x + 2) > y) ? ((x == 3) ? x * 2 : x) : y * 2;"
        lexer = CalcLexer(InputStream(input))
        stream = CommonTokenStream(lexer)
        parser = CalcParser(stream)
        tree = parser.prog()
        result = self.visitor.visit(tree)
        self.assertEqual(result, 10)

        
    def test_return_value(self):
        input_stream = InputStream("let result = 5; result * 10;")
        self.lexer.inputStream = input_stream
        token_stream = CommonTokenStream(self.lexer)
        self.parser.setTokenStream(token_stream)
        tree = self.parser.prog()
        result = self.visitor.visit(tree)
        self.assertEqual(result, 50)
    
    def test_duplicate_variable_declaration(self):
        input = "let x = 10; let x = 5;"
        lexer = CalcLexer(InputStream(input))
        stream = CommonTokenStream(lexer)
        parser = CalcParser(stream)
        with self.assertRaises(Exception) as context:
            tree = parser.prog()
            self.visitor.visit(tree)
        exception_message = str(context.exception)
        self.assertTrue('Variable \'x\' already declared' in exception_message)


    def test_undefined_variable(self):
        input = "x + 5;"
        lexer = CalcLexer(InputStream(input))
        stream = CommonTokenStream(lexer)
        parser = CalcParser(stream)
        with self.assertRaises(Exception) as context:
            tree = parser.prog()
            self.visitor.visit(tree)
        self.assertTrue('Undefined variable: x' in str(context.exception))
        
if __name__ == '__main__':
    unittest.main()