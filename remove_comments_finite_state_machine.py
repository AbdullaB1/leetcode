from enum import Enum, auto


class State(Enum):
    Reading = auto()
    LineComment = auto()
    BlockComment = auto()
    String = auto()


class FiniteStateParser:

    def __init__(self, code):
        self.state = State.Reading
        self.code = code
        self.cur = 0
        self.symbol = code[0]
        self.parsed = []

    def hasNext(self):
        # нужно обработать последний символ
        return self.cur + 1 <= len(self.code)

    def lookahead(self):
        return self.code[self.cur + 1]

    def next(self):
        self.cur += 1
        if self.hasNext():
            self.symbol = self.code[self.cur]

    def parse(self):
        while self.hasNext():
            if self.state == State.Reading:
                if self.symbol == '/':
                    if self.lookahead() == '*':
                        self.state = State.BlockComment
                        self.next()
                    elif self.lookahead() == '/':
                        self.state = State.LineComment
                        self.next()
                    else:
                        self.parsed.append(self.symbol)
                elif self.symbol == '"':
                    self.state = State.String
                    self.parsed.append(self.symbol)
                else:
                    self.parsed.append(self.symbol)
            elif self.state == State.String:
                if self.symbol == '\\' and self.lookahead() == "\"":
                    self.parsed.append("\\\"")
                elif self.symbol == "\"":
                    self.state = State.Reading
                    self.parsed.append("\"")
                else:
                    self.parsed.append("\"")
            elif self.state == State.LineComment:
                if self.symbol == '\n':
                    self.state = State.Reading
                    self.parsed.append('\n')
            elif self.state == State.BlockComment:
                if self.symbol == '*' and self.lookahead() == '/':
                    self.state = State.Reading
                    self.next()
            self.next()


code = """/*Test program */
int main()
{ 
    // variable declaration 
    int a, b, c;
    /* This is a test
    multiline  
    comment for 
    testing */
    a = b + c;
}"""
parser = FiniteStateParser(code)
parser.parse()

print(''.join(parser.parsed))
