from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    # return render(request, 'home.html')
    no1= int(request.GET.get('no1'))
    no2= int(request.GET.get('no2'))

    answer = no1 + no2

    return render (request, 'result.html',{ 'answer' : answer})
