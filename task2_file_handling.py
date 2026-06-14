number = int(input("How many students? "))

with open("student.txt","w") as file:

    for i in range(number):

        name = input("Enter student name: ")

        file.write(name + "\n")

print("Student names stored successfully")

with open("student.txt","r") as file:

    text = file.read()

    print("\nStudent Names:")
    print(text)