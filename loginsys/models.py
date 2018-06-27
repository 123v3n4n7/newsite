from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, null = True, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	age = models.IntegerField(null = True, blank = True)
	places = models.TextField(max_length = 200, null = True, blank = True)
	music = models.TextField(max_length = 200, null = True, blank = True)
	hobby = models.TextField(max_length = 300, null = True, blank = True)
	picture = models.ImageField(upload_to = 'pictures/%Y/%m/%d/', max_length = 255, null = True, blank = True)
	def __str__(self):
		return self.user.username

@receiver(post_save, sender = User)
def user_create_or_edit(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user = instance)
	else:
		instance.profile.save()
# Create your models here.
