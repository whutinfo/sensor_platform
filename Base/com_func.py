from echarts import *


""""已将这几个函数封装成类  begin"""
'''
json_frame_construct：针对页面的get命令进行处理   拼接前端表格的column数据
参数column_name:字段名  column_cnt：列的数量   column_width：列的宽度  column_align：对齐格式
除 column_cnt 是int，其它都是列表格式  列表的长度 与 数量匹配
返回值：将送进来的字段名与相应的列的各种参数拼接成前端需要的json形式返回
'''
def json_frame_construct(column_name,column_cnt,column_width,column_align):
	column = []
	for i in range(column_cnt):
		value = 'value'+str(i)
		width = str(column_width[i]) + '%'
		json_frame={'field': value, 'title': column_name[i], 'width':width, 'align': column_align[i]}
		column.append(json_frame.copy())
	return column
	# [
    #     {'field': 'value1', 'title': '生产厂商名称', 'width': '18%', 'align': 'center'},
    #     {'field': 'value2', 'title': '负责人姓名', 'width': '10%', 'align': 'center'},
    #     {'field': 'value3', 'title': '负责人手机号', 'width': "12%", 'align': 'center'},
    #     {'field': 'value4', 'title': '联系地址', 'width': "20%", 'align': 'center'}]

    #construct json

'''
拼接 get命令下，针对列表模式下的页面结构 
databasename:数据库名  tablename：表名  columnname：字段名 columncnt：字段个数  columnwidth：宽度 columnalign：对齐格式
'''
def fun_Get_Cmd_Trans(databasename,tablename,columnname,columncnt,columnwidth,columnalign):
    l_column_name = []
    for i in range(columncnt):
        comment = fun_call_db_proc(databasename,tablename,columnname[i])  #获得表的该字段的注释 即为前端表格的中文列名  返回元组如：(ID,)
        l_column_name.append(comment[0])
    column=json_frame_construct(l_column_name,columncnt,columnwidth,columnalign) #将所有列的参数送进去拼接成json

    return column

"""已将这几个函数封装成类   end"""


'''
wangyu test
http://blog.sina.com.cn/s/blog_70dc706b0100oavh.html  这个是针对存储过程的调用方法
获得表的该字段的注释  返回元组如：(ID,)
'''
def fun_call_db_proc(database_str,table_str,column_str):
	from django.db import connection
	data2 = ''
	data2 = 'SELECT column_comment FROM INFORMATION_SCHEMA.Columns WHERE table_schema = "'  + database_str + '" AND table_name= "' + \
			 table_str + '" AND  column_name= "' + column_str + '"'
	cursor1 = connection.cursor()
	data1= cursor1.execute(data2)
	data_str = cursor1.fetchone()
	if data_str != None:
		return data_str
	else:       #参数有误报错
		return print('请检查参数是否输入有误，无法获取注释')

