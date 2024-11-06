from SymbolTable import SymbolTable

import re


def identify_token(token):
    keywords = ["nothing", "integer", "text", "character", "boolean", "true", "false", "list", "dictionary", "structure",
                "if", "else", "match", "case", "while", "for", "fun", "ret", "fixed", "try", "catch", "throw", "go"]

    # identifiers_regex_string = "(_)?[a-zA-Z](_)? | (_)?[0-9](_)? | (_)?[a-zA-Z](_)?([a-zA-Z])?(_)?([0-9])?(_)? | (_)?[0-9](_)?([a-zA-Z])?(_)?([0-9])?(_)?"
    identifiers_regex_pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"

    # - constants: "fixed" + IDENTIFIER +  ":" + TYPE | arraydecl
    constants_regex_pattern = r"^-?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][-+]?[0-9]+)?$"

    # - strings: starts and ends with ", or ' for char

    operators = {"+": "addition", "-": "subtraction", "*": "multiplication", "/": "division", "%": "remainder", "**": "power", "=": "assign",
                 "+=": "i_addition", "-=": "i_subtraction", "/=": "i_division", "*=": "i_multiplication", "**=": "i_power", "<": "less_than",
                 "<=": "less_or_equal_than", ">": "greater_than", ">=": "greater_or_equal_than", "==": "equal", "!=": "not_equal",
                 "and": "logical_and", "&&": "logical_and", "or": "logical_or", "||": "logical_or", "++": "increment", "--": "decrement",
                 "->": "return_type", ".": "selector"}

    separators = {" ": "white_space", ",": "enumeration", ";": "statement_end", ":": "specifier", "&": "reference", "(": "call_start", ")": "call_end",
                  "[": "selector_start", "]": "selector_end", "{": "block_start", "}": "block_end"}

    if token in keywords:
        return "keyword"

    if bool(re.match(identifiers_regex_pattern, token)):
        return "identifier"

    if token in operators:
        return "operator"

    if token in separators:
        return "separator"

    if len(token) >= 2:
        if token[0] == '"' and token[len(token) - 1] == '"' or token[0] == "'" and token[len(token) - 1] == "'":
            return "string"

    if bool(re.match(constants_regex_pattern, token)):
        return "constant"

    return "error"


def test_identifier_type():
    expected_results = {'_validIdentifier': "identifier", '123Invalid': "error", '_123': "identifier", 'valid_123': "identifier", 'not-valid': "error"}

    for token, token_type in expected_results.items():
        assert identify_token(token) == token_type


def test_keyword_type():
    expected_results = {'_validIdentifier': "identifier", '123Invalid': "error", '_123': "identifier", 'for': "keyword", 'if': "keyword"}

    for token, token_type in expected_results.items():
        assert identify_token(token) == token_type


def test_constant_type():
    expected_results = {'123': "constant", '-456': "constant", '3.14': "constant", '-.678': "constant", '1e10': "constant", '123.': "constant", '.456': "constant", '-2.5E-3': "constant", '"not_a_number"': "string"}

    for token, token_type in expected_results.items():
        assert identify_token(token) == token_type


def test_identify_token():
    test_keyword_type()
    test_identifier_type()

    test_constant_type()


def is_symbol(token):
    symbol_types = ["identifier", "constant", "string"]

    token_type = identify_token(token)

    return token_type in symbol_types


def scan(file):
    line_number = 0
    column_number = 0

    separators_regex = r"[ ,;:&()\[\]{}]"

    # TODO maintain the correct order of symbols
    symbols = set()  # the symbols to add in the ST

    with open(file) as file:
        for line in file:
            line = line.strip()

            line_number += 1

            tokens = re.split(separators_regex, line)
            tokens = set([token for token in tokens if token])  # symbols are unique in ST

            for token in tokens:
                if is_symbol(token):
                    symbols.add(token)

        print(symbols)

    return symbols


def main():
    symbol_table = SymbolTable()

    input_files = ["p1.txt", "p2.txt", "p3.txt", "error.txt"]

    for file in input_files:
        symbols = scan(file)

        for symbol in symbols:
            symbol_table.add(symbol)

        break  # TODO read the rest

    print(symbol_table)


if __name__ == "__main__":
    main()
