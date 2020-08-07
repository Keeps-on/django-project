
"""
扩展类的试图函数
"""
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response  
from rest_framework.generics import GenericAPIView
from .models import BookInfo,HeroInfo
from .serializers import BookInfoSerializer


"""
所谓的扩展类表示的在该类中只有一个方法
当我们使用该方法的时候恶意继承该扩展类

源码：
class ListModelMixin(object):
    
    # List a queryset.
    
    def list(self, request, *args, **kwargs):
        # 过滤
        queryset = self.filter_queryset(self.get_queryset())
        # 分页
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        # 序列化
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


"""
# path('book/list/', exten_views.BookListView.as_view()),
class BookListView(ListModelMixin,GenericAPIView):
	"""
	List a queryset
	"""
	queryset = BookInfo.objects.all()
	serializer_class = BookInfoSerializer

	def get(self,request):
		return self.list(request)

"""
该方法的总结：
在该方法中使用的是
	GenericAPIView 中的 queryset 和 serializer_class
	使用了ListModelMixin中的 list 方法
	
"""
# CreateModelMixin
"""
创建视图扩展类，提供create(request, *args, **kwargs)方法快速实现创建资源的视图，成功返回201状态码。

"""

#############使用视图集ViewSet#############

# list() 提供一组数据
# retrieve() 提供单个数据
# create() 创建数据
# update() 保存数据
# destory() 删除数据
from rest_framework.viewsets import ViewSet
class BookInfoViewSet(ViewSet):

    def list(self, request):
        books = BookInfo.objects.all()
        serializer = BookInfoSerializer(books, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            books = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookInfoSerializer(books)
        return Response(serializer.data)

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action

class BooksInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer


from rest_framework.viewsets import ModelViewSet 
class BooksModelInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer


from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action

class BookActionInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    def latest(self, request):
        """
        返回最新的图书信息
        """
        print(self.action)
        book = BookInfo.objects.latest('id')
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    def read(self, request, pk):
        """
        修改图书的阅读量数据
        """

        book = self.get_object()
        book.bread = request.data.get('read')
        book.save()
        serializer = self.get_serializer(book)
        return Response(serializer.data)

        