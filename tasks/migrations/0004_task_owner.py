# Generated by Django 4.1 on 2022-08-12 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_remove_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='owner',
            field=models.CharField(default='dummy', max_length=100),
            preserve_default=False,
        ),
    ]
