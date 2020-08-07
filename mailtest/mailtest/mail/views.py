from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse

# Create your views here.

# https://www.programcreek.com/python/index/1015/django.template.loader
# https://www.cnblogs.com/zhangxinqi/p/9113859.html
# https://www.cnblogs.com/hainan-zhang/p/6647980.html
# https://www.programcreek.com/python/index/1015/django.template.loader
# https://www.cnblogs.com/haoshine/p/5944392.html render_to_string
# https://www.pythonheidong.com/blog/article/156588/ 路径解决方案

# def index(request):
#     template=loader.get_template('index.html')
#     context={'city': '北京'}
#     # 2.渲染模板
#     return HttpResponse(template.render(context))

# from django.shortcuts import render
 
# def index(request):
#     context={'city': '北京'}
#     return render(request,'index.html',context)


# 发送带有图片的html内容的邮件

# 包含带有处理图片的方式
# https://blog.csdn.net/qq_35867759/article/details/85613505

import os 
from email.mime.image import MIMEImage
from django.core import mail

def add_img(src,img_id):
	with open(src,'rb') as f:
		msg_image = MIMEImage(f.read())
		msg_image.add_header('Content-ID', img_id)
	return msg_image



def send_util(subject, from_email, to,  cc=None, html=None):
 
    if isinstance(to, tuple):
        to = list(to)
    if not isinstance(to, list):
        to = [to]
    if cc:
        if isinstance(cc, tuple):
            cc = list(cc)
        if not isinstance(cc, list):
            cc = [cc]
    else:
        cc = []
 
    msg = mail.EmailMessage(subject,from_email,to,html,cc=cc)
    if html:
        msg.content_subtype = 'html'
        msg.encoding = 'utf-8'
        image = add_img('/tmp/tup.png','test_cid')
        msg.attach(image)
    try:
        msg.send()
    except Exception as e:
        print('send_mail exec error'+str(e))
    return True




# from django.conf import settings


# from django.core.mail import send_mail  
# # send_mail的参数分别是  邮件标题，邮件内容，发件箱(settings.py中设置过的那个)，收件箱列表(可以发送给多个人),失败静默(若发送失败，报错提示我们)


from django.shortcuts import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.template import loader
from django.core.mail import EmailMessage
from email.mime.image import MIMEImage

def add_img(src, img_id):
    # with open(os.path.join(os.path.dirname(__file__), src), 'rb') as f:
    with open(src, 'rb') as f:
        msg_image = MIMEImage(f.read())
    msg_image.add_header('Content-ID', img_id)
    return msg_image



def index(request):
    subject = '请注意这是Django邮件测试'
    # msg = '服务器运行良好'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["564060577@qq.com"]
    html_content = loader.render_to_string('mail.html', 
    	{
			'name': 'kevin'
		})
    print(html_content)
    msg = EmailMessage(subject, html_content, from_email, recipient_list)
    msg.content_subtype = 'html'
    msg.encoding = 'utf-8'
    image = add_img('templates/test.jpg','test_cid')
    msg.attach(image)
    msg.send()
    # send_mail(
    #     subject='请注意这是Django邮件测试',
    #     message=html_content,
    #     from_email=settings.EMAIL_HOST_USER, 
    #     recipient_list=["564060577@qq.com"] # 这里注意替换成自己的目的邮箱，不然就发到我的邮箱来了：）
    # )
    return HttpResponse('测试邮件已发出请注意查收')


"""
关于Python发送邮件的整理
链接内中实现了发送的方法
https://blog.csdn.net/qq_35867759/article/details/85613505 
jie
https://www.cnblogs.com/zhangxinqi/p/9113859.html

"""




