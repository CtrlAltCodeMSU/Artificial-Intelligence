class Student:
    def __init__(self, name):
        self.__name = name
        self.__grades = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError("Name must be a String")
    
    def add_grade(self, grade):
        if isinstance(grade, (int, float)) and 0 <= grade <= 100:
            self.__grades.append(grade)
        else:
            raise ValueError("Grade must be between 0 and 100")
    
    def get_average(self):
        if len(self.__grades) > 0:
            return sum(self.__grades) / len(self.__grades)
        else:
            return 0
    
    def display_grades(self):
        return self.__grades

def student_details():
    
    name = input("Enter student's name: ")
    
    student1 = Student(name)
    
    for i in range(5):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))  
                if 0 <= grade <= 100:  
                    student1.add_grade(grade)
                    break  
                else:
                    print("Grade must be between 0 and 100")
            except ValueError:
                print("Please enter a valid number for the grade")
    
    print(f"Student: {student1.name}")
    print(f"Grades: {student1.display_grades()}")
    print(f"Average Grade: {student1.get_average()}")

student_details()
