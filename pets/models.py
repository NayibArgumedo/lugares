from django.db import models

# Create your models here.

class Person(models.Model):
    namePerson = models.CharField(max_length=60)
    age = models.PositiveIntegerField(default=0)
    phone = models.PositiveIntegerField(max_length=11, default=0)
    city = models.CharField(max_length=40)
    neighborhood = models.CharField(max_length=40)
   

    def __str__(self) -> str:
        return "{} - {} - {} - {}- {}".format(self.namePerson, self.age, self.phone, self.city, self.neighborhood)



class Pets(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    namePets = models.CharField(max_length=30)
    petType = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    observation = models.TextField()

    def __str__(self) -> str:
        return "{} - {} - {} - {} - {} ".format(self.person.namePerson, self.namePets, self.petType, self.breed, self.observation) 