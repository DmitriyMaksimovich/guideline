from django.db import models
from accounts.models import CustomUser


class Section(models.Model):
    section_name = models.CharField(max_length=50)
    guides_in_section = models.IntegerField(default=0)

    def __str__(self):
        return self.section_name


class Guide(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    guide_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    tags = models.CharField(max_length=255, blank=True)
    guide_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)
    preview = models.ImageField(upload_to='pic_folder/')
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    hidden = models.BooleanField(default=False)
    user_voted = models.ManyToManyField(CustomUser, related_name='guide_voted')

    def __str__(self):
        return "{} by {}".format(self.guide_name, self.author)
