class LexicalError(Exception):
    def __init__(self, message="[!] Lexical error"):
        super().__init__(self, message)
