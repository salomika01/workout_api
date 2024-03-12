from .models import Exercise

exercises = [
    {
        'name': 'Push-up',
        'description': 'A basic bodyweight exercise targeting the chest, shoulders, and triceps.',
        'instructions': 'Start in a plank position with hands shoulder-width apart. Lower your body until your chest nearly touches the ground, then push back up to the starting position.',
        'target_muscles': 'Chest, Shoulders, Triceps'
    },
    {
        'name': 'Squat',
        'description': 'A fundamental lower body exercise targeting the quadriceps, hamstrings, and glutes.',
        'instructions': 'Stand with feet shoulder-width apart. Lower your body by bending your knees and pushing your hips back, as if sitting in a chair. Keep your chest up and back straight. Return to the starting position by pushing through your heels.',
        'target_muscles': 'Quadriceps, Hamstrings, Glutes'
    },
    {
        'name': 'Pull-up',
        'description': 'An upper body exercise targeting the back, biceps, and forearms.',
        'instructions': 'Hang from a pull-up bar with hands shoulder-width apart and palms facing away. Pull your body upward until your chin clears the bar, then lower yourself back down to the starting position.',
        'target_muscles': 'Back, Biceps, Forearms'
    },
    {
        'name': 'Deadlift',
        'description': 'A compound exercise targeting multiple muscle groups including the back, legs, and core.',
        'instructions': 'Stand with feet hip-width apart, shins close to the bar. Bend at the hips and knees, keeping your back flat, and grasp the barbell with hands shoulder-width apart. Lift the bar by extending your hips and knees until you are standing upright, then lower the bar back down to the starting position.',
        'target_muscles': 'Back, Legs, Core'
    },
    {
        'name': 'Bench Press',
        'description': 'A popular strength training exercise targeting the chest, shoulders, and triceps.',
        'instructions': 'Lie on a flat bench with feet flat on the floor. Grasp the barbell with hands slightly wider than shoulder-width apart. Lower the barbell to the chest, then press it upward until arms are fully extended. Lower the barbell back down to the chest and repeat.',
        'target_muscles': 'Chest, Shoulders, Triceps'
    },
    {
        'name': 'Plank',
        'description': 'A core stability exercise that engages multiple muscle groups including the abs, back, and shoulders.',
        'instructions': 'Start in a push-up position with elbows bent 90 degrees and forearms resting on the floor. Keep your body in a straight line from head to heels, engaging your core muscles. Hold this position for the desired duration.',
        'target_muscles': 'Abs, Back, Shoulders'
    },
    {
        'name': 'Lunges',
        'description': 'A unilateral lower body exercise targeting the quadriceps, hamstrings, and glutes.',
        'instructions': 'Stand with feet hip-width apart. Take a step forward with one foot, lowering your body until both knees are bent at a 90-degree angle. Keep your front knee aligned with your ankle and your back knee just above the floor. Push through your front heel to return to the starting position, then repeat on the other side.',
        'target_muscles': 'Quadriceps, Hamstrings, Glutes'
    },
    {
        'name': 'Russian Twist',
        'description': 'An abdominal exercise that targets the obliques and improves rotational core strength.',
        'instructions': 'Sit on the floor with knees bent and feet lifted off the ground. Lean back slightly and clasp your hands together in front of your chest. Twist your torso to one side, bringing your hands toward the floor beside your hip. Return to the center and repeat on the other side.',
        'target_muscles': 'Obliques'
    },
    {
        'name': 'Burpees',
        'description': 'A full-body exercise that combines a squat, push-up, and jump, providing cardiovascular and strength benefits.',
        'instructions': 'Start in a standing position. Drop into a squat position with hands on the floor. Kick your feet back into a push-up position. Perform a push-up, then immediately return to the squat position. Jump up explosively from the squat position.',
        'target_muscles': 'Full body'
    },
    {
        'name': 'Mountain Climbers',
        'description': 'A dynamic exercise that targets the core, shoulders, and legs while also providing cardiovascular benefits.',
        'instructions': 'Start in a push-up position with hands under shoulders and body in a straight line. Bring one knee toward the chest, then quickly switch legs, bringing the other knee toward the chest. Continue alternating legs at a fast pace.',
        'target_muscles': 'Core, Shoulders, Legs'
    },

]

def populate_exercises():
    for exercise_data in exercises:
        Exercise.objects.create(
            name=exercise_data['name'],
            description=exercise_data['description'],
            target_muscles=exercise_data['target_muscles']
        )

if __name__ == "__main__":
    populate_exercises()
