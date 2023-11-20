# print("hello", end="\n")
# print("what are you doing?")

# my_list = [1,2,3,4,5,6,7,8,9]
# my_list[0] = 100
# my_list = (1,2,3,4,5,6,7,8,9)

# for number in my_list:
#     print(number ** 3)

# print(my_list[:4])


# favorite_sports = {'ali':['football','tennis'],'sara':'tennis','reza':"baseball"}

# print(f"ali likes {favorite_sports['ali']}")
# print(f"sara likes {favorite_sports['sara']}")
# print(f"reza likes {favorite_sports['reza']}")

# for item in favorite_sports.items():
#     if type(item[1]) == str:
#         if item[1] == "tennis":
#             print(item[0])
#     elif type(item[1]) == list:
#         for sport in item[1]:
#             if sport == "tennis":
#              print(item[0])


from colorama import Fore, Back, Style
message = f"""{Fore.CYAN}Welcome to our school.{Style.RESET_ALL}
{Back.RED}to add a new student -> 0{Style.RESET_ALL}
to exit -> 0
to add a new student -> 5
to show all students -> 1
to search for a student info -> 2
to delete a student -> 3
to update a student -> 4
"""
all_students = []

def show_all_students_info(students):
    print(f"{'name':<25}{'age':^5}{'course':^15}")
    for student in students:
        print(f"{student['name']:<25}{student['age']:^5}{student['course']:^15}")



while True:
    print(message)
    print("Enter a number : ")
    user_selection = input("> ")
    if user_selection == "0":
        print("bye")
        exit()

    elif user_selection == "1":
        show_all_students_info(all_students)
    elif user_selection == "5":
        student = {}
        name = input("enter student's name: ")
        # try:
        #     user_input = input("enter student's age: ")
        #     age = int(user_input)
        # except:
        #     print(f'{user_input} is not valid. you must enter an integer!!!')
        age = ""
        while not age.isdecimal():
            age = input("enter student's age: ")
        age = int(age)

        course = input("enter course's name: ")
        student['name'] = name
        student['age'] = age
        student['course'] = course
        all_students.append(student)
