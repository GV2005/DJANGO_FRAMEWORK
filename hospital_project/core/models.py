from django.db import models

#patient model

class Patient(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    disease=models.CharField(max_length=100)

    def __str__(self):
        return self.name