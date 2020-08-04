from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views
from .views import ( login, register, logout, home, verify_password, profile, 
send_verification_email_, broken_link, update_password, )
from django.conf import settings
from django.conf.urls.static import static 
from django_email_verification import urls as mail_urls
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',          login,                  name='login'),
    path('register/',       register,               name='register'),
    path('logout/',         logout,                 name='logout'),
    path('home/',           home,                   name='home'),
    path('verify-password/', verify_password,        name='verify'),
    path('verify-password/update-password/', update_password,        name='update'),
    # path('recover/',        reset_password,         name='recoverpassword'),
    # path('emailcode/',      code_match,             name='matchcode'),
    # path('newpassword/',    new_password,           name='newpassword'),
    path('email/', include(mail_urls)),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/',        profile,                name='profile'),
    path('broken/',        broken_link,                name='broken_link'),
    path('email_verification/',        send_verification_email_,                name='send_verification_email'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)