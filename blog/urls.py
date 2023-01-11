from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('inicio', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('contactanos', views.contact, name='contact'),
    path('sobrenosotros', views.about, name='about'),

]
