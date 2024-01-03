from django.urls import path, include
from myapp.views import BookModelViewSet, AuthorModelViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register('books', BookModelViewSet)
router.register('authors', AuthorModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]