import argparse
import textwrap

# Note, more info --> https://docs.python.org/3/library/argparse.html
# Note, more info --> https://docs.python.org/3/library/argparse.html#the-add-argument-method  # noqa(E501)

DESCRIPTION = """\t---+==  WELCOME!  ==+---\n This is a demo of the argparse import..."""  # noqa(E501)

EPILOG = """--+=  And that's all the help you're getting, make sure you have fun!  =+--"""  # noqa(E501


def greeter(number_of_greetings: int) -> None:
    for _ in range(number_of_greetings):
        print("Hello!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(DESCRIPTION),
        epilog=EPILOG,
        prog="DIR\\argument_parser.py"
    )
    parser.add_argument(
        "--hello",
        required=False,
        type=int,
        nargs=1,
        default=1,
        help="displays greeting, takes argument for number of times greeted"
    )

    args = parser.parse_args()

    greeter(number_of_greetings=args.hello)
