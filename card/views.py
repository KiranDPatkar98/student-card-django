from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from django.db.models.functions import Rank
# Create your views here.


def get_students(request):
    queryset = Student.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains=search) |
            Q(department__department__icontains=search) |
            Q(student_email__icontains=search) |
            Q(student_age__icontains=search)
        )

    paginator = Paginator(queryset, 10)  # Show 10 contacts per page.
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'report/students.html', context={'students': page_obj})


def see_marks(request, student_id):
    query_set = SubjectMarks.objects.filter(
        student__student_id__student_id=student_id)
    total_marks = query_set.aggregate(total_marks=Sum('marks'))

    # grouping the values on the bais of student
    # ranks = SubjectMarks.objects.values('student__student_id').annotate(
    #     total_marks=Sum('marks')
    # ).order_by('-total_marks')

    # ranks = Student.objects.annotate(
    #     marks=Sum('studentmarks__marks')).order_by('-marks')

    # student_rank = 1

    # for i, rank in enumerate(ranks):
    #     if student_id == rank.student_id.student_id:
    #         student_rank = i+1
    #         break

    return render(request, 'report/marks.html', context={'marks': query_set, "total_marks": total_marks})
