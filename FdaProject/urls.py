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
from rest_framework import routers
from fdap.views import TaskViewSet

router = routers.DefaultRouter()
# router.register(r'admin/', admin.site.urls)
# router.register(r'Langdetec', views.LangdetectViewSet)
# router.register(r'SentenceSplitting', views.SentenceSplittingViewSet)
# router.register(r'Tokenizer', views.TokenizerViewSet)
# router.register(r'Postagging', views.PostaggingViewSet)
# router.register(r'Wsdtagger', views.WsdtaggerViewSet)
# router.register(r'Ner', views.NerViewSet)
# router.register(r'DatesDetect', views.DatesDetectViewSet)
# router.register(r'Parser', views.ParserViewSet)
# router.register(r'Dependencies', views.DependenciesViewSet)

router.register(r'', TaskViewSet, base_name='tasks')

urlpatterns = router.urls

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
