from django.http import HttpResponse
from django.shortcuts import render
from Models import models

# 每个响应对应一个函数，函数必须返回一个响应
# 函数必须存在一个参数，一般约定为request
# 每个响应函数对应一个url


###ajax提交页面不刷新
# 在用对话框的时候一般用ajax,对话框一般在少量输入的时候使用
#用表单提交,url跳转方式  用于对大量的数据以及操作，比如博客这种

def login(request):
    '''
    处理用户请求，并返回内容
    :param request: 用户请求相关的所有信息（对象）
    :return:
    '''
    # return HttpResponse('hello world')
    #用判断请求方式来执行不同的命令
    if request.method=='GET':
        return render(request, 'login/login.html')#自动找到模板路径下的login.html文件，读取内容并返回给用户
    else:
        user_name = request.POST.get('Account')
        user_pwd = request.POST.get('Pwd')

        user = models.User.objects.filter(name=user_name)  #根据用户名查找数据库是否存在
        if user.exists():
            pwd = user[0].pwd
            id = user[0].user_id

        else:
            Msg='4'  #账号或密码不存在

        if (user_pwd == pwd):
            # print('提交')   这种会在下面的运行里进行打印，平时测试方便
            request.session["Login_UserId"] = id
            user_id=request.session.get("Login_UserId")
            print(request.session.exists("session_key"))
            print(request.session.exists("Login_UserId"))
            Msg='3'
            # 表单形式提交才可以用重定向这种方式直接跳转url
            # ajax用redirect是没有用的，只能返回字符串，所以需要在html中用location.href的方式写跳转
        else:
            Msg='4'
        return HttpResponse(Msg)


def demo(request):

    return render(request,'login/demo.html')

def index(request):
    # models.User.objects.create(name='管理员',pwd=123)
    # models.Menu.objects.create(menu_name='系统配置',menu_img='accodin_system.png',menu_show=1,menu_node='1000')
    # models.Menu.objects.create(menu_name='商品信息配置',menu_url='/goods/',menu_img='emotion_happy.png',menu_show=1,menu_node='10001002')
    # models.Menu.objects.create(menu_name='商品类型配置', menu_url='/goodsCat/',menu_img='emotion_happy.png',menu_show=1,menu_node='10001003')
    # models.Role.objects.create(name='处长', node='1001')
    # models.Role.objects.create(name='副处长', node='10011000')
    # models.Role.objects.create(name='党支书', node='100110001000')
    # models.Role.objects.create(name='科长', node='10011001')
    # models.Role.objects.create(name='副科长', node='100110011000')
    # models.Role.objects.create(name='仓库管理员', node='1001100110001000')
    # models.Role.objects.create(name='后勤', node='100110011001')
    # models.User_Role.objects.create(user_id=2,role_id=1)
    # models.User_Role.objects.create(user_id=2, role_id=2)
    """  测试当一个用户有多种角色，将其所有角色的菜单权限合并 """
    # models.Role_Menu.objects.create(role_id=1,menu_id=1)
    # models.Role_Menu.objects.create(role_id=1, menu_id=2)
    # models.Role_Menu.objects.create(role_id=1, menu_id=3)
    # models.Role_Menu.objects.create(role_id=2,menu_id=1)
    # models.Role_Menu.objects.create(role_id=2, menu_id=2)
    # models.Role_Menu.objects.create(role_id=2, menu_id=3)
    """测试用户不仅拥有其角色的菜单权限，该用户还有自己的菜单权限， 将用户权限和角色权限合并"""
    #models.User_Menu.objects.create(user_id=2, menu_id=2)
    # models.Menu.objects.create(menu_name='安全管理', menu_img='accodin_system.png', menu_show=1, menu_node='1005')
    # models.Menu.objects.create(menu_name='用户管理',menu_url='',menu_img='emotion_happy.png',menu_show=1,menu_node='10051000')
   # models.Menu.objects.create(menu_name='角色管理', menu_url='', menu_img='emotion_happy.png', menu_show=1, menu_node='10051001')
   #  models.Menu.objects.create(menu_name='菜单管理', menu_url='', menu_img='emotion_happy.png', menu_show=1, menu_node='10051002')
   #  models.Menu.objects.create(menu_name='模块管理', menu_url='', menu_img='emotion_happy.png', menu_show=1, menu_node='10051003')
   #  models.Role_Menu.objects.create(role_id=1, menu_id=4)
   #  models.Role_Menu.objects.create(role_id=1, menu_id=5)
   #  models.Role_Menu.objects.create(role_id=1, menu_id=6)
   #  models.Role_Menu.objects.create(role_id=1, menu_id=7)
   #  models.Role_Menu.objects.create(role_id=1, menu_id=8)
    ''' 测试部门角色用户  '''
    # models.Department.objects.create(name='业务部,node='1000')
    # models.Department.objects.create(name='业务部下的销售部',node='10001000')
    # models.Department.objects.create(name='业务部下的市场开发部',node='10001001')
    # models.Department.objects.create(name='工程部',node='1001')
    # models.Department.objects.create(name='工程部下的开发组', node='10011000')
    # models.Department.objects.create(name='工程部下的设计组', node='10011001')
    # models.Depart_Role.objects.create(depart_id=1,role_id=1)
    # models.Depart_Role.objects.create(depart_id=1, role_id=2)
    # models.Depart_Role.objects.create(depart_id=2, role_id=3)
    # models.Depart_Role.objects.create(depart_id=2, role_id=7)
    # models.Depart_User.objects.create(depart_id=1,user_id=2)
    # models.User.objects.create(name='小红销售', pwd=123)
    # models.Depart_User.objects.create(depart_id=2, user_id=3)
    # models.User_Role.objects.create(user_id=3,role_id=3)
    # models.User_Role.objects.create(user_id=3, role_id=7)
    # models.User.objects.create(name='工程师1', pwd=123)
    # models.Depart_User.objects.create(depart_id=3, user_id=4)
    # models.User_Role.objects.create(user_id=4,role_id=1)
    # models.User_Role.objects.create(user_id=4, role_id=2)
    # models.Depart_Role.objects.create(depart_id=3,role_id=1)
    # models.Depart_Role.objects.create(depart_id=3, role_id=2)
    '''用户管理下的权限管理'''
    # models.Access.objects.create(access_name='浏览')
    # models.Access.objects.create(access_name='添加')
    # models.Access.objects.create(access_name='编辑')
    # models.Access.objects.create(access_name='删除')
    # models.Access.objects.create(access_name='查询')
    # models.Access.objects.create(access_name='打印')
    # models.Access.objects.create(access_name='预览')
    # models.Access.objects.create(access_name='导出')
    print(request.session.exists("session_key"))
    s = models.Goods.objects.all()
    querys = models.Goods.objects.all().extra({'id': 'id','name':'goodsname'}).values('id','name')  #给字段起别名，必须写上values，不然并没有成功
    for row in querys:
        print(row['id'])
        print(row['name'])
    return HttpResponse(3)