# 1. total lines in the file => 100
def total_lines(_list):  # input is list
    return len(_list)  # output is int


# 2. total words in file     => 500
def total_words(_list):
    words_list = get_words_list(_list)
    count = len(words_list)
    return count


# 3.words in list
def get_words_list(_list):
    words = []
    for line in _list:
        words.extend(line.split())
    return words


# . words starting vowels   => 120
def get_vowel_consonant_count(_list):
    vowel = ('a', 'e,''i', 'o', 'u')
    vowel_count = 0
    consonant_count = 0
    num_count = 0
    for word in _list:
        words_as_list = list(word)
        if word.isdigit():
            num_count += 1
        if words_as_list[0] in vowel:
            vowel_count += 1
        else:
            consonant_count += 1
    return vowel_count, consonant_count, num_count


# 4.words starting with const => 300
def even_odd(words_list):
    even_count = 0
    odd_count = 0
    for word in words_list:
        if word.isdigit():
            try:
                number = int(word)
                if number % 2 == 0:
                    even_count += 1
                elif number % 2 == 1:
                    odd_count += 1
            except ValueError:
                print("Error when converting %s to int" % word)

    return even_count, odd_count


# total of even numbers => 400
# total of odd numbers => 500
def sum_even_odd(word_list):
    even_sum = 0
    odd_sum = 0
    for word in word_list:
        if word.isdigit():
            number = int(word)
            if number % 2 == 0:
                even_sum = even_sum + number
            elif number % 2 == 1:
                odd_sum = odd_sum + number
    return even_sum, odd_sum
