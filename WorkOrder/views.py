from django.shortcuts import render
from django.shortcuts import HttpResponse
from Models import models
import json

'''创建工单'''
def edit(request):
	if request.method == 'GET':
		return render(request,'WorkOrder/edit.html')
	else:
		action = request.POST.get('action')
		user_id = request.session.get("Login_UserId")
		if action == 'LoadType':
			bases = models.Base.objects.values('type', 'title').distinct()#按照 type,title 组合去除重复的内容.
		#<QuerySet [{'type': 10, 'title': '玻璃报修'}, {'type': 11, 'title': '玻璃报修'}]>
			value_dict = {'type':'','title':''}
			value_list = []
			for base in bases: # base {'type': 10, 'title': '玻璃报修'}
				value_dict['type'] = base['type']
				value_dict['title'] = base['title']
				value_list.append(value_dict.copy())
				value_dict.clear()
			return HttpResponse(json.dumps(value_list))
		elif action =='LoadData':
			#看情况加载用户的工单还是当前类型的工单
			check_gdtype = request.POST.get('check_gdtype')   #没有选择工单类型，则返回0   否则返回的type值
			work_json = LoadWorkByUid(user_id,check_gdtype)
			return HttpResponse(json.dumps(work_json))

		elif action == 'Save':
			back = 0
			select_type = request.POST.get('select_type')
			position = request.POST.get('position')
			text = request.POST.get('text')
			models.Work.objects.create(type=select_type,step=1,flag=1,text=text,position=position,user_id=user_id)
			#新建工单时step为1，flag为1
			back = 1
			return HttpResponse(back)

'''审批工单'''
def approve(request):
	if request.method == 'GET':
		return render(request,'WorkOrder/approve.html')
	else:
		action = request.POST.get('action')
		user_id = request.session.get("Login_UserId")
		if action == 'LoadType':
			bases = models.Base.objects.values('type', 'title').distinct()  # 按照 type,title 组合去除重复的内容.
			# <QuerySet [{'type': 10, 'title': '玻璃报修'}, {'type': 11, 'title': '玻璃报修'}]>
			value_dict = {'type': '', 'title': ''}
			value_list = []
			for base in bases:  # base {'type': 10, 'title': '玻璃报修'}
				value_dict['type'] = base['type']
				value_dict['title'] = base['title']
				value_list.append(value_dict.copy())
				value_dict.clear()
			return HttpResponse(json.dumps(value_list))
		elif action == 'LoadData':
			# 看情况加载用户的工单还是当前类型的工单
			check_gdtype = request.POST.get('check_gdtype')  # 没有选择工单类型，则返回0   否则返回的type值
			approval_json = LoadApprovalByDR(user_id, check_gdtype)
			return HttpResponse(json.dumps(approval_json))
			'''更新审批意见及工单表信息及状态'''
		elif action == 'updateInfo':
			approve_flag = request.POST.get('approve')  #是否同意 1 同意 0 否决
			advise = request.POST.get('advise')
			work_id = request.POST.get('work_id')
			cur_step = request.POST.get('cur_step')

			back = update_WorkApprove(approve_flag,advise,work_id,user_id,cur_step)
			return HttpResponse(back)
			'''更新工单表状态'''
		elif action == 'updateFlag':
			back = 0
			work_id = request.POST.get('work_id')
			step = request.POST.get('step')
			performer_index = 'performer'+str(step)+'_id'
			field_dict={performer_index:user_id}
			#不能直接Update(performer_index=user_id)  列名不能是字符串
			models.Work.objects.filter(id=work_id).update(flag=2,**field_dict)
			# flag = 0 撤回  1 待审批  2 进行中  3 已结束
			back = 1
			return HttpResponse(back)

'''
如果gdtype为0  则加载该用户所有申请的工单
否则 按type分类加载
'''
def LoadWorkByUid(user_id,gdtype):
	value_dict = {'value1':'','value2':'','value3':'','value4':'','value5':'','value6':'','value7':'','value20':'','value8':'','value21':'','value9':'','value22':''}
	value_list =[]
	if gdtype != '0':
		works = models.Work.objects.filter(user_id=user_id,type=gdtype)

	else:
		works = models.Work.objects.filter(user=user_id)
	for work in works:
		base_title = models.Base.objects.values('type', 'title').distinct().get(type=work.type) #工单名称
		value_dict['title'] = base_title['title']
		value_dict['value1'] = work.type #工单类型
		value_dict['value2'] = work.text  # 工单内容
		value_dict['value3'] = work.position  # 地点
		value_dict['value4'] = work.flag  # 工单状态
		value_dict['value5'] = work.user.name  #通过外键获取名字
		value_dict['value6'] = work.create_time.strftime("%Y-%m-%d %H:%M:%S")  #创建时间
		performer1 = ''
		performer2 = ''
		performer3 = ''
		advise1 = ''
		advise2 = ''
		advise3 = ''
		if work.performer1!=None:#如果有审批人Id则查找
			performer1 = work.performer1.name
			# advise1 = models.Approval.objects.filter(work=work.id)
			if models.Approval.objects.filter(work_id=work.id, performer_id=work.performer1_id).count() != 0:
				advise1 = work.work_approval.get(performer_id=work.performer1_id,work=work.id).advise # 获取对应的approval表query_set

		if work.performer2 != None:
			performer2 = work.performer2.name
			if models.Approval.objects.filter(work_id=work.id, performer_id=work.performer2_id).count() != 0:
				advise2 = work.work_approval.get(performer_id=work.performer2_id,work=work.id).advise # 获取对应的approval表query_set

		if work.performer3 != None:
			performer3 = work.performer3.name
			if models.Approval.objects.filter(work_id=work.id, performer_id=work.performer3_id).count() != 0:
				advise3 = work.work_approval.get(performer_id=work.performer3_id,work=work.id).advise # 获取对应的approval表query_set

		value_dict['value7'] = performer1  # 审批人1
		value_dict['value8'] = performer2  # 审批人2
		value_dict['value9'] = performer3  # 审批人3
		value_dict['value20'] = advise1  # 审批人1意见
		value_dict['value21'] = advise2  # 审批人2意见
		value_dict['value22'] = advise3  # 审批人3意见

		value_list.append(value_dict.copy())
		value_dict.clear()
	return value_list


