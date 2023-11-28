from django.db import models
# Create your models here.
class guest(models.Model):
    image = models.ImageField(upload_to='insect/images/', height_field=None, width_field=None, max_length=None)
    date = models.DateField(auto_now=True, auto_now_add=False)
class bug(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=150)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    description = models.TextField(max_length=300)
    treatment = models.TextField(max_length=300)
    def __str__(self):
        return self.name
class medic(models.Model):
    id  = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    bite_used = models.ForeignKey(bug,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    price = models.IntegerField(null=True)
    def __str__(self):
        return self.name