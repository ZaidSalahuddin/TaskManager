from django.db import models

# Create your models here.
class Name(models.Model):
    task = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    time_to_complete = models.CharField(max_length=11)


    def __str__(self):
        return(self.task + " " + self.description)