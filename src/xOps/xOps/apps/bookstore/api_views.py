


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

