from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 
from django.conf import settings
from django.conf.urls.static import static

# all the urls for correct redirection regarding the account stuff(login logout register)
urlpatterns = [
    path('', views.render_account, name='account'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_signup, name='register'),
    path('logout/', views.user_logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)