class DFA:
    def __init__(self, states=[], alphabet=[], initial_state=None, final_states=[], transitions={}):
        self.__states = states
        self.__alphabet = alphabet
        self.__initial_state = initial_state
        self.__final_states = final_states
        self.__transitions = transitions
        self.__state = initial_state

    def reset_state(self):
        self.__state = self.__initial_state

    def transition(self, char):
        if char.isdigit():
            char = 'd'

        transition_key = self.__state + char

        if transition_key in self.__transitions:
            self.__state = self.__transitions[transition_key]
        else:
            self.__state = "REJECT"

    def is_accepting(self):
        return self.__state in self.__final_states

    def check_string(self, string):
        self.reset_state()  # "123"

        for char in string:
            if char not in self.__alphabet and not char.isdigit():
                return False  # Reject if the character is not in the alphabet or not a digit

            self.transition(char)

            if self.__state == 'REJECT':
                return False

        return self.is_accepting()

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "" + str(self.__states) + "\n" + str(self.__alphabet) + "\n" + self.__initial_state + "\n" + str(self.__final_states) + "\n" + str(self.__transitions)
