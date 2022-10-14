from a_functions import length_function
from a_functions import length_with_for_loop
from a_functions import avg_function 
from a_functions import total_function
from a_functions import max_function
from a_functions import min_function
from a_functions import start_with_vowel
from a_functions import end_with_vowel
from a_functions import percentage_cal


list_1=[10,22,33,55,66,12]
print("length of list:",length_function(list_1))
print("avg function:",avg_function(list_1))
print("length using for loop for list:",length_with_for_loop(list_1))
print("total function:",total_function(list_1))
print("total value in list:",total_function(list_1))
print("max value:",max_function(list_1))
print("min value:",min_function(list_1))
print("Percentage of each item in list : ", percentage_cal(list_1))

vowel_str = "apple"
print("%s starts with vowel letter = %s"%(vowel_str, start_with_vowel(vowel_str)))

non_vowel_str = "python"
print("%s starts with vowel letter = %s"%(non_vowel_str, start_with_vowel(non_vowel_str)))


print("%s ends with vowel letter = %s"%(vowel_str, end_with_vowel(vowel_str)))

print("%s ends with vowel letter = %s"%(non_vowel_str, end_with_vowel(non_vowel_str)))


