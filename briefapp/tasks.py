from .models import Caption, MeetingSummary


def summarize_caption(caption_id):
    print('caption_id', caption_id)
    caption = Caption.objects.filter(id=caption_id)



