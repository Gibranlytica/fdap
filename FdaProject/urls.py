"""FdaProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from fdap import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^langdetect/',views.langdetect),
    url(r'^sentenceSplitting/',views.sentenceSplitting),
    url(r'^tokenizer/',views.tokenizer),
    url(r'^postagging/',views.postagging),
    url(r'^wsdtagger/',views.wsdtagger),
    url(r'^ner/',views.ner),
    url(r'^datesDetect/',views.datesDetect),
    url(r'^parser/',views.parser),
    url(r'^dependencies/',views.dependencies),
]
