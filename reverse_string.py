def return_reverse_string(str):

    '''
    Args: string to reverse
    Return: reversed string
    '''

    answer_list = [""] * len(str)
    for i in range(len(str)):
        answer_list[i] = str[len(str) - i - 1]
    return answer_list


