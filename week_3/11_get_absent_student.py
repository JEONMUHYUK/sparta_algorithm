all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

'''for all_student in all_students:
    for present_student in present_students:
        if all_student == present_student:
            break
        elif all_student not in present_students:
            print(all_student)'''

def get_absent_student(all_array, present_array):  #O(N)
    student_dict = {}
    for key in all_array:
        student_dict[key] = True

    for key in present_array:
        del student_dict[key]

    for key in student_dict.keys():
        return  key


print(get_absent_student(all_students, present_students))