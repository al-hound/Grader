from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from .models import Student, Module, LearningOutcomeGrade, FormativeCycle

def index_view(request):
    formative_cycles = FormativeCycle.objects.all()
    students = []

    if request.method == 'GET':
        cycle_id = request.GET.get('cycle')

        if cycle_id:
            students = Student.objects.filter(modules__formative_cycle__id=cycle_id).distinct()

    return render(request, 'grader/index.html', {
        'formative_cycles': formative_cycles,
        'students': students,
    })


def student_grades_view(request):
    students = Student.objects.all()
    student_grades = []

    for student in students:
        student_data = {
            'student': student,
            'modules': []
        }
        for module in student.modules.all():
            learning_outcomes = module.learning_outcomes.all()
            grades = LearningOutcomeGrade.objects.filter(student=student, learning_outcome__in=learning_outcomes)
            average_grade = grades.aggregate(Avg('grade'))['grade__avg'] or 0.0
            module_data = {
                'module': module,
                'grades': grades,
                'average_grade': average_grade
            }
            student_data['modules'].append(module_data)
        student_grades.append(student_data)
    
    return render(request, "grader/student_grades.html", {
        'student_grades': student_grades
    })


def student_detail_view(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    modules = student.modules.all()
    module_grades = []

    for module in modules:
        learning_outcomes = module.learning_outcomes.all()
        grades = LearningOutcomeGrade.objects.filter(student=student, learning_outcome__in=learning_outcomes)
        
        weighted_sum = 0
        total_weight = 0
        for grade in grades:
            weight = grade.learning_outcome.weight
            weighted_sum += float(grade.grade) * weight
            total_weight += weight
        
        average_grade = round(weighted_sum / total_weight, 2) if total_weight > 0 else 0
        
        module_data = {
            'module': module,
            'grades': grades,
            'average_grade': average_grade
        }
        module_grades.append(module_data)
        
    return render(request, 'grader/student_detail.html', {
        'student': student,
        'module_grades': module_grades
    })