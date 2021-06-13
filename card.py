class Card:
    """A flashcard object.
    === Attributes ===
    a: the first operand of the question.
    op: the operator of the question.
    b: the second operand of the question.
    result: the result to the question.
    attempts: number card attempts
    solved: True if the card has been solved. False otherwise.
    """
    a: int
    op: any
    b: int
    result: int
    attempts: int
    solved: bool

    def __init__(self, a: int, op: any, b: int) -> None:
        """Initialize a new flashcard. It has not been attempted yet or solved yet."""
        self.a = a
        self.op = op
        self.b = b
        self.result = eval(str(a) + op + str(b))
        self.attempts = 0
        self.solved = False

    def display_card(self):
        """Print the card nicely."""
        question = "*** {} {} {} = {} ***".format(
            self.a, self.op, self.b, self.result)
        print("".join('*' for _ in question))
        print(question)
        print("".join('*' for _ in question))
