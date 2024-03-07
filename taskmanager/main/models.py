from django.db import models

# Create your models here.
class Name(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200, blank=True)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return(self.first_name + " " + self.last_name)
    
class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
#    due_date = models.DateTimeField(default="1/1/1970")
    time_to_complete = models.IntegerField(default=0, blank=True)
    assigned_worker = models.ManyToManyField(Name, blank=True)

    def __str__(self):
          return (self.name)