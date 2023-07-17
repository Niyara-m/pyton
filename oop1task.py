class Student:
    def __init__(self, name = 'Ivan', age = 18, group_number = '10A'):
        self.name = name
        self.age = age
        self.group_number = group_number

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.group_number

    def setNameAge(self, new_age):
        self.age = new_age

    def setGroupNumber(self, new_group):
        self.group_number = new_group

student1 = Student('Nikita', 14, '9B')
student2 = Student('Artem', 8, '1B')
student3 = Student('Bagdan', 14, '8A')
student4 = Student('Oleg', 15, '9b')
student5 = Student('Volodya', 16, '11C')

students = [student1, student2, student3, student4, student5]

while True:
    student_name = input("Информацию о каком студенте вы хотите получить (student1,student2,student3,student4,student5)")
    student_index = student_name[-1]
    choice = int(input('1-Имя студента, 2-возраст студента, 3-номере группы студента, 4-изменить возраст, 5-изменить номер группы'))


    if choice == 1:
        print(students[int(student_index) - 1].getName())
    elif choice == 2:
        print(students[int(student_index) - 1].getAge())
    elif choice == 3:
        print(students[int(student_index) - 1].getGroupNumber())
    elif choice == 4:
        age = int(input('Введите возраст для изменения'))
        students[int(student_index) - 1].setNameAge(age)
        print(students[int(student_index) - 1].age)
    elif choice == 5:
        group = input('Введите группу для изменения')
        students[int(student_index) - 1].setGroupNumber(group)
        print(students[int(student_index) - 1].group_number)
    else:
        print('I dont understand you')