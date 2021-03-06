from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	
	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.name

class Page(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)
	
	def __str__(self):
		return self.title

#each time you make  new model -> $ python manage.py makemigrations rango
#then commit -> $python manage.py migratem
#access databse with shell -> $ python manage.py shell