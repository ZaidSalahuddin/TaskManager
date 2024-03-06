from django.db import models

# Create your models here.
class Task(models.Model):
	task_name = models.CharField(max_length=30)
	worker_name = models.CharField(max_length=30)
	task_description = models.CharField(max_length=30)
	time_to_complete = models.IntegerField(default=0)
 
	def __str__(self):
          return (self.task_name)


class Name(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact = models.IntegerField(default=0)
    task_owner = models.ManyToManyField(Task, blank=True)


    def __str__(self):
        return(self.first_name + " " + self.last_name)