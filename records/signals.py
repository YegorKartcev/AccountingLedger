from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.utils import generate_random_string
from records.models import Task, Income, Expenditure

@receiver(pre_save, sender=Task)
def add_slug_to_task(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        text = instance.title
        if len(instance.title) > 30:
            text = text[:30]
        slug = slugify(text)
        random_string = generate_random_string()
        instance.slug = slug + "-" + random_string

@receiver(pre_save, sender=Income)
def add_slug_to_income(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        text = instance.source
        if len(instance.source) > 30:
            text = text[:30]
        slug = slugify(text)
        random_string = generate_random_string()
        instance.slug = slug+ "-"+ str(instance.amount) + "-" + random_string

@receiver(pre_save, sender=Expenditure)
def add_slug_to_expenditure(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        text = instance.target
        if len(instance.target) > 30:
            text = text[:30]
        slug = slugify(text)
        random_string = generate_random_string()
        instance.slug = slug+ "-"+ str(instance.amount) + "-" + random_string