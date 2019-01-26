from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist
from .models import Guide, Section


class GuideForm(ModelForm):
    class Meta:
        model = Guide
        fields = ['guide_name', 'description', 'preview', 'hidden', 'tags', 'guide_text']

    def __init__(self, user, section, *args, **kwargs):
        self.user = user
        self.section = section.capitalize()
        super(GuideForm, self).__init__(*args, **kwargs)

    def get_guide_section(self):
        try:
            section_object = Section.objects.get(section_name__iexact=self.section)
            return section_object
        except ObjectDoesNotExist:
            guide_section = Section(section_name=self.section)
            guide_section.save()
            return guide_section

    def save(self):
        guide = super(GuideForm, self).save(commit=False)
        guide.author = self.user
        guide.section = self.get_guide_section()
        guide.save()
        return guide
