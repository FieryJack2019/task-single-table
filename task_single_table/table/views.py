from django.http.response import JsonResponse
from .models import TableModel
from django.views.generic import ListView
from django.core.paginator import Paginator

class TableListView(ListView):
    model = TableModel
    template_name = 'table/index.html'
    paginate_by = 10

    def post(self, request):
        fieldName = request.POST.get('fieldName', '')
        condition = request.POST.get('condition', '')
        value = request.POST.get('value', '')
        if all(map(lambda x: x, [fieldName, value])):
            queryset = TableModel.objects.filter(**{fieldName+condition: value})
        else:
            queryset = TableModel.objects.all()
        paginator = Paginator(queryset, per_page=10)
        page = paginator.page(request.POST.get('page', 1))

        return JsonResponse({'object_list': list(page.object_list.values()), 
                             'page_obj': {'has_next': page.has_next(),
                                          'has_previous': page.has_previous()}})

    def get_queryset(self):
        new_context = TableModel.objects.all()
        return new_context