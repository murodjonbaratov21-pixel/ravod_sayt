from django.contrib import admin
from django.urls import path
from ravod_web import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.bosh_sahifa),
    path('katalog/', views.katalog),
    path('biz-haqimizda/', views.biz_haqimizda),
    path('savatcha/', views.savatcha),
    path('profil/', views.profil),
    path('katalog/<int:pk>/', views.mahsulot_batafsil),
]

# Rasmlar brauzerda ochilishi uchun sehrli kod:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)