from django.forms import ModelForm
from .models import Guide


class GuideForm(ModelForm):
    class Meta:
        model = Guide
        fields = ['section', 'guide_name', 'description', 'preview', 'hidden', 'tags', 'guide_text']

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(GuideForm, self).__init__(*args, **kwargs)

    def save(self):
        guide = super(GuideForm, self).save(commit=False)
        guide.author = self.user
        guide.save()
        return guide
