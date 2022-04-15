from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.toLogin_view),
    path('login/', views.login_view),
    path('toregister/', views.toregister_view),
    path('register/', views.register_view),
    path('main/', views.main_view),
    path('newBusiness/', views.new_business),
    path('savebusiness/', views.savebusiness),
    path('delbusiness/', views.delbusiness),
    path('export/', views.exportbusiness, name='export'),
    path('import/', views.importbusiness, name='import'),
    path('search/', views.search),

] #+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

