from django.db import models

class HealthProgram(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
class Client(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    programs = models.ManyToManyField(HealthProgram, through='Enrollment')
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Enrollment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    program = models.ForeignKey(HealthProgram, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client} enrolled in {self.program}"    