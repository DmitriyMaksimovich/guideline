# Generated by Django 2.1.4 on 2019-01-09 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0007_auto_20190109_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]
