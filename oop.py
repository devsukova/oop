class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        Student_Info = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average_grade():.2f}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return Student_Info

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def rate_lecturer (self, lecturer, course, grade): # Оценка Лектору
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self): # Средняя оценка
        grades = [g for course in self.grades.values() for g in course]
        return sum(grades) / len(grades) if grades else 0

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self): # Средняя оценка
        grades = [g for course in self.grades.values() for g in course]
        return sum(grades) / len(grades) if grades else 0

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade():.2f}')

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()
    # grades = {} 

class Reviewer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        Mentor_Info = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return Mentor_Info

    def rate_hw(self, student, course, grade): # Оценка за домашнее задание
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Тестируем

# Студенты
student1 = Student('Игорь', 'Игорев', 'М')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Git', 'C++']

student2 = Student('Мария', 'Иванова', 'Ж')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Git']

# Лекторы
lecturer1 = Lecturer('Егор', 'Сидоров')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Светлана', 'Петрова')
lecturer2.courses_attached += ['Python']

# Проверяющие
reviewer1 = Reviewer('Дмитрий', 'Орлов')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Елена', 'Кузнецова')
reviewer2.courses_attached += ['Python'] 

# Проверяющие оценивают студентов
reviewer1.rate_hw(student1, 'Python', 5)
reviewer2.rate_hw(student1, 'Python', 7)

reviewer1.rate_hw(student2, 'Python', 2)
reviewer2.rate_hw(student2, 'Python', 6)

# Студенты оценивают лекторов
student1.rate_lecturer(lecturer1, 'Python', 6)
student1.rate_lecturer(lecturer2, 'Python', 3)

student2.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer2, 'Python', 5)

print(student1)
print()
print(student2)
print()
print(lecturer1)
print()
print(lecturer2)
print()
print(reviewer1)
print()

print(f'Сравнение студентов: {student1 < student2}')
print(f'Сравнение лекторов: {lecturer1 > lecturer2}')

def average_student_grade(students, course):
    total = grades = 0
    for s in students:
        if course in s.grades:
            total += sum(s.grades[course])
            grades += len(s.grades[course])
    return total / grades if grades else 0

def average_lecturer_grade(lecturers, course):
    total = grades = 0
    for l in lecturers:
        if course in l.grades:
            total += sum(l.grades[course])
            grades += len(l.grades[course])
    return total / grades if grades else 0

print(f'Средняя оценка студентов по курсу Python: {average_student_grade([student1, student2], "Python"):.2f}')
print(f'Средняя оценка лекторов по курсу Python: {average_lecturer_grade([lecturer1, lecturer2], "Python"):.2f}')