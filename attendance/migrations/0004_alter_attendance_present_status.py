# Generated by Django 3.2.9 on 2021-11-25 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_alter_attendance_present_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='present_status',
            field=models.ManyToManyField(blank=True, null=True, to='attendance.Student'),
        ),
    ]
