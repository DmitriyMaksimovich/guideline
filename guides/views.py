from django.views import generic
from django.shortcuts import render
import datetime
from .models import Guide, Section


class IndexView(generic.ListView):
    model = Guide
    template_name = 'guides/index.html'
    context_object_name = 'guides_list'
    paginate_by = 3

    def get_queryset(self):
        return Guide.objects.order_by("-votes")

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['sections'] = Section.objects.order_by('guides_in_section')[:10]
        return context


class SortedIndexView(IndexView):
    def get_queryset(self):
        guides_filter = self.kwargs.get('filter', None)
        if not guides_filter or guides_filter == 'top_all_time':
            guides = Guide.objects.order_by("-votes")
        elif guides_filter == "top_month":
            current_month = datetime.date.today().month
            current_year = datetime.date.today().year
            guides = Guide.objects.filter(pub_date__gte=datetime.date(current_year, current_month, 1))
            guides = guides.order_by("-votes")
        elif guides_filter == 'new':
            guides = Guide.objects.order_by("-pub_date")
        else:
            guides = []
        return guides

    def get_context_data(self, **kwargs):
        context = super(SortedIndexView, self).get_context_data(**kwargs)
        context['sections'] = Section.objects.order_by('guides_in_section')[:10]
        return context


class SectionView(IndexView):
    def get_queryset(self):
        section = self.kwargs.get('section', None)
        return Guide.objects.filter(section=section).order_by("-votes")

    def get_context_data(self, **kwargs):
        context = super(SectionView, self).get_context_data(**kwargs)
        context['sections'] = Section.objects.order_by('guides_in_section')[:10]
        return context


class SectionBrowserView(generic.ListView):
    paginate_by = None
    template_name = 'guides/sections_browser.html'
    context_object_name = 'sections_list'

    def get_queryset(self):
        return Section.objects.order_by("-guides_in_section")

    def get_context_data(self, **kwargs):
        context = super(SectionBrowserView, self).get_context_data(**kwargs)
        context['sections'] = Section.objects.order_by('guides_in_section')[:10]
        return context


class GuideView(generic.DetailView):
    model = Guide
    template_name = 'guides/guide.html'
    context_object_name = 'guide'


def about_us_view(request):
    return render(request, 'guides/about_us.html', {})
