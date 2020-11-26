groupmates = [
 {
 "name": "Елизавета",
 "surname": "Вязовова",
 "exams": ["Информатика", "ОАП", "Web"],
 "marks": [4, 3, 5]
 },
 {
 "name": "Темирлан",
 "surname": "Дзариев",
 "exams": ["Web", "ОБД", "История"],
 "marks": [5, 5, 4]
 },
 {
 "name": "Анастасия",
 "surname": "Алпатова",
 "exams": ["История", "ОБД", "ОАП"],
 "marks": [5, 4, 5]
 },
 {
 "name": "Данила",
 "surname": "Золотухин",
 "exams": ["Философия", "Web", "ОБД"],
 "marks": [3, 5, 5]
 },
{
 "name": "Кирилл",
 "surname": "Сорокин",
 "exams": ["Информатика", "История", "Философия"],
 "marks": [5, 3, 4]
 }
]

def print_students(students):
 print(u"Имя".ljust(15), u"Фамилия".ljust(10),
u"Экзамены".ljust(30), u"Оценки".ljust(20))
 for student in students:
    print(student["name"].ljust(15),
    student["surname"].ljust(10), str(student["exams"]).ljust(30),
    str(student["marks"]).ljust(20))
print_students(groupmates)
