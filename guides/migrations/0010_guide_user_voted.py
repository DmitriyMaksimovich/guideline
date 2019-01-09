# Generated by Django 2.1.4 on 2019-01-09 18:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guides', '0009_auto_20190109_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='user_voted',
            field=models.ManyToManyField(related_name='guide_voted', to=settings.AUTH_USER_MODEL),
        ),
    ]
