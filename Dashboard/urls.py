from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Dashboard import views

urlpatterns = [
    path('', views.dashboard_list),
    path('<int:pk>', views.dashboard_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
