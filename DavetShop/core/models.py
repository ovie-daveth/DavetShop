from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=250, default='category')

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class item(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()
    slashed = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='items', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    