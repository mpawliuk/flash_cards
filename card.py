class card:
    """A flashcard object.
    === Attributes ===
    a: the first operand of the question.
    op: the operator of the question.
    b: the second operand of the question.
    result: the result to the question.
    wrong: the number of times the student got this question wrong
    """
    a:int
    op:any
    b:int
    result: int
    wrong:int

    def __init__(self, a:int, op:any, b:int) -> None:
        """Initialize a new flashcard."""
        self.a = a
        self.op = op
        self.b = b
        self.result = eval(str(a) + op + str(b))

    def display_card(self):
        """Print the card nicely."""
        question = "*** {} {} {} = {} ***".format(self.a, self.op, self.b, self.result)
        print("".join('*' for _ in question))
        print(question)
        print("".join('*' for _ in question))