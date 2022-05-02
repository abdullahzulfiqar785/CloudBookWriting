from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BookViewSet, SectionViewSet


router = SimpleRouter()
router.register('book', BookViewSet, basename='book')
router.register('section', SectionViewSet, basename='section')


urlpatterns = router.urls
