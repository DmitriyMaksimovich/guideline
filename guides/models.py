from django.db import models
from accounts.models import CustomUser
from ckeditor.fields import RichTextField


class Section(models.Model):
    section_name = models.CharField(max_length=50)

    def __str__(self):
        return self.section_name


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag


class Guide(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    guide_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    tags = models.ManyToManyField(Tag, related_name='guide_tags', blank=True)
    guide_text = RichTextField(config_name='guide_creation')
    pub_date = models.DateTimeField(auto_now_add=True)
    preview = models.CharField(max_length=255)
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    hidden = models.BooleanField(default=False)
    user_voted = models.ManyToManyField(CustomUser, related_name='guide_voted', blank=True)

    def __str__(self):
        return "{}. {} by {}".format(self.pk, self.guide_name, self.author)

    def convert_tags_to_string(self):
        tags_query = self.tags.all()
        tags_list = [tag_obj.tag for tag_obj in tags_query]
        tags_string = ', '.join(tags_list)
        return tags_string


class Comment(models.Model):
    comment_text = RichTextField(config_name='comment')
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    user_voted = models.ManyToManyField(CustomUser, related_name='comment_voted', blank=True)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)

    def __str__(self):
        return "{} by {}".format(self.comment_text, self.author)
