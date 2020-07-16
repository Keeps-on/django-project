from . import api_views
from django.urls import path
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # ...APIView
    path('book/', api_views.BookListView.as_view()),
    # GenericAPIView
    
    # path('book/(?P<pk>\d+)/$', api_views.BookListView.as_view()),
]

