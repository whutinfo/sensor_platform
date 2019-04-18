from django.shortcuts import render
from django.shortcuts import HttpResponse
from Models import models
from Base.com_func import *
from SensorData.user_code import *
import json

def historydata(request):
	if request.method == 'GET':

		""" user variable begin"""
		# 这个tab的名称，前端已在后面补充  '折线图'  ，即tab_title+折线图
		tab_title = '传感器'

		# html 地址

		html_name = 'SensorData/historydata.html'

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






def currentdata(request):

	if request.method == 'GET':

		""" user variable begin"""
		# 这个tab的名称，前端已在后面补充  '折线图'  ，即tab_title+折线图
		tab_title = '传感器'

		# html 地址
		html_name = 'SensorData/currentdata.html'

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
			return HttpResponse(json.dumps(option))

		elif action == 'realData_option':

			"""sys variable begin"""

			x_list = []
			y_list = []
			option = ""

			"""sys variable end"""

			chart_type = request.POST.get('chart_type')
			show_data_type = request.POST.get('show_type')
			show_data_name = request.POST.get('show_name')
			cur_time = request.POST.get('cur_time')
			"""user varible begin"""

			# 图的标题
			title = show_data_name

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

			# 获取x,y列表，按x,y的顺序接收！
			x_list,y_list = fun_user_get_realData(cur_time,show_type = show_data_type)

			"""user code begin   """
			# 创建气温的一个图
			#   chart_type  1为折线，2为柱状，3为饼图
			option=fun_user_create_a_chart(chart_type, title=title, x_data=x_list, y_data=y_list,
				                        y_tick_name=y_tick_name, legend_name=legend_name)
			"""user code end   """

			print(option)
			return HttpResponse(json.dumps(option))

		elif action == 'update_realData':

			"""sys variable begin"""

			x_data = []
			y_data = []
			value_list = []
			value_dict = {'x_data':'',
			              'y_data':''}

			"""sys variable end"""
			show_data_type = request.POST.get('show_type')
			cur_time =  request.POST.get('cur_time')

			# 获取x,y实时数据的列表，按x,y的顺序接收！
			x_data,y_data = fun_user_get_realData(cur_time,show_num=5,show_type = show_data_type)

			value_dict['x_data'] = x_data
			value_dict['y_data'] = y_data
			value_list.append(value_dict)
			return HttpResponse(json.dumps(value_list))







