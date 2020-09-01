from django.contrib import admin
from django.urls import path

from sdh.shortener import views as shortener_views

urlpatterns = [
    path('', shortener_views.root, name='root'),
    path('shorten/', shortener_views.ShortenView.as_view(), name='shorten-url'),
    path('shortened-list/', shortener_views.list, name='shortened-list'),
    path('<slug:slug>/', shortener_views.redirect_shortened, name='redirect-slug'),
    path('admin/', admin.site.urls),
]
