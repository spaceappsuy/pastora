from django.conf.urls import url
from .views import PredictView

urlpatterns = [
    url(r'^predict/$', PredictView.as_view(), name='predict_view'),
]