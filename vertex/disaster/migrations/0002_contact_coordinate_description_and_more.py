# Generated by Django 5.1.4 on 2024-12-19 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disaster', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='coordinate',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coordinate',
            name='disaster_type',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coordinate',
            name='number_of_volunteers',
            field=models.IntegerField(default=0),
        ),
    ]
