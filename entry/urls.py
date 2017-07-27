from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from . import views
from .models import Beer

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Beer.objects.all().order_by("-purchDate"), template_name = 'entry/table.html')),
    url(r'^postSale/$', views.postSale, name='postSale'),
    url(r'^makeSale/$', views.makeSale, name='makeSale'),
    ]