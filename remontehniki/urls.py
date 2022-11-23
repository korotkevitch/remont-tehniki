"""remontehniki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from remont import views
from remont.views import HomeView, ContactFormView, CallBackFormView, ThanksView
from django.conf.urls.static import static
from django.conf import settings
from django.db import models
from django.views.generic import TemplateView

admin.site.site_header = 'remontehniki.by'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='index'),
    path('contact_form', ContactFormView.as_view(), name="contact_form"),
    path('callback_form', CallBackFormView.as_view(), name="callback_form"),
    path('thanks/', ThanksView.as_view(), name='thanks'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
