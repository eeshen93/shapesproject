# Generated by Django 4.0 on 2022-06-03 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_shape_area_shape_perimeter'),
    ]

    operations = [
        migrations.AddField(
            model_name='shape',
            name='msg',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
