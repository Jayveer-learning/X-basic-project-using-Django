"""
URL configuration for Jhaimer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.urls import views as auth_views # import the django built-in authentication views for routing the authentication urls to the main urls.py file for routing the authentication urls.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tweet.urls')), # include the tweet app urls.py file to the main urls.py file for routing the urls of the tweet app. 
    path('accounts/', include('django.contrib.auth.urls')), # include the django built-in authentication urls to the main urls.py file for routing the authentication urls. 


    path('__reload__/', include('django_browser_reload.urls')) # add this line to enable browser reload feature in development mode only not in production because it is not secure to use in production. 
]
# + static(
#     settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
#     ) # use in development for media rouding.

# use in production for media routing. we use web server like Nginx or Apache to server your media files like images, videos

if settings.DEBUG:  # execute only when DEBUG is True. use web server in profuction. 
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
        )
