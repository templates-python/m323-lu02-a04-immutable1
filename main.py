students = [
    ('Alice', 20, 1),
    ('Bob', 22, 2),
    ('Charlie', 19, 3),
]

def print_students(student_list):
    print('Studenten Informationen:')
    for student in student_list:
        name, age, student_id = student
        print(f'Name: {name}, Alter: {age}, ID: {student_id}')

if __name__ == '__main__':
    print_students(students)