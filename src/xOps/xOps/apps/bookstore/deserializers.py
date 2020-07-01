

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
                """图书数据序列化器"""
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
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20,validators=[about_django])
    bpub_date = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    image = serializers.ImageField(label='图片', required=False)







