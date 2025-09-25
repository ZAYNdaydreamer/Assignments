# SRMS using Nested List

students = []

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Record")
    print("6. Sort by Marks")
    print("7. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        name = input("Name: ")
        roll = input("Roll: ")
        sub = input("Subject: ")
        marks = int(input("Marks: "))
        students.append([name, roll, sub, marks])

    elif ch == "2":
        for s in students:
            print(s)

    elif ch == "3":
        r = input("Enter roll: ")
        for s in students:
            if s[1] == r:
                print("Found:", s)
                break
        else:
            print("Not found")

    elif ch == "4":
        r = input("Roll to update: ")
        for s in students:
            if s[1] == r:
                s[3] = int(input("New marks: "))
                print("Updated!")
                break

    elif ch == "5":
        r = input("Roll to delete: ")
        for s in students:
            if s[1] == r:
                students.remove(s)
                print("Deleted!")
                break

    elif ch == "6":
        students.sort(key=lambda x: x[3], reverse=True)
        print("Sorted!")

    elif ch == "7":
        break

    else:
        print("Invalid choice")

# SRMS using List of Dictionaries

students = []

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Record")
    print("6. Sort by Marks")
    print("7. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        stu = {
            "name": input("Name: "),
            "roll": input("Roll: "),
            "sub": input("Subject: "),
            "marks": int(input("Marks: "))
        }
        students.append(stu)

    elif ch == "2":
        for s in students:
            print(s)

    elif ch == "3":
        r = input("Enter roll: ")
        for s in students:
            if s["roll"] == r:
                print("Found:", s)
                break
        else:
            print("Not found")

    elif ch == "4":
        r = input("Roll to update: ")
        for s in students:
            if s["roll"] == r:
                s["marks"] = int(input("New marks: "))
                print("Updated!")
                break

    elif ch == "5":
        r = input("Roll to delete: ")
        for s in students:
            if s["roll"] == r:
                students.remove(s)
                print("Deleted!")
                break

    elif ch == "6":
        students.sort(key=lambda x: x["marks"], reverse=True)
        print("Sorted!")

    elif ch == "7":
        break

    else:
        print("Invalid choice")