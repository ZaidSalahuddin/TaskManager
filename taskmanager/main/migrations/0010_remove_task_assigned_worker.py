# Generated by Django 5.0.3 on 2024-03-07 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_task_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='assigned_worker',
        ),
    ]