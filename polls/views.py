from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Manufacturer,GPU,Videokart

def index(request):
    latest_videokart_list = Videokart.objects.order_by('-id')[:5]
    latest_gpu_list = GPU.objects.order_by('-id')[:5]
    latest_manufacturer_list = Manufacturer.objects.order_by('-id')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_videokart_list': latest_videokart_list,
        'latest_gpu_list': latest_gpu_list,
        'latest_manufacturer_list': latest_manufacturer_list,
    }
    return HttpResponse(template.render(context, request))

def videokart(request):
    latest_videokart_list=Videokart.objects.all()
    videokart_field= Videokart._meta.get_fields()
    template = loader.get_template('polls/videokart.html')
    context = {
        'latest_videokart_list': latest_videokart_list,
        'videokart_field': videokart_field,
    }
    return HttpResponse(template.render(context, request))

def gpu(request):
    latest_gpu_list=GPU.objects.all()
    gpu_field= GPU._meta.get_fields()
    template = loader.get_template('polls/gpu.html')
    context = {
        'latest_gpu_list': latest_gpu_list,
        'gpu_field': gpu_field,
    }
    return HttpResponse(template.render(context, request))

def manufacturer(request):
    latest_manufacturer_list=Manufacturer.objects.all()
    manufacturer_field= Manufacturer._meta.get_fields()
    template = loader.get_template('polls/manufacturer.html')
    context = {
        'latest_manufacturer_list': latest_manufacturer_list,
        'manufacturer_field': manufacturer_field,
    }
    return HttpResponse(template.render(context, request))

def videokart_detail(request, question_id):
    videokart=Videokart.objects.get(id=question_id)
    videokart_field= Videokart._meta.get_fields()
    template = loader.get_template('polls/model_detail.html')
    a=[]
    for i in videokart_field:
        a.append(i.name)
    context = {
        'object': videokart,
        'model_table_attrs': a,
        'info': "/polls/videokart/"+str(question_id)+"/edit",
    }
    return HttpResponse(template.render(context, request))

def gpu_detail(request, question_id):
    gpu=GPU.objects.get(id=question_id)
    gpu_field= GPU._meta.get_fields()
    template = loader.get_template('polls/model_detail.html')
    a=[]
    for i in gpu_field:
        a.append(i.name)
    context = {
        'object': gpu,
        'model_table_attrs': a,
        'info': "/polls/gpu/"+str(question_id)+"/edit",
    }
    return HttpResponse(template.render(context, request))

def manufacturer_detail(request, question_id):
    manufacturer=Manufacturer.objects.get(id=question_id)
    manufacturer_field= Manufacturer._meta.get_fields()
    template = loader.get_template('polls/model_detail.html')
    a=[]
    for i in manufacturer_field:
        a.append(i.name)
    context = {
        'object': manufacturer,
        'model_table_attrs': a,
        'info': "/polls/manufacturer/"+str(question_id)+"/edit",
    }
    return HttpResponse(template.render(context, request))

def gpu_add(request):
    if request.method == 'GET':
        template = loader.get_template('polls/gpu_add.html')
        context = {
        }
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        try:
            gpu=GPU(name=request.POST['name'],kernel_NVIDIA_CUDA=request.POST['kernel_NVIDIA_CUDA'],clock_frequency_with_acceleration_GHz=request.POST['clock_frequency_with_acceleration_GHz'],video_memory_size=request.POST['video_memory_size'],memory_type=request.POST['memory_type'])
            gpu.save()
        except:
            print("An exception occurred: gpu")
        url = reverse('polls:gpu_detail', kwargs={'question_id': gpu.id})
        return HttpResponseRedirect(url)

def gpu_edit(request, question_id):
    if request.method == 'GET':
        gpu=GPU.objects.get(id=question_id)
        template = loader.get_template('polls/gpu_edit.html')
        context = {
            'object': gpu,
        }
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        gpu=GPU.objects.get(id=question_id)
        try:
            gpu.name=request.POST['name']
            gpu.kernel_NVIDIA_CUDA=request.POST['kernel_NVIDIA_CUDA']
            gpu.clock_frequency_with_acceleration_GHz=request.POST['clock_frequency_with_acceleration_GHz']
            gpu.video_memory_size=request.POST['video_memory_size']
            gpu.memory_type=request.POST['memory_type']
            gpu.save()
        except:
            print("An exception occurred: gpu")
        url = reverse('polls:gpu_detail', kwargs={'question_id': question_id})
        return HttpResponseRedirect(url)

def manufacturer_add(request):
    if request.method == 'GET':
        template = loader.get_template('polls/manufacturer_add.html')
        context = {
        }
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        try:
            manufacturer=Manufacturer(name=request.POST['name'],address=request.POST['address'],info=request.POST['info'])
            manufacturer.save()
        except:
            print("An exception occurred: manufacturer")
        url = reverse('polls:manufacturer_detail', kwargs={'question_id': manufacturer.id})
        return HttpResponseRedirect(url)

def manufacturer_edit(request, question_id):
    if request.method == 'GET':
        manufacturer=Manufacturer.objects.get(id=question_id)
        template = loader.get_template('polls/manufacturer_edit.html')
        context = {
            'object': manufacturer,
        }
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        manufacturer=Manufacturer.objects.get(id=question_id)
        try:
            manufacturer.name=request.POST['name']
            manufacturer.address=request.POST['address']
            manufacturer.info=request.POST['info']
            manufacturer.save()
        except:
            print("An exception occurred: manufacturer")
        url = reverse('polls:manufacturer_detail', kwargs={'question_id': question_id})
        return HttpResponseRedirect(url)

def videokart_add(request):
    if request.method == 'GET':
        template = loader.get_template('polls/videokart_add.html')
        context = {
        }
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        try:
            gpu=GPU.objects.get(id=int(request.POST['idGPU']))
            manufacturer=Manufacturer.objects.get(id=int(request.POST['manufacturerid']))
            videokart=Videokart(name=request.POST['name'],price=int(request.POST['price']),kolvo=int(request.POST['kolvo']),year=request.POST['year'],info=request.POST['info'],idGPU=gpu,manufacturerid=manufacturer)
            videokart.save()
        except:
            print("An exception occurred: videokart")
        url = reverse('polls:videokart_detail', kwargs={'question_id': videokart.id})
        return HttpResponseRedirect(url)

def videokart_edit(request, question_id):
    if request.method == 'GET':
        videokart=Videokart.objects.get(id=question_id)
        template = loader.get_template('polls/videokart_edit.html')
        context = {
            'object': videokart,
        }
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        videokart=Videokart.objects.get(id=question_id)
        try:
            videokart.name=request.POST['name']
            videokart.price=int(request.POST['price'])
            videokart.kolvo=int(request.POST['kolvo'])
            videokart.year=request.POST['year'] #DateField
            videokart.info=request.POST['info']
            gpu=GPU.objects.get(id=int(request.POST['idGPU']))
            videokart.idGPU=gpu
            manufacturer=Manufacturer.objects.get(id=int(request.POST['manufacturerid']))
            videokart.manufacturerid=manufacturer
            videokart.save()
        except Exception as e:
            print("An exception occurred: videokart:")
            print(e)
        url = reverse('polls:videokart_detail', kwargs={'question_id': question_id})
        return HttpResponseRedirect(url)