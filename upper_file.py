# read lines from a file convert it to the upper case and write into another file
input_file = open("inputFile.txt", 'r')
output_file = open("outputFile.txt", 'w')
line = input_file.readlines()
for i1 in line:
    line_upper = i1.upper()
    output_file.write(line_upper)
    print("Read line:", line_upper)
   # line = input_file.readline()
input_file.close()
output_file.close()
