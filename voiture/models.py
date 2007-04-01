from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.


class Marque(models.Model):
	name = models.CharField(max_length=120)
		
	def __str__(self):
		return self.name


class Voiture(models.Model):
	marque = models.ForeignKey(Marque, on_delete=models.CASCADE)
	name = models.CharField(max_length=120)
	price = models.DecimalField(max_digits=19, decimal_places=2) 
	image = models.FileField(upload_to='uploads/')

	def __str__(self):
		return '%s %s'%(self.marque, self.name)

	def get_absolute_url(self):
		return reverse('voiture:detail', kwargs={'pk': self.pk})


class Reviews(models.Model):
	"""Model definition for Reviews."""

	# TODO: Define fields here
	voiture =models.ForeignKey(Voiture, on_delete=models.CASCADE)
	auteur =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	reviews =models.TextField()
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)


	class Meta:
		"""Meta definition for Reviews."""

		verbose_name = 'review'
		verbose_name_plural = 'Reviews'

	def __str__(self):
		"""Unicode representation of Reviews."""
		return "created by {} at {}".format(self.auteur, self.created_at)