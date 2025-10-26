from django.db import models
from django.utils import timezone

# Create your models here.
class Gallery(models.Model):
    image = models.ImageField(upload_to='uploads/gallery', blank=True, null=True,)
    title = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'Created at {self.created_at} in {self.location}'
    
    class Meta:
        verbose_name_plural = 'Galleries'
        ordering = ['-created_at']