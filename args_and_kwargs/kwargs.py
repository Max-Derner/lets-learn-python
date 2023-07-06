

# kwargs, or keyword arguments are interacted with in much the same
# manner as a dictionary
def print_out(**kwargs) -> None:
    fancy_default = False
    words_default = "You forgot to give me words!"
    fancy = kwargs.get('fancy', fancy_default)
    words = kwargs.get('words', words_default)
    if fancy is True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(words)
    if fancy is True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


if __name__ == "__main__":
    print_out()
    print_out(words="Hello, this is words!")
    print_out(fancy=True)
    print_out(words="I'm fancy!", fancy=True)
    print_out(words="I might be fancy?", fancy='definitely not though')
