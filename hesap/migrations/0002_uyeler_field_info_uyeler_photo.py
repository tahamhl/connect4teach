# Generated by Django 5.0.6 on 2024-05-31 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hesap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uyeler',
            name='field_info',
            field=models.CharField(default='.', max_length=30),
        ),
        migrations.AddField(
            model_name='uyeler',
            name='photo',
            field=models.ImageField(default='.', upload_to='uyeler'),
        ),
    ]
