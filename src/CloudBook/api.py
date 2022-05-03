from django.urls import path, include

urlpatterns = [
    path('book/', include("BookWriting.api")),
    path('auth/', include('rest_framework.urls'))
]
