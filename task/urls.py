from django.conf.urls import url
from task import views

urlpatterns = [
    url(r'^create/$', views.TaskCreateView.as_view(), name='create'),
    url(r'^update/(?P<id>\d+)/$', views.TaskUpdateView.as_view(), name='update'),
    url(r'^list/$', views.TaskListView.as_view(), name='list'),
    url(r'^delete/(?P<id>\d+)/$', views.TaskDeleteView.as_view(), name='delete'),
    url(r'^train/$', views.TrainView.as_view(), name='api_data_train'),
    url(r'^prediction/$', views.PredictionView.as_view(), name='api_data_prediction'),
]
