# Generated by Django 4.1.2 on 2022-10-28 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiares',
            name='agno',
            field=models.CharField(max_length=50),
        ),
    ]
