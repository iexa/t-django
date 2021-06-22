"""ajaxviews URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from halls import views
import debug_toolbar



urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dash', views.dashboard, name='dashboard'),
    # auth
    path('signup', views.SignUp.as_view(), name='signup'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    # hall -
    path('halloffame/create', views.CreateHall.as_view(), name='create_hall'),
    path('halloffame/<int:pk>', views.DetailHall.as_view(), name='detail_hall'),
    path('halloffame/<int:pk>/update', views.UpdateHall.as_view(), name='update_hall'),
    # deleteview has a get and a post too. get shows a template, post does delete
    path('halloffame/<int:pk>/delete', views.DeleteHall.as_view(), name='delete_hall'),

]
