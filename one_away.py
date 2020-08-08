from collections import defaultdict
def is_one_away(word1, word2):

    table1 = get_letter_frequency(word1)
    table2 = get_letter_frequency(word2)

    longer = word1 if len(table1)>len(table2) else word2
    num_of_difference = 0
    for item in longer:
        if table1[item] != table2[item]:
            num_of_difference +=1
        if num_of_difference >1:
            return False
    return True



def get_letter_frequency(word):
    table = defaultdict(int)

    for l in word:
        table[l.lower()] +=1

    return table

print(is_one_away("pale", "ple"))
print(is_one_away("pales", "pale"))
print(is_one_away("pale", "bale"))
print(is_one_away("pale", "bakee"))
print(is_one_away("pale", "bake"))
