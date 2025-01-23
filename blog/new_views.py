from django.views.generic import ListView, DetailView
from .models import Topic, Category


# list view
class TopListView(ListView):
    model = Topic
    context_object_name = "topics"
    template_name = "top_list.html"

    def get_queryset(self):
        queryset = Topic.objects.all()
        category_slug = self.request.GET.get('category')

        if category_slug:
            queryset = queryset.filter(category__name=category_slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
# detail view. 

class TopDetailView(DetailView):
    model = Topic
    template_name = "top_detail.html"
    context_object_name = 'topic'
