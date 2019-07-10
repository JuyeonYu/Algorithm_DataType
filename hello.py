# hello coding 알고리즘 p10
import hashmap
import selection_sort
import countdown
# import dijkstra
import remove_duplicated_in_list
import recursive
import single_number
import z

def binaey_serach(list, item):
    low = 0;
    high = len(list) - 1

    if item > list[high]:
        return "범위보다 높은 숫자"

    if item < list[low]:
        return "범위보다 낮은 숫자"

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1

        else:
            low = mid + 1

    return None

my_list = [4,7,2,10,1,0,3,5]
my_list2 = [1,1,1,2,3,3,3,3,3,3,3,3,4,5,5,5,5,5,5,5,5,6,6,7,7,8,9,100]
my_list3 = [1,1,4,4,8,10,10]
#print("이진 검색: " + binaey_serach(my_list, 123))
#print(selection_sort.selection_sort(my_list))
#countdown.countdown_while(10)
#countdown.countdown_self(10)
#print(countdown.quick_sort(my_list))
#print(hashmap.search("i"))
#print(hashmap.shortest_way())

# print(dijkstra.test())

# print(recursive.find_bigest(my_list))
# print(recursive.answer_find_bigest(my_list2))
# print(remove_duplicated_in_list.remove_duplicated_in_list(my_list2))
# print(remove_duplicated_in_list.remove_duplicated_in_list_using_set(my_list2))
# print(single_number.fine_single_number(my_list3))
print(z.get_answer(z.get_location(3,7,7)))
list = input()

print(z.get_answer(z.get_location(int(list[0]),int(list[2]),int(list[4]))))
# print(z.get_answer(z.get_location(3,7,7)))
