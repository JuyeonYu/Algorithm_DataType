def fine_single_number(list):
    check_list = []
    for i in list:
        if len(check_list) is 0:
            check_list.append(i)
        else:

            for j in check_list:
                if i is not j :
                    check_list.append(i)
                else:
                    check_list.remove(i)

    return check_list
