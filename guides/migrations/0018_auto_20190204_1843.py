# Generated by Django 2.1.5 on 2019-02-04 18:43

from django.db import migrations, models
import guides.models


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0017_auto_20190204_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='preview',
            field=models.CharField(max_length=255),
        ),
    ]
