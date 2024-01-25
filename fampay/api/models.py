from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    published_at = models.DateTimeField()
    thumbnail_url = models.URLField()
    video_url = models.URLField()
    channel_title = models.CharField(max_length=100)
    channel_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Videos"
        ordering = ['-published_at']
        
