from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage

from django.template import Context,loader
# from settings import dev
# https://www.cnblogs.com/chenjianhong/p/4144304.html
# https://blog.csdn.net/yima1006/article/details/8991145
# https://zhuanlan.zhihu.com/p/575356694
# https://blog.csdn.net/qq_38542085/article/details/90913404
# https://www.cnblogs.com/polly-ling/p/9950792.html
# https://blog.csdn.net/CurtainOfNight/article/details/104053669 带有一部分源码

# https://www.cnblogs.com/haoshine/p/5944392.html

# file_path = '/data/django-project/src/xOps/xOps/apps/mail/1.jpg'
# def add_img(file_path):
#     file = open(file_path,'rb')
#     img_data = file.read()
#     file.close()
#     return img_data


def send_html_mail(subject, html_content, recipient_list):
    msg = EmailMessage(subject, html_content, EMAIL_HOST_USER, recipient_list)
    msg.content_subtype = "html" # Main content is now text/html
    msg.send()


def index(request):
    context = {
        'nickname':'Test',
        'verify_url':'http://www.baidu.com',
        # 'img':add_img(file_path)
    }
    # email_template_name = '/data/django-project/src/xOps/templates/mail/main.html'
    t = loader.get_template('mail/main.html').render(Context(context))
    main_list = ['564060577@qq.com',]
    send_html_mail()
    print('test')
    return HttpResponse('OK')

# def check_mail(reuqest):

#     context = {
#         'nickname':'Test',
#         'verify_url':'http://www.baidu.com',
#         'img':add_img(file_path)
#     }
#     email_template_name = 'mail.html'
#     t = loader.get_template(email_template_name).render(Context(context))
#     main_list = ['564060577@qq.com',]
#     send_mail(
#         subject='测试邮件',
#         message = t,
#         from_email = dev.EMAIL_HOST_USER,
#         recipient_list=mail_list,
#         fail_silently=False,
#         auth_user=dev.EMAIL_HOST_USER,          # SMTP服务器的认证用户名
#         auth_password=EMAIL_HOST_PASSWORD,  # SMTP服务器的认证用户密码
#     )
#     HttpResponse('发送成功')

    
