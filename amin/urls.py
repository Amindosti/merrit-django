from django.contrib import admin
from django.urls import path, include
import djoser.urls.authtoken


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(djoser.urls)),
    path('api/v1/', include(djoser.urls.authtoken)),
    path('', include('Home_page.urls')),
    path('form', include('Form.urls')),
    path('dataentry/', include('Data_Entry.urls'))
]
