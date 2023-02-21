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
  cantdebaños = models.IntegerField()
  hayasensor = models.BooleanField()
  descuento = models.IntegerField(default = 0)
  descripcion = models.TextField()
  preciodolares = models.IntegerField(default = 0)

  listadeestados = [
    (1, "En construccion"),
    (2, "En planos"),
    (3, "Departamento"),
    (4, "Casa"),
    (5, "Terreno")
    ]

  estadodepredio = models.IntegerField(
    null=False,
    blank=False,
    choices=listadeestados,
    default=1
  )

  # get_tipo_display=estadodepredio.get_estadodepredio_choices()

  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)


  imagenprincipal = models.ImageField(upload_to='images/', null = True, blank = False)
  imagensecundaria00 = models.ImageField(upload_to='images/', null = True, blank = True)
  imagensecundaria01 = models.ImageField(upload_to='images/', null = True, blank = True)
  imagensecundaria02 = models.ImageField(upload_to='images/', null = True, blank = True)
  imagensecundaria03 = models.ImageField(upload_to='images/', null = True, blank = True)
  imagensecundaria04 = models.ImageField(upload_to='images/', null = True, blank = True)
  imagensecundaria05 = models.ImageField(upload_to='images/', null = True, blank = True)
  imagensecundaria06 = models.ImageField(upload_to='images/', null = True, blank = True)
  imagensecundaria07 = models.ImageField(upload_to='images/', null = True, blank = True)
  imagensecundaria08 = models.ImageField(upload_to='images/', null = True, blank = True)
  imagensecundaria09 = models.ImageField(upload_to='images/', null = True, blank = True)
  imagensecundaria10 = models.ImageField(upload_to='images/', null = True, blank = True)
  imagensecundaria11 = models.ImageField(upload_to='images/', null = True, blank = True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.titulo

