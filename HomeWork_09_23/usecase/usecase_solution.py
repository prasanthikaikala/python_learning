from usecase_functions import even_odd
from usecase_functions import get_vowel_consonant_count
from usecase_functions import sum_even_odd
from usecase_functions import total_lines, get_words_list
from usecase_functions import total_words

# 1. open the file
path = 'C:\\Users\\kaika\\Desktop\\prasanthi\\HomeWork_09_23\\usecase\\usecase_1.txt'
usecase_file = open(path, 'r')
usecase_list = usecase_file.readlines()
print(usecase_list)
usecase_file.close()

total_lines_in_file = total_lines(usecase_list)
print("total lines in the file:", total_lines_in_file)
total_words_in_file = total_words(usecase_list)
print("total words in the file:", total_words_in_file)

words_list = get_words_list(usecase_list)
vowel_count, consonant_count, num_count = get_vowel_consonant_count(words_list)
print("words start with vowel_count:", vowel_count)
print("words start with consonant_count:", consonant_count)
print("numbers count:", num_count)

even_count, odd_count = even_odd(words_list)
print("even number count:", even_count)
print("odd number count:", odd_count)

even_sum, odd_sum = sum_even_odd(words_list)
print("sum of even numbers:", even_sum)
print("sum of odd numbers:", odd_sum)

output_path = 'C:\\Users\\kaika\\Desktop\\prasanthi\\HomeWork_09_23\\usecase\\usecase_1_output.txt'
summary_report_file = open(output_path, 'w')
summary_report = "******************************************" + "\n**********  Summary Report ***************\n" \
                 + "1. total lines in the file => " + str(total_lines_in_file) \
                 + "\n2. total words in file     => " + str(total_words_in_file) \
                 + "\n3. words starting vowels   => " + str(vowel_count) \
                 + "\n4. words starting with const => " + str(consonant_count) \
                 + "\n5. there are number count =>  " + str(num_count) \
                 + "\n6. even numbers count =>  " + str(even_count) \
                 + "\n7. odd numbers  count => " + str(odd_count) \
                 + "\n8. total of even numbers => " + str(even_sum) \
                 + "\n9. Total of odd numbers => " + str(odd_sum) \
                 + "\n*******************************************"
summary_report_file.write(summary_report)
summary_report_file.close()
