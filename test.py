i1 = ["hello", "hi", "apple", "ant", "month", "eagle"]
vowel = ('a', 'e,''i', 'o', 'u')
vowel_count = 0
consonant_count = 0
for word in i1:
    words_as_list = list(word)
    if words_as_list[0] in vowel:
        vowel_count += 1
    else:
        consonant_count += 1

print("no of words start with vowel:", vowel_count)
print("no of words start with consonant:", consonant_count)
