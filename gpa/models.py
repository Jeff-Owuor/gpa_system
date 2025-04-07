from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
# Create your models here.

# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email

class Major(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    student_number = models.CharField(max_length=20, unique=True)
    major = models.ForeignKey(Major, on_delete=models.SET_NULL, null=True, blank=True)
    cumulative_gpa = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    total_credit_hours = models.IntegerField(default=0)


class Course(models.Model):
    course_code = models.CharField(max_length=10, unique=True)
    course_name = models.CharField(max_length=100)
    credit_hours = models.IntegerField()
    major = models.ForeignKey(Major, on_delete=models.CASCADE)

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=20)
    year = models.IntegerField()
    projected_grade = models.CharField(max_length=2, blank=True, null=True)
    actual_grade = models.CharField(max_length=2, blank=True, null=True)

class Assessment(models.Model):
    QUIZ = 'Quiz'
    ASSIGNMENT = 'Assignment'
    ATTENDANCE = 'Attendance'
    MIDTERM = 'Midterm'
    FINAL = 'Final Exam'
    ASSESSMENT_TYPES = [
        (QUIZ, 'Quiz'),
        (ASSIGNMENT, 'Assignment'),
        (ATTENDANCE, 'Attendance'),
        (MIDTERM, 'Midterm'),
        (FINAL, 'Final Exam')
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assessment_type = models.CharField(max_length=20, choices=ASSESSMENT_TYPES)
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # e.g. 20.00 for 20%
    total_marks = models.DecimalField(max_digits=6, decimal_places=2)  # e.g. out of 20 or 100

class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=6, decimal_places=2)

class GradeScale(models.Model):
    letter_grade = models.CharField(max_length=2)
    min_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    max_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    gpa_value = models.DecimalField(max_digits=3, decimal_places=2)

class Projection(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    current_gpa = models.DecimalField(max_digits=4, decimal_places=2)
    desired_gpa = models.DecimalField(max_digits=4, decimal_places=2)
    required_final_exam_score = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    is_on_track = models.BooleanField(default=True)