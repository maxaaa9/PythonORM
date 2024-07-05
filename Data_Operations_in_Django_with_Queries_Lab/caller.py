import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Student


def add_students():
    students_list = [
        {'student_id': 'FC5204',
         'first_name': 'John',
         'last_name': 'Doe',
         'birth_date': '1995-05-15',
         'email': 'john.doe@university.com'},

        {'student_id': 'FE0054',
         'first_name': 'Jane',
         'last_name': 'Smith',
         'birth_date': None,
         'email': 'jane.smith@university.com'},

        {'student_id': 'FH2014',
         'first_name': 'Alice',
         'last_name': 'Johnson',
         'birth_date': '1998-02-10',
         'email': 'alice.johnson@university.com'},

        {'student_id': 'FH2015',
         'first_name': 'Bob',
         'last_name': 'Wilson',
         'birth_date': '1996-11-25',
         'email': 'bob.wilson@university.com'}
    ]

    students = [
        Student(
            student_id=data['student_id'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            birth_date=data['birth_date'],
            email=data['email']
        )
        for data in students_list
    ]
    Student.objects.bulk_create(students)


def get_students_info():
    my_student_info = []
    for student in Student.objects.all():
        my_student_info.append(f"Student №{student.student_id}: "
                               f"{student.first_name} "
                               f"{student.last_name}; "
                               f"Email: {student.email}")

    return '\n'.join(my_student_info)


def update_students_emails():
    for students in Student.objects.all():
        students.email = students.email.replace(students.email.split("@")[1], "uni-students.com")
        students.save()


def truncate_students():
    Student.objects.all().delete()


# Run and print your queries


# update_students_emails()
# for student in Student.objects.all():
#     print(student.email)
# truncate_students()
# print(Student.objects.all())
# print(f"Number of students: {Student.objects.count()}")

