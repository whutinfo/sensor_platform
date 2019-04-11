from django.shortcuts import render
from django.http import HttpResponse
from Models import models
import json


def frame(request):# request  接收的请求
    # return HttpResponse('hello world')  #返回字符串
    action = request.POST.get('action')

    if request.method == 'GET':
        return render(request, 'MainIndex/main.html')  ##用render，从第二个参数中找
    else:
        if action=='Loadsy':
            return HttpResponse('/home/')
        elif action=='LoadFirstMenuByPermis':
            #user_id=request.session.get("Login_UserId")
            # request.session[‘Login_UserId’]=id
            user_id=request.session.get("Login_UserId")    #注意小括号！！

            # 1、根据role_id得到角色权限菜单权限列表
            # obj= models.User.objects.filter(user_id=user_id).first()
            # roles=obj.roles.all()
            # for role in roles:
            #     role_id=role.role_id
            roles_id=models.User.objects.filter(user_id=user_id).values('user_role__role__role_id')# 一个字典  #根据user_id 获取role_id
            user_role_menu_get=[]
            for role_id in roles_id:
                roles=models.Role.objects.get(role_id=role_id['user_role__role__role_id']) #根据id只会有一条数据
                #if roles.count():
                menus=roles.permissions.filter(menu_show=1)
                for menu in menus:
                    user_role_menu_get.append(menu.menu_id)#将菜单名添加进列表
            # 2、根据user_id，查出其所有用户权限所拥有的菜单列表
            users = models.User.objects.filter(user_id=user_id)
            if users.count() != 0:
                menus = users.first().menus.filter(menu_show=1)
                for menu in menus:
                    user_role_menu_get.append(menu.menu_id)
            user_role_menu = list(set(user_role_menu_get))  # 去重
            user_role_menu.sort(key=user_role_menu_get.index)  # 按原来排序，此时将user对应的所有的role的角色权限菜单已全部以列表形式获取
            menu_dict = {'menu_id': '', 'menu_name': '', 'menu_describe': '', 'menu_url': '', 'menu_img': '',
                    'menu_show': '', 'menu_open': '', 'menu_node': '', }  # 用字典和列表拼接很方便形成Json格式
            menu=[]
            for menu_id in user_role_menu:
                menu_qs=models.Menu.objects.filter(menu_id=menu_id)
                for row in menu_qs:
                    menu_dict['menu_id'] = row.menu_id
                    menu_dict['menu_name'] = row.menu_name
                    menu_dict['menu_describe'] = row.menu_describe
                    menu_dict['menu_url'] = row.menu_url
                    menu_dict['menu_img'] = row.menu_img
                    menu_dict['menu_show'] = row.menu_show
                    menu_dict['menu_open'] = row.menu_open
                    menu_dict['menu_node'] = row.menu_node
                    menu.append(menu_dict.copy())# 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
            #     # 用.copy()就不会跟着改变
            menu.sort(key=lambda x: x['menu_node']) #lambda是一个匿名函数，是固定写法，不要写成别的单词；
            # x表示列表中的一个元素，在这里，表示一个字典，x只是临时起的一个名字，你可以使用任意的名字；
            # x['node']表示字典里的node键，所以这句命令的意思就是按照列表中node键排序
            request.session["AllMenuInfoByUserId"] = menu
            menuJSON = json.dumps(menu)  # 将列表转字符串传给前端
            return HttpResponse(menuJSON)
        elif action=='LoadSecondMenu':
            ParentNode = request.POST.get('ParentNode')  #前端foreach每一次获得的一个顶级节点，是字符串
            wholemenus = request.session.get('AllMenuInfoByUserId') #[{}]
            getsecondmenu = GetSecondMenu(ParentNode,wholemenus)
            secondmenu=json.dumps(getsecondmenu)
            return HttpResponse(secondmenu)
        elif action=='JudgeOverTime':
            isovertime = 0
            if (request.session.get("Login_UserId") == None):
                isovertime = 1
        return HttpResponse(isovertime)


#根据给的父节点在整个菜单结点中找到下级子结点
def GetSecondMenu(parentNode,wholeMenues):
    menujson=[]
    for menu in wholeMenues:
        #menu  {'menu_id': 3, 'menu_name': '商品类型配置', 'menu_describe': None, 'menu_url': '/goodsCat/', 'menu_img': 'emotion_happy.png', 'menu_show': 1, 'menu_open': None, 'menu_node': '10001003'}
        if len(menu['menu_node']) == len(parentNode)+4 and parentNode == menu['menu_node'][0:len(parentNode)]:
            menujson.append(menu)
#[{'menu_id': 2, 'menu_name': '商品信息配置', 'menu_describe': None, 'menu_url': '/goods/', 'menu_img': 'emotion_happy.png', 'menu_show': 1, 'menu_open': None, 'menu_node': '10001002'},
# {'menu_id': 3, 'menu_name': '商品类型配置', 'menu_describe': None, 'menu_url': '/goodsCat/', 'menu_img': 'emotion_happy.png', 'menu_show': 1, 'menu_open': None, 'menu_node': '10001003'}]
    return menujson



