# Generated by Django 2.1.3 on 2018-12-19 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0002_guide_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guide',
            old_name='preveiw',
            new_name='preview',
        ),
        migrations.AddField(
            model_name='guide',
            name='hidden',
            field=models.CharField(default='', max_length=5),
            preserve_default=False,
        ),
    ]
