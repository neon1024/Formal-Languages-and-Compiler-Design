from DFA import DFA


def scan(input_filename, data):
    with open(input_filename) as file:
        data["type"] = input_filename.removesuffix(".txt")

        print(data["type"])

        line = file.readline()

        states = line.strip().split(',')

        print("states:", states)

        data["states"] = states

        line = file.readline()

        input_symbols = line.strip().split(',')

        print("input symbols:", input_symbols)

        data["input_symbols"] = input_symbols

        line = file.readline()

        initial_state = line.strip()

        print("initial state:", initial_state)

        data["initial_state"] = initial_state

        line = file.readline()

        final_states = line.strip().split(',')

        print("final states:", final_states)

        data["final_states"] = final_states

        transition_functions = {}

        for line in file:
            stripped_line = line.strip()
            key = stripped_line[0:2]
            value = stripped_line[2:]
            transition_functions[key] = value

        print("transition functions:", transition_functions)

        data["transition_functions"] = transition_functions


def print_menu_options():
    print("1: read file")
    print("2: show the set of states")
    print("3: show the set of input symbols")
    print("4: show the initial state")
    print("5: show the set of final states")
    print("6: show the transition functions")
    print("7: create the DFA")
    print("8: test the DFA")
    print("x: exit")


def read_file(data):
    file = input("file: ")

    scan(file, data)


def show_the_set_of_states(data):
    print(data["states"])


def show_the_set_of_input_symbols(data):
    print(data["input_symbols"])


def show_the_initial_state(data):
    print(data["initial_state"])


def show_the_set_of_final_states(data):
    print(data["final_states"])


def show_the_transition_functions(data):
    transition_functions = data["transition_functions"]

    for transition_function in transition_functions:
        print(transition_function)


def create_DFA(data):
    dfa = DFA(data["type"], data["states"], data["input_symbols"], data["initial_state"], data["final_states"], data["transition_functions"])

    data["DFA"] = dfa

    print(dfa)


def test_DFA_constants(data):
    expected_true = ['123', "+1", '-1', '3.14', '-0.99', "+.9", '-.5', '12e10', "1E10", '0.5E-6', "1e-.1"]
    expected_false = ['"string"', ".", "9.", "99.", "+", "-", "e", "E", "1e.", "1e.+"]

    dfa = data["DFA"]

    results = {}

    for string in expected_true:
        result = dfa.check_string(string)
        results[string] = "OK" if result else "WRONG"

    for string in expected_false:
        result = dfa.check_string(string)
        results[string] = "OK" if not result else "WRONG"

    print(results)


def test_DFA_identifiers(data):
    expected_true = ["a", "a_", "a1", "_a", "_1", "a1_", "_a_", "_a1_", "_a_a_"]
    expected_false = ["1", "1_", "1a", "11"]

    dfa = data["DFA"]

    results = {}

    for string in expected_true:
        result = dfa.check_string(string)
        results[string] = "OK" if result else "WRONG"

    for string in expected_false:
        result = dfa.check_string(string)
        results[string] = "OK" if not result else "WRONG"

    print(results)


def test_DFA(data):
    match data["type"]:
        case "identifiers":
            test_DFA_identifiers(data)

        case "constants":
            test_DFA_constants(data)


def menu():
    menu_options = {"1": read_file,
                    "2": show_the_set_of_states,
                    "3": show_the_set_of_input_symbols,
                    "4": show_the_initial_state,
                    "5": show_the_set_of_final_states,
                    "6": show_the_transition_functions,
                    "7": create_DFA,
                    "8": test_DFA,
                    "x": exit}

    dfa = DFA()
    data = {"type": None, "states": [], "input_symbols": [], "initial_state": "", "final_states": [], "transition_functions": [], "DFA": dfa}

    while True:
        print_menu_options()

        chosen_option = input("> ")

        if chosen_option not in menu_options.keys():
            print("[!] Invalid option. Try again.")
        else:
            menu_options[chosen_option](data) if chosen_option != "x" else exit()


def main():
    menu()


if __name__ == "__main__":
    main()
