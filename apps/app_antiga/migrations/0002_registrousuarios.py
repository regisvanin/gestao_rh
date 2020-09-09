# Generated by Django 3.1 on 2020-09-08 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_antiga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroUsuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('salario', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'db_table': 'registro_usuarios',
            },
        ),
    ]