def home(request):
    action = request.POST.get('action')

    if request.method == 'GET':
        return render(request, 'MainIndex/home.html') ##用render，从第二个参数中找
    else:
        model_name = models.Device_Site
        if action == 'LoadMapData':
            site_id = request.POST.get('site_id') #  site_id为0时是加载地图后并没有点击任何地图菜单结点
            if site_id == '0':
                querys = model_name.objects.all()  # 获取需要的字段名的数据
            else:
                querys = model_name.objects.filter(pk = site_id)  # 获取需要的字段名的数据
            value_dict = {'value0': '', 'value1': '', 'value2': '', 'value3': '', 'value4': '', 'value5': ''}  # 有几个需要的列就有多少value 包括Id
            value_list = []
            for row in querys:
                value_dict['value0'] = row.id
                value_dict['value1'] = row.name
                value_dict['value2'] = row.longitude
                value_dict['value3'] = row.latitude
                value_dict['value4'] = row.map_label
                value_dict['value5'] = row.parent_id
                value_list.append(value_dict.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                # 用.copy()就不会跟着改变
                value_dict.clear()  # 防止出错时保存了上一次的值而导致看不出问题在哪

            return HttpResponse(json.dumps(value_list))  # 将列表拼字典仿Json格式转字符串传给前端 [{},{},{}]

        elif action == 'LoadTree':
            menus = models.Site_Tree.objects.all().order_by('node')
            index = {'index': 1}
            tree = [{'id': 0, 'trueid': 0, 'nature_id': 0, 'text': '监测站点', 'own_deviceid': 0, 'own_devicename': '',
                     'own_nodeid': 0, 'own_nodename': '', 'state': 'closed',
                     'children': ''}]  # 索引标题
            value_list = []
            value_dict = {}
            for row in menus:
                # 1、获取所有顶级节点
                if (len(row.node) == 4):
                    value_dict['id'] = index['index']
                    value_dict['trueid'] = row.id  # 真实id
                    value_dict['nature_id'] = 1  # 用来划分是索引节点，0是索引节点，1是所有节点，2是设备
                    value_dict['text'] = row.name
                    # value_dict['own_deviceid'] = 0
                    # value_dict['own_devicename'] = ''
                    value_dict['own_nodeid'] = 0  # 它所属的节点  向上找的！
                    value_dict['own_nodename'] = ''
                    value_dict['state'] = 'closed'

                    # 在所有顶级节点中找到其下所有的子节点（包括设备）

                    # select * from Department_Table where node like '%1000'用模糊查询
                    ztrees = models.Site_Tree.objects.filter(node__startswith=row.node)
                    children2 = GetSubDevice(row.id, row.name, index)  # 先获取其下所有设备
                    children1 = GetSubTree(row, ztrees, index)  # 再获取子节点

                    index['index'] += 1
                    if children1 != [] and children2 != []:  # 将其下设备和子节点都加载

                        value_dict['children'] = children2 + children1

                    elif children1 != []:
                        # 否则获取子节点
                        value_dict['children'] = children1

                    elif children2 != []:
                        # 否则获取设备
                        value_dict['children'] = children2

                    value_list.append(value_dict.copy())
                    value_dict.clear()  # 防止上次保存的结果干扰下一次的值，比如下一次没有这个键值，而上一次却有，就会保存上一次

            tree[0]['children'] = value_list
            return HttpResponse(json.dumps(tree))



def GetSubDevice(node_id, node_name, index):
    """
    根据node_id 节点id 在Video表中找到他拥有的所有设备
    :param node_id: 需要获取设备的节点
    :param node_name: 节点名称
    :param index: 自增的索引，是树的所有节点的唯一id
    :return:
    """

    videos = models.Device_Site.objects.filter(parent_id=node_id)
    values = {}
    value = []

    for row in videos:
        index['index'] += 1
        values['id'] = index['index']
        values['trueid'] = row.id  # 真实 Id
        values['nature_id'] = 2  # 用来划分是索引节点，0是索引节点，1是所有节点，2是设备
        values['text'] = row.name
        # values['own_deviceid'] = row.id
        # values['own_devicename'] = row.name
        values['own_nodeid'] = node_id
        values['own_nodename'] = node_name

        value.append(values.copy())
        values.clear()  # 防止上次保存的结果干扰下一次的值，比如下一次没有这个键值，而上一次却有，就会保存上一次
    return value


"""
获取部门子节点，即下一级部门
depart是department对象，ztrees是qs，所有子节点包括父节点自己
"""
def GetSubTree(video_menu, ztrees, index):
    """
    在当前顶级节点中找到下面所有子节点
    :param video_menu: 长度为4 的顶级节点
    :param ztrees: 顶级节点的所有子节点包括自己
    :param index: 索引
    :return:
    """
    values = {}
    value = []

    for sub in ztrees:

        # 节点长度+4的即为子节点
        if len(video_menu.node)+4 == len(sub.node):
            index['index'] += 1
            values['id'] = index['index']
            values['trueid'] = sub.id
            values['nature_id'] = 1
            values['text'] = sub.name
            values['own_nodeid'] = video_menu.id
            values['own_nodename'] = video_menu.name
            values['state'] = 'closed'

            ztrees = models.Site_Tree.objects.filter(node__startswith=sub.node)

            children = GetSubTree(sub, ztrees, index)

            if children != []:
                values['children'] = children

            else:
                # 没有下级子节点，找设备
                children = GetSubDevice(sub.id, sub.name, index)

                if children != []:
                    values['children'] = children

            value.append(values.copy())
            values.clear()  # 防止上次保存的结果干扰下一次的值，比如下一次没有这个键值，而上一次却有，就会保存上一次

    return value




