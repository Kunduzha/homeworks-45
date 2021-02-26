from django.shortcuts import render
from webapp.models import List, status_choices


# Create your views here.
def list_view(request):
    lists=List.objects.all()
    return render(request, 'list_view.html', {'lists': lists})


def add_list(request):
    if request.method == "GET":
        return render(request, 'add_list.html', {"choices": status_choices})
    else:
        status = request.POST.get("status")
        description=request.POST.get("description")
        date_created=request.POST.get("created_at ")


        List.objects.create(status=status, description=description, date_created=date_created  )