from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('electrocar/', include('map.urls')),
    path('electrocar_c/', include('customer.urls')),
]
