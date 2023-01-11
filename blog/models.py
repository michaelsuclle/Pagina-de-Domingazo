from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


  titulo = models.CharField(max_length=200)
  ubicacion = models.TextField()
  areatotal = models.IntegerField()
  areaconstruida = models.IntegerField()
  cantdedormitorios = models.IntegerField()
  hayasensor = models.BooleanField()
  descuento = models.IntegerField(default = 0)
  descripcion = models.TextField()

  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)




  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.titulo

