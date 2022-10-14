# print all letter except vowels(continue)
def except_vowel(str1):
    str_list = list(str1)
    vowel = ['a', 'e', 'i', 'o', 'u']
    non_vowel_letter = []
    for letter in str_list:
        if letter.lower() in vowel:
            continue
        else:
            non_vowel_letter.append(letter)
    return "".join(non_vowel_letter)


# print all letters till vowel appears(break)
def all_letter(str1):
    str_list = list(str1)
    vowel = ['a', 'e', 'i', 'o', 'u']
    non_vowel_except = []
    for letter in str_list:
        if letter.lower() in vowel:
            break
        non_vowel_except.append(letter)
    return "".join(non_vowel_except)


# print letters till first space appears (break)

def till_first(str1):
    str_list = list(str1)
    return_list = []
    for letter in str_list:
        if letter == ' ':
            break
        return_list.append(letter)
    return "".join(return_list)


# print all items till -negative number comes (break)
def neg_check(list_a):
    pos_list = []
    for i1 in list_a:
        if i1 < 0:
            break
        pos_list.append(i1)
    return pos_list


# print all items leaving -negative number comes(continue)
def remove_neg(list_a):
    pos_list = []
    for i1 in list_a:
        if i1 < 0:
            continue
        pos_list.append(i1)
    return pos_list


# print all even number(continue)
def even_num(list_a):
    even_list = []
    for i1 in list_a:
        if i1 % 2 == 0 and i1 > 0:
            even_list.append(i1)
            continue
    return even_list


# print all odd numbers(continue)
def odd_num(list_a):
    odd_list = []
    for i1 in list_a:
        if i1 % 2 == 1 and i1 > 0:
            odd_list.append(i1)
            continue
    return odd_list


# print all numbers(continue)
def all_num(list_c):
    nums_list = []
    for i1 in list_c:
        if isinstance(i1, str):
            continue
        nums_list.append(i1)
    return nums_list


# print all numbers till 'c' item(break)
def till_c(list_c):
    num_list = []
    for i1 in list_c:
        if i1 == 'c':
          num_list.append(i1)
          break
    return num_list
