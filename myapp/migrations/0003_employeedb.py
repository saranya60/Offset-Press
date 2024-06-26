# Generated by Django 4.2 on 2023-06-11 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_servicedb_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='employeedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empname', models.CharField(blank=True, max_length=100, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Salary', models.IntegerField(blank=True, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='employee')),
            ],
        ),
    ]
