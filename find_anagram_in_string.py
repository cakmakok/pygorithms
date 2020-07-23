from collections import Counter

s = "abbc"
b = "cbabadcbbabbcbabaabccbabc"


def find_anagram(short, long):
    found = []

    short_counter = Counter(short)
    long_counter = Counter(long[0:len(short)])
    i = 0
    while i <= len(long)-len(short):
        # print("-"*50)
        #
        # print("compare: \n{}\n{}".format(short_counter,long_counter))
        if short_counter == long_counter:
            # print("found")

            found.append(i)


        # print("current index\t{}\ncurrent dict\t{}\ncurrent frame\t{}-{}-{}".format(i,
        #                                                                             long_counter,
        #                                                                             long[:i],
        #                                                                             long[i:i+len(short)],
        #                                                                             long[i+len(short):]))

        # decrement current element from hashtable for next iteration
        if long_counter.get(long[i]):
            if long_counter.get(long[i]) == 1:
                del long_counter[long[i]]
            else:
                long_counter[long[i]] -= 1


        # add/increment next element to  frame on hashtable:
        if i!=len(long)-len(short):
            next_element = long[i+len(short)]
            if long_counter.get(next_element):
                long_counter[next_element] +=1
            else:
                long_counter[next_element] = 1
        else:
            return found



        i+=1

print(find_anagram(s,b))
