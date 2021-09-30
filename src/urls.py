from django.contrib import admin
from django.urls import path, include
from allauth.account.views import confirm_email
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls', namespace='books')),
    path('basket/', include('basket.urls', namespace='basket')),
    path('api/', include('books_api.urls', namespace='books_api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('account/', include('allauth.urls')),
    path('index/', TemplateView.as_view(template_name='index.html')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
