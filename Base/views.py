from django.shortcuts import render
from django.shortcuts import HttpResponse
from Models import models
from Base.com_func import *
import json



'''
将想要在前端展示的相应字段的中文名写到数据库中对应的注释里
公共函数在Base下的com_func中，不要动！只需在自己的views下 from Base.com_func import * 导入即可

单页的页面函数在Base下的views中，复制到自己写的app下的views中做相应的更改
保存需要读取前端Save传值写的那些参数  具体看前端save函数  有注释

单页的页面html 在 Base/templates/Base/sample_single.html  全部替换到自己的页面中
分页的页面html 在 Base/templates/Base/sample_div.html  全部替换到自己的页面中
'''


'''单页面单表数据的页面函数'''
def Sample_Singe(request):
	action = request.POST.get('action')

	'''sys code define variable begin  '''
	column = ''

	'''sys code define variable end  '''

	if request.method == 'GET':
		'''user code define variable begin  '''
		''' !!  都只改值，不动变量名    !!'''
		html_name = 'Base/sample_single.html' #配置html的所在地址
		head_title = '' #  网页的标题title

		'''!!    表格初始化  版本1  单表查字段注释   !! '''
		datagrid_version  = 1  #哪一代版本的 int
		datagrid_title = '生产厂商信息'  #表格的名称
		datagrid_tablename = 'Manufactor_Table'  # 在数据库找到想要获取字段的表，应为数据库中真实表名，即Models中的db_table
		''' id(数据库中自增长的那个字段，同样应为真实字段名)一定要有！！并放在第一个，不是用来显示，用来处理信息  其余顺序根据前端想要的摆放顺序来'''
		datagrid_columnname = ['id', 'name','managerName','phone','address']  # 在数据库找到想要获取的字段，应为数据库中真实的字段名,即Models中的db_column，如有的话
		datagrid_columncnt = 5  # 需要获取的列的数量 包括id
		datagrid_columnwidth = [0, 18, 10, 12, 20]  # 列的宽度 个数与cnt匹配
		datagrid_columnalign = ['center'] * datagrid_columncnt  # 对齐格式 个数与cnt匹配   可以不用改！！

		''' !!  新增数据时的弹框初始化    新增数据是不需要传id这个参数的  id是新增后生成的自增长字段      !! '''
		add_tab_version = 1
		add_tab_title = '新增生产厂商'
		add_tab_tablename = 'Manufactor_Table'  # 在数据库找到想要获取字段的表，应为数据库中真实表名，即Models中的db_table
		add_tab_columnname = ['name', 'managerName',
		                      'phone', 'address']  # 在数据库找到想要获取的字段，应为数据库中真实的字段名,即Models中的db_column，如有的话
		add_tab_columncnt = 4  # 需要获取的列的数量 不包括id！
		add_tab_boxtype = [1] * add_tab_columncnt
		'''user code define variable  end  '''

		'''sys code begin  '''

		'''        表格初始化      '''
		base_html_construct = base_html_construct_trans(datagrid_version , datagrid_tablename,datagrid_columnname,datagrid_columnwidth,datagrid_columnalign)
		base_html_construct.encode() #先将传送进来的参数进行解析
		column = base_html_construct.fun_Get_Cmd_Trans(datagrid_columncnt) #拼接cnt列Json
		'''  新增数据时的弹框初始化     '''
		add_tab_construct = add_tab_construct_trans(add_tab_version, add_tab_tablename, add_tab_columnname, add_tab_boxtype)
		add_tab_construct.encode()  # 先将传送进来的参数进行解析
		add_tab_dict = add_tab_construct.fun_Get_Cmd_Trans(add_tab_columncnt)  # 拼接cnt列Json

		return_dict = {'head_title':head_title,'info_dict': column,'datagrid_title':datagrid_title,'add_dict':add_tab_dict,'add_title':add_tab_title}

		return render(request, html_name,return_dict)#将初始化信息全部返回到前端
		'''sys code end'''

	else:
		'''user code define variable begin  '''
		model_name = models.Manufactor  # 想要展示的表的Model对象
		'''user code define variable end  '''

		'''usr code begin  '''

		if action == 'LoadData':
			querys = model_name.objects.all()  # 获取需要的字段名的数据
			value_dict = {'value0':'','value1': '', 'value2': '','value3':'','value4':''}   #有几个需要的列就有多少value 包括Id
			value_list = []
			for row in querys:
				value_dict['value0'] = row.id  # 一定要获取id 并放进第一个value0
				value_dict['value1'] = row.name  # 根据前端想要的摆放顺序来
				value_dict['value2'] = row.manager  #负责人姓名
				value_dict['value3'] = row.phone    #负责人联系电话
				value_dict['value4'] = row.address  #生产厂商地址

				value_list.append(value_dict.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
			# 用.copy()就不会跟着改变
				value_dict.clear()  # 防止出错时保存了上一次的值而导致看不出问题在哪

			return HttpResponse(json.dumps(value_list))  # 将列表拼字典仿Json格式转字符串传给前端 [{},{},{}]
		elif action == 'Save':

			back = 0

			# 获取要新增的信息
			add_name = request.POST.get('name')
			add_manager = request.POST.get('manager')
			add_phone = request.POST.get('phone')
			add_address = request.POST.get('address')

			models.Manufactor.objects.create(name=add_name, phone=add_phone, manager=add_manager, address=add_address)

			back = 1
			return HttpResponse(back)

		elif action == 'Edit':

			back = 0

			# 获取要更新的信息
			value_id = request.POST.get('value_id')
			add_name = request.POST.get('name')
			add_manager = request.POST.get('manager')
			add_phone = request.POST.get('phone')
			add_address = request.POST.get('address')

			back = models.Manufactor.objects.filter(pk = value_id).update(name=add_name, phone=add_phone, manager=add_manager,
			                                   address=add_address)

			return HttpResponse(back)

		elif action == 'Delete':

			back = 0

			# 获取要更新的信息
			value_id = request.POST.get('value_id')
			delete_flag = request.POST.get('delete_flag')

			# 判断在goodsinfo表中是否存在该索引Id ，若存在，则提示警告 ！ 若删除会将关联的所有信息一并删除，请确认
			if delete_flag == '0':  # 第一次点删除，还未做级联判断
				row = models.GoodsInfo.objects.filter(manufactor_id=value_id)

				if row.exists() != True:
					models.Manufactor.objects.filter(pk = value_id).delete()  # 因为外键会级联直接删除入库单中涉及该条信息的所有行
					back =1

				else:
					back = '在其他表中存在该信息，若删除将级联删除，是否确定删除？'
				# back = 1 正常删除 back = 警告，级联删除  back = 0 其他异常

			elif delete_flag == '1':  #确认级联删除，则直接删除

				models.Manufactor.objects.filter(pk=value_id).delete()  # 因为外键会级联直接删除入库单中涉及该条信息的所有行
				back = 1

			return HttpResponse(back)

		'''usr code end '''


'''
上下分页的页面函数
'''
def Sample_Div(request):
	action = request.POST.get('action')

	'''sys code define variable begin  '''
	column = ''
	'''sys code define variable begin  '''

	if request.method == 'GET':
		'''user code define variable begin  '''
		html_name = 'Base/sample_div.html' #配置html的所在地址
		head_title = '' #  网页的标题title


		'''!!    上表格初始化    !! '''
		top_datagrid_version = 1  #哪一种初始化 int
		top_datagrid_title = '生产厂商信息'  #表格的名称
		top_datagrid_tablename = 'Manufactor_Table'  # 在数据库找到想要获取字段的表，应为数据库中真实表名，即Models中的db_table
		''' id(数据库中自增长的那个字段，同样应为真实字段名)一定要有！！并放在第一个，不是用来显示，用来处理信息  其余顺序根据前端想要的摆放顺序来'''
		top_datagrid_columnname = ['id', 'name','managerName','phone','address']  # 在数据库找到想要获取的字段，应为数据库中真实的字段名,即Models中的db_column，如有的话
		top_datagrid_columncnt = 5  # 需要获取的列的数量 包括id
		top_datagrid_columnwidth = [0, 18, 10, 12, 20]  # 列的宽度 个数与cnt匹配
		top_datagrid_columnalign = ['center'] * top_datagrid_columncnt  # 对齐格式 个数与cnt匹配   可以不用改！！


		'''!!    下表格初始化    !! '''
		below_datagrid_version  = 1  #哪一种初始化 int
		below_datagrid_title = '生产厂商详情'  # 表格的名称
		below_datagrid_tablename = 'Manufactor_Table'  # 在数据库找到想要获取字段的表，应为数据库中真实表名，即Models中的db_table
		''' id(数据库中自增长的那个字段，同样应为真实字段名)一定要有！！并放在第一个，不是用来显示，用来处理信息  其余顺序根据前端想要的摆放顺序来'''
		below_datagrid_columnname = ['id', 'name', 'managerName', 'phone',
		                           'address']  # 在数据库找到想要获取的字段，应为数据库中真实的字段名,即Models中的db_column，如有的话
		below_datagrid_columncnt = 5  # 需要获取的列的数量 包括id
		below_datagrid_columnwidth = [0, 18, 10, 12, 20]  # 列的宽度 个数与cnt匹配
		below_datagrid_columnalign = ['center'] * top_datagrid_columncnt  # 对齐格式 个数与cnt匹配   可以不用改！！


		''' !!  新增数据时的弹框初始化    新增数据是不需要传id这个参数的  id是新增后生成的自增长字段      !! '''
		add_tab_version = 1    #版本号
		add_tab_title = '新增生产厂商'
		add_tab_tablename = 'Manufactor_Table'  # 在数据库找到想要获取字段的表，应为数据库中真实表名，即Models中的db_table
		add_tab_columnname = ['name', 'managerName',
		                      'phone', 'address']  # 在数据库找到想要获取的字段，应为数据库中真实的字段名,即Models中的db_column，如有的话
		add_tab_columncnt = 4  # 需要获取的列的数量 不包括id！
		add_tab_boxtype = [1]*add_tab_columncnt  # 是 1:输入框textbox,还是 2:下拉框combobox,还是 3 :日历datebox
		'''user code define variable  end  '''

		'''sys code begin  '''

		'''        上表格初始化      '''
		top_datagrid_construct = base_html_construct_trans(top_datagrid_version ,top_datagrid_tablename,top_datagrid_columnname,
		                                                   top_datagrid_columnwidth,top_datagrid_columnalign)
		top_datagrid_construct.encode() #先将传送进来的参数进行解析
		column = top_datagrid_construct.fun_Get_Cmd_Trans(top_datagrid_columncnt) #拼接cnt列Json

		'''        下表格初始化      '''
		below_datagrid_construct = base_html_construct_trans(below_datagrid_version , below_datagrid_tablename, below_datagrid_columnname,
		                                                     below_datagrid_columnwidth, below_datagrid_columnalign)
		below_datagrid_construct.encode()  # 先将传送进来的参数进行解析
		detail_dict = below_datagrid_construct.fun_Get_Cmd_Trans(below_datagrid_columncnt)  # 拼接cnt列Json

		'''  新增数据时的弹框初始化     '''
		add_tab_construct = add_tab_construct_trans(add_tab_version, add_tab_tablename, add_tab_columnname, add_tab_boxtype)
		add_tab_construct.encode()  # 先将传送进来的参数进行解析
		add_tab_dict = add_tab_construct.fun_Get_Cmd_Trans(add_tab_columncnt)  # 拼接cnt列Json

		return_dict = {'head_title':head_title, 'info_dict': column, 'datagrid_title':top_datagrid_title,
		               'detail_dict':detail_dict, 'detail_name':below_datagrid_title, 'add_dict':add_tab_dict, 'add_title':add_tab_title}

		return render(request, html_name,return_dict)#将初始化信息全部返回到前端

		'''sys code end  '''

	else:
		'''user code define variable begin  '''
		model_name = models.Manufactor  # 想要展示的表的Model对象
		'''user code define variable end  '''

		'''usr code begin  '''

		if action == 'LoadData':
			querys = model_name.objects.all()  # 获取需要的字段名的数据
			value_dict = {'value0':'','value1': '', 'value2': '','value3':'','value4':''}   #有几个需要的列就有多少value 包括Id
			value_list = []
			for row in querys:
				value_dict['value0'] = row.id  # 一定要获取id 并放进第一个value0
				value_dict['value1'] = row.name  # 根据前端想要的摆放顺序来
				value_dict['value2'] = row.manager  #负责人姓名
				value_dict['value3'] = row.phone    #负责人联系电话
				value_dict['value4'] = row.address  #生产厂商地址

				value_list.append(value_dict.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
			# 用.copy()就不会跟着改变
				value_dict.clear()  # 防止出错时保存了上一次的值而导致看不出问题在哪

			return HttpResponse(json.dumps(value_list))  # 将列表拼字典仿Json格式转字符串传给前端 [{},{},{}]
		elif action == 'Save':
			back = 0
			''' user code begin '''

			add_name = request.POST.get('name')
			add_manager = request.POST.get('manager')
			add_phone = request.POST.get('phone')
			add_address = request.POST.get('address')
			models.Supplier.objects.create(name=add_name, phone=add_phone, managername=add_manager, address=add_address)
			back = 1
			return HttpResponse(back)

			''' user code end '''
			back = 1
			return HttpResponse(back)

		elif action == 'LoadDetail':
			value_id =  request.POST.get('value_id')
			querys = model_name.objects.filter(pk = value_id)  # 获取需要的字段名的数据
			value_dict = {'value0': '', 'value1': '', 'value2': '', 'value3': '', 'value4': ''}  # 有几个需要的列就有多少value 包括Id
			value_list = []
			for row in querys:
				value_dict['value0'] = row.id  # 一定要获取id 并放进第一个value0
				value_dict['value1'] = row.name  # 根据前端想要的摆放顺序来
				value_dict['value2'] = row.manager  # 负责人姓名
				value_dict['value3'] = row.phone  # 负责人联系电话
				value_dict['value4'] = row.address  # 生产厂商地址

				value_list.append(value_dict.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
				# 用.copy()就不会跟着改变
				value_dict.clear()  # 防止出错时保存了上一次的值而导致看不出问题在哪

			return HttpResponse(json.dumps(value_list))  # 将列表拼字典仿Json格式转字符串传给前端 [{},{},{}]

		'''usr code end '''


'''单页面多表数据的页面函数'''
def Muti_Table(request):
	action = request.POST.get('action')

	'''sys code define variable begin  '''
	column = ''

	'''sys code define variable end  '''

	if request.method == 'GET':
		'''user code define variable begin  '''
		''' !!  都只改值，不动变量名    !!'''
		html_name = 'Base/muti_single.html' #配置html的所在地址
		head_title = '' #  网页的标题title

		'''!!    表格初始化 版本2 涉及多表查注释或直接给列的中文名   !! '''
		datagrid_version  = 2  #哪一代版本的 int
		datagrid_title = '入库信息'  #表格的名称

		datagrid_columncnt = 13  # 需要获取的列的数量 包括id
		datagrid_columnwidth = [0, 8, 12, 12, 15, 15, 15, 15, 15, 12, 12, 12, 18]  # 列的宽度 个数与cnt匹配
		datagrid_columnalign = ['center'] * datagrid_columncnt  # 对齐格式 个数与cnt匹配   可以不用改！！
					# '''   获取字段的注释的参数  直接写简单点  '''
		column_comment = ('ID','入库单编号','商品名称','商品类型','条形码','入库数量','进货总价',
		                  '保质期限','进库商户','操作人','入库时间','生产厂家','供货商')

		''' !!  新增数据时的弹框初始化    新增数据是不需要传id这个参数的  id是新增后生成的自增长字段      !! '''
		add_tab_version = 2
		add_tab_title = '新增入库单'
		add_tab_columncnt = 10  # 需要获取的列的数量 不包括id！
		add_tab_boxtype = [1,2,2,1,1,1,3,2,2,2]  # 1:输入框textbox,还是 2:下拉框combobox,还是 3 :日历datebox

		add_tab_comment = ('入库单编号', '商品名称', '商品类型', '条形码', '入库数量', '进货总价',
		                  '保质期限', '进库商户', '生产厂家', '供货商')
		'''user code define variable  end  '''

		'''sys code begin  '''

		'''        表格初始化      '''
		base_html_construct = base_html_construct_trans(datagrid_version ,datagrid_columnwidth,datagrid_columnalign)
		base_html_construct.encode() #先将传送进来的参数进行解析
		column = base_html_construct.fun_Get_Muti_Table(datagrid_columncnt,column_comment) #拼接cnt列Json
		'''  新增数据时的弹框初始化     '''
		add_tab_construct = add_tab_construct_trans(add_tab_version, add_tab_boxtype)
		add_tab_construct.encode()  # 先将传送进来的参数进行解析
		add_tab_dict = add_tab_construct.fun_Get_Muti_Table(add_tab_columncnt,add_tab_comment)  # 拼接cnt列Json

		return_dict = {'head_title':head_title,'info_dict': column,'datagrid_title':datagrid_title,'add_dict':add_tab_dict,'add_title':add_tab_title}

		return render(request, html_name, return_dict)#将初始化信息全部返回到前端
		'''sys code end'''


	else:
		user_id = request.session.get("Login_UserId")
		action = request.POST.get('action')

		if action == 'LoadData':

			# value_dict = {'value0': '', 'value1': '','combobox1':{'id':'','name':''}, 'value2': '', 'value3': '', 'value4': '', 'value5': '', 'value6': '',
			#
			#               'value7': '', 'value8': '', 'value9': '', 'value10': '', 'value11': '', 'value12': '', }

			value_dict = {'value0': '', 'value1': '', 'combobox1': {'id': '', 'name': ''}, 'combobox2': {'id': '', 'name': ''},
			              'combobox3': {'id': '', 'name': ''},'combobox4': {'id': '', 'name': ''},'combobox5': {'id': '', 'name': ''},
			              'value2': '','value3': '','value4': '', 'value5': '', 'value6': '', 'value7': '',
			              'value8': '', 'value9': '', 'value10': '', 'value11': '', 'value12': '', }

			# 入库单编号 商品名称 商品类型 条形码 入库数量 进货总价 保质期限 进库商户 操作人 入库时间 生产厂家 供货商

			value_list = []

			stock_Ins = models.StockIn.objects.all()

			for stock_in in stock_Ins:

				value_dict['value0'] = stock_in.id  # ID

				value_dict['value1'] = str(stock_in.stockin_id).zfill(9)  # 入库单编号

				if stock_in.goods != None:

					# 涉及下拉框的注意！！！   除了给value值以外，另外加一个'combobox1': {'id': '', 'name': ''} 键值对
					# 编辑时前端加载需要
					value_dict['combobox1']['id'] = stock_in.goods.id  # 商品名称

					value_dict['combobox1']['name'] = stock_in.goods.goodsname  # 商品名称

					value_dict['value2'] = stock_in.goods.goodsname  # 商品名称

				else:

					value_dict['value2'] = ''

				if stock_in.cat != None:

					value_dict['combobox2']['id'] = stock_in.cat.id

					value_dict['combobox2']['name'] = stock_in.cat.catname

					value_dict['value3'] = stock_in.cat.catname  # 商品类型

				else:

					value_dict['value3'] = ''

				value_dict['value4'] = stock_in.goods_sn  # 条形码

				value_dict['value5'] = stock_in.in_amount  # 入库数量

				value_dict['value6'] = stock_in.cost  # 进货总价

				goodsInfo = stock_in.goodsinfo_set.filter(stockin_id=stock_in.id)  # 保质期限

				if goodsInfo.count() != 0:

					if goodsInfo.first().exp_date != None:
						value_dict['value7'] = goodsInfo.first().exp_date.strftime("%Y-%m-%d %H:%M:%S")

				else:

					value_dict['value7'] = ''

				if stock_in.seller != None:

					value_dict['combobox3']['id'] = stock_in.seller.id

					value_dict['combobox3']['name'] = stock_in.seller.Sellername

					value_dict['value8'] = stock_in.seller.Sellername  # 进库商户

				else:

					value_dict['value8'] = ''

				if stock_in.performer != None:

					value_dict['value9'] = stock_in.performer.name  # 操作人

				else:

					value_dict['value9'] = ''

				value_dict['value10'] = stock_in.in_time.strftime("%Y-%m-%d %H:%M:%S")  # 入库时间

				if stock_in.manufactor != None:

					value_dict['combobox4']['id'] = stock_in.manufactor.id

					value_dict['combobox4']['name'] = stock_in.manufactor.name

					value_dict['value11'] = stock_in.manufactor.name  # 生产厂家

				else:

					value_dict['value11'] = ''

				if stock_in.supplier != None:
					value_dict['combobox5']['id'] = stock_in.supplier.id

					value_dict['combobox5']['name'] = stock_in.supplier.name

					value_dict['value12'] = stock_in.supplier.name  # 供货商

				else:

					value_dict['value12'] = ''

				value_list.append(value_dict.copy())

			return HttpResponse(json.dumps(value_list))

			'''新建入库单时生成单号，加载下拉框内容'''

		elif action == 'CreateStockInId':

			id = LoadStockInId()

			next_id = GetNextNumber(id)

			return HttpResponse(next_id)

		elif action == 'LoadGoodsName':

			value_list = getGoodsCombobox('goodsName')

			return HttpResponse(json.dumps(value_list))

		elif action == 'LoadGoodsCat':

			value_list = getGoodsCombobox('goodsCat')

			return HttpResponse(json.dumps(value_list))

		elif action == 'LoadSeller':

			value_list = getGoodsCombobox('seller')

			return HttpResponse(json.dumps(value_list))

		elif action == 'LoadManufactor':

			value_list = getGoodsCombobox('manufactor')

			return HttpResponse(json.dumps(value_list))

		elif action == 'LoadSupplier':

			value_list = getGoodsCombobox('supplier')

			return HttpResponse(json.dumps(value_list))

			'''保存新增的入库单'''

		elif action == 'Save':

			back = 0

			id = request.POST.get('stockIn_id')  # '000000003'    int(id)=3

			goods_id = request.POST.get('goods_id')  # '1'

			cat = request.POST.get('cat')  # '1'

			rfid = request.POST.get('rfid')  # 'S1233'

			amount = request.POST.get('amount')  # '15'

			cost = request.POST.get('cost')  # '56'

			# 提交回来的是总的成本价，保存在数据库goodsInfo 中保存的是单价 ,stockIn中直接保存的总价

			exp_date = request.POST.get('exp_date')  # '05/13/2020'

			'''时间格式问题 前端dd/mm/yy 保存格式应是yy-mm-dd 暂时不知道怎么解决，先不添加时间数据'''

			seller = request.POST.get('seller')

			manufactor = request.POST.get('mfrs')

			supplier = request.POST.get('supplier')

			# 更新stockIn表   先添加主表数据

			In = models.StockIn.objects.create(stockin_id=id, goods_id=goods_id, cat_id=cat, goods_sn=rfid,
			                                   in_amount=amount,

			                                   cost=float(cost), performer_id=user_id, seller_id=seller,
			                                   manufactor_id=manufactor,

			                                   supplier_id=supplier)

			# 更新goodsInfo表

			models.GoodsInfo.objects.create(stockin_id=In.id, goods_id=goods_id, cat_id=cat, goods_sn=rfid,
			                                goods_stock=amount, sale_count=0,

			                                cost=float(cost) / int(amount), manufactor_id=manufactor, seller_id=seller,
			                                supplier_id=supplier)

			back = 1

			return HttpResponse(back)

		elif action == 'Edit':

			back = 0
			input_error = 0  # 判断下拉框输入是否有问题
			# 获取要更新的信息
			value_id = request.POST.get('value_id')
			id = request.POST.get('stockIn_id')  # '000000003'    int(id)=3
			goods_id = request.POST.get('goods_id')  # '1'

			if goods_id.isdigit()!= True:
				input_error = 1

			cat = request.POST.get('cat')  # '1'

			if cat.isdigit()!= True:
				input_error = 1

			rfid = request.POST.get('rfid')  # 'S1233'
			amount = request.POST.get('amount')  # '15'
			cost = request.POST.get('cost')  # '56'
			# 提交回来的是总的成本价，保存在数据库goodsInfo 中保存的是单价 ,stockIn中直接保存的总价

			exp_date = request.POST.get('exp_date')  # '05/13/2020'
			'''时间格式问题 前端dd/mm/yy 保存格式应是yy-mm-dd 暂时不知道怎么解决，先不添加时间数据'''

			seller = request.POST.get('seller')
			if seller.isdigit() != True:
				input_error = 1

			manufactor = request.POST.get('mfrs')
			if manufactor.isdigit() != True:
				input_error = 1

			supplier = request.POST.get('supplier')
			if supplier.isdigit() != True:
				input_error = 1

			if input_error != 1:
				back = models.StockIn.objects.filter(pk=value_id).update(stockin_id=id, goods_id=goods_id, cat_id=cat, goods_sn=rfid, in_amount=amount,
			                              cost=float(cost), performer_id=user_id, seller_id=seller, manufactor_id=manufactor,
			                              supplier_id=supplier)

			else:
				back ='下拉框中没有该项，请检查输入是否有错，或在系统配置中添加该项！'

			return HttpResponse(back)


'''
加载最大入库单编号 字符串形式，9位
若无数据返回的id为''
'''

def LoadStockInId():
	int_id = 1
	id = ''
	stock_Ins = models.StockIn.objects.all().order_by('-stockin_id')
	if stock_Ins.count() != 0:
		int_id = stock_Ins.first().stockin_id  # first是一个stockIn对象
		id = str(int_id).zfill(9)  # 给字符串前面补零，保证9位长度
	return id

def LoadStockOutId():
	int_id = 1
	id = ''
	stock_Outs = models.StockOut.objects.all().order_by('-stockout_id')
	if stock_Outs.count() != 0:
		int_id = stock_Outs.first().stockout_id  # first是一个stockIn对象
		id = str(int_id).zfill(9)  # 给字符串前面补零，保证9位长度
	return id

'''
生成下一个商品编号
BaseNumber 为字符串
'''

def GetNextNumber(BaseNumber):
	NewNumber = ""  # 新值
	InNumber = 1  # 进位
	PlaceValue = 0  # 位值

	for num in BaseNumber[::-1]:
		if num == '9' and InNumber == 1:  # 当前为9，并且需要进位
			InNumber = 1
			NewNumber = '0' + NewNumber
		else:
			if InNumber == 1 and num >= '0' and num < '9':  # 需进位，但当前不是9，只需动当前这一位
				PlaceValue = int(num)
				PlaceValue = InNumber + PlaceValue  # +1
				InNumber = 0  # 进位结束
				NewNumber = str(PlaceValue) + NewNumber  # 字符串拼接
			else:  # 不需进位
				InNumber = 0
				NewNumber = num + NewNumber  # 字符串拼接，注意顺序！

	if (BaseNumber == NewNumber):
		NewNumber = "0000000001"
	return NewNumber

'''加载商品下拉框'''

def getGoodsCombobox(select):
	querys = ''
	value_dict = {'id': '', 'name': ''}
	value_list = []
	if select == "goodsName":
		querys = models.Goods.objects.all().extra({'id': 'id', 'name': 'goodsname'}).values('id',
		                                                                                    'name')  # 给字段起别名，必须写上values，不然并没有成功
	elif select == "goodsCat":
		querys = models.GoodsCat.objects.all().extra({'id': 'id', 'name': 'catname'}).values('id',
		                                                                                     'name')  # 给字段起别名，必须写上values，不然并没有成功
	elif select == "manufactor":
		querys = models.Manufactor.objects.all().extra({'id': 'id', 'name': 'name'}).values('id',
		                                                                                    'name')  # 给字段起别名，必须写上values，不然并没有成功
	elif select == "supplier":
		querys = models.Supplier.objects.all().extra({'id': 'id', 'name': 'name'}).values('id',
		                                                                                  'name')  # 给字段起别名，必须写上values，不然并没有成功
	elif select == "seller":
		querys = models.Seller.objects.all().extra({'id': 'id', 'name': 'Sellername'}).values('id',
		                                                                                      'name')  # 给字段起别名，必须写上values，不然并没有成功
	if querys.count != 0:
		for row in querys:
			value_dict['id'] = row['id']
			value_dict['name'] = row['name']
			value_list.append(value_dict.copy())
			value_dict.clear()
	return value_list

def load_commodity(request):
	action = request.POST.get('action')
	if request.method == 'GET':
		return render(request, 'Commodity/commodity.html')
	else:
		load_commodity = []
		if action == 'LoadData':
			load_commodity_list = models.GoodsInfo.objects.all()
			value = {'value1': '', 'value2': '', 'value3': '', 'value4': '', 'value5': '', 'value6': '',
			         'value7': '',
			         'value8': '', 'value9': '', 'value10': '', 'value11': '', 'value12': '', 'value13': '',
			         'value14': '', 'value15': '', }  # 用字典和列表拼接很方便形成Json格式
			for row in load_commodity_list:
				value['value1'] = row.goods_sn  # 条形码
				if row.goods != None:
					value['value2'] = row.goods.goodsname  # 商品名称
				else:
					value['value2'] = ''
				if row.cat != None:
					value['value3'] = row.cat.catname  # 商品类型
				else:
					value['value3'] = ''
				value['value4'] = row.goods_stock  # 库存量
				if row.stockin != None:
					value['value5'] = row.stockin.in_amount  # 进货量
				else:
					value['value5'] = ''
				value['value6'] = row.sale_count  # 销售量
				value['value7'] = row.cost  # 成本
				value['value8'] = row.price  # 交易额
				if row.exp_date != None:  # 为None 是没有strftime转换格式这种属性的
					value['value9'] = row.exp_date.strftime("%Y-%m-%d %H:%M:%S")  # 保质期限
				if row.manufactor != None:
					value['value10'] = row.manufactor.name  # 商品厂家
				else:
					value['value10'] = ''
				if row.supplier != None:
					value['value11'] = row.supplier.name  # 供货商
				else:
					value['value11'] = ''
				if row.seller != None:
					value['value12'] = row.seller.Sellername  # 销售
				else:
					value['value12'] = ''
				if row.out_time != None:  # 为None 是没有strftime转换格式这种属性的
					value['value13'] = row.out_time.strftime("%Y-%m-%d %H:%M:%S")
				load_commodity.append(value.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
				value.clear()  # 不保存上一次字典的记录，这是其实可以不要上面else时为空这句，返回不会有该key
			# 用.copy()就不会跟着改变

			return HttpResponse(json.dumps(load_commodity))  # 将列表转字符串传给前端


