from django.shortcuts import render

# Create your views here.


from rest_framework.viewsets import ModelViewSet
from .serializers import BookInfoSerializer,HeroInfoSerializer
from .models import BookInfo,HeroInfo

class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer


class HeroInfoViewSet(ModelViewSet):
    queryset = HeroInfo.objects.all()
    serializer_class = HeroInfoSerializer

"""
queryset 指明该视图集在查询数据时使用的查询集
serializer_class 指明该视图在进行序列化或反序列化时使用的序列化器
"""