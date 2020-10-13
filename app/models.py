from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import redirect, reverse
from decimal import Decimal
from django.dispatch import receiver
import os
import shutil
from django.utils.translation import ugettext_lazy as _


from phonenumber_field.modelfields import PhoneNumberField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit

class MyModelName(models.Model):

    name = models.CharField(_('Name'), max_length=150)
    slug = models.SlugField(editable=False)
    status = models.BooleanField()
    order = models.PositiveSmallIntegerField(default=0)

    stock = models.IntegerField(default=0, verbose_name=_('Stock'))
    price = models.DecimalField(_('Price'), validators=[MinValueValidator(Decimal('0.01'))], max_digits=6, decimal_places=2, default=1)

    image_unprocessed = models.ImageField(upload_to = "product")
    image = ProcessedImageField(upload_to='images', processors=[ResizeToFit(1000, 1000)], format='JPEG', options={'quality': 75})
    image_medium = ImageSpecField(source='image', processors=[ResizeToFit(600, 900)], format='JPEG', options={'quality': 75})
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(84, 84)], format='JPEG', options={'quality': 75})

    phone = PhoneNumberField(_('Phone'), unique=True)
    gender = models.CharField(_('Gender'), max_length=15, choices=[('m', 'Male'),('f', 'Female')], blank=True, null=True)
    birthday = models.DateField(_('Birthday'), null=True, blank=True)

    created_date = models.DateTimeField(_('Added'), auto_now_add=True)
    last_update = models.DateTimeField(_('Last Update'), auto_now=True)

    class Meta:
        verbose_name = _('MyModelName')
        verbose_name_plural = _('MyModelNames')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("MyModelName_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(MyModelName, self).save(*args, **kwargs)


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