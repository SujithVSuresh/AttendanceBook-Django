# Generated by Django 3.2.9 on 2021-11-19 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_remove_attendance_student_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='present_status',
            field=models.ManyToManyField(to='attendance.Student'),
        ),
    ]
