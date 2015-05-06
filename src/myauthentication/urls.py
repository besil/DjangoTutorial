from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register/', views.MyRegister.as_view(), name="register"),
    url(r'^login/', views.MyLogin.as_view(), name="login"),
    url(r'^logout/', views.MyLogout.as_view(), name="logout"),
    url(r'^home/', views.MyHome.as_view(), name="home")
]
