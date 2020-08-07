from . import api_views
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from . import exten_views 
urlpatterns = [
    # ...APIView
    path('book/', api_views.BookListView.as_view()),
    # GenericAPIView
    re_path('^book/(?P<pk>\d+)/$', api_views.BookDetailView.as_view()),
    # 扩展类
    path('book/list/', exten_views.BookListView.as_view()),
    # ViewSet
    re_path(r'^bookviewset/$', exten_views.BookInfoViewSet.as_view({'get':'list'})),
    re_path(r'^bookviewset/(?P<pk>\d+)/$', exten_views.BookInfoViewSet.as_view({'get': 'retrieve'})),
    # GenericViewSet
    re_path(r'^booksviewset/$', exten_views.BooksInfoViewSet.as_view({'get':'list'})),
    re_path(r'^booksviewset/(?P<pk>\d+)/$', exten_views.BooksInfoViewSet.as_view({'get': 'retrieve'})),
    # ModelViewSet
    re_path(r'^booksmodelviewset/$', exten_views.BooksModelInfoViewSet.as_view({'get':'list'})),
    re_path(r'^booksmodelviewset/(?P<pk>\d+)/$', exten_views.BooksModelInfoViewSet.as_view({'get': 'retrieve'})),
    # Action
    re_path(r'^booksaction/$', exten_views.BookActionInfoViewSet.as_view({'get': 'list'})),
    re_path(r'^booksaction/latest/$', exten_views.BookActionInfoViewSet.as_view({'get': 'latest'})),
    re_path(r'^booksaction/(?P<pk>\d+)/$', exten_views.BookActionInfoViewSet.as_view({'get': 'retrieve'})),
    re_path(r'^booksaction/(?P<pk>\d+)/read/$', exten_views.BookActionInfoViewSet.as_view({'put': 'read'})),
]

