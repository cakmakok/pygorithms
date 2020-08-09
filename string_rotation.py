def is_substring(word1, word2):
    return (word2 in word1) or (word1 in word2)

def string_rotation(word1, word2):
    return is_substring(word2*2,word1)


print(string_rotation("waterbottle","erbottlewat"))