'''
html页面的表格初始化的公共类
传参顺序：版本号，获取注释的表名，获取注释的字段， 宽度 ， 对齐方式
如： base_html_construct_trans(datagrid_version, datagrid_tablename, datagrid_columnname, datagrid_columnwidth, datagrid_columnalign)
'''
class base_html_construct_trans(object):
	database_name = 'aliyun'
	def __init__(self, *var):
		self.param = var
		self.table_name = ''
		self.column_list = ''
		self.width_list = ''
		self.align_list = ''
	def encode(self):
		self.version = int( self.param[0] ) # 容许你输入的参数为'1' 容错
		if self.version == 1:  # 版本1  单表
			self.table_name = self.param[1]  # 要获取注释信息的表名  数据库中真实表名
			self.column_list = self.param[2]  # 要获取注释的字段名  数据库中真实字段名
			self.width_list = self.param[3]  # 列的宽度 元组
			self.align_list = self.param[4]  # 列的对齐格式  元组
		elif self.version == 2:  # 版本2  多表（已经获取过字段注释） 或直接输入字段注释
			#self.table_name = self.param[1]  # 要获取注释信息的表名  数据库中真实表名
			#self.column_list = self.param[2]  # 要获取注释的字段名  数据库中真实字段名
			self.width_list = self.param[1]  # 列的宽度 元组
			self.align_list = self.param[2]  # 列的对齐格式  元组

		self.fielddic = {}

	'''
	json_frame_construct：针对页面的get命令进行处理   拼接前端表格的column数据
	参数column_name:字段名  column_cnt：列的数量   column_width：列的宽度  column_align：对齐格式
	除 column_cnt 是int，其它都是列表格式  列表的长度 与 数量匹配
	返回值：将送进来的字段名与相应的列的各种参数拼接成前端需要的json形式返回
	'''
	def json_frame_construct(self,column_name,column_cnt,column_width,column_align ):
		column = []
		for i in range(column_cnt):
			value = 'value' + str(i)
			width = str(column_width[i]) + '%'
			json_frame = {'field': value, 'title': column_name[i], 'width':width, 'align': column_align[i]}
			column.append(json_frame.copy())
		return column
	# construct json

	'''
	拼接 get命令下，针对列表模式下的页面结构   单表查询
	databasename:数据库名  tablename：表名  columnname：字段名 columncnt：字段个数  columnwidth：宽度 columnalign：对齐格式
	'''
	def fun_Get_Cmd_Trans(self, columncnt):
		l_column_name = []
		self.fielddic = ''

		if self.table_name != '' and self.column_list != '' and self.width_list != '' and self.align_list != '':   #检查参数是否经过encode解析
			for i in range(columncnt):
				comment = fun_call_db_proc(self.database_name, self.table_name,self.column_list[i])  # 获得表的该字段的注释 即为前端表格的中文列名  返回元组如：(ID,)
				if comment != None: #参数无误
					l_column_name.append(comment[0])
			if len(self.width_list) == columncnt and len(self.align_list) == columncnt: #检查参数长度是否匹配
				self.fielddic = self.json_frame_construct(l_column_name, columncnt, self.width_list, self.align_list)  # 将所有列的参数送进去拼接成json
			else:
				print('请检查width和align参数的长度是否与cnt个数匹配')
		else:
			print('请先对参数进行encode解析,注意系统代码段是否做过更改')
		return self.fielddic

	'''
	拼接 get命令下，针对列表模式下的页面结构  需要连表查询获取字段注释  或 不获取直接输入列的中文名
	column_name：字段注释 即列的中文名 columncnt：字段个数 
	'''
	def fun_Get_Muti_Table(self, columncnt, column_name):

		self.fielddic = ''
		if self.width_list != '' and self.align_list != '':  # 检查参数是否经过encode解析
			if len(self.width_list) == columncnt and len(self.align_list) == columncnt:  # 检查参数长度是否匹配
				self.fielddic = self.json_frame_construct(column_name, columncnt, self.width_list,
				                                          self.align_list)  # 将所有列的参数送进去拼接成json
			else:
				print('请检查width和align参数的长度是否与cnt个数匹配')
		else:
			print('请先对参数进行encode解析,注意系统代码段是否做过更改')
		return self.fielddic

