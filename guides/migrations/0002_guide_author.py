# Generated by Django 2.1.3 on 2018-12-02 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='author',
            field=models.CharField(default='nobody', max_length=100),
            preserve_default=False,
        ),
    ]
