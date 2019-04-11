# -*- coding:utf-8 -*-
from Models import models
from Base.com_func import *


def fun_user_get_data(start_time,end_time,show_type=''):
	"""
	用户自己编写的获取x,y数据的函数
	:param start_time: 搜索条件：开始时间
	:param end_time: 搜索条件：结束时间
	:param show_type: 搜索条件：选择展示的数字是哪个
	:return: x列表,y列表
	"""

	temp = models.Sensor_data.objects.filter(create_time__range=(start_time, end_time)).order_by('create_time')

	x_list = []
	y_list = []
	for row in temp:

		x_list.append(row.create_time.strftime("%Y-%m-%d %H:%M:%S"))
		if int(show_type) == 1:
			y_list.append(row.type_1)
		elif int(show_type) == 2:
			y_list.append(row.type_2)
		elif int(show_type) == 3:
			y_list.append(row.type_3)
		elif int(show_type) == 4:
			y_list.append(row.type_4)
		elif int(show_type) == 5:
			y_list.append(row.type_5)
		elif int(show_type) == 6:
			y_list.append(row.type_6)
		elif int(show_type) == 7:
			y_list.append(row.type_7)
		elif int(show_type) == 8:
			y_list.append(row.type_8)
		elif int(show_type) == 9:
			y_list.append(row.type_9)
		elif int(show_type) == 10:
			y_list.append(row.type_10)
		elif int(show_type) == 11:
			y_list.append(row.type_11)
		elif int(show_type) == 12:
			y_list.append(row.type_12)
		elif int(show_type) == 13:
			y_list.append(row.type_13)
		elif int(show_type) == 14:
			y_list.append(row.type_14)
		elif int(show_type) == 15:
			y_list.append(row.type_15)
		elif int(show_type) == 16:
			y_list.append(row.type_16)
		elif int(show_type) == 17:
			y_list.append(row.type_17)
		elif int(show_type) == 18:
			y_list.append(row.type_18)
		elif int(show_type) == 19:
			y_list.append(row.type_19)
		elif int(show_type) == 20:
			y_list.append(row.type_20)
		elif int(show_type) == 21:
			y_list.append(row.type_21)
		elif int(show_type) == 22:
			y_list.append(row.type_22)
		elif int(show_type) == 23:
			y_list.append(row.type_23)
		elif int(show_type) == 24:
			y_list.append(row.type_24)
		elif int(show_type) == 25:
			y_list.append(row.type_25)
	return x_list,y_list


def fun_user_create_a_chart(chart_type,title='',x_data=[],y_data=[],y_tick_name='',legend_name=''):

	option = []

	# 在一张图上！ 可以画两条折线
	# 可改参数 description=''  若需要子标题，描述性文字，可在上面 User varible 中添加该变量
	figure = new_a_chart(chart_type,title=title)

	# 强制性转int ，防止参数进来可能是int,可能是str的错误，兼容
	if int(chart_type) == 1:
		# 创建气温的一个折线图
		# 初始化x,y轴刻度，初始化图例列表，即完成series键值对
		figure.line(x_data=x_data, y_data=y_data, label=legend_name)

		# 图例位置  默认(x:'center',y: 'top') 以元组形式
		legend_position = ('right', 'top')

		# 创建图例  默认 (x:'center',y: 'top') 以元组形式
		figure.Set_Legend(position=legend_position)

		# x轴刻度,x 轴的位置，可选：'top'，'bottom'	，用的默认bottom
		figure.x_axis()

		# y轴的位置，可选：'left'，'right', 用的默认left   单位tick_name
		figure.y_axis(tick_name=y_tick_name)

	elif int(chart_type) == 2:
		# 创建气温的一个柱状图
		figure.bar(x_data=x_data, y_data=y_data, label=legend_name)

		# 图例位置  默认(x:'center',y: 'top') 以元组形式
		legend_position = ('right', 'top')

		# 创建图例  默认 (x:'center',y: 'top') 以元组形式
		figure.Set_Legend(position=legend_position)

		# x轴刻度,x 轴的位置，可选：'top'，'bottom'	，用的默认bottom
		figure.x_axis()

		# y轴的位置，可选：'left'，'right', 用的默认left   单位tick_name
		figure.y_axis(tick_name=y_tick_name)

	elif int(chart_type) == 3:
		# 创建饼图
		figure.pie(x_data=x_data, y_data=y_data)

		# 图例位置  默认(x:'center',y: 'top') 以元组形式
		legend_position = ('right', 'top')

		# 创建图例  默认 (x:'center',y: 'top') 以元组形式
		figure.Set_Legend(position=legend_position)


	# 获取Json格式，其实是字典格式，以下变成json格式再转字符串，前端才能用
	datajson = figure.get_json()

	option.append({'option': datajson})

	return option



