from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class FormativeCycle(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=9)  # Example: 2023-2024

    def __str__(self):
        return f"{self.name} ({self.course})"

class Module(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    formative_cycle = models.ForeignKey(FormativeCycle, related_name='modules', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dni = models.CharField(max_length=9, unique=True)
    birth_date = models.DateField()
    modules = models.ManyToManyField(Module, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class LearningOutcome(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    weight = models.FloatField(default=1.0, validators=[MinValueValidator(0.0), MaxValueValidator(1)])  # Pes de la RA
    module = models.ForeignKey(Module, related_name='learning_outcomes', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code}: {self.name}"

class LearningOutcomeGrade(models.Model):
    student = models.ForeignKey(Student, related_name='grades', on_delete=models.CASCADE)
    learning_outcome = models.ForeignKey(LearningOutcome, related_name='grades', on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.student} - {self.learning_outcome}: {self.grade}"
