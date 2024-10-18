from django.shortcuts import render
from .forms import StuForm



def index(request):
    stu = StuForm()

    return render(request, "index.html", {'form': stu})
