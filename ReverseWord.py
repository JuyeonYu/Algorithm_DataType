def reverse_word(str):
    word_list = str.split(" ")
    reversed_list = [""] * len(word_list)
    for index, value in enumerate(word_list):
        reversed_list[len(reversed_list) - index - 1] = value
    return reversed_list

