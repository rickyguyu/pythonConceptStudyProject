from django.urls import path
from . import views
urlpatterns = [
    path('', views.toLogin_view),
    path('login/', views.login_view),
    path('toregister/', views.toregister_view),
    path('register/', views.register_view),
    path('main/', views.main_view),
    path('newBusiness/', views.new_business),
    path('savebusiness/', views.savebusiness),
]