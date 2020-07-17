from . import api_views
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from . import exten_views 
urlpatterns = [
    # ...APIView
    path('book/', api_views.BookListView.as_view()),
    # GenericAPIView
    # re_path('^book/(?P<pk>\d+)/&', api_views.BookDetailView.as_view()),
    # 扩展类
    path('book/list/', exten_views.BookListView.as_view()),
]

