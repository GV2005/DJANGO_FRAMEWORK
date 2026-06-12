from django.db import models

#Doctor model

class Doctor(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    department=models.CharField(max_length=60)

    def __str__(self):
        return self.name

#Disease model

class Disease(models.Model):
    disease_name=models.CharField()

    def __str__(self):
        return self.disease_name

#patient model

class Patient(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()

    doctor=models.ForeignKey(
        Doctor,
        on_delete=models.SET_NULL,
        null=True
        )
    
    disease=models.ManyToManyField(
        Disease,
        )

    def __str__(self):
        return self.name
    
class PatientProfile(models.Model):
    patient=models.OneToOneField(
        Patient,
        on_delete=models.CASCADE
    )
    blood_group=models.CharField(max_length=5)
    emergency_contact=models.IntegerField()

