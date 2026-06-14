students = {}

while True:

    print("\n111. Add Student")
    print("2. Search Student")
    print("3. Display Students")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        roll = input("Enter roll no: ")

        name = input("Enter name: ")
        marks = input("Enter marks: ")
        contact = input("Enter contact number: ")

        students[roll] = {
            "name": name,
            "marks": marks,
            "contact": contact
        }

        print("Student added successfully")

    elif choice == "2":

        roll = input("Enter roll no to search: ")

        if roll in students:

            print("Name:", students[roll]["name"])
            print("Marks:", students[roll]["marks"])
            print("Contact:", students[roll]["contact"])

        else:

            print("Student not found")

    elif choice == "3":

        for roll in students:

            print("\nRoll:", roll)
            print("Name:", students[roll]["name"])
            print("Marks:", students[roll]["marks"])
            print("Contact:", students[roll]["contact"])

    elif choice == "4":

        break

    else:

        print("Invalid choice")