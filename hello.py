# hello coding 알고리즘 p10
import hashmap
import selection_sort
import countdown
# import dijkstra
import recursive

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
my_list2 = [1,2,3]

#print("이진 검색: " + binaey_serach(my_list, 123))
#print(selection_sort.selection_sort(my_list))
#countdown.countdown_while(10)
#countdown.countdown_self(10)
#print(countdown.quick_sort(my_list))
#print(hashmap.search("i"))
#print(hashmap.shortest_way())

# print(dijkstra.test())

print(recursive.find_bigest(my_list))
print(recursive.answer_find_bigest(my_list2))
