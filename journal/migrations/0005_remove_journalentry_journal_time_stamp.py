# Generated by Django 4.1.4 on 2023-02-10 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0004_remove_todolist_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journalentry',
            name='journal_time_stamp',
        ),
    ]