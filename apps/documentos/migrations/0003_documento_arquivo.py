# Generated by Django 3.1 on 2020-08-19 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0002_auto_20200810_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(default='', upload_to='documentos'),
            preserve_default=False,
        ),
    ]