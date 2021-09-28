from django.contrib import admin
from django.urls import path, include
from allauth.account.views import confirm_email
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls', namespace='books')),
    path('api/', include('books_api.urls', namespace='books_api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('account/', include('allauth.urls')),
    path('index/', TemplateView.as_view(template_name='index.html'))
#    url(r'^rest-auth/', include('rest_auth.urls')),
#    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
#    path('^account/', include('allauth.urls')),
#    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# https://www.youtube.com/watch?v=56w8p0goIfs&list=RDCMUC1mxuk7tuQT2D0qTMgKji3w&start_radio=1