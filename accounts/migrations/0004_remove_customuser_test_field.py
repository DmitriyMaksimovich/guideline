# Generated by Django 2.1.4 on 2019-01-09 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190109_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='test_field',
        ),
    ]