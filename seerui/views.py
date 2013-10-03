# Create your views here.

from django.shortcuts import render

context = {
    'webAppName': 'Your App Name'
}


def index(request):
    context['tabId'] = ''
    return render(request, "index.html", context)


def tab1(request):
    context['tabId'] = 'tab1'
    return render(request, "tab1.html", context)


def tab2(request):
    context['tabId'] = 'tab2'
    return render(request, "tab2.html", context)


def tab3(request):
    context['tabId'] = 'tab3'
    return render(request, "tab3.html", context)


def page_not_found_error(request):
    """
    This view is for test only. In production stage, you should turn off the DEBUG and remove the '404page' URL.
    Django will call the 404.html page by default for handling 404 error.
    """
    context['tabId'] = ''
    return render(request, "404.html", context)


def server_error(request):
    """
    Just like page_not_found_error function. In production stage, you should remove the '500page' URL. This function
    is just for test only.
    """
    context['tabId'] = ''
    return render(request, "500.html", context)