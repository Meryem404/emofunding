from django.shortcuts import render

# Create your views here.
def index(request):
   return  render(request, 'projects/projects.html')

def project(request):
   return render(request, 'projects/project.html')

def search(request):
    return render(request, 'projects/search.html')
