from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, Student, Course, Enrollment, Assessment, Score, GradeScale, Projection
from .serializers import (
    CustomUserSerializer, StudentSerializer, CourseSerializer, EnrollmentSerializer, 
    AssessmentSerializer, ScoreSerializer, GradeScaleSerializer, ProjectionSerializer
)

# User ViewSet
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

# Student ViewSet
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

# Course ViewSet
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

# Enrollment ViewSet
class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

# Assessment ViewSet
class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [IsAuthenticated]

# Score ViewSet
class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [IsAuthenticated]

# Grade Scale ViewSet
class GradeScaleViewSet(viewsets.ModelViewSet):
    queryset = GradeScale.objects.all()
    serializer_class = GradeScaleSerializer
    permission_classes = [IsAuthenticated]

# GPA Projection ViewSet
class ProjectionViewSet(viewsets.ModelViewSet):
    queryset = Projection.objects.all()
    serializer_class = ProjectionSerializer
    permission_classes = [IsAuthenticated]
