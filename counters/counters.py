from collections import Counter


def split():
    print("\n---------------------------\n")


if __name__ == "__main__":
    # count individual elements of a list
    list_to_be_counted = [0, 0, 0, 0, 1, 1, 1, 1, 1, 'a', 'a', 'b']
    count = Counter(list_to_be_counted)
    print(count)
    for key in count.keys():
        print(f"{key}: {count[key]}")

    split()

    # count letters in a string
    s = "Hello World!"
    count = Counter(s)
    print(count)

    split()

    # spilt a string and count the individual words
    s = "How much wood could a wood chuck chuck if a wood chuck could chuck wood"  # noqa: E501
    count = Counter(s.lower().split())
    print(count)
    print("Item \t Count")
    for item, count in count.items():
        print(f"{item} \t {count}")

    split()

    # using to separate unique and duplicate values
    list_with_duplicates = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3,
                            4, 5, 5, 5, 6, 7, 8, 8, 9, 9]
    counter_of_list_with_duplicates = Counter(list_with_duplicates)
    unique_elements = []
    duplicate_elements = []
    for element in counter_of_list_with_duplicates:
        if counter_of_list_with_duplicates[element] > 1:
            duplicate_elements.append(element)
        else:
            unique_elements.append(element)
    print(counter_of_list_with_duplicates)
    print(f"Unique elements: {unique_elements}, duplicate elements: {duplicate_elements}")  # noqa: E501
