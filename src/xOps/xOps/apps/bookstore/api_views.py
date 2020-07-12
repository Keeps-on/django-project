


"""
两个基类
    APIView
        rest_framework.views.APIView
            APIView是REST framework提供的所有视图的基类，继承自Django的View父类。
        APIView与View的不同之处在于：
            传入的是 rest_framework Request 对象 === 而不是Django的HttpRequeset对象
            视图方法可以返回rest_framework的 Response 对象，视图会为响应数据设置（render）符合前端要求的格式；
            任何APIException异常都会被捕获到，并且处理成合适的响应信息
            在进行dispatch()分发前
            请求进行
                身份认证、
                权限检查、
                流量控制
        支持定义的属性
            authentication_classes 列表或元祖
            permissoin_classes 列表或元祖,权限检查类
            hrottle_classes 列表或元祖，流量控制类
    
    GenericAPIView 继承自 APIView 主要增加了序列化器和数据库查询的方法,
        作用是为下面Mixin扩展类的执行提供方法支持,通常在使用时,可搭配一个或多个Minin扩展类
        在GenericAPIView中通过设置属相的方式,每个属性有对应的方法进行对数据的操作
        单一数据：rest_framework.generics.RetrieveAPIView 
        提供的方法
            get_queryset(self)
            get_object()
            get_serializer(self,*args,**kwargs)
            get_serializer_calss(self)
            get_serializer_context(self)
            filter_queryset(self,queryset)
        提供的属性
            queryset
            serializer_class
            lookup_field
            lookup_url_kwarg
            filter_backends
            pagination_class
        常用的扩展类
            作用：提供了几种后端视图(对数据资源进行增删改查)处理流程的实现,如果需要编写的视图属于这五种,则视图
            可以通过继承响应的扩展类来复用代码,减少自己编写的代码量。
            【注意：】这五个扩展类需要搭配GenericAPIView父类,因为五个扩展类的实现小调用GenericAPIView提供的序列化器与数据
            库查询方法
            ListModelMixin





    【注意】：当你去写列表或者详情的时候可以从GenericAPIView继承
"""

from rest_framework.views import APIView
# 注意的是在这里引入的是Response 
from rest_framework.response import Response  

from .models import BookInfo,HeroInfo
from .serializers import BookInfoSerializer

class BookListView(APIView):
    
    def get(self,request):
        books = BookInfo.objects.all()
        serializer = BookInfoSerializer(books, many=True)
        return Response(serializer.data)

