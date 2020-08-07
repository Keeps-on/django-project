from django.shortcuts import render

# Create your views here.


from rest_framework.viewsets import ModelViewSet
# 普通的序列化器
from .serializers import BookInfoSerializer,HeroInfoSerializer
# 带有保存和更新的序列化器
from .deserializers import BookInfoSerializer
from .models import BookInfo,HeroInfo
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    # authentication_classes = (SessionAuthentication,BasicAuthentication)
    # permission_classes = (IsAuthenticated,)


class HeroInfoViewSet(ModelViewSet):
    queryset = HeroInfo.objects.all()
    serializer_class = HeroInfoSerializer

"""
queryset 指明该视图集在查询数据时使用的查询集
serializer_class 指明该视图在进行序列化或反序列化时使用的序列化器
"""