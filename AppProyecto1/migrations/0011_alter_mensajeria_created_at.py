# Generated by Django 4.0 on 2022-02-14 23:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyecto1', '0010_mensajeria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajeria',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
