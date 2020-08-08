# O(k+n2)
def string_compression(word):

    compressed_word = ""
    consecutive_letter_count =0
    for idx,letter in enumerate(word):
        consecutive_letter_count += 1
        if idx +1 >= len(word) or word[idx +1] != letter:
            # strike ends:
            compressed_word+= str(consecutive_letter_count)+letter
            consecutive_letter_count=0
    return compressed_word if len(compressed_word)<len(word) else word

print(string_compression("aabcccccaaa"))
