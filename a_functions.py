# Calculates length of given list
def length_function(list_1):
    return len(list_1)


# Calculates avg value from given list
def avg_function(list_1):
    avg = sum(list_1) / len(list_1)
    return avg


# Calculates length value from given list
def length_with_for_loop(list_1):
    count = 0
    for i1 in list_1:
        count = count + 1

    return count


# Calculates total of given list
def total_function(list_1):
    total = 0
    for i1 in list_1:
        total = total + i1
    return total


# Calculates maximum value from given list
def max_function(list_1):
    max_function = list_1[0]
    for i1 in list_1:
        if max_function < i1:
            max_function = i1
    return max_function


# Calculates minimum value from given list
def min_function(list_1):
    min_function = list_1[0]
    for i1 in list_1:
        if min_function > i1:
            min_function = i1
    return min_function


# percentage of value = value/total * 100
def percentage_cal(list_1):
    total = total_function(list_1)
    percentage_list = {}
    for i1 in list_1:
        percentage_list[i1] = float((total * 100) / 400)

    return percentage_list


def start_with_vowel(str_1):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_with_vowel = False
    str_list = list(str_1)
    first_ltr = str_list[0]
    for i1 in vowels:
        if i1 == first_ltr:
            start_with_vowel = True
            break
    return start_with_vowel


def end_with_vowel(str_1):
    vowels = ['a', 'e', 'i', 'o', 'u']
    end_with_vowel = False
    str_list = list(str_1)
    end_ltr = str_list[len(str_list) - 1]
    for i1 in vowels:
        if i1 == end_ltr:
            end_with_vowel = True
            break
    return end_with_vowel
