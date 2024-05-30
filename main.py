"""1masala"""

# class Student:

#     def __init__(self, ism) -> None:
#         self.ism = ism

#     def __iter__(self):
#         return self

#     def __next__(self):
#         try:
#             return "next ishlayapdi"
#         except IndexError:
#             raise StopIteration


# for i in Student("salom"):
#     print(i)

"""2masala"""


# class Student:

#     objects = []
#     count = 0

#     def __init__(self, f_name):
#         self.f_name = f_name
#         self.objects.append(self)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         try:
#             object = self.objects[self.count]
#             self.count += 1
#             return object.f_name
#         except IndexError:
#             self.count = 0
#             raise StopIteration


# Student("Noila")
# Student("zilola")
# Student("Bonu")
# Student("Shahlo")

# for student in Student("Sarvinoz"):
#     print(student)

"""3masala"""


# class Student:

#     objects = []
#     count = 0

#     def __init__(self, f_name):
#         self.f_name = f_name
#         self.objects.append(self)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         try:
#             object = self.objects[self.count]
#             self.count += 1
#             return object.f_name
#         except IndexError:
#             self.count = 0
#             raise StopIteration


# Student("Noila")
# Student("zilola")
# Student("Bonu")
# Student("Shahlo")

# data = list(filter(lambda x: x.istitle(), Student("Sarvinoz")))

# print(data)


"""4masala"""


class Student:

    objects = []
    count = 0

    def __init__(self, id, f_name):
        self.id = id
        self.f_name = f_name
        self.objects.append(self)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            object = self.objects[self.count]
            self.count += 1
            return object.id
        except IndexError:
            self.count = 0
            raise StopIteration


Student(1, "Noila")
Student(2, "zilola")
Student(3, "Bonu")
Student(4, "Shahlo")

for student in Student(5, "Sarvinoz"):
    print("id: ", student)
