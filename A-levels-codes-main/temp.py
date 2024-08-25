# Student

class Student:
    def __init__(self, name, examMark):
        self.name = name
        self.dateOfBirth = None
        self.examMark = examMark

    def displayExamMark(self):
        print(f"{self.name} scored {self.examMark}")


class PartTimeStudent(Student):
    def __init__(self, name, examMark):
        Student.__init__(self, name, examMark)
        self.name = name
        self.examMark = examMark


class FullTimeStudent(Student):
    def __init__(self, name, examMark):
        Student.__init__(self, name, examMark)
        self.name = name
        self.examMark = examMark


student = FullTimeStudent("Simba", 22)
student.displayExamMark()
