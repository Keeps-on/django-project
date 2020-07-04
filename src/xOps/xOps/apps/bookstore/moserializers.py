
# 模型类序列化器ModelSerializer
"""
如果我们想要使用序列化器对应的是Django的模型类，DRF为我们提供了ModelSerializer模型类序列化器来帮助我们快速创建一个Serializer类。
ModelSerializer与常规的Serializer相同，但提供了:
    1. 自带create()/update()方法
        基于模型类自动生成一系列字段,包含默认的create()和update()的实现
    2. 指定字段
        fields
            __all__:表名包含所有字段,也可以写明具体哪些字段
            fields = ('id', 'btitle', 'bpub_date')
            exclude = ('image')
           

"""
from rest_framework import serializers
from bookstore.models import BookInfo, HeroInfo

class BookInfoSerializer(serializers.ModelSerializer):
    """
        图书数据序列化器
        model: 指明参照哪个模型类
        fields: 指明为模型的哪些字段生成
    """
    class Meta:
        model = BookInfo
        fields = '__all__'
        # fields = ('id', 'btitle', 'bpub_date')
        # exclude = ('image',)

class HeroInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroInfo
        fields = '__all__'
        depth = 1

"""
fields = '__all__'
HeroInfoSerializer():
    id = IntegerField(label='ID', read_only=True)
    hname = CharField(label='名称', max_length=20)
    hgender = ChoiceField(choices=((0, '男'), (1, '女')), label='性别', required=False, validators=[<django.core.validators.MinValueValidator object>, <django.core.validators.MaxValueValidator object>])
    hcomment = CharField(allow_null=True, label='备注信息', max_length=200, required=False)
    is_delete = BooleanField(label='删除标记', required=False)
    hbook = NestedSerializer(read_only=True):
        id = IntegerField(label='ID', read_only=True)
        btitle = CharField(label='标题', max_length=20)
        bpub_date = DateField(label='发布日期')
        bread = IntegerField(label='阅读量', max_value=2147483647, min_value=-2147483648, required=False)
        bcomment = IntegerField(label='评论量', max_value=2147483647, min_value=-2147483648, required=False)
        is_delete = BooleanField(label='删除标记', required=False)
        image = ImageField(allow_null=True, label='图片', max_length=100, required=False)

"""

class HeroInfoSerializer2(serializers.ModelSerializer):
    hbook = BookInfoSerializer()
    class Meta:
        model = HeroInfo
        fields = ('id', 'hname', 'hgender', 'hcomment', 'hbook')
"""

HeroInfoSerializer2():
    id = IntegerField(label='ID', read_only=True)
    hname = CharField(label='名称', max_length=20)
    hgender = ChoiceField(choices=((0, '男'), (1, '女')), label='性别', required=False, validators=[<django.core.validators.MinValueValidator object>, <django.core.validators.MaxValueValidator object>])
    hcomment = CharField(allow_null=True, label='备注信息', max_length=200, required=False)
    is_delete = BooleanField(label='删除标记', required=False)
    hbook = NestedSerializer(read_only=True):
        id = IntegerField(label='ID', read_only=True)
        btitle = CharField(label='标题', max_length=20)
        bpub_date = DateField(label='发布日期')
        bread = IntegerField(label='阅读量', max_value=2147483647, min_value=-2147483648, required=False)
        bcomment = IntegerField(label='评论量', max_value=2147483647, min_value=-2147483648, required=False)
        is_delete = BooleanField(label='删除标记', required=False)
        image = ImageField(allow_null=True, label='图片', max_length=100, required=False)

"""


class BookInfoSerializerRead(serializers.ModelSerializer):
    """图书数据序列化器"""
    class Meta:
        model = BookInfo
        fields = ('id', 'btitle', 'bpub_date', 'bread', 'bcomment')
        read_only_fields = ('id', 'bread', 'bcomment')

"""
可以通过read_only_fields指明只读字段，即仅用于序列化输出的字段
BookInfoSerializerRead():
    id = IntegerField(label='ID', read_only=True)
    btitle = CharField(label='标题', max_length=20)
    bpub_date = DateField(label='发布日期')
    bread = IntegerField(label='阅读量', read_only=True)
    bcomment = IntegerField(label='评论量', read_only=True)
【注意】
    看当前的只读字段分别为
        id 字段的主键值
        bread 阅读量
        bcommnet 评论量
    这些字段是只读的,就例如id字段是数据库的主键不需要,主动创建
"""

class BookInfoSerializerExtra(serializers.ModelSerializer):
    """图书数据序列化器"""
    class Meta:
        model = BookInfo
        fields = ('id', 'btitle', 'bpub_date', 'bread', 'bcomment')
        extra_kwargs = {
            'bread': {'min_value': 0, 'required': True},
            'bcomment': {'min_value': 0, 'required': True},
        }

"""
我们可以使用extra_kwargs参数为ModelSerializer添加或修改原有的选项参数

BookInfoSerializerExtra():
    id = IntegerField(label='ID', read_only=True)
    btitle = CharField(label='标题', max_length=20)
    bpub_date = DateField(label='发布日期')
    bread = IntegerField(label='阅读量', max_value=2147483647, min_value=0, required=True)
    bcomment = IntegerField(label='评论量', max_value=2147483647, min_value=0, required=True)
"""