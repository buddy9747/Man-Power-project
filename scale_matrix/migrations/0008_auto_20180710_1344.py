# Generated by Django 2.0 on 2018-07-10 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scale_matrix', '0007_auto_20180709_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scale',
            name='use',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
