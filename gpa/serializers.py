from rest_framework import serializers
from .models import CustomUser, Student, Course, Enrollment, Assessment, Score, GradeScale, Projection,Major

# Custom user serializer with password hashing
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        # Automatically create associated student record
        Student.objects.create(user=user, student_number=f"S{user.id}")
        return user

# Student serializer that shows user info (read-only)
class StudentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Student
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'

class GradeScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeScale
        fields = '__all__'

class ProjectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projection
        fields = '__all__'
class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = '__all__'