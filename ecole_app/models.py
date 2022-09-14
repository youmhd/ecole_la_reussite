from django.db import models


class Student(models.Model):
    name = models.CharField('Name', max_length=120)
    gender = models.CharField('Gender', max_length=20)
    email = models.CharField('Email Address', max_length=120)
    description = models.TextField(blank=True)
    
    

        
    def __str__(self):
        return self.name