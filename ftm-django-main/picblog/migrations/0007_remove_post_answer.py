# Generated by Django 3.2.4 on 2021-06-15 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picblog', '0006_auto_20210613_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='answer',
        ),
    ]