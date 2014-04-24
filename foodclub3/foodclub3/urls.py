from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foodclub3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^submit/', 'blog.views.submit'),
	url(r'^About/', 'blog.views.about'),
	url(r'^(?P<name>[\w\-]+)/$', 'blog.views.post'),
	url(r'^(?P<name>[\w|\W]+)/$', 'blog.views.post'),
	url(r'^$', 'blog.views.index'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)