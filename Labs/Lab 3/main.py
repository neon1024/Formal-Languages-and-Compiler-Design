from SymbolTable import SymbolTable

def identify_token(token):
    keywords = ["nothing", "integer", "text", "character", "boolean", "true", "false", "list", "dictionary", "structure",
                "if", "else", "match", "case", "while", "for", "fun", "return", "fixed", "try", "catch", "throw", "go"]

    identifiers_regex_string = "(_)?[a-zA-Z](_)? | (_)?[0-9](_)? | (_)?[a-zA-Z](_)?([a-zA-Z])?(_)?([0-9])?(_)? | (_)?[0-9](_)?([a-zA-Z])?(_)?([0-9])?(_)?"

    # - constants: "fixed" + IDENTIFIER +  ":" + TYPE | arraydecl

    # - strings: starts and ends with ", or ' for char

    operators = {"+": "addition", "-": "subtraction", "*": "multiplication", "/": "division", "%": "remainder", "**": "power", "=": "assign",
                 "+=": "i_addition", "-=": "i_subtraction", "/=": "i_division", "*=": "i_multiplication", "**=": "i_power", "<": "less_than",
                 "<=": "less_or_equal_than", ">": "greater_than", ">=": "greater_or_equal_than", "==": "equal", "!=": "not_equal",
                 "and": "logical_and", "&&": "logical_and", "or": "logical_or", "||": "logical_or", "++": "increment", "--": "decrement",
                 "->": "return_type", ".": "selector"}

    separators = {" ": "white_space", ",": "enumeration", ";": "statement_end", ":": "specifier", "(": "call_start", ")": "call_end",
                  "[": "selector_start", "]": "selector_end", "{": "block_start", "}": "block_end"}


def scan(file):
    line_number = 0
    column_number = 0

    separators = " ,;:()[]{}"

    with open(file) as input_file:
        line = input_file.readline()

        line_number += 1

        token_start = -1

        for character in line:
            column_number += 1

            token = ""

            if character in separators:
                if token_start != -1:  # we have a full token
                    token = line[token_start:column_number]

                    identify_token(token)

                token_start = -1  # reset the start of the token

            if token_start == -1:  # we have a new token
                token_start = column_number - 1




def main():
    symbol_table = SymbolTable()

    input_files = ["p1.txt", "p2.txt", "p3.txt", "error.txt"]

    for file in input_files:
        scan(file)


if __name__ == "__main__":
    main()
