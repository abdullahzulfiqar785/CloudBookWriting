from django.urls import path, include

urlpatterns = [
    path('book/', include("BookWriting.api"))
]