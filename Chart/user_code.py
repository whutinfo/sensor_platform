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
	temp = models.Temperature.objects.filter(time__range=(start_time, end_time)).order_by('time')
	x_list = []
	y_list = []
	for row in temp:
		# 时间从datetime格式转字符串，才能json序列化
		x_list.append(row.time.strftime("%Y-%m-%d %H:%M:%S"))
		if int(show_type) == 1:
			y_list.append(row.temperate)
		elif int(show_type) == 2:
			y_list.append(row.humidity)
		elif int(show_type) == 3:
			y_list.append(row.rainfall)

	return x_list,y_list


def fun_user_get_pie_data():
	"""
	用户自己编写的获取x,y数据的函数
	:param start_time: 搜索条件：开始时间
	:param end_time: 搜索条件：结束时间
	:return: x列表,y列表
	"""
	# 数据项的名称
	x_list = ['视频广告','联盟广告','邮件营销','直接访问','搜索引擎']

	# 数据项的值
	y_list = [235,274,225,465,356]

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