'''
针对GET 对新增信息的弹框做初始化处理
传参顺序如 ：版本号，获取注释的表名，获取注释的字段 输入框类型
add_tab_construct_trans(add_tab_version, add_tab_tablename, add_tab_columnname, add_tab_boxtype)
'''
class add_tab_construct_trans(object):
	database_name = 'aliyun'

	def __init__(self, *var):
		self.param = var
		self.table_name = ''
		self.column_list = ''
		self.box_type = ''

	def encode(self):
		self.version = int( self.param[0] ) # 容许你输入的参数为'1' 容错
		if self.version == 1:  # 版本
			self.table_name = self.param[1]  # 要获取注释信息的表名  数据库中真实表名
			self.column_list = self.param[2]  # 要获取注释的字段名  数据库中真实字段名
			self.box_type = self.param[3]  # 是输入框textbox,还是下拉框combobox,还是日历datebox
		elif self.version == 2:  # 版本2 直接输入注释
			self.box_type = self.param[1]  # 是 1:输入框textbox,还是 2:下拉框combobox,还是 3 :日历datebox

		self.fielddic = {}

	'''
	json_frame_construct：针对页面的get命令进行处理   拼接前端新增信息弹框的Json
	参数column_name:字段名  column_cnt：列的数量 box_type : 输入框的类型
	返回值：将送进来的字段名与相应的列的各种参数拼接成前端需要的json形式返回
	'''
	def json_frame_construct(self,column_name,column_cnt,box_type):
		column = []
		type = ''
		for i in range(column_cnt):
			value = 'dlg1_2_txt_' + str(i+1)  #前端需要这种格式  从dlg1_2_txt_1开始

			if box_type[i] == 1:
				type = 'easyui-textbox'
			elif box_type[i] == 2:
				type = 'easyui-combobox'
			elif box_type[i] == 3:
				type = 'easyui-datebox'

			json_frame = {'id': value, 'title': column_name[i],'box_type':type}
			column.append(json_frame.copy())
		return column

	'''
	拼接 get命令下，针对新增弹框下的页面结构 
	columncnt：字段个数 
	'''
	def fun_Get_Cmd_Trans(self, columncnt):
		l_column_name = []
		self.fielddic = ''

		if self.table_name != '' and self.column_list != '' and self.box_type != '':   #检查参数是否经过encode解析
			for i in range(columncnt):
				comment = fun_call_db_proc(self.database_name, self.table_name,self.column_list[i])  # 获得表的该字段的注释 即为前端表格的中文列名  返回元组如：(ID,)
				if comment != None: #参数无误
					l_column_name.append(comment[0])
			if len(self.column_list) == columncnt: #检查参数长度是否匹配
				self.fielddic = self.json_frame_construct(l_column_name, columncnt,self.box_type)  # 将所有列的参数送进去拼接成json
			else:
				print('请检查width和align参数的长度是否与cnt个数匹配')
		else:
			print('请先对参数进行encode解析,注意系统代码段是否做过更改')
		return self.fielddic

	'''
	拼接 get命令下，针对列表模式下的页面结构  需要连表查询获取字段注释  或 不获取直接输入列的中文名
	column_name：字段注释 即列的中文名 columncnt：字段个数 
	'''
	def fun_Get_Muti_Table(self, columncnt, column_name):

		self.fielddic = ''
		if self.box_type != '' :  # 检查参数是否经过encode解析

			self.fielddic = self.json_frame_construct(column_name, columncnt,self.box_type)  # 将所有列的参数送进去拼接成json
		else:
			print('请先对参数进行encode解析,注意系统代码段是否做过更改')
		return self.fielddic


#还没有用到
class html_base_var(object):
		'''!!    表格初始化    !! '''
		datagrid_type = ''  #哪一种初始化 int  1： 初始化datagrid表格  2：  初始化新增信息的弹框
		datagrid_title = ''  #表格的名称
		datagrid_tablename = ''  # 在数据库找到想要获取字段的表，应为数据库中真实表名，即Models中的db_table
		''' id(数据库中自增长的那个字段，同样应为真实字段名)一定要有！！并放在第一个，不是用来显示，用来处理信息  其余顺序根据前端想要的摆放顺序来'''
		datagrid_columnname = []  # 在数据库找到想要获取的字段，应为数据库中真实的字段名,即Models中的db_column，如有的话
		datagrid_columncnt = ''  # 需要获取的列的数量 包括id
		datagrid_columnwidth = []  # 列的宽度 个数与cnt匹配
		datagrid_columnalign = []   # 对齐格式 个数与cnt匹配   可以不用改！！

		''' !!  新增数据时的弹框初始化    新增数据是不需要传id这个参数的  id是新增后生成的自增长字段      !! '''
		add_tab_type = ''
		add_tab_title = '' #框的名称
		add_tab_tablename = ''  # 在数据库找到想要获取字段的表，应为数据库中真实表名，即Models中的db_table
		add_tab_columnname = []  # 在数据库找到想要获取的字段，应为数据库中真实的字段名,即Models中的db_column，如有的话
		add_tab_columncnt = ''  # 需要获取的列的数量 不包括id！

'''    
    cursor1.execute("select * from Goods_Table")
    data = cursor1.fetchone()
    for data1 in data:
        print(data1)
'''
#    cursor1.execture()

