from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team='Marvel', is_superhero=True),
            User(name='Iron Man', email='ironman@marvel.com', team='Marvel', is_superhero=True),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='DC', is_superhero=True),
            User(name='Batman', email='batman@dc.com', team='DC', is_superhero=True),
        ]
        for user in users:
            user.save()

        # Activities
        activities = [
            Activity(user='Spider-Man', type='Running', duration=30, calories=300, date=date.today()),
            Activity(user='Iron Man', type='Cycling', duration=45, calories=500, date=date.today()),
            Activity(user='Wonder Woman', type='Swimming', duration=60, calories=700, date=date.today()),
            Activity(user='Batman', type='Yoga', duration=40, calories=200, date=date.today()),
        ]
        for activity in activities:
            activity.save()

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=800, rank=1)
        Leaderboard.objects.create(team='DC', points=900, rank=1)

        # Workouts
        workouts = [
            Workout(name='Hero HIIT', description='High intensity interval training for heroes', difficulty='Hard', duration=30),
            Workout(name='Power Yoga', description='Yoga for strength and flexibility', difficulty='Medium', duration=40),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
