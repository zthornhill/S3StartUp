from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('about/', TemplateView.as_view(template_name='About.html'), name='About'),
    path('features/', TemplateView.as_view(template_name='Features.html'), name='Features'),
    path('home/', TemplateView.as_view(template_name='home.html'), name='Home')


]

