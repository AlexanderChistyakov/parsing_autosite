from django.urls import path, include
from rest_framework.routers import SimpleRouter

app_name = 'api'
router = SimpleRouter()

...


urlpatterns = [
    path('', include(router.urls)),
]