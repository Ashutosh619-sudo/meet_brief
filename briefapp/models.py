from django.db import models
from authapp.models import CustomUser

# Create your models here.
class Meeting(models.Model):

    title = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="meetings")


class Caption(models.Model):

    meeting = models.OneToOneField(Meeting, on_delete=models.CASCADE, related_name="caption")
    timestamp = models.DateTimeField(auto_now_add=True)
    url = models.TextField()


class MeetingSummary(models.Model):

    meeting = models.OneToOneField(Meeting, on_delete=models.CASCADE, related_name="summary")
    summary_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
