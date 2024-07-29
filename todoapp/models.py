from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class TodoModel(models.model):
class Todo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
