from django.contrib import admin
from octofit_tracker.models.user import User
from octofit_tracker.models.team import Team
from octofit_tracker.models.activity import Activity
from octofit_tracker.models.leaderboard import Leaderboard
from octofit_tracker.models.workout import Workout

admin.site.register(User)
admin.site.register(Team)
admin.site.register(Activity)
admin.site.register(Leaderboard)
admin.site.register(Workout)
