from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class PrivateMessage(models.Model):
	pmsender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pmsender')
	pmreciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pmreciever')
	pmbody = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	is_seen = models.BooleanField(default=False)
	def __str__(self):
		return str(self.id) + '  ' + str(self.pmsender) + ' to ' + str(self.pmreciever)