import unittest
from utils import get_variables, truth_combos, replace_variables
from utils import replace_negation, create_postfix, evaluate_postfix


class TestPostfixCreation(unittest.TestCase):
    
    def test_simple_expr(self):
        expr = '1'
        self.assertEqual(create_postfix(expr), '1')

    def test_simple_and(self):
        expr = '1&0'
        self.assertEqual(create_postfix(expr), '10&')

    def test_and_or_combo(self):
        expr = '1&(0|1)'
        self.assertEqual(create_postfix(expr), '101|&')

    def test_complicated_brackets(self):
        expr = '1&((0|1)&(1|0))'
        self.assertEqual(create_postfix(expr), '101|10|&&')

class TestVariableCreation(unittest.TestCase):
    def test_single_variable(self):
        expr = 'a'
        self.assertEqual(get_variables(expr), ['a'])

    def test_simple_two_variable(self):
        expr = 'a&b'
        self.assertEqual(get_variables(expr), ['a', 'b'])

    def test_repitition(self):
        expr = 'a&(a|b)'
        self.assertEqual(get_variables(expr), ['a', 'b'])

    def test_complicated_brackets(self):
        expr = 'a&((a|b)&(b|c))'
        self.assertEqual(get_variables(expr), ['a', 'b', 'c'])


class TestTruthCombos(unittest.TestCase):
    
    def test_single_variable(self):
        self.assertEqual(truth_combos('a'), [{'a': 1}, {'a': 0}])


class TestReplaceNegation(unittest.TestCase):
    
    def test_simple_expr(self):
        expr = '!0'
        self.assertEqual(replace_negation(expr), '1')

    def test_repeated_negation(self):
        expr = '!!1'
        self.assertEqual(replace_negation(expr), '1')

    def test_complex_expression(self):
        expr = '!!1|!0'
        self.assertEqual(replace_negation(expr), '1|1')


class TestEvaluatePostfix(unittest.TestCase):
    def test_simple_expr(self):
        expr = '1'
        self.assertEqual(evaluate_postfix(expr), 1)

    def test_simple_and(self):
        expr = '10&'
        self.assertEqual(evaluate_postfix(expr), 0)

    def test_and_or_combo(self):
        expr = '101|&'
        self.assertEqual(evaluate_postfix(expr), 1)

    def test_complicated_repitition(self):
        expr = '101|10|&&'
        self.assertEqual(evaluate_postfix(expr), 1)


class TestReplaceVariables(unittest.TestCase):

    def test_simple_expr(self):
        string = 'a'
        truth_values = {'a': 1}
        output = replace_variables(string, truth_values)
        self.assertEqual(output, '1')

    def test_multiple_variables(self):
        string = 'a|b'
        truth_values = {'a': 1, 'b': 0}
        output = replace_variables(string, truth_values)
        self.assertEqual(output, '1|0')






if __name__ == '__main__':
    unittest.main()