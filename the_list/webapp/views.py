from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from webapp.forms import ListForms
from webapp.models import List, status_choices
from django.urls import reverse


# Create your views here.
def list_view(request):
    lists = List.objects.all()
    print(request.GET)
    return render(request, 'list_view.html', {'lists': lists})


def list_more(request, pk):
    # list_more=List.objects.get(id=pk)
    list = get_object_or_404(List, id=pk)
    return render(request, 'see_more.html', context={'list': list})


def add_list(request, *args, **kwargs):
    if request.method == "GET":
        form = ListForms()
        return render(request, 'add_list.html', {'form': form})
    elif request.method == "POST":
        form = ListForms(data=request.POST)
        if form.is_valid():
            status = form.cleaned_data["status"]
            description = form.cleaned_data["description"]
            date_created = form.cleaned_data["created_at"]
            about_list = form.cleaned_data['about_list']
            new_list = List.objects.create(status=status, description=description, created_at=date_created,
                                           about_list=about_list)
            return redirect('list_more', pk=new_list.pk)
        else:
            return render(request, 'add_list.html', {'form': form})
    # else:
    # new_list = List.objects.create(status=status, description=description, created_at=date_created, about_list=about_list )
    # return redirect('list_more', pk=new_list.id)


def list_update(request, pk):
    list = get_object_or_404(List, pk=pk)
    if request.method == 'GET':
        return render(request, 'update.html', context={'list': lists})
    elif request.method == 'POST':
        article.title = request.POST.get('title')
        list.description = request.POST.get('description')
        list.status = request.POST.get('status')
        list.created_at = request.POST.get('created_at')
        list.about_list = request.POST.get('about_list')
        list.save()
        return redirect('list_more', pk=list.pk)
