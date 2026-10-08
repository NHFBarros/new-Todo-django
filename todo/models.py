from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    due_date = models.DateField()
    priority = models.CharField(max_length=50)
    done = models.BooleanField()

    def __str__(self) -> str:
        return self.title