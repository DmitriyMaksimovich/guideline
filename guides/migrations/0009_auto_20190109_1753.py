# Generated by Django 2.1.4 on 2019-01-09 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0008_guide_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
