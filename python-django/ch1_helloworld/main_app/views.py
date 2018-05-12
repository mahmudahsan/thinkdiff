from django.http import HttpResponse

def homeView(request):
    return HttpResponse('Hello World')

def anotherView(request):
    return HttpResponse("<h1>Another<h1>")