'''
wangyu test

def fun_call_db_proc(request):
    models.Models
    django.db
    cursor1 = dbTrans.cursor()
    cursor1.execute("select * from Goods_Table")
    cursor.fetchall()
#    cursor1.execture()

'''


#已经不用的函数

'''
base_fun_get_demo : 实现对某个表中的特定字段，将其注释内容返回  即中文列名
形参：Model_Object  是特定表的字段  如： Model_Object= models.GoodsCat
返回值：字段名和字段的注释内容，返回类型为字典
该函数也不用了
'''
def base_fun_get_demo(Model_Object):  # Model_Object= models.GoodsCat
    fielddic = {}
    table_name = Model_Object._meta.db_table  #获取该Model对象的表名
    for field in Model_Object._meta.fields:
        var = field.get_attname_column()#获取当前列的列名  ( model field ，db_column)形式 (models中写定的列名，实际数据库中的列名)
        field_name = var[0]
        db_column = var[1]
        comment = fun_call_db_proc('aliyun', table_name, db_column)  #<class 'tuple'>: ('索引号',)
        fielddic[field_name] = comment[0]
    return fielddic


def fun_sys_pie_series(x_data,y_data):
	"""
	拼接饼图中series的数据格式 [{ // 数据项的名称 name: '数据1',   // 数据项值8   value: 10		},
							  {  name: '数据2', value: 20		}]
	:param x_data: 饼图的数据项名称
	:param y_data: 饼图的数据项值
	:return: 拼接后的series_data
	"""

	value_list = []
	value_dict = {'name':'','value':''}

	# 先判断x_data与y_data的个数是否匹配
	if len(x_data) != len(y_data):
		print('请检查输入的x和y的个数是否一致！')
		return None
	else:
		for i in range(len(x_data)):
			value_dict['name'] = x_data[i]
			value_dict['value'] = y_data[i]
			value_list.append(value_dict.copy())

		return value_list



