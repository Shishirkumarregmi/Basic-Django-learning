from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser #get_user_model #get_user_model to grab the user model provided by Django
#User=get_user_model()
# Create your models here.
class User(AbstractUser):#customizing the user model #Don't forget to register in settings.py file
    pass


class Lead(models.Model):    
    first_name = models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField(default=0)
    agent=models.ForeignKey("Agent",on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"


class Agent(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.email
    
class Article(models.Model):
    DRAFT = 'D'
    PUBLISHED = 'P'
    STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=4000)
    status = models.CharField(max_length=1, choices=STATUS, default=DRAFT)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(blank=True, null=True)
