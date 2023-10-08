from django.urls import path

from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name='index'),
    path('home/', views.home,name='home'),
    path('contact/', views.contact,name='contact'),
    path('buy/', views.buy,name='buy'),
    path('about/', views.about,name='about'),
    path('medicine/', views.medicine,name='medicine'),
    path('Category1', views.cow_category, name='cow'),
    path('Category2', views.buf_category, name='buff'),
    path('Species1/<int:pk>/', views.cow_sp, name='spcow'),
    path('Species2/<int:pk>/', views.buf_sp, name='spbuff'),

   
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)