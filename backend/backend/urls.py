
from django.contrib import admin
from django.conf import settings  # new
from django.urls import path
from django.conf.urls.static import static  # new

urlpatterns = [
    path('admin/', admin.site.urls),
]
if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)