from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    template = "index.html"
    return render(request, template)

