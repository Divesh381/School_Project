# Generated by Django 5.0 on 2023-12-18 09:43

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesDataFilter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicesDataFilter_icon', models.CharField(max_length=50)),
                ('servicesDataFilter_title', models.CharField(max_length=50)),
                ('servicesDataFilter_desc', tinymce.models.HTMLField()),
            ],
        ),
    ]