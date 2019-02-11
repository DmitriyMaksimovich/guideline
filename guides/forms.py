from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist
from .models import Guide, Section, Tag, Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

    def save(self, user, guide):
        comment = super(CommentForm, self).save(commit=False)
        comment.author = user
        comment.guide = guide
        comment.save()
        return comment


class GuideForm(ModelForm):
    class Meta:
        model = Guide
        fields = ['guide_name', 'description', 'preview', 'hidden', 'guide_text']

    def __init__(self, user, section, tags, *args, **kwargs):
        self.user = user
        self.section = section
        self.tags = tags
        super(GuideForm, self).__init__(*args, **kwargs)

    def save(self):
        guide = super(GuideForm, self).save(commit=False)
        guide.author = self.user
        guide.section = get_guide_section(self.section)
        guide.save()
        tags = get_tags_objects(self.tags)
        [guide.tags.add(tag) for tag in tags]
        return guide


def get_guide_section(section_name):
    # form have default value, it can be '', .get('section', default) did'n work in this case
    if not section_name:
        section_name = 'Other'
    try:
        section_object = Section.objects.get(section_name__iexact=section_name)
    except ObjectDoesNotExist:
        section_name = section_name.strip().capitalize()
        section_object = Section(section_name=section_name)
        section_object.save()
    return section_object


def get_tags_objects(tags_string):
    tags = set()
    tags_list = tags_string.split(',')
    tags_list = [tag.strip().capitalize() for tag in tags_list]
    for tag_name in tags_list:
        try:
            tag_object = Tag.objects.get(tag__iexact=tag_name)
        except ObjectDoesNotExist:
            tag_object = Tag(tag=tag_name)
            tag_object.save()
        tags.add(tag_object)
    return tags
