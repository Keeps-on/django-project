
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






