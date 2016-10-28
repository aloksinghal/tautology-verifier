from sets import Set
import itertools
from stack import Stack

OPERATORS = ['&', '|', '!']
PARENTHESES = ['(', ')']


def check_tautology(input_string):
    is_tautology = True
    input_string = input_string.replace(" ", "")
    variables = get_variables(input_string)
    input_combos = truth_combos(variables, input_string)
    for truth_values in input_combos:
        valued_statement = replace_variables(input_string, truth_values)
        new_statement = replace_negation(valued_statement)
        postfix_expression = create_postfix(new_statement)
        result = evaluate_postfix(postfix_expression)
        if result != 1:
            is_tautology = False
            break
    return is_tautology


def get_variables(input_string):
    variables = Set()
    for letter in input_string:
        if letter not in OPERATORS and letter not in PARENTHESES:
            variables.add(letter)
    return list(variables)


def truth_combos(variables, statement):
    combo_list = []
    for booleans in itertools.product([True, False], repeat=len(variables)):
        int_bool = [int(x) for x in booleans]  # Replace True with 1, False with 0
        combo_list.append(dict(zip(variables, int_bool)))
    return combo_list


def replace_variables(string, truth_values):
    for variable in truth_values:
        bool_string = str(truth_values[variable])
        string = string.replace(variable, bool_string)
    return string


def replace_negation(string):
    while "!" in string:
        string = string.replace("!1", "0")
        string = string.replace("!0", "1")
    return string


def create_postfix(string):
    expression_stack = Stack()
    expression_stack.push('(')
    string += ')'
    postfix_expression = ''
    for letter in string:
        top = expression_stack.peek()
        if letter in ['0', '1']:
            postfix_expression += letter
        elif letter == '(':
            expression_stack.push(letter)
        elif letter == ')':
            while top != '(':
                operator = expression_stack.pop()
                postfix_expression += operator
                top = expression_stack.peek()
            expression_stack.pop()
        else:
            expression_stack.push(letter)
    while not expression_stack.is_empty():
        postfix_expression += expression_stack.pop()
    return postfix_expression


def evaluate_postfix(string):
    result_stack = Stack()
    for symbol in string:
        if symbol in ['0', '1']:
            result_stack.push(int(symbol))
        else:
            operand_1 = result_stack.pop()
            operand_2 = result_stack.pop()
            if symbol == '&':
                result = operand_2 and operand_1
            if symbol == '|':
                result = operand_2 or operand_1
            result_stack.push(result)
    return result_stack.pop()
