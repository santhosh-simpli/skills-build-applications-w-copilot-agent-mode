from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting existing data...')
        
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        self.stdout.write('Creating teams...')
        
        # Create teams
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Assemble! The mightiest heroes training together.'
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League united for ultimate fitness.'
        )
        
        self.stdout.write('Creating users...')
        
        # Create Marvel heroes
        iron_man = User.objects.create(
            name='Tony Stark',
            email='ironman@avengers.com',
            password='arc_reactor',
            fitness_level='Advanced',
            team_id=str(team_marvel._id)
        )
        
        captain_america = User.objects.create(
            name='Steve Rogers',
            email='cap@avengers.com',
            password='vibranium_shield',
            fitness_level='Expert',
            team_id=str(team_marvel._id)
        )
        
        black_widow = User.objects.create(
            name='Natasha Romanoff',
            email='blackwidow@avengers.com',
            password='red_room',
            fitness_level='Expert',
            team_id=str(team_marvel._id)
        )
        
        thor = User.objects.create(
            name='Thor Odinson',
            email='thor@asgard.com',
            password='mjolnir',
            fitness_level='God-tier',
            team_id=str(team_marvel._id)
        )
        
        # Create DC heroes
        batman = User.objects.create(
            name='Bruce Wayne',
            email='batman@wayne.com',
            password='gotham_knight',
            fitness_level='Expert',
            team_id=str(team_dc._id)
        )
        
        superman = User.objects.create(
            name='Clark Kent',
            email='superman@dailyplanet.com',
            password='krypton',
            fitness_level='God-tier',
            team_id=str(team_dc._id)
        )
        
        wonder_woman = User.objects.create(
            name='Diana Prince',
            email='wonderwoman@themyscira.com',
            password='amazon_warrior',
            fitness_level='Expert',
            team_id=str(team_dc._id)
        )
        
        flash = User.objects.create(
            name='Barry Allen',
            email='flash@speedforce.com',
            password='speed_force',
            fitness_level='Advanced',
            team_id=str(team_dc._id)
        )
        
        self.stdout.write('Creating activities...')
        
        # Create activities for users
        base_date = datetime.now() - timedelta(days=7)
        
        # Iron Man activities
        Activity.objects.create(
            user_id=str(iron_man._id),
            activity_type='Running',
            duration_minutes=45,
            distance_km=8.5,
            calories_burned=520,
            date=base_date
        )
        
        Activity.objects.create(
            user_id=str(iron_man._id),
            activity_type='Strength Training',
            duration_minutes=60,
            distance_km=0,
            calories_burned=380,
            date=base_date + timedelta(days=1)
        )
        
        # Captain America activities
        Activity.objects.create(
            user_id=str(captain_america._id),
            activity_type='Running',
            duration_minutes=60,
            distance_km=12.0,
            calories_burned=720,
            date=base_date
        )
        
        Activity.objects.create(
            user_id=str(captain_america._id),
            activity_type='Cycling',
            duration_minutes=90,
            distance_km=35.0,
            calories_burned=850,
            date=base_date + timedelta(days=2)
        )
        
        # Batman activities
        Activity.objects.create(
            user_id=str(batman._id),
            activity_type='Martial Arts',
            duration_minutes=120,
            distance_km=0,
            calories_burned=960,
            date=base_date
        )
        
        Activity.objects.create(
            user_id=str(batman._id),
            activity_type='Running',
            duration_minutes=50,
            distance_km=9.0,
            calories_burned=580,
            date=base_date + timedelta(days=1)
        )
        
        # Superman activities
        Activity.objects.create(
            user_id=str(superman._id),
            activity_type='Flying',
            duration_minutes=30,
            distance_km=500.0,
            calories_burned=150,
            date=base_date
        )
        
        Activity.objects.create(
            user_id=str(superman._id),
            activity_type='Strength Training',
            duration_minutes=45,
            distance_km=0,
            calories_burned=320,
            date=base_date + timedelta(days=3)
        )
        
        self.stdout.write('Creating leaderboard entries...')
        
        # Create leaderboard entries
        Leaderboard.objects.create(
            user_id=str(captain_america._id),
            team_id=str(team_marvel._id),
            total_points=1570,
            total_activities=2,
            rank=1
        )
        
        Leaderboard.objects.create(
            user_id=str(batman._id),
            team_id=str(team_dc._id),
            total_points=1540,
            total_activities=2,
            rank=2
        )
        
        Leaderboard.objects.create(
            user_id=str(iron_man._id),
            team_id=str(team_marvel._id),
            total_points=900,
            total_activities=2,
            rank=3
        )
        
        Leaderboard.objects.create(
            user_id=str(superman._id),
            team_id=str(team_dc._id),
            total_points=470,
            total_activities=2,
            rank=4
        )
        
        self.stdout.write('Creating workout suggestions...')
        
        # Create workout suggestions
        Workout.objects.create(
            name='Super Soldier Circuit',
            description='High-intensity circuit training inspired by Captain America',
            category='Strength',
            difficulty='Advanced',
            duration_minutes=45,
            exercises=[
                {'name': 'Push-ups', 'reps': 50, 'sets': 3},
                {'name': 'Pull-ups', 'reps': 20, 'sets': 3},
                {'name': 'Squats', 'reps': 50, 'sets': 3},
                {'name': 'Burpees', 'reps': 30, 'sets': 3}
            ]
        )
        
        Workout.objects.create(
            name='Speed Force Training',
            description='High-speed cardio workout for maximum endurance',
            category='Cardio',
            difficulty='Advanced',
            duration_minutes=30,
            exercises=[
                {'name': 'Sprint intervals', 'duration': '30s', 'sets': 10},
                {'name': 'Jump rope', 'duration': '5min', 'sets': 1},
                {'name': 'High knees', 'reps': 100, 'sets': 3}
            ]
        )
        
        Workout.objects.create(
            name='Amazon Warrior Training',
            description='Strength and agility training from Themyscira',
            category='Mixed',
            difficulty='Expert',
            duration_minutes=60,
            exercises=[
                {'name': 'Sword swings', 'reps': 40, 'sets': 4},
                {'name': 'Shield blocks', 'reps': 50, 'sets': 3},
                {'name': 'Combat rolls', 'reps': 20, 'sets': 3},
                {'name': 'Lasso drills', 'duration': '10min', 'sets': 1}
            ]
        )
        
        Workout.objects.create(
            name='Dark Knight Conditioning',
            description='Gotham-style combat conditioning',
            category='Martial Arts',
            difficulty='Expert',
            duration_minutes=90,
            exercises=[
                {'name': 'Shadow boxing', 'duration': '15min', 'sets': 1},
                {'name': 'Grappling drills', 'duration': '20min', 'sets': 1},
                {'name': 'Acrobatics', 'reps': 30, 'sets': 3},
                {'name': 'Meditation', 'duration': '10min', 'sets': 1}
            ]
        )
        
        Workout.objects.create(
            name='Beginner Hero Training',
            description='Start your superhero journey with this beginner workout',
            category='Full Body',
            difficulty='Beginner',
            duration_minutes=30,
            exercises=[
                {'name': 'Walking', 'duration': '10min', 'sets': 1},
                {'name': 'Bodyweight squats', 'reps': 15, 'sets': 3},
                {'name': 'Wall push-ups', 'reps': 10, 'sets': 3},
                {'name': 'Stretching', 'duration': '5min', 'sets': 1}
            ]
        )
        
        self.stdout.write(self.style.SUCCESS('Successfully populated database with superhero test data!'))
        self.stdout.write(f'Created {Team.objects.count()} teams')
        self.stdout.write(f'Created {User.objects.count()} users')
        self.stdout.write(f'Created {Activity.objects.count()} activities')
        self.stdout.write(f'Created {Leaderboard.objects.count()} leaderboard entries')
        self.stdout.write(f'Created {Workout.objects.count()} workouts')
