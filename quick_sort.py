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


def quicksort(arr):
    from random import randint
    if len(arr)<=1:
        return arr


    node = arr[randint(0,len(arr)-1)]

    smaller, equal,greater = [],[],[]


    for i in arr:
        if i<node:
            smaller.append(i)
        elif i == node:
            equal.append(i)
        else:
            greater.append(i)

    return quicksort(smaller)+ equal + quicksort(greater)

print(quicksort(create_array(100,700)))
