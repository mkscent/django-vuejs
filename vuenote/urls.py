from django.urls import path, include
from rest_framework.routers import DefaultRouter

from vuenote import views

router = DefaultRouter()
router.register(r'notes', views.NoteViewSet)

urlpatterns = [
    path('', include(router.urls))
]
