from collections import defaultdict
def check_palindrome(word):
    counter = defaultdict(int)

    for l in word:
        if l != " ":
            counter[l.lower()] += 1

    odd_letters = 0
    print(counter)
    for keys, values in counter.items():
        if values %2 != 0:
            odd_letters +=1
        if odd_letters>1:
            return False
    return True


print(check_palindrome("Tact Coa"))
