# Generated by Django 5.1.4 on 2024-12-16 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GrubHub', '0003_alter_restaurant_gst_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='gst_number',
            field=models.CharField(max_length=15),
        ),
    ]