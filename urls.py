from django.urls import path, include
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = ""
admin.site.site_title = ""
admin.site.index_title = ""