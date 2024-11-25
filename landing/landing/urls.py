from django.urls import path
from website.views import SimpleView

urlpatterns = [
    path('', SimpleView.as_view(), name='simple_view'),
]

handler404 = 'website.views.custom_404'
handler500 = 'website.views.custom_500'
handler403 = 'website.views.custom_403'
handler400 = 'website.views.custom_404'