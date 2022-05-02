from rest_framework.viewsets import ModelViewSet
from BookWriting.models import Book, Section
from .serializers import BookSerializer, SectionSerializer


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.prefetch_related('sections').all()


class SectionViewSet(ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.filter()
