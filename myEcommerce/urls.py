
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('App_account.urls')),
    path('store/', include('App_store.urls')),
    path('', views.index,name ='index'),
]
