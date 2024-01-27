from django.db import models
import datetime

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
        
class APIAuthKey(models.Model):
    auth_key = models.CharField(max_length=250, db_index=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    exhausted = models.BooleanField(default=False)

    @classmethod
    def get_auth_key(cls):
        """
            This function returns the non exhausted auth api key
            sorted by created time in ascending order
        """
        api_key = cls.objects.filter(exhausted=False).order_by('created').values()
        if len(api_key):
            return api_key[0]['auth_key']
        return None

    @classmethod
    def mark_auth_key_exhausted(cls, auth_key):
        """
            This function marks the api auth key as exhausted
        """
        row = cls.objects.get(auth_key=auth_key)
        row.exhausted = True
        row.updated = datetime.datetime.now()
        row.save()
        return row
        
