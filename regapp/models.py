from django.db import models

class regInfo(models.Model):
	class Meta():
		db_table = "registration_app"
	regInfo_username = models.CharField(max_length = 10)
	regInfo_password = models.CharField(max_length = 15)
	def __str__(self):
		return self.username, self.password

# Create your models here.
