from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('contactanos', views.contact, name='contact'),
    path('sobrenosotros', views.about, name='about'),
    path('vendeconnosotros', views.sellwithus, name='sellwithus'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#ESTO ES PARA PODER VER LAS IMAGENES EN OTRA PESTAÑA