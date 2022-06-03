# Generated by Django 4.0 on 2022-06-02 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape_type', models.CharField(blank=True, max_length=50, null=True)),
                ('side1', models.IntegerField(blank=True, null=True)),
                ('side2', models.IntegerField(blank=True, null=True)),
                ('side3', models.IntegerField(blank=True, null=True)),
                ('side4', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]