from m_functions import except_vowel
from m_functions import all_letter
from m_functions import till_first
from m_functions import neg_check
from m_functions import remove_neg
from m_functions import even_num
from m_functions import odd_num
from m_functions import till_c
from m_functions import all_num

str1 = "Today is Tuesday and it is a sunny day"
str2 = "Crypt cry my by on"
print("Non vowel letters of \"%s\":%s" % (str1, except_vowel(str1)))
print("All letter except vowel:", all_letter(str2))
print("Letters till first space:", till_first(str1))

list_a = [90, 56, 23, 56, 23, -45, -98, 67, 99]
list_b = [0, -1]
print("All item till negative numbers:", neg_check(list_a))
print("All item till negative numbers:", neg_check(list_b))
print("All items leaving negative numbers:", remove_neg(list_a))
print("All even numbers:", even_num(list_a))
print("All odd numbers:", odd_num(list_a))

list_c = [10, 45, 43, 67, 23, 'c', 45, 'd', 67]
print("All numbers till 'c':", till_c(list_c))
print("All numbers:",all_num(list_c))