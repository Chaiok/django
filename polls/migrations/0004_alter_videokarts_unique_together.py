# Generated by Django 3.2 on 2021-04-18 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_videokarts_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='videokarts',
            unique_together={('idGPU', 'manufacturersid')},
        ),
    ]