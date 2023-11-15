# from faker import Faker
import random
from .models import *
from django.db.models import Sum


# fake = Faker()

# to generate random student


# def generate(n=10) -> None:
#     try:
#         for i in range(0, n):

#             department_objs = Department.objects.all()
#             random_index = random.randint(0, len(department_objs)-1)
#             department = department_objs[random_index]
#             student_id = f'STU-0{random.randint(100,999)}'
#             student_name = fake.name()
#             student_email = fake.email()
#             student_age = random.randint(20, 30)
#             student_address = fake.address()

#             student_id_obj = StudentID.objects.create(student_id=student_id)

#             student_obj = Student.objects.create(
#                 department=department,
#                 student_id=student_id_obj,
#                 student_name=student_name,
#                 student_email=student_email,
#                 student_age=student_age,
#                 student_address=student_address
#             )
#             student_obj.save()
#     except Exception:
#         print(Exception)


# To generate marks for student
# def create_subject_marks():
#     try:
#         student_objs = Student.objects.all()
#         for student in student_objs:
#             subjects = Subject.objects.all()
#             for subject in subjects:
#                 SubjectMarks.objects.create(
#                     subject=subject,
#                     student=student,
#                     marks=random.randint(10, 100)
#                 )

#     except Exception as e:
#         print(e)


def generate_report_card():
    ranks = Student.objects.annotate(
        marks=Sum('studentmarks__marks')).order_by('-marks')

    for i, rank in enumerate(ranks):
        ReportCard.objects.create(
            student=rank,
            student_rank=i+1,
        )
