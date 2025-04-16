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
        read_only_fields = ('user',)

    def update(self, instance, validated_data):
        # Let student update their own info
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class AssessmentSerializer(serializers.ModelSerializer):
    assessment_type_display = serializers.CharField(source='get_assessment_type_display', read_only=True)
    class Meta:
        model = Assessment
        fields = ['id', 'course', 'assessment_type', 'assessment_type_display', 'weight', 'total_marks']

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'

class GradeScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeScale
        fields = '__all__'

class ProjectionSerializer(serializers.ModelSerializer):
    projected_cumulative_gpa = serializers.DecimalField(
        max_digits=4, decimal_places=2, read_only=True
    )

    class Meta:
        model = Projection
        fields = [
            'id', 'student', 'semester', 'desired_semester_gpa', 'total_credit_hours',
            'required_average_final_exam_score', 'projected_cumulative_gpa', 'is_on_track'
        ]
        read_only_fields = ['projected_cumulative_gpa', 'is_on_track']

    def create(self, validated_data):
        projection = Projection.objects.create(**validated_data)
        projection.projected_cumulative_gpa = projection.calculate_projected_cumulative_gpa()
        projection.save()
        return projection

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.projected_cumulative_gpa = instance.calculate_projected_cumulative_gpa()
        instance.save()
        return instance

class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = '__all__'