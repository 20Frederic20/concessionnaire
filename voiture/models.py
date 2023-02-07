from django.db import models

# Create your models here.


class Marque(models.Model):
	name = models.CharField(max_length=120)
		
	def __str__(self):
		return self.name


class Voiture(models.Model):
	marque = models.ForeignKey(Marque, on_delete=models.CASCADE)
	name = models.CharField(max_length=120)
	price = models.DecimalField(max_digits=19, decimal_places=2) 
	image = models.FileField(upload_to='media/uploads/')

	def __str__(self):
		return '%s %s'%(marque, name)
