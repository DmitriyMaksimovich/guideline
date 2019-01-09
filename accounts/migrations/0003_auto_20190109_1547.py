# Generated by Django 2.1.4 on 2019-01-09 15:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190109_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='test_field',
            field=models.CharField(default='test', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
    ]
