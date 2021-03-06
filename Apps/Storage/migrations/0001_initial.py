# Generated by Django 2.0.6 on 2021-10-31 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bebidas',
            fields=[
                ('pk_bebidas', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.TextField()),
                ('imagen1', models.URLField(default='https://i.postimg.cc/Y0gkNhTM/3aabe0e9a520b9ad90407a82f85adb42.jpg', max_length=800)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'verbose_name': 'bebida',
                'verbose_name_plural': 'bebidas',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('pk_extras', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_ext', models.CharField(max_length=9)),
                ('nombre_ext', models.CharField(max_length=40)),
                ('descripcion_ext', models.TextField()),
                ('imagen1', models.URLField(default='https://i.postimg.cc/Y0gkNhTM/3aabe0e9a520b9ad90407a82f85adb42.jpg', max_length=800)),
                ('precio_ext', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'verbose_name': 'extra',
                'verbose_name_plural': 'extras',
                'ordering': ['nombre_ext'],
            },
        ),
        migrations.CreateModel(
            name='Postres',
            fields=[
                ('pk_postres', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_post', models.CharField(max_length=9)),
                ('nombre_post', models.CharField(max_length=40)),
                ('descripcion_post', models.TextField()),
                ('imagen1', models.URLField(default='https://i.postimg.cc/Y0gkNhTM/3aabe0e9a520b9ad90407a82f85adb42.jpg', max_length=800)),
                ('precio_post', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'verbose_name': 'postre',
                'verbose_name_plural': 'postres',
                'ordering': ['nombre_post'],
            },
        ),
    ]
