from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from webapp.models import List, status_choices
from django.urls import reverse


# Create your views here.
def list_view(request):
    lists=List.objects.all()
    return render(request, 'list_view.html', {'lists': lists})

def list_more(request, pk):

    # list_more=List.objects.get(id=pk)
    list1=get_object_or_404(List, id=pk)
    return render(request, 'see_more.html', context={'list': list_more})


def add_list(request):
    if request.method == "GET":
        return render(request, 'add_list.html', {"choices": status_choices})
    else:
        status = request.POST.get("status")
        description=request.POST.get("description")
        date_created=request.POST.get("created_at ")
        about_list=request.POST.get('about_list')


        new_list = List.objects.create(status=status, description=description, created_at=date_created, about_list=about_list )
        return redirect('list_more', pk=new_list.id)