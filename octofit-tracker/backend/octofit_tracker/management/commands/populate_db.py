from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        team_names = [
            ('Marvel', 'Marvel Superheroes'),
            ('DC', 'DC Superheroes'),
            ('Avengers', 'Earth’s Mightiest Heroes'),
            ('Justice League', 'United for Justice'),
            ('Guardians', 'Guardians of the Galaxy'),
            ('X-Force', 'Covert mutant strike team'),
        ]

        teams = {}
        for name, desc in team_names:
            teams[name] = Team.objects.create(name=name, description=desc)

        hero_names = [
            'Spider-Man', 'Iron Man', 'Captain America', 'Thor', 'Hulk', 'Black Widow', 'Hawkeye',
            'Black Panther', 'Doctor Strange', 'Scarlet Witch', 'Vision', 'Ant-Man', 'Wasp', 'Falcon',
            'Star-Lord', 'Gamora', 'Drax', 'Rocket', 'Groot', 'Mantis',
            'Batman', 'Superman', 'Wonder Woman', 'Flash', 'Aquaman', 'Cyborg', 'Green Lantern',
            'Shazam', 'Martian Manhunter', 'Green Arrow'
        ]

        random.shuffle(hero_names)
        users = []
        for idx, name in enumerate(hero_names[:40]):
            team_name = random.choice(list(teams.keys()))
            email_local = name.lower().replace(' ', '.')
            email = f"{email_local}{idx}@{team_name.lower()}.example.com"
            users.append(User(name=name, email=email, team=team_name, is_superhero=True))
        for u in users:
            u.save()

        workouts_catalog = [
            ('Hero HIIT', 'High intensity intervals to boost power', 'Hard', 28),
            ('Power Yoga', 'Strength + mobility flow', 'Medium', 40),
            ('Shield Strength', 'Upper-body compound lifts', 'Medium', 45),
            ('Lightning Sprint', 'Track sprints and agility', 'Hard', 22),
            ('Recovery Flow', 'Mobility and breathing', 'Easy', 25),
            ('Cosmic Core', 'Core stability and rotation', 'Medium', 30),
            ('Urban Run', 'Tempo run through the city', 'Medium', 35),
            ('Battle Rope Blast', 'Ropes + bodyweight circuits', 'Hard', 20),
            ('Aqua Endurance', 'Low-impact pool cardio', 'Easy', 30),
        ]
        for n, d, diff, dur in workouts_catalog:
            Workout.objects.create(name=n, description=d, difficulty=diff, duration=dur)

        activity_types = ['Running', 'Cycling', 'Swimming', 'Yoga', 'Strength', 'HIIT', 'Rowing', 'Hiking', 'Boxing']

        today = date.today()
        all_user_names = [u.name for u in users]
        total_activities = 300
        for _ in range(total_activities):
            user_name = random.choice(all_user_names)
            a_type = random.choice(activity_types)
            duration = random.randint(20, 120)
            cal_per_min = random.randint(5, 12)
            calories = duration * cal_per_min
            day_offset = random.randint(0, 59)
            when = today - timedelta(days=day_offset)
            Activity.objects.create(user=user_name, type=a_type, duration=duration, calories=calories, date=when)

        points_by_team = {t: 0 for t in teams.keys()}
        user_team_map = {u.name: u.team for u in users}
        for a in Activity.objects.all():
            team = user_team_map.get(a.user)
            if team:
                points_by_team[team] += a.calories

        leaderboard_entries = []
        for team, pts in points_by_team.items():
            leaderboard_entries.append((team, pts))
        leaderboard_entries.sort(key=lambda x: x[1], reverse=True)

        rank = 1
        for team, pts in leaderboard_entries:
            Leaderboard.objects.create(team=team, points=pts, rank=rank)
            rank += 1

        self.stdout.write(self.style.SUCCESS(
            f"Base populada: {len(teams)} equipes, {len(users)} usuários, {Activity.objects.count()} atividades, {Workout.objects.count()} treinos, {Leaderboard.objects.count()} ranking entries."
        ))
