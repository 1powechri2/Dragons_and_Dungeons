from django.contrib import admin
from django.urls import include, path
from dungdrag import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('login_user', views.login_user, name='login_user'),
    path('user_page', views.user_page, name='user_page'),
    path('logout_user', views.logout_user, name='logout_user'),
]
