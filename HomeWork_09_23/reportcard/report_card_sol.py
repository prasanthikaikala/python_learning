from report_card_function import get_dictionary_from_list, generate_report_card

student_name_file = 'C:\\Users\\kaika\\Desktop\\prasanthi\\HomeWork_09_23\\reportcard\\case2_student_names.txt'
english_marks = 'C:\\Users\\kaika\\Desktop\\prasanthi\\HomeWork_09_23\\reportcard\\case2_english_marks.txt'
maths_marks = 'C:\\Users\\kaika\\Desktop\\prasanthi\\HomeWork_09_23\\reportcard\\case2_maths_marks.txt'
science_marks = 'C:\\Users\\kaika\\Desktop\\prasanthi\\HomeWork_09_23\\reportcard\\case2_science_marks.txt'
social_marks = 'C:\\Users\\kaika\\Desktop\\prasanthi\\HomeWork_09_23\\reportcard\\case2_social_marks.txt'

with open(student_name_file, 'r') as name_file:
    with open(english_marks, 'r') as english_marks_file:
        with open(maths_marks, 'r') as maths_marks_file:
            with open(science_marks, 'r') as science_marks_file:
                with open(social_marks, 'r') as social_marks_file:
                    total_marks, percentage = generate_report_card(
                        get_dictionary_from_list(name_file.readlines()),
                        get_dictionary_from_list(english_marks_file.readlines()),
                        get_dictionary_from_list(maths_marks_file.readlines()),
                        get_dictionary_from_list(science_marks_file.readlines()),
                        get_dictionary_from_list(social_marks_file.readlines()))
                    print("total marks = {total}\npercentage = {percent}".format(total=total_marks,
                                                                                 percent=percentage))
