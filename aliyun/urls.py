"""aliyun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

'''
web框架本质
    浏览器（socket客户端）
     2、发送IP和端口  http://www.baidu.com:80/index/
     GET:
        请求头
            http1.1 /index?p=123
            ...
        请求体（无内容）
    POST:
        请求头
            http1.1 /index?p=123
            ...
        请求体
            ...
    4、接收响应
        普通响应：页面直接显示
        重定向响应：再发起一次http请求
        
    
    服务器（socket服务端）
    1、启动并监听ip和端口，等待用户连接
    3、接收请求进行处理，并返回
        普通返回：
            响应头：
            ...
            响应体：
            <html></html>
        重定向返回：
            响应头：
                LOCATION:'http://www.baidu.com'
'''


'''
DjangoWeb框架
    1、创建Project
    2、配置
        a、模板    # 'DIRS': [os.path.join(BASE_DIR, 'templates')],
                # 'APP_DIRS': True,
                'APP_DIRS': False,
                'OPTIONS': {
                'loaders': [
                 'django.template.loaders.app_directories.Loader',
                ]
                },
        b、静态文件   STATICFILES_DIRS = (
                        os.path.join(BASE_DIR, "commonstatic/"),#一定要加  逗号！
                  ） 
        #为了在每个APP下写自己的html文件
        #防止不同的app下用相同名字的html，在templates下再建个相同app名的文件夹放html
        c、在MIDDLEWARE中 将csrf注释掉  #'django.middleware.csrf.CsrfViewMiddleware',
            ajax时需要
        d、DATABASES = {
            'default': {
                'ENGINE':'django.db.backends.mysql',#'sql_server.pyodbc',django_pyodbc',
                'NAME':'student',
                'HOST':'39.108.107.126',
                'PORT':'3306',
                'USER':'user',
                'PASSWORD':'user',
                    }
            }
        }
        在__init__.py中添加   import pymysql
                             pymysql.install_as_MySQLdb()
        e、注册app
        f、创建数据表  执行如下命令
        python manage.py makemigrations
        python manage.py migrate
    3、路由关系
        url -> 函数   
    4、视图函数
        def index(request):
            request.method
            request.GET
            request.POST
            
            return HttpResponse('字符串')
            return redirect('URL')
            return render(request,'模板路径',{})
                1、获取模板+数据，渲染
                2、HttpResponse(...)返回给用户
    5、模板渲染
    显示值的方式
    {{k1}}
    {{k2.id}}
    
    {% for i in result %}
        {{i}}
    {% endfor %}
    
    {% if i>2 %}
    {% endif %}
'''



from django.contrib import admin
from django.urls import path
from login import views as lv
from MainIndex import views as mv
from SystemSettings import views as sv
from security import views as sec_v
from WorkOrder import views as work
from Commodity import views as com_v
from customermanager import views as cv
from Base import views as base
from Chart import views as chart
from video import views as video
from SensorData import views as sensor

urlpatterns = [
    #path('admin/', admin.site.urls),
        # 主框架
    path('login/',lv.login),
    path('mainIndex/', mv.frame),
    path('home/',mv.home),

    #单页面的基础框架
    path('single/',base.Sample_Singe),
    path('div/',base.Sample_Div),
    path('muti/',base.Muti_Table),

        #安全管理
    path('user/', sec_v.userControl),
    path('role/', sec_v.roleControl),
    path('menu/', sec_v.menuControl),

        #商品管理方面的系统配置
    path('goods/',sv.goods),
    path('goodsCat/',sv.goodsCat),
    path('manufactor/',sv.manufactor),
    path('supplier/', sv.supplier),
    path('site/',sv.site_set),

#wangyu add 2019/1/21 begin
    path('Seller/', sv.Seller_Trans),
    path('SellerPro/', sv.SellerProp_Trans),
#wangyu add 2019/1/21 end

        # 工单管理
    path('editWork/', work.edit),
    path('approveWork/', work.approve),

    #商品管理 出入库
    path('stockIn/', com_v.stockIn),
    path('stockOut/', com_v.stockOut),
    path('commodity/', com_v.load_commodity),
    #客户管理
    path('customermanager/', cv.customermanager),

    # 图表
    path('line_or_bar/',chart.show_line_or_bar),
    path('pie/',chart.show_pie),

    # 传感器

#视频用
    path('index/', lv.index),
    path('demo/', lv.demo),
    path('videoview/', video.view),
    path('videoplay/', video.videoplay),
    path('videoSettings/', video.videosettings),

#传感器数据
    path('sensor/', sensor.historydata),

]
