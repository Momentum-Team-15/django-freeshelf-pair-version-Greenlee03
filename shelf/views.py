from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Resource   
from shelf.forms import ResourceForm

# Create your views here.

def index(request):
        resource = Resource.objects.all().order_by('name')
        return render(request, 'shelf/index.html', {'resource': resource})

def resource_info(request):
        resource = Resource.objects.get(pk=pk)
        return render(request, 'shelf/resource_info.html', {'resource': resource})

@login_required
def create_resource(request):
        if request.method == 'POST':
                form = ResourceForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save()
                        return redirect("index")
        else:
                form = ResourceForm()
        return render(request, 'shelf/create_resource.html', {'form': form})
