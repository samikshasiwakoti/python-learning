# student record system
# we have to add student, view all students, search student

def add_student():
    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    with open("students.txt", "a") as f:
        f.write(name + "," + marks + "\n")

    print("Student added successfully\n")


def view_students():
    print("\n--- Student List ---")

    try:
        with open("students.txt", "r") as f:
            data = f.read()

            if data == "":
                print("No records found!\n")
            else:
                print(data)

    except FileNotFoundError:
        print("No records found!\n")


def search_student():
    name = input("Enter name to search: ").strip().lower()

    try:
        with open("students.txt", "r") as f:
            found = False

            for line in f:
                data = line.strip().split(",")

                if data[0].strip().lower() == name:
                    print(f" Name: {data[0]}, Marks: {data[1]}")
                    found = True
                    break

            if not found:
                print("Student not found!")

    except FileNotFoundError:
        print("No data available!")


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")