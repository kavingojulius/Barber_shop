from django.db import models

# Create your models here.

class Price(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class WorkCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Work Category'

class Item(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='work_images', null=True, blank=True)
    category = models.ForeignKey(WorkCategory , on_delete=models.CASCADE, related_name='items')        

    
    def __str__(self):
        return self.title  


    
