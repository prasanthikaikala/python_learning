# is even write into one file if it is odd write into another file
number_file = open("numbers.txt", 'r')
even = open("even.txt", 'w')
odd = open("odd.txt", 'w')
for number_line in number_file:
    number = int(number_line)
    if number % 2 == 0:
        even.write(str(number))
        even.write("\n")
    elif number % 2 == 1:
        odd.write(str(number))
        odd.write("\n")

number_file.close()
even.close()
odd.close()
 
