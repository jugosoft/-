def is_orange(fruit: str):
    return fruit == "orange"

graph = {}
current_queue = []
checked_nodes = []

#Найти путь от лемона до аплесина
graph["lemon"]     = ["apple", "grape"]
graph["apple"]     = ["melon", "pineapple"]
graph["pineapple"] = ["watermelon", "melon"]
graph["melon"] = ["orange"]

current_queue.extend(graph["lemon"])
length = 0

while len(current_queue) != 0:
    if is_orange(fruit=current_queue[0]):
        print("Got it!")
        print(str(length) + " steps")
        break
    elif not current_queue[0] in checked_nodes:
        checked_nodes.append(current_queue[0])
        if current_queue[0] in graph.keys():
            current_queue.extend(graph[current_queue[0]])
            length = length + 1
        print(current_queue)
        current_queue.pop(0)
    elif len(current_queue) == 1:
        print("Nothing found!")
        break


