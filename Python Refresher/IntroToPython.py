tuple = (1,2,3)
tuple = tuple + (1,)
print(tuple)

tuple = 1,
print(tuple)

set_grade = {1,2,3}
## set_grade[2]=9
set_grade.add(3)
print(set_grade)

print(set_grade.intersection({1}))

user_wants_input = "n"
while user_wants_input=="y":
    print(10)
    user_wants_input = input("y/n? ")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Modify the method below to make sure only even numbers are returned.
def even_numbers():
    evens = []
    for number in numbers:
        if number%2==0:
            evens.append(number)
    return evens


# Modify the below method so that "Quit" is returned if the choice parameter is "q".
# Don't remove the existing code
def user_menu(choice):
    if choice == "a":
        return "Add"
    if choice == "q":
        return "Quit"

test = "Alok"
print("name is {}".format(test))
print("{}".format("Alok"))

# def who_do_you_know():
#     return [names.strip().lower() for names in input("Who do you know? ").split(",")]
#
# known_people = who_do_you_know()
#
# def ask_user():
#     name = input("Give me a name - ")
#     if name in known_people:
#         print("You know {}".format(name))
#
# ask_user()

# range_5 = [x*3 for x in range(5)]
#
# print(range_5)
#
# print([n for n in range(10) if n%2==0])



# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {'name':'Jose','school':'Computing','grades':(50,)}

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades =   data['grades']
    return sum(grades) / len(grades)


# Implement the function below
# Given a list of students (dictionaries), calculate the average grade of the class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = len(student_list)
    for student in student_list:
        total+=average_grade(student)

    return total / count


print(average_grade_all_students([student]))