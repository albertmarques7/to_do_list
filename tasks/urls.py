from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, index

router = DefaultRouter()
router.register(r'', TaskViewSet)  

urlpatterns = [
    path('', index, name='index'),  
    path('api/tasks/', include(router.urls)),
]
