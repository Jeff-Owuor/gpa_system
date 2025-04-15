from django.contrib import admin
from .models import CustomUser, Student, Course, Enrollment, Assessment, Score, GradeScale, Projection,Major

# Register your models
admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Major)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Assessment)
admin.site.register(Score)
admin.site.register(GradeScale)
admin.site.register(Projection)