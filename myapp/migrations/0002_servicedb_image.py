# Generated by Django 4.2 on 2023-06-09 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedb',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='service'),
        ),
    ]
