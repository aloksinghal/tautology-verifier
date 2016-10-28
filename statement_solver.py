from utils import get_variables, truth_combos, replace_variables
from utils import replace_negation, create_postfix, evaluate_postfix


def check_tautology(input_string):
    is_tautology = True
    input_string = input_string.replace(" ", "")
    variables = get_variables(input_string)  # get list of distinct variables in string
    input_combos = truth_combos(variables)  # generate all possible input combinations
    for truth_values in input_combos:  # iterate over all input combinations
        valued_statement = replace_variables(input_string, truth_values)  # replace variables with their corresponding truth values
        new_statement = replace_negation(valued_statement)  # Replace all the negation operators directly
        postfix_expression = create_postfix(new_statement)  # create a postfix expresion
        result = evaluate_postfix(postfix_expression)   # Evaluate postfix
        if result != 1:
            is_tautology = False
            break
    return is_tautology

