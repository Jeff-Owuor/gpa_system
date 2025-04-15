
from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from gpa.views import StudentViewSet, CourseViewSet, EnrollmentViewSet, AssessmentViewSet, ScoreViewSet, GradeScaleViewSet, ProjectionViewSet, MajorListView

schema_view = get_schema_view(
    openapi.Info(
        title = "API Docs.",
        default_version = "v1",
        description = "lorem ipsum"
    ),
    public = True,
    permission_classes = (permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'students', StudentViewSet,basename='student')
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'assessments', AssessmentViewSet)
router.register(r'scores', ScoreViewSet)
router.register(r'grade-scales', GradeScaleViewSet)
router.register(r'projections', ProjectionViewSet)
router.register(r'majors', MajorListView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include("dj_rest_auth.urls")),
    path("auth/registration",include("dj_rest_auth.registration.urls")),
    path(
        "swagger<format>/",schema_view.without_ui(cache_timeout=0),name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger",cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/",schema_view.with_ui("redoc",cache_timeout=0),name="schema-redoc"),
    path('api/', include(router.urls)),
    
    
]
