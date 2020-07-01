from rest_framework import serializers
from bookstore.models import BookInfo, HeroInfo


class BookInfoSerializer(serializers.ModelSerializer):
    """图书数据序列化器"""
    class Meta:
        model = BookInfo
        fields = '__all__'


class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(
        choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(
        label='描述信息', max_length=200, required=False, allow_null=True)
    # hbook = serializers.PrimaryKeyRelatedField(label='图书', read_only=True)
    # 返回的是整个对象
    # hbook = BookInfoSerializer()
    # 此字段将被序列化为关联对象的字符串表示方式（即__str__方法的返回值）
    hbook = serializers.StringRelatedField(label='图书')
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return HeroInfo.objects.create(**validated_data)


class BookInfoSerializerBySelf(serializers.Serializer):
    """
    图书数据序列化器
    注意：
        serializer不是只能为数据库模型类定义，
        也可以为非数据库模型类的数据定义。
        serializer是独立于数据库之外的存在。
    """
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)  # 字符串
    bpub_date = serializers.DateField(label='发布日期', required=False)  # 时间日期
    bread = serializers.IntegerField(label='阅读量', required=False)  # 整数类型
    bcomment = serializers.IntegerField(label='评论量', required=False)  # 整数类型
    image = serializers.ImageField(label='图片', required=False)  # 图片类型
    heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)  # 新增



"""
创建Serializer对象
    Serializer(instance=None, data=empty, **kwarg)
    参数说明:
        1. 用于序列化时,将模型类对象传入instance
        2. 用于反序列化,将要被反序列化的数据传入data
        3. 除了instance和data参数外，在构造Serializer对象时，还可通过context参数额外添加数据，如
        serializer = AccountSerializer(account, context={'request': request})
        【注意】: 通过context参数附加的数据，可以通过Serializer对象的context属性获取。
Serializer的基本使用
    1. 获取models对象 
        book = BookInfo.objects.get(id=1)
    2. 构造序列化对象
        ser
    3. 获取序列化数据
        序列化对象(单个对象)
            serializer = BookInfoSerializer(book)
        常用的属性
            data: 获取序列化数据
                serializer.data ==> 单个数据
                type(serializer.data)                                                                                                 
                rest_framework.utils.serializer_helpers.ReturnDict
            context
                serializer = BookInfoSerializer(book,context={'name': 'kevin'})                                                                                              
                serializer.context == > {'name': 'kevin'}                                                                                                                                   {'name': 'kevin'}
        序列化对象(多个对象)
            book_queryset = BookInfo.objects.all()
            serializer = BookInfoSerializer(book_queryset, many=True)
            serializer.data == > [OrderedDict([('id', 1), ('btitle', '大话设计模式'),
        序列化对象(嵌套序列) 
            表关联关系 HeroInfo 当前英雄在哪本书中 图书表BookInfo
            如果需要序列化的数据中包含有其他关联对象，则对关联对象数据的序列化需要指明。
            在定义英雄数据的序列化器时，外键hbook(即所属的图书)
            1. 第一步定义HeroInfoSerialzier的字段除外键字段的其他部分
            2. 但是对于关联字段
                2.1 PrimaryKeyRelatedField:此字段将被序列化为关联对象的主键
                    hbook = serializers.PrimaryKeyRelatedField(label='图书', read_only=True)
                    hbook = serializers.PrimaryKeyRelatedField(label='图书', queryset=BookInfo.objects.all())
                【注意】: read_only=True 或者 queryset 参数:
                    read_only=True参数时,该字段将不能用作反序列化使用
                    包含queryset参数时，将被用作反序列化时参数校验使用

                2.2 关联对象 hbook = BookInfoSerializer()
                hero = HeroInfo.objects.get(id=1) == > 单条数据
                serializer = HeroInfoSerializer(hero) ==> 创建序列化器
                serializer.data ==> 获取序列化的数据
                {'id': 1, 'hname': '小龙女', 'hgender': 1, 'hcomment': '小龙女帅气', 'hbook': 4}
                【注意】: 此时拿到的是hbook的普通字段
                hbook = serializers.PrimaryKeyRelatedField(label='图书', read_only=True)
                替换
                hbook = BookInfoSerializer()
                    serializer.data ==> 获取序列化的数据 此时返回的数据为OrderedDict
                    {   
                        'id': 1, 'hname': '小龙女', 'hgender': 1, ... 
                        'hbook': OrderedDict([
                            ('id', 4), ('btitle', '射雕英雄传'), 
                            ('bpub_date', '2013-05-29'), ('bread', 56), 
                            ('bcomment', 78), ('is_delete', False), 
                            ('image', None)
                            ])
                    }
                2.3 StringRelatedField : 此字段将被序列化为关联对象的字符串表示方式(即__str__方法的返回值)
                class HeroInfo(models.Model):
                    # ...

                    def __str__(self):
                        return self.hname
                hbook = serializers.StringRelatedField(label='图书')
                serializer.data == >
                {
                    'id': 1, 
                    'hname': '小龙女', 
                    'hgender': 1, 
                    'hcomment': '小龙女帅气', 
                    'hbook': '射雕英雄传'
                }
                2.4 many参数
                如果关联的对象数据不是只有一个,而是包含多个数据,如想序列化图书BookInfo数据,
                每个BookInfo对象关联的英雄HeroInfo对象可能有多个,此时关联字段类型的指明仍可使用上述几种方式,
                只是在声明关联字段时，多补充一个many=True参数即可。
                此处仅拿PrimaryKeyRelatedField类型来举例，其他相同。
                在BookInfoSerializer中添加关联字段:
                # 此处更新字段
                heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)  # 新增
                book = BookInfo.objects.get(id=4)
                serializer = BookInfoSerializerBySelf(book)
                serializer.data
                {
                    'id': 4, 'btitle': '射雕英雄传', 'bpub_date': '2013-05-29', 
                    'bread': 56, 'bcomment': 78, 'image': None, 
                    'heroinfo_set': [1, 2]
                }

"""
