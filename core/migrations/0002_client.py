# Generated by Django 3.2.5 on 2021-07-31 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('lastName', models.CharField(max_length=100, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
            ],
        ),
    ]
