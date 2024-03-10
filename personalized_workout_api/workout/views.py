from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import logout
from .forms import WorkoutPlanForm
from .models import WorkoutPlan
from rest_framework.permissions import IsAuthenticated

class MyProtectedAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'This is a protected endpoint'}
        return Response(content)


class UserRegistrationAPIView(APIView):
    def post(self, request):
        form = UserRegistrationForm(request.data)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            User.objects.create_user(username=username, email=email, password=password)
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):
    def post(self, request):
        form = UserLoginForm(request.data)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)


class WorkoutPlanListCreateAPIView(APIView):
    def get(self, request):
        workout_plans = WorkoutPlan.objects.all()
        data = [{'id': workout_plan.id, 'title': workout_plan.title, 'description': workout_plan.description} for workout_plan in workout_plans]
        return Response(data)

    def post(self, request):
        form = WorkoutPlanForm(request.data)
        if form.is_valid():
            form.save()
            return Response({'message': 'Workout plan created successfully'}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkoutPlanDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return WorkoutPlan.objects.get(pk=pk)
        except WorkoutPlan.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        workout_plan = self.get_object(pk)
        data = {'id': workout_plan.id, 'title': workout_plan.title, 'description': workout_plan.description}
        return Response(data)

    def put(self, request, pk):
        workout_plan = self.get_object(pk)
        form = WorkoutPlanForm(request.data, instance=workout_plan)
        if form.is_valid():
            form.save()
            return Response({'message': 'Workout plan updated successfully'})
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        workout_plan = self.get_object(pk)
        workout_plan.delete()
        return Response({'message': 'Workout plan deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
