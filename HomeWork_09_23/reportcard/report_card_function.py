import datetime


def get_dictionary_from_list(_list):  # EP3 Raghu --> {"EP3":"Raghu"}
    dictionary = {}
    for line in _list:  # EP3 Raghu -> str
        line_split = line.split()  # ['EP1', 'Ramu'] -> list
        key = line_split[0]  # key= EP1
        value = line_split[1]  # value = Ramu
        dictionary[key] = value  # {'EP1': 'Ramu'}
    return dictionary


def generate_report_card(name_dict,
                         english_marks_dict,
                         maths_marks_dict,
                         science_marks_dict,
                         social_marks_dict):
    total_marks = {}
    percentage = {}
    for student in name_dict.keys():
        name = name_dict[student]
        try:
            total = int(english_marks_dict[student]) \
                    + int(maths_marks_dict[student]) \
                    + int(science_marks_dict[student]) \
                    + int(social_marks_dict[student])
            percent = float((total * 100) / 400)
            total_marks[student] = total
            percentage[student] = percent
            current_datetime=datetime.datetime.now()
            report_card = "1st Term Report card\n-----------------\n" \
                          "Date and Time : {date_time}\n-----------------\n" \
                          "Name: {name} \n-----------------\n" \
                          "Marks\n-----------------\n" \
                          "Social : {social}\n" \
                          "Science : {science}\n" \
                          "English : {english}\n" \
                          "Maths : {maths}\n------------------\n" \
                          "Total : {total}\n" \
                          "Percentage: {percent}\n" .format(
                name=name,
                date_time = current_datetime,
                social=social_marks_dict[student],
                science=science_marks_dict[student],
                english=english_marks_dict[student],
                maths=maths_marks_dict[student],
                total=total, percent=percent)
            report_card_file_name = "C:\\Users\\kaika\\Desktop\\prasanthi\\HomeWork_09_23\\reportcard\\{file}.txt".format(
                file=name)
            report_card_file = open(report_card_file_name, 'w')
            report_card_file.write(report_card)
            report_card_file.close()
            print("Report Card generated for : %s, saved in file path = %s" % (name, report_card_file_name))
        except ValueError:
            print("Exception occurred while generating report card for : ", name)
    return total_marks, percentage
