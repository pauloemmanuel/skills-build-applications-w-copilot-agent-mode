from djongo import models

class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    team = models.CharField(max_length=50)
    points = models.IntegerField()
    rank = models.IntegerField()

    def __str__(self):
        return f"{self.team} - Rank {self.rank}"
