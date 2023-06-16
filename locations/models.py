from django.db import models

# Create your models here.

class Department(models.Model):
    namedepartment = models.CharField(max_length=30)

    def __str__(self) -> str:
        return "{}".format(self.namedepartment)

class City(models.Model):
    nameCity = models.CharField(max_length=30)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{}".format(self.nameCity, self.department)


class Neighborhood(models.Model):
    nameNeighborhood = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{}".format(self.nameNeighborhood, self.city)