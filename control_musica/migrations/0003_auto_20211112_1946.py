# Generated by Django 3.2.8 on 2021-11-13 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_musica', '0002_auto_20211112_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumes',
            name='foto',
            field=models.ImageField(default='albumes/default.jpg', upload_to='albumes/'),
        ),
        migrations.AddField(
            model_name='artistas',
            name='foto',
            field=models.ImageField(default='albumes/default.jpg', upload_to='artistas/'),
        ),
    ]
