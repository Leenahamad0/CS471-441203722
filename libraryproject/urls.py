from django.contrib import admin
from django.urls import include, path
from django.conf import settings  # Lab 11 - Task 3
from django.conf.urls.static import static  # Lab 11 - Task 3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include("apps.bookmodule.urls")),
    path('users/', include("apps.usermodule.urls"))
]

# This configuration allows Django to serve uploaded media files during local development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)