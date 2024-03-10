from django.urls import path
from .views import (
    UserRegistrationAPIView,
    UserLoginAPIView,
    UserLogoutAPIView,
    WorkoutPlanListCreateAPIView,
    WorkoutPlanDetailAPIView,
    MyProtectedAPIView
)

urlpatterns = [
    path('my_protected_view/', MyProtectedAPIView.as_view(), name='my_protected_view'),
    path('register/', UserRegistrationAPIView.as_view(), name='register_user'),
    path('login/', UserLoginAPIView.as_view(), name='login_user'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout_user'),

    # Workout plan CRUD operation URLs
    path('workout_plans/', WorkoutPlanListCreateAPIView.as_view(), name='workout_plan_list_create'),
    path('workout_plans/<int:pk>/', WorkoutPlanDetailAPIView.as_view(), name='workout_plan_detail'),
]
