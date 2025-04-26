from rest_framework.routers import DefaultRouter
from .views import HealthProgramViewSet, ClientViewSet, EnrollmentViewSet, register_user, login_user, client_profile,ClientSearchView
from django.urls import path, include

router = DefaultRouter()
router.register(r'health_programs', HealthProgramViewSet, basename='healthprogram')
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('profile/<int:client_id>/', client_profile, name='client_profile'),
    path('clients/search/', ClientSearchView.as_view(), name='client_search'),
      path('', include(router.urls)),
]