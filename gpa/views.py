from rest_framework import viewsets,generics,mixins
from rest_framework.decorators import action
from rest_framework.response import Response
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
            user_serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------------------------------
# ViewSets for Models
# -------------------------------
class StudentViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()

    @action(detail=False, methods=['get', 'patch'], url_path='me')
    def me(self, request):
        student = request.user.student
        if request.method == 'GET':
            serializer = self.get_serializer(student)
            return Response(serializer.data)
        elif request.method == 'PATCH':
            serializer = self.get_serializer(student, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

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
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        student = self.request.user.student  # Assumes logged-in user is a Student
        serializer.save(student=student)

class MajorListView(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer