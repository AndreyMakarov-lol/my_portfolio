# Generated by Django 4.2.4 on 2023-08-07 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='img',
            field=models.ImageField(default=2, upload_to='image/%Y', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]