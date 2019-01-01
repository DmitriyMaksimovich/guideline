from django.views import generic
from django.shortcuts import render
import datetime
from .models import Guide, Section


class IndexView(generic.ListView):
    template_name = 'guides/index.html'

    def get_queryset(self):
        return

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['sections'] = Section.objects.order_by('guides_in_section')[:10]
        context['guides_list'] = Guide.objects.order_by("-votes")[:10]
        return context


class SortedIndexView(generic.ListView):
    template_name = 'guides/index.html'

    def get_queryset(self):
        return

    def get_context_data(self, **kwargs):
        context = super(SortedIndexView, self).get_context_data(**kwargs)
        context['sections'] = Section.objects.order_by('guides_in_section')[:10]
        guides_filter = self.kwargs.get('filter', None)
        if not guides_filter or guides_filter == 'top_all_time':
            guides = Guide.objects.order_by("-votes")[:10]
        elif guides_filter == "top_month":
            current_month = datetime.date.today().month
            current_year = datetime.date.today().year
            guides = Guide.objects.filter(pub_date__gte=datetime.date(current_year, current_month, 1))
            guides = guides.order_by("-votes")[:10]
        elif guides_filter == 'new':
            guides = Guide.objects.order_by("-pub_date")[:10]
        else:
            guides = []
        context['guides_list'] = guides
        return context


class SectionView(generic.ListView):
    template_name = 'guides/index.html'

    def get_queryset(self):
        return

    def get_context_data(self, **kwargs):
        context = super(SectionView, self).get_context_data(**kwargs)
        context['sections'] = Section.objects.order_by('guides_in_section')[:10]
        section = self.kwargs.get('section', None)
        context['guides_list'] = Guide.objects.filter(section=section).order_by("-votes")[:10]
        return context


class GuideView(generic.DetailView):
    model = Guide
    template_name = 'guides/guide.html'


def about_us_view(request):
    return render(request, 'guides/about_us.html', {})
