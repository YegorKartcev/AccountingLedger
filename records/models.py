from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator



class Task(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # content = models.ManyToManyField(TaskRecord, related_name="task", blank=True, null=True)
    title = models.CharField(max_length=240, null=False, blank=False)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="tasks")


    def __str__(self):
        return self.title

    @property
    def choices(self):
        return self.choice_set.all()        

class Choice(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="taskRecords")
    checked = models.BooleanField(default=False)
    def __str__(self):
        return self.text


class Income(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=30, unique=True)
    source = models.CharField(max_length=240)
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                     MaxValueValidator(2000000000)])
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="incoms")

    def __str__(self):
        return "%s - %s" % (self.amount, self.source)


class Category(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=240)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="categories")

    def __str__(self):
        return "%s" % (self.title)

    class Meta:
        verbose_name_plural = "categories"


class Expenditure(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=30, unique=True)
    target = models.CharField(max_length=240)
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                     MaxValueValidator(2000000000)])
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="expenditures")
    category = models.ForeignKey(Category,
                               on_delete=models.CASCADE,
                               related_name="expenditures_category")                               

    def __str__(self):
        return "%s - %s" % (self.amount, self.target)


