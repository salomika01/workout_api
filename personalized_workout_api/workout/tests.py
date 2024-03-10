
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import WorkoutPlan

class WorkoutAPITests(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_workout_list(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        # Create some workout entries
        WorkoutPlan.objects.create(user=self.user, date='2024-01-01', duration='01:00:00', calories_burned=300)
        WorkoutPlan.objects.create(user=self.user, date='2024-01-02', duration='00:45:00', calories_burned=250)

        response = client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_workout(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        data = {'date': '2024-01-03', 'duration': '00:55:00', 'calories_burned': 275}

        response = client.post('/api/workouts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the workout entry was created
        self.assertTrue(WorkoutPlan.objects.filter(user=self.user, date='2024-01-03', duration='00:55:00', calories_burned=275).exists())

    def test_update_workout(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        workout = WorkoutPlan.objects.create(user=self.user, date='2024-01-04', duration='00:50:00', calories_burned=270)

        data = {'date': '2024-01-05', 'duration': '01:05:00', 'calories_burned': 320}

        response = client.put(f'/api/workouts/{workout.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the workout entry was updated
        workout.refresh_from_db()
        self.assertEqual(workout.date.strftime('%Y-%m-%d'), '2024-01-05')
        self.assertEqual(workout.duration, '01:05:00')
        self.assertEqual(workout.calories_burned, 320)

    def test_delete_workout(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        workout = WorkoutPlan.objects.create(user=self.user, date='2024-01-06', duration='00:55:00', calories_burned=280)

        response = client.delete(f'/api/workouts/{workout.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check if the workout entry was deleted
        self.assertFalse(WorkoutPlan.objects.filter(id=workout.id).exists())
