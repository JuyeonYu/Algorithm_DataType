from collections import deque

graph = {}
graph["i"] = ["alice", "bob", "claire"]
graph["bob"] = ["anju", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["tom", "johnny"]
graph["anju"] = []
graph["peggy"] = []
graph["tom"] = []
graph["johnny"] = []

ways = {}
ways[1] = [2, 4]
ways[2] = [3]
ways[3] = []
ways[4] = [5]
ways[5] = [0]

def shortest_way():
    queue = deque()
    queue += ways[1]
    goal = 0
    level = 0
    route = [1]
    flag = True

    while queue:
        point = queue.popleft()
        if flag:
            route.append(point)

        if point is goal:
            print("find in", level, route + [goal])
            return True

        else:
            queue += ways[point]
            level = level + 1
        flag = False
    return False

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()

        if not person in searched:
            if person_is_seller(person):
                print(person + " IS SELLER!")
                return True

            else:
                search_queue += graph[person]
                searched.append(person)
        return False

def person_is_seller(name):
    return name[-1] == 'm'