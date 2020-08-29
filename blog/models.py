from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class CV(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to = 'static/images/', default = 'pic_folder/None/no-img.jpg')
    name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=11)
    professional_profile = models.TextField()
    additional_skills_description = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Work(models.Model):
    cv = models.ForeignKey(CV, on_delete = models.CASCADE)
    work_experience_location= models.CharField(max_length=200)
    work_experience_date = models.CharField(max_length=200)
    work_experience_description = models.TextField()

    
    def __str__(self):
        return self.work_experience_location

    def publish(self):
        self.save()

class Education(models.Model):
    cv = models.ForeignKey(CV, on_delete = models.CASCADE)
    education_location = models.CharField(max_length=200)
    education_date = models.CharField(max_length=200)
    education_description = models.TextField()

    def __str__(self):
        return self.education_location

    def publish(self):
        self.save()
    

