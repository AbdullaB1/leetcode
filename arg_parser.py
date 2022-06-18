import sys


class ArgParser:
    def __init__(self, argv: list[str]) -> None:
        self.args = argv

    def get_args(self) -> tuple[list, dict]:
        args = []
        kwargs = {}
        prev = None
        for word in self.args:
            if prev:
                kwargs[prev] = word
                prev = None
            elif word[0:2] == "--":
                prev = word[2:]
            elif word[0] == "-":
                prev = word[1:]
            else:
                args.append(word)
        return args, kwargs


if __name__ == '__main__':
    print(sys.argv)
    parser = ArgParser(sys.argv[1:])
    print(*parser.get_args(), sep="\n")
