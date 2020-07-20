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


def merge(list1, list2):
    merged = []
    idx1 = idx2 = 0
    while idx1 < len(list1) and idx2 < len(list2):
        if list1[idx1] < list2[idx2]:
            merged.append(list1[idx1])
            idx1 += 1
        else:
            merged.append(list2[idx2])
            idx2 += 1

    if idx1 == len(list1):
        merged.extend(list2[idx2:])
    else:
        merged.extend(list1[idx1:])

    return merged


def merge_sort(a):
    # a list of zero or one elements is sorted, by definition
    if len(a) <= 1:
        return a
    # split the list in half and call merge sort recursively on each half
    left, right = merge_sort(a[:len(a) // 2]), merge_sort(a[len(a) // 2:])

    # merge the now-sorted sublists
    return merge(left, right)


print(merge_sort(create_array(5,5)))

