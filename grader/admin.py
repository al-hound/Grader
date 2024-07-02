from django.contrib import admin
from .models import FormativeCycle, Module, Student, LearningOutcome, LearningOutcomeGrade

@admin.register(FormativeCycle)
class FormativeCycleAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'course')
    search_fields = ('name', 'course')

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'formative_cycle')
    search_fields = ('name',)
    list_filter = ('formative_cycle',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dni', 'birth_date')
    search_fields = ('first_name', 'last_name', 'dni')
    list_filter = ('modules',)
    filter_horizontal = ('modules',)

@admin.register(LearningOutcome)
class LearningOutcomeAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'module')
    search_fields = ('name', 'module__name')
    list_filter = ('module',)

@admin.register(LearningOutcomeGrade)
class LearningOutcomeGradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'learning_outcome', 'grade')
    search_fields = ('student__first_name', 'student__last_name', 'learning_outcome__name')
    list_filter = ('student', 'learning_outcome')

