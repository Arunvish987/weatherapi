# Generated by Django 3.1.2 on 2020-12-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={},
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
