from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
 
urlpatterns = [
    url(r'^$',views.index),
    url(r'^langdetect/$',views.langdetect.as_view()),
    url(r'^sentenceSplitting/$',views.sentenceSplitting.as_view()),
    url(r'^tokenizer/$',views.tokenizer.as_view()),
    url(r'^postagging/$',views.postagging.as_view()),
    url(r'^wsdtagger/$',views.wsdtagger.as_view()),
    url(r'^ner/$',views.ner.as_view()),
    url(r'^datesDetect/$',views.datesDetect.as_view()),
    url(r'^parser/$',views.parser.as_view()),
    url(r'^dependencies/$',views.dependencies.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)