import datetime
from django.views import generic
from django.db.models import Count
from .models import Guide, Section
from .forms import GuideForm


class IndexView(generic.ListView):
    template_name = 'guides/index_content.html'
    context_object_name = 'guides_list'
    paginate_by = 15

    def get_queryset(self):
        return Guide.objects.filter(hidden=False).annotate(Count('user_voted'))

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['sections'] = Section.objects.annotate(num_guides=Count('guide'))[:10]
        return context


class SortedIndexView(IndexView):
    def get_queryset(self):
        guides_filter = self.kwargs.get('filter', None)
        if not guides_filter or guides_filter == 'top_all_time':
            guides = Guide.objects.filter(hidden=False).annotate(Count('user_voted'))
        elif guides_filter == "top_month":
            current_month = datetime.date.today().month
            current_year = datetime.date.today().year
            guides = Guide.objects.filter(pub_date__gte=datetime.date(current_year, current_month, 1), hidden=False)
            guides = guides.annotate(Count('user_voted'))
        elif guides_filter == 'new':
            guides = Guide.objects.filter(hidden=False).order_by("-pub_date")
        else:
            guides = []
        return guides


class SectionView(IndexView):
    def get_queryset(self):
        section = self.kwargs.get('section', None)
        return Guide.objects.filter(section=section, hidden=False).annotate(Count('user_voted'))


class SectionBrowserView(IndexView):
    paginate_by = None
    template_name = 'guides/sections_browser.html'
    context_object_name = 'sections_list'

    def get_queryset(self):
        return Section.objects.annotate(num_guides=Count('guide')).order_by('-num_guides')


class MyGuidesView(IndexView):
    template_name = 'guides/my_guides.html'

    def get_queryset(self):
        return Guide.objects.filter(author=self.request.user.pk).order_by('-pub_date')


class GuideView(generic.DetailView):
    model = Guide
    template_name = 'guides/guide.html'
    context_object_name = 'guide'

    def get_context_data(self, **kwargs):
        context = super(GuideView, self).get_context_data(**kwargs)
        context['sections'] = Section.objects.annotate(num_guides=Count('guide'))[:10]
        return context


class CreateGuideView(generic.edit.FormView):
    template_name = 'guides/guide_creation.html'
    form_class = GuideForm
    success_url = '/my_guides/'

    def get_form_kwargs(self):
        kwargs = super(CreateGuideView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['section'] = self.request.POST.get('section', 'other')
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(CreateGuideView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateGuideView, self).get_context_data(**kwargs)
        sections_query = Section.objects.all()
        sections_list = [section.section_name for section in sections_query]
        context["existing_sections"] = sections_list
        return context


def vote():
    pass


class AboutUsView(generic.TemplateView):
    template_name = 'guides/about_us.html'
