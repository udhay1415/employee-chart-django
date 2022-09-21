from pyexpat import model
from django.db import models

class Employee(models.Model):
  emp_id = models.IntegerField()
  email = models.CharField(max_length=512, unique=True)
  name = models.CharField(max_length=512)
  designation = models.CharField(max_length=512)
  team = models.CharField(max_length=512)
  x_coord = models.IntegerField()
  y_coord = models.IntegerField()

class Manager(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, related_name='employee')
  manager = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, related_name='manager')