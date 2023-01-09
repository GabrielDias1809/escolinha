from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Aula(models.Model):
    titulo = models.CharField(max_length=255)
    data = models.DateTimeField()
    hora = models.TimeField()
    instrutor = models.ForeignKey(User, on_delete=models.CASCADE,)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('checkin', args=(str(self.id)))