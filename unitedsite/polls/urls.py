from django.urls import path
from . import views
urlpatterns = [
    path('', views.toLogin_view),
    path('main/', views.login_view),
    path('toregister/', views.toregister_view),
    path('register/', views.register_view)
]