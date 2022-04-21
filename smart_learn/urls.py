from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import users
import school

urlpatterns = [
    path('', include('users.urls')),
    path('school', include('school.urls')),
    path('admin/', admin.site.urls),
 
]




from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


admin.site.site_header = "All PC Solutions AdminPanel"
admin.site.site_title = "All PC Solutions App Admin"
admin.site.site_index_title = "Welcome To All PC Solutions Admin Panel"

