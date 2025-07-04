from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from root.settings import MEDIA_URL, MEDIA_ROOT
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/course/', include('course.urls')),

]+ static(MEDIA_URL, document_root=MEDIA_ROOT)
