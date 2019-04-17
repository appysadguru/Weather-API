from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('hw3/', include('hw3.urls')),
    path('admin/', admin.site.urls),
    path('', include('hw2.urls')),
]