def LoadApprovalByDR(user_id,gdtype):
	role_id = models.Role.objects.get(user_role__user__user_id=user_id).role_id
	depart_id = models.Department.objects.get(depart_user__user__user_id=user_id).id
	value_dict = {'step':'','value_id':'','value1':'','value2':'','value3':'','value4':'','value5':'','value6':'','value7':'','value20':'','value8':'','value21':'','value9':'','value22':''}
	#value_dict = {'step': 'step', 'value_id': 'id', 'value1': 'type', 'value2': 'text', 'value3': 'position', 'value4': 'flag', 'value5': '',
	#              'value6': '', 'value7': '', 'value20': '', 'value8': '', 'value21': '', 'value9': '', 'value22': ''}
	value_list =[]
	if gdtype != '0':
		#查找当前部门角色下可以审批的所有工单基础表
		bases = models.Base.objects.filter(depart_id=depart_id,role_id=role_id,type=gdtype)

	else:
		bases = models.Base.objects.filter(depart_id=depart_id, role_id=role_id)
	#根据Node判断已有工单work中是否已经到当前步骤

	for base in bases:
		works = models.Work.objects.filter(type=base.type).values()
		for work in works:
			if base.node == work['step']:
				# 该工单可以被该部门角色下的用户审批，若当前审批人Id为空或者为当前登陆者id均可查看
				step = work['step']
				perfor_index = 'performer'+str(step)+'_id'
				if work[perfor_index] == None or work[perfor_index] == user_id:
					value_dict['step'] = work['step']
					value_dict['value_id'] = work['id']
					base_title = models.Base.objects.values('type', 'title').distinct().get(type=work['type'])  # 工单名称
					value_dict['title'] = base_title['title']
					value_dict['value1'] = work['type']  # 工单类型
					value_dict['value2'] = work['text']  # 工单内容
					value_dict['value3'] = work['position']  # 地点
					value_dict['value4'] = work['flag']  # 工单状态
					value_dict['value5'] = models.User.objects.get(user_id=work['user_id']).name  # 通过外键获取名字
					value_dict['value6'] = work['create_time'].strftime("%Y-%m-%d %H:%M:%S")  # 创建时间
					performer1 = ''
					performer2 = ''
					performer3 = ''
					advise1 = ''
					advise2 = ''
					advise3 = ''
					if work['performer1_id'] != None:  # 如果有审批人Id则查找
						performer1 = models.User.objects.get(user_id=work['performer1_id']).name
						if models.Approval.objects.filter(work_id=work['id'],performer_id=work['performer1_id']).exists() == True:
							advise1 = models.Approval.objects.get(work_id=work['id'],performer_id=work['performer1_id']).advise 	# 获取对应的approval表query_set

					if work['performer2_id'] != None:
						performer2 = models.User.objects.get(user_id=work['performer2_id']).name
						if models.Approval.objects.filter(work_id=work['id'], performer_id=work['performer2_id']).exists() == True:
							advise2 = models.Approval.objects.get(work_id=work['id'],performer_id=work['performer2_id']).advise  # 获取对应的approval表query_set

					if work['performer3_id'] != None:
						performer3 = models.User.objects.get(user_id=work['performer3_id']).name
						if models.Approval.objects.filter(work_id=work['id'],performer_id=work['performer3_id']).exists() == True:
							advise3 = models.Approval.objects.get(work_id=work['id'],performer_id=work['performer3_id']).advise   # 获取对应的approval表query_set

					value_dict['value7'] = performer1  # 审批人1
					value_dict['value8'] = performer2  # 审批人2
					value_dict['value9'] = performer3  # 审批人3
					value_dict['value20'] = advise1  # 审批人1意见
					value_dict['value21'] = advise2  # 审批人2意见
					value_dict['value22'] = advise3  # 审批人3意见

					value_list.append(value_dict.copy())
					value_dict.clear()
	return value_list

def update_WorkApprove(flag,advise,work_id,user_id,cur_step):
	back = 0
	work_flag = 0
	next_step = 0
	if flag == '0':#同意
		bases = models.Base.objects.all()
		work = models.Work.objects.filter(id=work_id).first()  # 找到所审批的工单
		for base in bases:

			if work.type == base.type and base.node == int(cur_step): #在标准表中找到这一类工单流转 在当前步骤时那条数据
				#没有问题查找value2，如果有问题查找value1
				if base.value2 == 255:#流程结束
					work_flag = 3 # 结束
				else:
					work_flag = 2  #进行中
				next_step = base.value2
	else: #被撤回
		work_flag = 0
		next_step = 255 #结束工单流转
	models.Work.objects.filter(id=work_id).update(flag=work_flag,step=next_step)
	#创建一条审批意见数据
	models.Approval.objects.create(advise=advise,step=cur_step,performer_id=user_id,work_id=work_id)
	back = 1
	return back