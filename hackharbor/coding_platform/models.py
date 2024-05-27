from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.username
    


class Job(models.Model):
    company = models.CharField(max_length=100)
    
    description = models.TextField()
    job_type = models.CharField(max_length=50)
    apply_link = models.URLField()

    def __str__(self):
        return self.company