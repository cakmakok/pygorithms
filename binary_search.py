def create_array(len=10, max=50, unique=False):
    from random import randint
    if not unique:
        return [randint(0, max) for _ in range(len)]
    else:
        array = []
        i = 0
        while i < len:
            new_random = randint(0, max)
            if new_random not in array:
                array.append(new_random)
                i += 1
        return array

def binary_search(list, item):

    if len(list)<=1:
        print("not in list")
        return
    mid_idx = len(list) // 2
    mid_element = list[mid_idx]
    if item < mid_element:
        binary_search(list[0:mid_idx], item)
    elif item > mid_element:
        binary_search(list[mid_idx:len(list)], item)
    elif item == mid_element:
        print("found {}".format(mid_element))

binary_search([1,2,3,4,5,6,7,8,9],33)
