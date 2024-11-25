from django.views.generic import TemplateView
from django.shortcuts import render


class SimpleView(TemplateView):
    template_name = 'index.html'


def custom_404(request, exception):
    context = {}
    return render(request, 'index.html', status=404, context=context)


def custom_403(request, exception):
    context = {}
    return render(request, 'index.html', status=403, context=context)


def custom_400(request, exception):
    context = {}
    return render(request, 'index.html', status=400, context=context)


def custom_500(request):
    context = {}
    return render(request, 'index.html', status=500, context=context)