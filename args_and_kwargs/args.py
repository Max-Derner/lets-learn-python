

# Note, this does not have to be called args
def sum_up(*args: int) -> int:
    total = 0
    for x in args:
        total += x
    return total


# Here, we chose the variable name substrings, but it works just the same
def concat(*substrings: str) -> str:
    text = ''
    for substring in substrings:
        text += substring + " "
    return text


if __name__ == "__main__":
    sums = sum_up(1)
    print(sums)
    sums = sum_up(1, 2, 3, 4, 5, 6, 7)
    print(sums)
    words = concat("hello")
    print(words)
    words = concat("I", "think", "this", "is", "kinda", "cool")
    print(words)
