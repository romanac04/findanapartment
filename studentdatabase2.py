students = [
    {"name": "Sarah", "hometown": "Detroit", "favorite_food": "sushi"},
    {"name": "Fred", "hometown": "Ann Arbor", "favorite_food": "pizza"},
    {"name": "Mike","hometown": "Sterling Heights", "favorite_food":"tacos" },
    {"name": "Aria", "hometown": "Grand Rapids", "favorite_food": "burgers"}
]
while True:
    action = input("Please select which action you'd like to do: add, view, or quit ")
    if action == "add":
        def get_new_student():
            student = {}
            name = input("Enter name: ")
            hometown = input("Enter hometown: ")
            favorite_food = input("Enter favorite food: ")
            student['name'] = name
            student['hometown'] = hometown
            student['favorite food'] = favorite_food
            return student
        new_student = get_new_student()
        students.append(new_student)
        print(students)
    elif action == "view":
        def list_names(students):
            for student in students:
                print(student["name"])
        list_names(students)
        number_of_students = len(students)
        student_choice = int(input(f"Welcome! Which student would you like to learn more about? Enter number 1 through {number_of_students} "))
        student = students[student_choice-1]
        information = input("Enter hometown or favorite food ")
        if information == "hometown":
            print(f"{student['name']} is from {student['hometown']}")
            continue
        elif information == "favorite food":
            print(f"{student['name']} favorite food is {student['favorite_food']}")
        else:
            print("Invalid choice. Try again.")

    elif action == "quit":
        print("Good bye!")
        break
    else:
        print("Invalid. Try again.")