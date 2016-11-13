from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.auth import views
from backend.forms import LoginForm
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^', include('frontend.urls')),
	url(r'^plataforma/', include('backend.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^api/', include('api.urls')),
	url(r'^plataforma/login/$', views.login, {'template_name': 'plataforma/login.html', 'authentication_form': LoginForm}),
	url(r'^plataforma/logout/$', views.logout, {'next_page': '/plataforma/login'}),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
