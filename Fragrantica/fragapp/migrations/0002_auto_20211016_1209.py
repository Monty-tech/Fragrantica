# Generated by Django 3.2.8 on 2021-10-16 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fragapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='reference',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='rating',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
