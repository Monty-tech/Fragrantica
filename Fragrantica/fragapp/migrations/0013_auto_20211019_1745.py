# Generated by Django 3.2.8 on 2021-10-19 12:15

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fragapp', '0012_auto_20211019_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_notes',
            name='base_note',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100, null=True), size=10), size=10),
        ),
        migrations.AlterField(
            model_name='product_notes',
            name='middle_note',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100, null=True), size=10), size=10),
        ),
        migrations.AlterField(
            model_name='product_notes',
            name='others',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100, null=True), size=10), size=10),
        ),
        migrations.AlterField(
            model_name='product_notes',
            name='top_note',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100, null=True), size=10), size=10),
        ),
    ]