# Generated by Django 5.0.2 on 2024-03-09 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('imagen', models.ImageField(upload_to='denuncias/')),
                ('status', models.PositiveSmallIntegerField(default=0)),
                ('autorizado', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
