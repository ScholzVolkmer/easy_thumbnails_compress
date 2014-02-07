from django.conf import settings

# register signals
def my_callback(sender, **kwargs):
    from easy_thumbnails_compress.tasks import CompressImage
    CompressImage.delay(sender)

from easy_thumbnails.signals import thumbnail_created

if settings.COMPRESS_IMAGES:
    thumbnail_created.connect(my_callback)
