# Generated by Django 2.1.5 on 2019-02-10 19:05

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guides', '0019_auto_20190205_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', ckeditor.fields.RichTextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_voted', models.ManyToManyField(blank=True, related_name='comment_voted', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='guide',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='guide_comments', to='guides.Comment'),
        ),
    ]