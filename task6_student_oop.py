class Student:

    def setData(self):

        self.name = input("Enter name: ")
        self.roll = input("Enter roll no: ")
        self.marks = input("Enter marks: ")

    def getData(self):

        print("\nStudent Details")
        print("Name :", self.name)
        print("Roll No :", self.roll)
        print("Marks :", self.marks)

obj = Student()

obj.setData()

obj.getData()