class new_a_chart(object):

	def __init__(self,chart_type,title='',description=''):

		self.title = title

		self.description = description

		self.y_data = []

		self.x_data = []

		self.legend = []

		self.chart_type=chart_type

		if int(self.chart_type) == 3: # 饼图的时候创建图的实例让axis坐标系为false
			# 创建一张图的实例
			self.chart = Echart(self.title,self.description,axis=False)
			# 提示框组件
			self.chart.use(Tooltip(trigger='item'))


		else:
			# 创建一张图的实例
			self.chart = Echart(self.title, self.description, axis=True)
			# 提示框组件
			self.chart.use(Tooltip(trigger='axis'))

	def line(self,x_data=None,y_data=None,label=''):
		'''
		在该图上画一条折线
		:param x_data: x轴真实显示的数据
		:param y_data: y轴真实显示的数据
		:param label: 该条折线显示的意义，即图例内容
		:return:None
		'''

		self.legend.append(label)

		# 在折线图上以圆点显示最大值最小值
		markPoint = {'data':
			             [{'type': 'max', 'name': '最大值'},
			              {'type': 'min', 'name': '最小值'}]
		             }
		# 在折线图以虚线画出平均值
		markLine = {'data': [{'type': 'average', 'name': '平均值'}]}

		self.x_data=x_data
		self.y_data=y_data

		# 创建一条折线
		self.chart.use(Line(name=label, data=self.y_data, markPoint=markPoint, markLine=markLine))

	def bar(self,x_data=None,y_data=None,label=''):
		'''
		在该图上画柱状
		:param x_data: x轴真实显示的数据
		:param y_data: y轴真实显示的数据
		:param label: 该条形显示的意义，即图例内容
		:return:None
		'''

		self.legend.append(label)

		# 在折线图上以圆点显示最大值最小值
		markPoint = {'data':
			             [{'type': 'max', 'name': '最大值'},
			              {'type': 'min', 'name': '最小值'}]
		             }
		# 在折线图以虚线画出平均值
		markLine = {'data': [{'type': 'average', 'name': '平均值'}]}

		self.x_data=x_data
		self.y_data=y_data

		# 创建一条折线
		self.chart.use(Bar(name=label, data=self.y_data, markPoint=markPoint, markLine=markLine))

	def pie(self,x_data=None,y_data=None,label=''):
		'''
		在该图上画饼图
		:param x_data: x轴真实显示的数据
		:param y_data: y轴真实显示的数据
		:param label: 该条折线显示的意义，即图例内容
		:return:None
		'''

		self.legend = x_data

		self.x_data=x_data
		self.y_data=y_data

		""" pie没有坐标轴，数据全由series展示，数据格式如下
		[{
            // 数据项的名称
            name: '数据1',
            // 数据项值8
            value: 10
		}, 
		{
			 name: '数据2',
			 value: 20
		}]
		"""

		series_data = fun_sys_pie_series(x_data,y_data)

		# 创建一个饼图 此时 name 是数据项的名称，即x_data
		self.chart.use(Pie(name=label, data=series_data))

	def Set_Legend(self, orient='horizontal', position=None):
		"""
		创建图例    data = ['类别1', '类别2', '类别3'],  series中根据名称区分 与series保持一致！
		:param orient: 'horizontal' 水平, 'vertical'  垂直
		:param position:默认 (x:'center',y: 'top') 以元组形式
		:return: None
		"""

		self.chart.use(Legend(data=self.legend,orient=orient,position=position))

	def x_axis(self,type='category', position='bottom'):
		"""
		设置直角坐标系 grid 中的 x 轴
		:param type:默认为种类
		:param position:x 轴的位置，可选：'top'，'bottom'
		:return:'value' 数值轴，适用于连续数据。
				'category' 类目轴，适用于离散的类目数据，为该类型时必须通过 data 设置类目数据。
				'time' 时间轴，适用于连续的时序数据，与数值轴相比时间轴带有时间的格式化，在刻度计算上也有所不同，
				例如会根据跨度的范围来决定使用月，星期，日还是小时范围的刻度。
		"""
		if type =='category':
			self.chart.use(Axis(type=type, position=position,data=self.x_data))
		elif type =='time':
			self.chart.use(Axis(type=type, position=position,data=self.x_data))

	def y_axis(self,type='value', position='left',tick_name=''):
		"""
		设置直角坐标系 grid 中的 y 轴
		:param type:默认为种类
		:param position:y 轴的位置，可选：'left'，'right'
		:param tick_name:y 轴的单位
		:return:'value' 数值轴，适用于连续数据。
				'category' 类目轴，适用于离散的类目数据，为该类型时必须通过 data 设置类目数据。
				'time' 时间轴，适用于连续的时序数据，与数值轴相比时间轴带有时间的格式化，在刻度计算上也有所不同，
				例如会根据跨度的范围来决定使用月，星期，日还是小时范围的刻度。
		"""
		self.chart.use(Axis(type=type, position=position,
		               axisLabel={'formatter': '{value}'+tick_name},
		               ))

	def get_json(self):
		"""
		配置完所有参数后获取该图的配置Json
		:return: json数据，用于前端
		"""
		return self.chart.json


'''
 针对页面的get命令进行处理 获取前cnt列列名  包括id  但是前端页面不会显示id 处理信息用
 cnt:列的数量
 var：()元组格式 以 列的宽度，对齐格式 的顺序传进来
 '''
'''
该函数不用了  替换成fun_Get_Cmd_Trans
def get_cnt_column(cnt,*var):
    j_str = []  #最终返回的column列的所有参数，json格式
    width_list = var[0] #列的宽度 元组
    align_list = var[1] #列的对齐格式  元组
    model_name = var[2] #要获取注释信息的model对象
    var = base_fun_get_demo(model_name)   #获取该表中所有的列名及其对应的注释，注释即为最后要展示的列名
    #{'id': '索引号', 'name': '生产厂商名称', 'manager': '负责人名称', 'phone': '负责人联系电话', 'address': '生产厂商地址'}
    i = 0
    for key,value in var.items():
        if i != cnt:
            # 构建列的HTML命令
            # comment + head_pre ......
            j_str = json_frame_construct(j_str, key, value, width_list[i], align_list[i])
            # 每一次往j_str添加一列json数据
        i += 1

    return j_str
'''

#已经不用的函数