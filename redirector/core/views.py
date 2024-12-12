from django.shortcuts import render

def redirect_with_path(request, path=""):
    return render(request, 'redirect.html', {'path': path})
