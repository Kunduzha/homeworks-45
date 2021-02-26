from django.shortcuts import render
from webapp.models import List
# Create your views here.
def list_view(request):
    lists=Listj.objects.all()
    return render(request, 'list_view.html', context={'lists': lists})


def add_list(request):
    list=get_object_or_404(List, id=pk)
    return render(request, 'add_list.html', context='list':list)

