from django.forms import ModelForm
from .models import Manufacturer,GPU,Videokart

class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name', 'address', 'info']

class VideokartForm(ModelForm):
    class Meta:
        model = Videokart
        fields = ['name', 'price', 'kolvo','year', 'info', 'idGPU','manufacturerid']

class GPUForm(ModelForm):
    class Meta:
        model = GPU
        fields = ['name', 'kernel_NVIDIA_CUDA', 'clock_frequency_with_acceleration_GHz','video_memory_size', 'memory_type']