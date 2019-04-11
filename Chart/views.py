from django.shortcuts import render
from django.shortcuts import HttpResponse
from Models import models
from Base.com_func import *
from Chart.user_code import *
import json

"""
图表的模板
将折线图和柱状图放在一个页面中，用select进行选择
饼图单独有一个页面
1、记得导入模块！
from Base.com_func import *
from Chart.user_code import *

2、Chart下的user_code模块是编写自己的  图表  函数用的，
	x,y获取分了饼图和其他两个函数，可以自行修改或仿照再写
	fun_user_create_a_chart函数是通用的建一张图的函数，里面分了折线图，柱状图，饼图三种
"""

def show_line_or_bar(request):

	if request.method == 'GET':

		""" user variable begin"""
		# 这个tab的名称，前端已在后面补充  '折线图'  ，即tab_title+折线图
		tab_title = '气象'

		# html 地址
		html_name = 'Chart/line_or_bar.html'

		""" user variable end"""

		return render(request, html_name,{'title':tab_title})

	else:
		action = request.POST.get('action')

		if action == 'create_line_or_bar':

			"""sys variable begin"""

			error_flag = 0
			x_list = []
			y_list = []
			option = []

			"""sys variable end"""

			start_time = request.POST.get('start_time')
			end_time = request.POST.get('end_time')
			chart_type = request.POST.get('chart_type')
			show_data_type = request.POST.get('show_type')
			show_data_name = request.POST.get('show_name')

			"""user varible begin"""

			# 图的标题
			title = '从' + start_time + '到' + end_time + '的'+show_data_name

			# 折线含义，即图例内容，要画几条就列几个
			#  如 legend_name = '气温'
			legend_name = show_data_name

			# y的单位
			if int(show_data_type) == 1:
				y_tick_name = '℃'
			elif int(show_data_type) == 2:
				y_tick_name = '%'
			elif int(show_data_type) == 3:
				y_tick_name = '%'

			"""user varible end"""

			if end_time > start_time:
				# 获取x,y列表，按x,y的顺序接收！
				x_list,y_list = fun_user_get_data(start_time,end_time,show_type = show_data_type)

			else:
				# 开始时间大于结束时间，有问题，返回报错
				error_flag = 1

			if error_flag != 1:

				"""user code begin   """

				# 创建气温的一个图
				#   chart_type  1为折线，2为柱状，3为饼图
				option=fun_user_create_a_chart(chart_type, title=title, x_data=x_list, y_data=y_list,
					                        y_tick_name=y_tick_name, legend_name=legend_name)
				"""user code end   """

			else:
				#'结束时间选的开始时间早，请重新选择！'
				option = ''
			print(option)
			return HttpResponse(json.dumps(option))



def show_pie(request):

	if request.method == 'GET':

		""" user variable begin"""
		# 这个tab的名称，前端已在后面补充  '折线图'  ，即tab_title+折线图
		tab_title = '气象'

		# html 地址
		html_name = 'Chart/pie.html'

		""" user variable end"""

		return render(request, html_name,{'title':tab_title})

	else:
		action = request.POST.get('action')

		if action == 'create_pie':

			"""sys variable begin"""
			# 数据项的名称
			x_list = []
			# 数据项的值
			y_list = []
			option = []
			chart_type = 3  #  3为饼图

			"""sys variable end"""

			"""user varible begin"""

			# 图的标题
			title = '访问来源'

			"""user varible end"""


			# 获取x,y列表，按x,y的顺序接收！
			x_list,y_list = fun_user_get_pie_data()


			"""user code begin  函数可自己仿照写  """

			# 创建气温的一个图
			option=fun_user_create_a_chart(chart_type, title=title, x_data=x_list, y_data=y_list)

			"""user code end   """
			print(option)

			return HttpResponse(json.dumps(option))







