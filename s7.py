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

print(message)
print("Enter a number : ")
user_selection = input("> ")
if user_selection == "0":
    print("bye")
    exit()
elif user_selection == "5":
    student = {}
    name = input("enter student's name: ")
    age = int(input("enter student's age: "))
    course = input("enter course's name: ")
    student['name'] = name
    student['age'] = age
    student['course'] = course
    all_students.append(student)
