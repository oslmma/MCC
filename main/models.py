from django.db import models
from django.urls import reverse
from django.utils import timezone


def user_directory_path(instance, filename):
    return 'uploads/{0}/{1}'.format(instance.name + ' ' + instance.family, filename)
class Main(models.Model):
    name = models.CharField(max_length=64, blank=False)
    family = models.CharField(max_length=126, blank=False)

    field = models.CharField(max_length=256, blank=True)
    university = models.CharField(max_length=256, blank=True)
    title = models.CharField(max_length=125, blank=True)
    doctor_adviser = models.CharField(max_length=125, blank=True)

    money = models.IntegerField()
    debt_payment1 = models.FileField(upload_to=user_directory_path, blank=True)
    debt_payment2 = models.FileField(upload_to=user_directory_path, blank=True)
    debt_payment3 = models.FileField(upload_to=user_directory_path, blank=True)

    start_date = models.DateTimeField()

    proposal = models.FileField(upload_to=user_directory_path, blank=True)
    ch123 = models.FileField(upload_to=user_directory_path, blank=True)
    ch45 = models.FileField(upload_to=user_directory_path, blank=True)

    translation = models.CharField(max_length=64, blank=True)
    # research assistant code 
    RAC = models.CharField(max_length=64, blank=True)
    representative = models.CharField(max_length=64, blank=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return str(self.name) + ' ' + str(self.family)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
    class Meta:
        unique_together = ('name', 'family',)

class TODO(models.Model):
    title = models.CharField(max_length=64)
    # zremind is that remind for order_by i must to rename that
    status = models.CharField(max_length=16, choices=[('today', 'امروز'), ('necessary', 'ضروروی'), ('zremind', 'یادآوری'),])
    remind_datetime = models.DateTimeField(blank=True, default=timezone.now)
    done = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return str(self.title)