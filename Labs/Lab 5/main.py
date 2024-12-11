from Grammar import Grammar
from RecursiveDescentParser import RecursiveDescentParser


def main():
    # Example of usage:
    grammar = Grammar("g1.txt")
    grammar.print_grammar()

    if grammar.is_cfg():
        print("The grammar is a valid context-free grammar (CFG).")
    else:
        print("The grammar is not a valid CFG.")

    # Load grammar and parse input string
    parser = RecursiveDescentParser(grammar)
    parser.parse("a a b")


if __name__ == "__main__":
    main()
