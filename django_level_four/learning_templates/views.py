from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict= {'name':'hello worl', 'number':100}
    return render(request,'basic_app/index.htm',context_dict)

def other(request):
    return render(request,'basic_app/other.htm')

def url_templates(request):
    return render(request,'basic_app/relative_url_templates.htm')
