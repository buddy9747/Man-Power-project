# Generated by Django 2.0 on 2018-06-28 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Absenteeism', '0007_remove_person_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='status',
            field=models.CharField(choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=10),
        ),
    ]
