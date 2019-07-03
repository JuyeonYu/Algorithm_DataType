def find_bigest(list):
    if len(list) < 2:
        return list

    else:
        pivot = list[0]
        greater = [i for i in list[1:] if i > pivot]
        if len(greater) is 0:
            return pivot
        list = greater
        return find_bigest(list)


def answer_find_bigest(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]

    sub_max = answer_find_bigest(list[1:])
    return list[0] if list[0] > sub_max else sub_max