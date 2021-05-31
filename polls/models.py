from django.db import models
from django.forms import ModelForm

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    info = models.CharField(max_length=200,default="")
    def __str__(self):
        return str(self.id)+":"+self.name

class GPU(models.Model):
    name = models.CharField(max_length=200)
    kernel_NVIDIA_CUDA = models.CharField(max_length=200)
    clock_frequency_with_acceleration_GHz = models.CharField(max_length=200)
    video_memory_size = models.CharField(max_length=200)
    memory_type = models.CharField(max_length=200)
    def __str__(self):
        return str(self.id)+":"+self.name

class Videokart(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    kolvo = models.IntegerField()
    year = models.DateField()
    info = models.CharField(max_length=200)
    idGPU = models.ForeignKey(GPU, on_delete=models.CASCADE)
    manufacturerid = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    class Meta:
        unique_together = ("idGPU", "manufacturerid")
    def __str__(self):
        return str(self.id)+":"+self.name