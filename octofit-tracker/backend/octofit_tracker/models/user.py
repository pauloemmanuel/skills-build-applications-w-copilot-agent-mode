from djongo import models

class User(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=50)
    is_superhero = models.BooleanField(default=True)

    def __str__(self):
        return self.name
