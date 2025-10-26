from django.urls import path
from .views import HomeView, ServiceView, contact, GalleryView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('services/', ServiceView.as_view(), name='services'),
    path('contact/', contact, name='contact'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
]