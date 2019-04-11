#-*- coding: UTF-8 -*-
from django.shortcuts import render
from django.shortcuts import HttpResponse
from Models import models
from Base.com_func import *
import json

# Create your views here.
def customermanager(request):
    action = request.POST.get('action')

    '''sys code define variable begin  '''
    column = ''
    '''sys code define variable begin  '''

    if request.method == 'GET':
        '''user code define variable begin  '''

        version = 1  # 哪一代版本的 int
        # databasename = 'aliyun'
        tablename = 'Customer_Table'  # 在数据库找到想要获取字段的表，应为数据库中真实表名，即Models中的db_table
        ''' id(数据库中自增长的那个字段，同样应为真实字段名)一定要有！！并放在第一个，不是用来显示，用来处理信息  其余顺序根据前端想要的摆放顺序来'''
        columnname = ['id', 'name', 'carId', 'phone', 'sex', 'birthday',
                      'point','create_time','update_time']  # 在数据库找到想要获取的字段，应为数据库中真实的字段名,即Models中的db_column，如有的话
        columncnt = 9  # 需要获取的列的数量 包括id
        columnwidth = [0, 10, 18, 12, 10, 20, 12, 20, 20]  # 列的宽度 个数与cnt匹配  第一个对应的Id,id 不显示，赋0即可
        columnalign = ['center'] * columncnt  # 对齐格式 个数与cnt匹配   可以不用改！！

        '''user code define variable  end  '''

        '''sys code begin  '''

        # column = fun_Get_Cmd_Trans(databasename, tablename, columnname, columncnt, columnwidth, columnalign)
        base_html_construct = base_html_construct_trans(version, tablename, columnname, columnwidth, columnalign)
        base_html_construct.encode()  # 先将传送进来的参数进行解析
        column = base_html_construct.fun_Get_Cmd_Trans(columncnt)  # 拼接cnt列Json

        '''sys code end'''

        '''usr code begin  '''
        return render(request, 'customermanager/customermanager.html', {'info_dict': column})
        '''usr code end '''

    else:
        '''user code define variable begin  '''
        model_name = models.Customer  # 想要展示的表的Model对象
        '''user code define variable end  '''

        '''usr code begin  '''

        if action == 'LoadData':
            querys = model_name.objects.all()  # 获取需要的字段名的数据
            value_dict = {'value0': '', 'value1': '', 'value2': '', 'value3': '', 'value4': '',
                          'value5': '', 'value6': '', 'value7': '', 'value8': ''}  # 有几个需要的列就有多少value 包括Id
            value_list = []
            for row in querys:
                value_dict['value0'] = row.id  # 一定要获取id 并放进第一个value0
                value_dict['value1'] = row.name  # 根据前端想要的摆放顺序来
                value_dict['value2'] = row.carid  # 卡号
                value_dict['value3'] = row.phone  # 手机号
                value_dict['value4'] = row.sex  # 性别
                value_dict['value5'] = row.birthday  # 生日
                value_dict['value6'] = row.point  # 积分
                value_dict['value7'] = row.create_time  # 创建时间
                value_dict['value8'] = row.update_time  # 更新时间
                value_list.append(value_dict.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                # 用.copy()就不会跟着改变
                value_dict.clear()#防止出错时保存了上一次的值而导致看不出问题在哪

            return HttpResponse(json.dumps(value_list))  # 将列表拼字典仿Json格式转字符串传给前端 [{},{},{}]

        elif action == 'Save':
            add_name = request.POST.get('name')
            add_birthday=request.POST.get('birthday')
            add_sex=request.POST.get('sex')
            add_phone=request.POST.get('phone')
            add_carid = request.POST.get('carId')
            add_point = request.POST.get('point')
            add_create_time = request.POST.get('create_time')
            add_update_time = request.POST.get('update_time')
            models.Customer.objects.create(name=add_name,birthday=add_birthday,sex=add_sex,phone=add_phone,carid=add_carid,point=add_point,create_time=add_create_time,update_time=add_update_time,)

            return HttpResponse(1)

        '''usr code end '''