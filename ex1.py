import random
import timeit

def insert(root, value):
    if root is None:
        return {"value": value, "left": None, "right": None}
    current = root
    while True:
        if value < current["value"]:
            if current["left"] is None:
                current["left"] = {"value": value, "left": None, "right": None}
                break
            else:
                current = current["left"]
        else:
            if current["right"] is None:
                current["right"] = {"value": value, "left": None, "right": None}
                break
            else:
                current = current["right"]
    return root


def search(root, value):
    current = root
    while current is not None:
        if value == current["value"]:
            return current
        elif value < current["value"]:
            current = current["left"]
        else:
            current = current["right"]
    return None


sort_vector = list(range(10000))

root_sort = None
for value in sort_vector:
    root_sort = insert(root_sort, value)

def performance(root, vector):
    time_total = 0
    for value in vector:
        time_taken = timeit.timeit(lambda: search(root, value), number=10)
        time_total += time_taken
    time_avg = time_total / len(vector)
    return time_avg, time_total

sort_avg_time, sort_total_time = performance(root_sort, sort_vector)
print(f"Sorted Input - Average Search Time: {sort_avg_time}, Total Search Time: {sort_total_time}")

shuffle_vector = sort_vector.copy()
random.shuffle(shuffle_vector)

root_shuffle = None
for value in shuffle_vector:
    root_shuffle = insert(root_shuffle, value)

avg_time_shuffle, total_time_shuffle = performance(root_shuffle, shuffle_vector)
print(f"Shuffled Input - Average Search Time: {avg_time_shuffle}, Total Search Time: {total_time_shuffle}")



"""
The shuffled vector approach is faster as the total search time for the shuffled input tree is 0.066 seconds, 
whereas for the sorted input tree, it is 13.88 seconds. This is because when it is shuffled, the nodes are distributed
accross left and right subtrees which is not the case in the sorted approach as it creates an unbalanced tree.
"""