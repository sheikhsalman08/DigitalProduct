from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime, timedelta


# Create your models here.
class Products(models.Model):
 	title = models.CharField(max_length = 200,default = 'nai')
	image = models.FileField(null = True, blank = True )
	choices = (
	(u'1',u'picture'),
	(u'2',u'logo'),
	(u'3',u'poster'),
	(u'4',u'videos'),
	# ('1','Instagram'),('2','facebook'),('3','youtube')
	)
	type = models.CharField(max_length = 230,default = "Did Not Put",blank = True, null = True, choices = choices)

	time = models.DateTimeField(blank = True, null = True)
	visibility_by_admin =  models.BooleanField(default=True)
	price = models.IntegerField(default=0)
	description = models.TextField(blank = True, null = True)
	license = models.CharField(max_length = 230,default = "Did Not Put",blank = True, null = True)
	file_size = models.IntegerField(default=0)
	by_user = models.ForeignKey(User, blank = True, null = True, related_name="owner")

	def __str__(self):
		return ('{} by {}'.format(self.title,self.by_user))

	def save(self, *args, **kwargs):
		if (self.time is None):
			self.time = now() + timedelta(hours=8)		# for malaysian time
			
		super(Products, self).save(*args, **kwargs)