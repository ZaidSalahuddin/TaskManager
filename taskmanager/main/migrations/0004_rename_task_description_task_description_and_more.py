# Generated by Django 5.0.3 on 2024-03-07 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_tasks_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='name',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='name',
            name='task_owner',
        ),
        migrations.RemoveField(
            model_name='task',
            name='worker_name',
        ),
        migrations.AddField(
            model_name='name',
            name='email',
            field=models.EmailField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='name',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='task',
            name='assigned_worker',
            field=models.ManyToManyField(blank=True, to='main.name'),
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_to_complete',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]