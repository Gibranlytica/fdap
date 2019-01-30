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
# from rest_framework import routers
# #from fdap.views import LangdetectViewSet, SentenceSplittingViewSet, TokenizerViewSet, PostaggingViewSet, WsdtaggerViewSet, NerViewSet, DatesDetectViewSet, ParserViewSet, DependenciesViewSet
# from fdap.views import LangdetectViewSet

# router = routers.DefaultRouter()

# # router.register(r'admin/', admin.site.urls)
# router.register(r'langdetec', LangdetectViewSet, base_name='langdetec')
# router.register(r'sentenceSplitting', SentenceSplittingViewSet, base_name='sentencesplitting')
# router.register(r'tokenizer', TokenizerViewSet, base_name='tokenizer')
# router.register(r'postagging', PostaggingViewSet, base_name='postagging')
# router.register(r'wsdtagger', WsdtaggerViewSet, base_name='wsdtagger')
# router.register(r'ner', NerViewSet, base_name='ner')
# router.register(r'datesDetect', DatesDetectViewSet, base_name='datesDetect')
# router.register(r'parser', ParserViewSet, base_name='parser')
# router.register(r'dependencies', DependenciesViewSet, base_name='dependencies')

# router.register(r'', TaskViewSet, base_name='tasks')

# urlpatterns = router.urls

#urlpatterns = [
    #url('admin/', admin.site.urls),
 
    #url(r'^$', views.api_root),
    #url(r'^', include('users.urls', namespace='users')),
    #url(r'^', include('todos.urls', namespace='todos')),
    
    # url(r'^$', views.index, name='index'),
    #url(r'^langdetect/',views.langdetect),
    #url(r'^sentenceSplitting/',views.sentenceSplitting),
    #url(r'^tokenizer/',views.tokenizer),
    #url(r'^postagging/',views.postagging),
    #url(r'^wsdtagger/',views.wsdtagger),
    #url(r'^ner/',views.ner),
    #url(r'^datesDetect/',views.datesDetect),
    #url(r'^parser/',views.parser),
    #url(r'^dependencies/',views.dependencies),
#]
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
 
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include('fdap.urls')),
]