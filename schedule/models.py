from django.db import models

# Create your models here.


class Events(models.Model):
    nameEvent =  models.CharField(max_length=40)
    place = models.CharField(max_length=40)
    date = models.DateTimeField()
    description = models.TextField()

    def __str__(self) -> str:
        return "{} ".format(self.nameEvent)


class Participants(models.Model):
    nameParticipants = models.CharField(max_length=50)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{} - {} ".format(self.nameParticipants, self.event.nameEvent)


