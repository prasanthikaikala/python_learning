class_2 = ["E1", "E3", "E5", "E8", "E10", "E11", "E15"]

names = {"E1": "Radha", "E3": "Raghu", "E5": "Hanish", "E8": "Anu", "E10": "Laxmi", "E11": "kiran", "E15": "Vijay"}

home_location = {"E1": "KPHB", "E3": "MADHAPUR", "E5": "JUBLEEHILLS", "E8": "KPHB", "E10": "MADHAPUR", "E11": "KKP",
                 "E15": "KKP"}

english_marks = {"E1": 90, "E3": 87, "E5": 76, "E8": 56, "E10": 72, "E11": 56, "E15": 85}
maths_marks = {"E1": 91, "E3": 82, "E5": 74, "E8": 55, "E10": 71, "E11": 36, "E15": 65}
science_marks = {"E1": 98, "E3": 84, "E5": 78, "E8": 54, "E10": 74, "E11": 57, "E15": 88}
social_marks = {"E1": 92, "E3": 83, "E5": 72, "E8": 58, "E10": 77, "E11": 54, "E15": 87}
total_marks = {}
percentage = {}
ranks = {}
for i1 in class_2:
    name = names[i1]
    result = "NAME: {}, LOCATION: {}".format(name, home_location[i1])
    marks = "Social : {}, English: {}, Maths: {}, Science :{}".format(social_marks[i1], english_marks[i1],
                                                                      maths_marks[i1], science_marks[i1])
    print(result)
    print(marks)
    total = english_marks[i1] + maths_marks[i1] + science_marks[i1] + social_marks[i1]
    print("Total marks for %s = %s" % (name, total))
    percent = float((total * 100) / 400)
    print("%s's percentage is: %s" % (name, percent))
    total_marks[i1] = total
    percentage[i1] = percent
    print("=================================================\n")

print("Total_marks dict = ", total_marks)
print("percentage dict = ", percentage)
