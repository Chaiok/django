# Generated by Django 3.2 on 2021-04-23 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('polls', '0006_auto_20210423_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('kernel_NVIDIA_CUDA', models.CharField(max_length=200)),
                ('clock_frequency_with_acceleration_GHz', models.CharField(max_length=200)),
                ('video_memory_size', models.CharField(max_length=200)),
                ('memory_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('info', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Videokart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('kolvo', models.IntegerField()),
                ('year', models.DateField()),
                ('info', models.CharField(max_length=200)),
                ('idGPU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.gpu')),
                ('manufacturerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.manufacturer')),
            ],
            options={
                'unique_together': {('idGPU', 'manufacturerid')},
            },
        ),
    ]
