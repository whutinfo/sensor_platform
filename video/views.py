from django.shortcuts import render
from django.http import HttpResponse
from Models import models
import json
from Base.com_func import *

def view(request):
    if request.method == 'GET':
        return render(request, 'video/videoview.html')
    else:
        action = request.POST.get('action')
        if action == 'LoadData':
            device_id = request.POST.get('device_id')
            cam = models.Video.objects.get(id=device_id)
            value_dict = {'value1': '', 'value2': '', 'value3': '', 'value4': '', 'value5': '', 'value6': '',
                          'value7': '', 'value8':'', 'value9':''}
            value_list = []
            value_dict['value1'] = cam.id
            value_dict['value2'] = cam.ip
            value_dict['value3'] = cam.port
            value_dict['value4'] = cam.user_name
            value_dict['value5'] = cam.pwd
            value_dict['value6'] = cam.rtsp_port
            value_dict['value7'] = cam.stream_type
            value_dict['value8'] = cam.device_port
            value_dict['value9'] = cam.device_type
            value_list.append(value_dict.copy())
            return HttpResponse(json.dumps(value_list))
        elif action == 'LoadTree':
            menus = models.videomeau.objects.all().order_by('node')
            index = {'index': 1}
            tree = [{'id': 0, 'trueid': 0, 'nature_id': 0, 'text': '所有地点的设备', 'own_deviceid': 0, 'own_devicename': '',
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
                    ztrees = models.videomeau.objects.filter(node__startswith=row.node)
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

def videoplay(request):
    if request.method == 'GET':
        return render(request, 'video/videoplay.html')
    else:
        action = request.POST.get('action')
        if action == 'LoadData':
            device_id = request.POST.get('device_id')
            cam = models.Video.objects.get(id=device_id)
            value_dict = {'value1': '', 'value2': '', 'value3': '', 'value4': '', 'value5': '', 'value6': '',
                          'value7': '', 'value8':''}
            value_list = []
            value_dict['value1'] = cam.id
            value_dict['value2'] = cam.ip
            value_dict['value3'] = cam.port
            value_dict['value4'] = cam.user_name
            value_dict['value5'] = cam.pwd
            value_dict['value6'] = cam.rtsp_port
            value_dict['value7'] = cam.stream_type
            value_dict['value8'] = cam.device_port
            value_list.append(value_dict.copy())
            return HttpResponse(json.dumps(value_list))
        elif action == 'LoadTree':
            menus = models.videomeau.objects.all().order_by('node')
            index = {'index': 1}
            tree = [{'id': 0, 'trueid': 0, 'nature_id': 0, 'text': '所有地点的设备', 'own_deviceid': 0, 'own_devicename': '',
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
                    ztrees = models.videomeau.objects.filter(node__startswith=row.node)
                    children2 = GetSubNVR(row.id, row.name, index)  # 先获取其下所有设备
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


def videosettings(request):
    column = ''

    '''sys code define variable end  '''

    if request.method == 'GET':
        '''user code define variable begin  '''
        ''' !!  都只改值，不动变量名    !!'''
        html_name = 'video/videoSettings.html'  # 配置html的所在地址
        head_title = ''  # 网页的标题title

        '''!!    表格初始化 版本2 涉及多表查注释或直接给列的中文名   !! '''
        datagrid_version = 2  # 哪一代版本的 int
        datagrid_title = '设备信息'  # 表格的名称

        datagrid_columncnt = 10  # 需要获取的列的数量 包括id
        datagrid_columnwidth = [0, 8, 12, 12, 15, 15, 15, 15, 15,15]  # 列的宽度 个数与cnt匹配
        datagrid_columnalign = ['center'] * datagrid_columncnt  # 对齐格式 个数与cnt匹配   可以不用改！！
        # '''   获取字段的注释的参数  直接写简单点  '''
        column_comment = ('ID', '摄像头名', 'ip地址', '端口号', '用户名', '密码', 'rtsp端口号',
                          '流类型', '设备端口','设备类型')

        '''sys code begin  '''

        '''        表格初始化      '''
        base_html_construct =  base_html_construct_trans(datagrid_version, datagrid_columnwidth, datagrid_columnalign)
        base_html_construct.encode()  # 先将传送进来的参数进行解析
        column = base_html_construct.fun_Get_Muti_Table(datagrid_columncnt, column_comment)  # 拼接cnt列Json

        return_dict = {'head_title': head_title, 'info_dict': column, 'datagrid_title': datagrid_title}

        return render(request, html_name, return_dict)  # 将初始化信息全部返回到前端

        '''sys code end'''
    else:

        '''user code define variable begin  '''
        action = request.POST.get('action')
        model_name = models.Video  # 想要展示的表的Model对象
        '''user code define variable end  '''

        '''usr code begin  '''

        if action == 'LoadData':
            querys = model_name.objects.all()  # 获取需要的字段名的数据
            value_dict = {'value0': '', 'value1': '', 'value2': '', 'value3': '', 'value4': ''
                , 'value5': '', 'value6': '', 'value7': '', 'value8': '', 'value9': ''}  # 有几个需要的列就有多少value 包括Id
            value_list = []
            for row in querys:
                value_dict['value0'] = row.id
                value_dict['value1'] = row.name
                value_dict['value2'] = row.ip
                value_dict['value3'] = row.port
                value_dict['value4'] = row.user_name
                value_dict['value5'] = row.pwd
                value_dict['value6'] = row.rtsp_port
                value_dict['value7'] = row.stream_type
                value_dict['value8'] = row.device_port
                value_dict['value9'] = row.device_type
                value_list.append(value_dict.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                # 用.copy()就不会跟着改变
                value_dict.clear()  # 防止出错时保存了上一次的值而导致看不出问题在哪

            return HttpResponse(json.dumps(value_list))  # 将列表拼字典仿Json格式转字符串传给前端 [{},{},{}]
        elif action == 'LoadTree':

            menus = models.videomeau.objects.all().order_by('node')
            index = {'index': 1}
            tree = [{'id': 0, 'trueid': 0, 'nature_id': 0, 'text': '所有地点的设备', 'own_deviceid': 0, 'own_devicename': '',
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
                    ztrees = models.videomeau.objects.filter(node__startswith=row.node)
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
        elif action == 'LoadDevice':
            querys = models.Video.objects.all()  # 获取需要的字段名的数据
            value_dict = {'id': '', 'name': ''}
            value_list = []
            for row in querys:
                value_dict['id'] = row.id
                value_dict['name'] = row.name

                value_list.append(value_dict.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                # 用.copy()就不会跟着改变
                value_dict.clear()  # 防止出错时保存了上一次的值而导致看不出问题在哪

            return HttpResponse(json.dumps(value_list))  # 将列表拼字典仿Json格式转字符串传给前端 [{},{},{}]
        elif action == 'LoadNode':
            querys = models.videomeau.objects.all()  # 获取需要的字段名的数据
            value_dict = {'id': '', 'name': ''}
            value_list = []
            for row in querys:
                value_dict['id'] = row.id
                value_dict['name'] = row.name
                value_list.append(value_dict.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                # 用.copy()就不会跟着改变
                value_dict.clear()  # 防止出错时保存了上一次的值而导致看不出问题在哪

            return HttpResponse(json.dumps(value_list))  # 将列表拼字典仿Json格式转字符串传给前端 [{},{},{}]
        elif action == 'AddNode':
            back = 0
            true_id = request.POST.get('trueid')
            node_name = request.POST.get('node')

            # 根据true_id 是否为0 判断为索引节点 还是自己建的节点
            # 获取的为str

            if true_id == '0':
                # 则新增的是顶级节点，其node长度应为4
                # 先逆序排列，若存在节点，则对最大节点+1

                addnode = "1000"  # 父节点初始值

                nodes = models.videomeau.objects.all().order_by('-node')

                for row in nodes:

                    if len(row.node) == 4:
                        addnode = int(row.node) + 1

                        break

                models.videomeau.objects.create(name=node_name, node=addnode)

                back = 1

            else:
                # 则新增的是子节点，其node是父节点与最大子节点的拼接
                # 先逆序排列，若存在节点，则对最大节点+1

                parent = models.videomeau.objects.filter(pk=true_id).first()  # 直接获取对象
                parent_node = parent.node
                if len(parent_node) == 4:
                    ztrees = models.videomeau.objects.filter(node__startswith=parent_node).order_by(
                        '-node')  # 所有子节点按倒序排列，一定会存在，因为包含它自己。选第一个，对其Node+1
                    if ztrees.count() <= 1:  # 最开始不存在子节点
                        checknode = '1000'  # 初始节点\
                    else:
                        checknode = str(int(ztrees.first().node) + 1)
                    insert_node = parent_node + checknode
                    models.videomeau.objects.create(name=node_name, node=insert_node)

                back = 1

            return HttpResponse(back)
        elif action == 'AddDevice':
            back = 0
            ishave = 0
            true_id = request.POST.get('trueid')  # 选择的节点id
            device_id = request.POST.get('device')  # 添加的设备id

            # 判断该设备是否已有父节点，若有，则不应再添加
            device = models.Video.objects.filter(pk=device_id).first()  # 已经是对象

            if not device.parent_id:
                ishave = 1

            if ishave != 0:

                back = '该设备已有父节点！若想更改其父节点请编辑该设备。'

            else:
                # 在video 表中添加其父节点即true_id
                models.Video.objects.filter(pk=device_id).update(parent_id=true_id)

                back = 1

            return HttpResponse(back)
        elif action == 'SaveDevice':
            v0 = request.POST.get('value0')
            v1 = request.POST.get('value1')
            v2 = request.POST.get('value2')
            v3 = request.POST.get('value3')
            v4 = request.POST.get('value4')
            v5 = request.POST.get('value5')
            v6 = request.POST.get('value6')
            v7 = request.POST.get('value7')
            v8 = request.POST.get('value8')
            v9 = request.POST.get('value9')
            nodeid = request.POST.get('node')
            models.Video.objects.create(name=v0,ip=v1,port=v2,user_name=v3,pwd=v4,rtsp_port=v5,stream_type=v6,device_port=v7,device_type=v8,manufacturer=v9,parent_id=nodeid)
            return HttpResponse(1)
        elif action == 'EditDevice':
            id = request.POST.get('field_id')
            v0 = request.POST.get('value0')
            v1 = request.POST.get('value1')
            v2 = request.POST.get('value2')
            v3 = request.POST.get('value3')
            v4 = request.POST.get('value4')
            v5 = request.POST.get('value5')
            v6 = request.POST.get('value6')
            v7 = request.POST.get('value7')
            v8 = request.POST.get('value8')
            v9 = request.POST.get('value9')
            models.Video.objects.filter(id=id).update(name=v0,ip=v1,port=v2,user_name=v3,pwd=v4,rtsp_port=v5,stream_type=v6,device_port=v7,device_type=v8,manufacturer=v9)
            return HttpResponse(1)


def GetSubDevice(node_id, node_name, index):
    """
    根据node_id 节点id 在Video表中找到他拥有的所有设备
    :param node_id: 需要获取设备的节点
    :param node_name: 节点名称
    :param index: 自增的索引，是树的所有节点的唯一id
    :return:
    """

    videos = models.Video.objects.filter(parent_id=node_id)
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
    values = {}
    value = []

    for sub in ztrees:

        # 节点更长的即为子节点
        if len(video_menu.node) < len(sub.node):
            index['index'] += 1
            values['id'] = index['index']
            values['trueid'] = sub.id
            values['nature_id'] = 1
            values['text'] = sub.name
            values['own_nodeid'] = video_menu.id
            values['own_nodename'] = video_menu.name
            values['state'] = 'closed'

            # 迭代下去找相应的子节点直到找完
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

def GetSubNVR(node_id, node_name, index):
    """
    根据node_id 节点id 在Video表中找到他拥有的所有设备
    :param node_id: 需要获取设备的节点
    :param node_name: 节点名称
    :param index: 自增的索引，是树的所有节点的唯一id
    :return:
    """

    videos = models.Video.objects.filter(device_type=2).filter(parent_id=node_id)
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