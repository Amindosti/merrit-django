from django.urls import path, include
from Home_page import views

urlpatterns = [
    path('', views.data_entry_list),
    path('<int:pk>', views.data_entry_detail),
    path('dashboard/', include('Dashboard.urls')),

]
