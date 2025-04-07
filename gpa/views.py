from rest_framework import viewsets,generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import CustomUser, Student, Course, Enrollment, Assessment, Score, GradeScale, Projection,Major
from .serializers import (
    CustomUserSerializer, StudentSerializer, CourseSerializer, EnrollmentSerializer, 
    AssessmentSerializer, ScoreSerializer, GradeScaleSerializer, ProjectionSerializer,MajorSerializer
)
from rest_framework.views import APIView
from django.db import transaction
# User ViewSet
class RegisterView(APIView):
    permission_classes = [AllowAny]

    @transaction.atomic
    def post(self, request):
        user_serializer = CustomUserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            Student.objects.create(user=user, student_number=f"STD-{user.id}")
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------------------------------
# ViewSets for Models
# -------------------------------
class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Student.objects.filter(user=self.request.user)


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

class MajorListView(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer