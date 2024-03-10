
from .models import WorkoutPlan, Exercise, Progress, WorkoutPlanExercise
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)



class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = ['title', 'description']

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'description']

class WorkoutPlanExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlanExercise
        fields = ['workout_plan', 'exercise', 'sets', 'repetitions', 'notes']

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['user', 'workout_plan', 'date', 'completed']
