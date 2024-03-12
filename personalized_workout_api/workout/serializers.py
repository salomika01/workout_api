# serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import WorkoutPlan, Exercise, WorkoutPlanExercise, Progress

class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = ['id', 'user', 'title', 'description', 'created_at']

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'created_at', 'target_muscles']

class WorkoutPlanExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlanExercise
        fields = ['id', 'workout_plan', 'exercise', 'sets', 'repetitions', 'notes']

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ['id', 'user', 'date', 'workout_plan', 'completed',]

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
