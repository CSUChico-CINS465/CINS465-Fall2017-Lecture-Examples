from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class suggestion(models.Model):
    suggestion = models.CharField(max_length=141)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    authored = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.suggestion

class comment(models.Model):
    comment = models.CharField(max_length=141)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion = models.ForeignKey(suggestion, on_delete=models.CASCADE)
    authored = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
