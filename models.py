from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import redirect, reverse
from decimal import Decimal
from django.dispatch import receiver
import os
import shutil



# These two auto-delete images from filesystem when they are unneeded:
@receiver(models.signals.post_delete, sender=MyModelName)
def auto_delete_MyModelName_image_on_delete(sender, instance, **kwargs):
    """
    Deletes image from filesystem
    when corresponding `MyModelName` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            # Delete CACHE Folder of Image
            image_cache_list = instance.image.name.split('.')
            del image_cache_list[-1]
            image_cache = '.'.join(image_cache_list)
            if os.path.isdir(os.path.join(
                BASE_DIR, 'media/CACHE/images/'+image_cache)):
                shutil.rmtree(os.path.join(
                    BASE_DIR, 'media/CACHE/images/'+image_cache))
            # Delete Original File
            os.remove(instance.image.path)

@receiver(models.signals.pre_save, sender=MyModelName)
def auto_delete_MyModelName_image_on_change(sender, instance, **kwargs):
    """
    Deletes old image from filesystem
    when corresponding `MyModelName` object is updated
    with new image.
    """
    if not instance.pk:
        return False

    try:
        old_image = MyModelName.objects.get(pk=instance.pk).image
    except MyModelName.DoesNotExist:
        return False

    new_image = instance.image

    # Check Old Photo Is Exist
    try: 
        old_image.path
    except:
        return False

    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            # Delete CACHE Folder of Image
            old_image_cache_list = old_image.name.split('.')
            del old_image_cache_list[-1]
            old_image_cache = '.'.join(old_image_cache_list)
            if os.path.isdir(os.path.join(
                BASE_DIR, 'media/CACHE/images/'+old_image_cache)):
                shutil.rmtree(os.path.join(
                    BASE_DIR, 'media/CACHE/images/'+old_image_cache))
            # Delete Original File
            os.remove(old_image.path)