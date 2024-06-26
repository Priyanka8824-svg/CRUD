from django.db import models

# Create your models here.
class Car(models.Model):
    cid = models.IntegerField(primary_key=True)
    car_company = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    seater = models.IntegerField()

    def __str__(self):
        return f"{self.cid}---{self.car_company}---{self.color}---{self.seater}"