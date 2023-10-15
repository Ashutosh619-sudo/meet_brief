from django.db.models.signals import post_save

from django.dispatch import receiver
from django_q.tasks import async_task

from .models import Caption
from .tasks import summarize_caption

@receiver(post_save, sender=Caption)
def run_post_caption_creation_triggers(sender, instance:Caption, **kwargs):


    async_task(summarize_caption, instance.id)