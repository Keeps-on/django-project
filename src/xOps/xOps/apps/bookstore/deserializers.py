

"""
反序列化 
    数据 --> 校验 --> 模型类对象
    1. 验证 is_valid()
        true  --> 通过序列化对象validated_data -- 获取属性数据
        false --> 序列化对象.errors属性获取错误信息
        验证失败，可以通过序列化器对象的errors属性获取错误信息，
        返回字典，包含了字段和字段的错误。如果是非字段错误，可以通过修改
        REST framework配置中的NON_FIELD_ERRORS_KEY来控制错误字典中的键名。
    2. 构造序列化器的对象,并将反序列化的数据传递给data构造参数
        | 校验 is_valid()
        2.1 自定义方法校验
            def fn(value):=>value表示字段值
                raise serializers.ValidationError('验证信息')
            btitle = serializers.CharField(label='名称', max_length=20,validators=[about_django])
        2.2 指定字段校验validate_<field_name>
            # 实例方法验证title字段
            def validate_btitle(self, value):
                if 'django' not in value.lower():
                    raise serializers.ValidationError("图书不是关于Django的")
                return value

        2.3 同时对于多个字段进行比较校验定义validate方法校验
            
            class BookInfoSerializer(serializers.Serializer):
                # 图书数据序列化器
                ...

                def validate(self, attrs):
                    bread = attrs['bread']
                    bcomment = attrs['bcomment']
                    if bread < bcomment:
                        raise serializers.ValidationError('阅读量小于评论量')
                    return attrs

"""
from rest_framework import serializers
from bookstore.models import BookInfo, HeroInfo

def about_django(value):
    if 'django' not in value.lower():
        raise serializers.ValidationError("图书不是关于Django的")



class BookInfoSerializer(serializers.Serializer):
    """
    图书数据序列化器
    {
        "id": null, // read_only=True
        "btitle": "Django-REST-Frame",
        "bpub_date": "2018-01-19",
        "bread": 3,
        "bcomment": 2,
        "image": null
    }
    """
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20,validators=[about_django])
    bpub_date = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    image = serializers.ImageField(label='图片', required=False)

    def create(self, validated_data):
        """新建"""
        print('--------------start-------------------')
        print(validated_data) # {'btitle': 'Django-REST-Frame', 'bpub_date': datetime.date(2018, 1, 19), 'bread': 3, 'bcomment': 2}
        print(type(validated_data)) # <class 'dict'>
        print('---------------end--------------------')
        return BookInfo(**validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        print('------------------------------')
        print(instance) # __str__ 大话设计模式
        print(type(instance)) # <class 'bookstore.models.BookInfo'>
        print('------------------------------')
        instance.btitle = validated_data.get('btitle', instance.btitle)
        instance.bpub_date = validated_data.get('bpub_date', instance.bpub_date)
        instance.bread = validated_data.get('bread', instance.bread)
        instance.bcomment = validated_data.get('bcomment', instance.bcomment)
        return instance
    

"""
保存对象
    1 案例演示 - is_valid
    1.1 错误演示
        data = {'bpub_date': 123}
        serializer.is_valid()  # 返回False
        serializer.errors                                                                                                                                             
        {
            'btitle': [ErrorDetail(string='该字段是必填项。', code='required')], 
            'bpub_date': [ErrorDetail(string='日期格式错误。请从这些格式中选择：YYYY-MM-DD。', code='invalid')]
        }
    1.2 正确校验
        data = {'btitle': 'python'}
        serializer = BookInfoSerializer(data=data)
        serializer.is_valid()  # True
        serializer.errors  # {}
        serializer.validated_data  #  OrderedDict([('btitle', 'python')])
    1.3 serializer.is_valid(raise_exception=True)
        erializers.ValidationError
        传递参数:raise_exception=True
        REST framework接收到此异常，会向前端返回HTTP 400 Bad Request响应。
        # Return a 400 response if the data was invalid.
        serializer.is_valid(raise_exception=True)
    2. 定义验证行为
    2.1 validators
        data = {'btitle': 'python'}
        serializer = BookInfoSerializer(data=data)
        serializer.is_valid()  # False   
        serializer.errors
        # {'btitle': [ErrorDetail(string='图书不是关于Django的', code='invalid')]}
    2.2 validate_<field_name>
        data = {'btitle': 'python'}
        serializer = BookInfoSerializer(data=data)
        serializer.is_valid()  # False   
        serializer.errors
        # {'btitle': [ErrorDetail(string='图书不是关于Django的', code='invalid')]}
    2.3 validate
        data = {'btitle': 'about django', 'bread': 10, 'bcomment': 20}
        s = BookInfoSerializer(data=data)
        s.is_valid()  # False
        s.errors
        # {'non_field_errors': [ErrorDetail(string='阅读量小于评论量', code='invalid')]}
    3. 保存
        基于validated_data ==> create()/update()




"""






