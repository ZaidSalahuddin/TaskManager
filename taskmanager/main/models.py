from django.db import models

# Create your models here.
class Name(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return(self.first_name + " " + self.last_name)
    
class Task(models.Model):
    task_name = models.CharField(max_length=30)
    task_description = models.CharField(max_length=30)
    due_date = models.DateTimeField()
    time_to_complete = models.IntegerField(default=0, blank=True)
    assigned_worker = models.ManyToManyField(Name, blank=True)

    def __str__(self):
          return (self.task_name)