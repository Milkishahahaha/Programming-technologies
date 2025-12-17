class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.marks = [] 
    
    def get_full_name(self):
        return f"{self.name} {self.surname}"
    
    def add_mark(self, mark):
        if 1 <= mark <= 5:
            self.marks.append(mark)
        else:
            print(f"Оценка {mark} недопустима")
    
    def get_average_mark(self):
        if not self.marks:  
            return 0.0
        return sum(self.marks) / len(self.marks)
    

student = Student("Миляуша", "Фасхутдинова")
print(student.get_full_name()) 

student.add_mark(5)
student.add_mark(4)
student.add_mark(3)
student.add_mark(6)  

print(student.get_average_mark())
    


