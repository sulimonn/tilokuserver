from django.shortcuts import render
from api.models import GroupItem


# Create your views here.
def index(request):
    class5 = GroupItem.objects.all()
    return render(request, "main/index.html", {"classes": class5})
