from scrumboard.api import CardViewSet, ListViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
from django.contrib import  admin
router = DefaultRouter()
router.register(r'lists', ListViewSet)
router.register(r'cards', CardViewSet)

# urlpatterns = router.urls
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),

]
