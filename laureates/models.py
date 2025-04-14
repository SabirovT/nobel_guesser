from django.db import models

class Laureate(models.Model):
    name = models.CharField(max_length=100)
    fact = models.TextField()
    q1_answer = models.CharField(max_length=50)
    q2_answer = models.CharField(max_length=50)
    q3_answer = models.CharField(max_length=50)
    q4_answer = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name