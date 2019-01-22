from django.db import models
from accounts.models import CustomUser
from ckeditor.fields import RichTextField


class Section(models.Model):
    section_name = models.CharField(max_length=50)

    def __str__(self):
        return self.section_name


class Guide(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    guide_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    tags = models.CharField(max_length=255, blank=True)
    guide_text = RichTextField(config_name='guide_creation')
    pub_date = models.DateTimeField(auto_now_add=True)
    preview = models.ImageField(upload_to='pic_folder/')
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    hidden = models.BooleanField(default=False)
    user_voted = models.ManyToManyField(CustomUser, related_name='guide_voted', blank=True)

    def __str__(self):
        return "{} by {}".format(self.guide_name, self.author)
