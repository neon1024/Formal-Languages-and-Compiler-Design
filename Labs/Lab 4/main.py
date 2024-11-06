def scan(file):
    with open(file) as file:
        line = file.readline()

        states = line.strip().split(',')

        print("states:", states)

        line = file.readline()

        input_symbols = line.strip().split(',')

        print("input symbols:", input_symbols)

        line = file.readline()

        initial_state = line.strip()

        print("initial state:", initial_state)

        line = file.readline()

        final_states = line.strip().split(',')

        print("final states:", final_states)

        transition_functions = []

        for line in file:
            transition_functions.append(line.strip())

        print("transition functions:", transition_functions)

        return {"states": states,
                "input_symbols": input_symbols,
                "initial_state": initial_state,
                "final_states": final_states,
                "transition_functions": transition_functions}


def create_input(file="1.txt"):
    with open(file, "w") as file:
        # for p in range(ord('a'), ord('z') + 1):
        #     for q in range(ord('a'), ord('z') + 1):
        #         for z in range(ord('a'), ord('z') + 1):
        #             file.write(chr(p) + chr(q) + chr(z) + "\n")
        for p in range(0, 2):
            for q in range(0, 2):
                for z in range(0, 2):
                    file.write(str(p) + str(q) + str(z) + "\n")


def print_menu_options():
    print("1: read file")
    print("2: show the set of states")
    print("3: show the set of input symbols")
    print("4: show the initial state")
    print("4: show the set of final states")
    print("5: show the transition functions")
    print("x: exit")


def read_file(data):
    file = input("file: ")

    data = scan(file)


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


def menu():
    menu_options = {"1": read_file,
                    "2": show_the_set_of_states,
                    "3": show_the_set_of_input_symbols,
                    "4": show_the_initial_state,
                    "5": show_the_set_of_final_states,
                    "6": show_the_transition_functions,
                    "x": exit}

    data = {"states": [], "input_symbols": [], "initial_state": "", "final_states": [], "transition_functions": []}

    while True:
        print_menu_options()

        chosen_option = input("> ")

        if chosen_option not in menu_options.keys():
            print("[!] Invalid option. Try again.")
        else:
            menu_options[chosen_option](data)


def main():
    menu()

    input_files = ["1.txt", "2.txt"]

    for file in input_files:
        scan(file)
        break


if __name__ == "__main__":
    main()
