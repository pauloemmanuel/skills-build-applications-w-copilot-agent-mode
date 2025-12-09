from djongo import models

class User(models.Model):
	_id = models.ObjectIdField()
	name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	team = models.CharField(max_length=50)
	is_superhero = models.BooleanField(default=True)

	def __str__(self):
		return self.name

	class Meta:
		app_label = 'octofit_tracker'

class Team(models.Model):
	_id = models.ObjectIdField()
	name = models.CharField(max_length=50, unique=True)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name

	class Meta:
		app_label = 'octofit_tracker'

class Activity(models.Model):
	_id = models.ObjectIdField()
	user = models.CharField(max_length=100)
	type = models.CharField(max_length=50)
	duration = models.IntegerField()  # minutes
	calories = models.IntegerField()
	date = models.DateField()

	def __str__(self):
		return f"{self.user} - {self.type}"

	class Meta:
		app_label = 'octofit_tracker'

class Leaderboard(models.Model):
	_id = models.ObjectIdField()
	team = models.CharField(max_length=50)
	points = models.IntegerField()
	rank = models.IntegerField()

	def __str__(self):
		return f"{self.team} - Rank {self.rank}"

	class Meta:
		app_label = 'octofit_tracker'

class Workout(models.Model):
	_id = models.ObjectIdField()
	name = models.CharField(max_length=100)
	description = models.TextField()
	difficulty = models.CharField(max_length=20)
	duration = models.IntegerField()  # minutes

	def __str__(self):
		return self.name

	class Meta:
		app_label = 'octofit_tracker'
