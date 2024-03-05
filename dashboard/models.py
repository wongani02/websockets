from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.

class Statistic(models.Model):
    name= models.CharField(max_length=255, null=True)
    slug = models.SlugField(blank=True)

    @property
    def data(self):
        return self.dataitem_set.all()

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs) 

    def get_absolute_url(self):
        return reverse('dashboard:dashboard', kwargs={'slug': self.slug})


class DataItem(models.Model):
    statistic = models.ForeignKey(Statistic, on_delete=models.CASCADE)
    value = models.PositiveIntegerField()
    owner = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.owner} - {self.value}'
