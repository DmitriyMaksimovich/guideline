from django.views import generic
from django.db.models import Count
import datetime
from .models import Guide, Section


class IndexView(generic.ListView):
    template_name = 'guides/index_content.html'
    context_object_name = 'guides_list'
    paginate_by = 15

    def get_queryset(self):
        return Guide.objects.filter(hidden=False).annotate(Count('user_voted'))

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['sections'] = Section.objects.order_by('guides_in_section')[:10]
        context['user_is_logged'] = self.user_is_logged
        return context

    @property
    def user_is_logged(self):
        if self.request.user.is_authenticated:
            return True
        else:
            return False


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
        return Section.objects.order_by("-guides_in_section")


class MyGuidesView(IndexView):
    def get_queryset(self):
        return Guide.objects.filter(author=self.request.user.pk).order_by('-pub_date')


class GuideView(generic.DetailView):
    model = Guide
    template_name = 'guides/guide.html'
    context_object_name = 'guide'


class CreateGuideView(generic.TemplateView):
    template_name = 'guides/guide_creation.html'


class AboutUsView(generic.TemplateView):
    template_name = 'guides/about_us.html'
