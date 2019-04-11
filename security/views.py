from django.shortcuts import render
from django.shortcuts import HttpResponse
from Models import models
import json

def userControl(request):
	action = request.POST.get('action')
	if request.method == 'GET':
		return render(request, 'security/user.html')  ##用render，从第二个参数中找
	else:
		user_id = request.session.get("Login_UserId")
		'''
		用户和用户组通常是定义客户内职位、职务等关系的，是面向客户内部职务级别关系的一个分类，是给客户看到的。
		而角色通常是用来定义各个模块功能的使用权限的，是后台的一个权限区分关系。
例如：客户单位内的一个部门里面用户可能都是“员工”，但角色可能不同，可能有“管理员”“XX（模块）工程师”“XX管理员”等。
同理，一个角色可能在不同部门里都有，如最常见的“XX管理员”、“考勤员”等。
按这种思路的话，职位最好 不等同于 角色     还有不同部门同一角色会拥有同一组权限的问题
	！！  目前先暂且将 角色 以职位划分，不考虑不同部门同一角色权限一样的问题。
		'''
		if action == 'LoadData':
			index = {'index': 1}
			if user_id == 2:#超级管理员获取所有
				# values={'id':,'trueid':,'nature_id':,'name':'',
				#         'own_departid':,'own_departname':'','own_roleid':,'own_rolename':'','create_time':'',
				#         'update_time': '','state':'','children':'',}
				values={}
				tree=[{'id':0,'trueid':0,'nature_id':0,'name':'所有部门',	'own_departid':0,'own_departname':'',
				       'own_roleid':0,'own_rolename':'', 'create_time': '', 'update_time': '','state':'open','children':''}]  #索引标题
				value = []

				#根据用户id，获取部门树
				#1、根据user_id查出其所在部门的id,name,node
				departs = models.Department.objects.all()
				for depart in departs:
					if len(depart.node) == 4:

						values['id'] = index['index']
						values['trueid'] = depart.id  # 真实id
						values['nature_id'] = 1  # 用来划分是索引节点，还是部门，还是角色，还是用户
						values['name'] = depart.name
						values['own_departid'] = 0
						values['own_departname'] = ''
						values['own_roleid'] = 0
						values['own_rolename'] = ''
						# values['create_time'] = depart.create_time
						# values['update_time'] = depart.update_time
						values['state'] = 'closed'
						# 在所有部门中找到用户所在部门的所有子部门
						# select * from Department_Table where node like '%1000'用模糊查询
						ztrees = models.Department.objects.filter(node__startswith=depart.node)
						children2 = GetSubRoleUserTreeGrid(depart.id, depart.name, index)  # 先获取其下所有角色和角色下的用户
						children1 = GetDepart_SubTree(depart, ztrees, index)  # 再获取子部门    因为index索引

						index['index'] += 1
						if children1 != [] and children2 != []:  # 若有子部门就加载子部门
							'''子部门暂时先不做这种数据，树形表格显示形式不太好，一级部门下面会显示一级部门的角色，同时还有二级部门'''
							values['children'] = children2 + children1
						elif children1 != []:
							# 否则获取子部门
							values['children'] = children1
						elif children2 != []:
							# 否则获取角色信息
							values['children'] = children2
						value.append(values.copy())
						values.clear()  # 防止上次保存的结果干扰下一次的值，比如下一次没有这个键值，而上一次却有，就会保存上一次

			else:
				values = {}
				tree = [{'id': 0, 'trueid': 0, 'nature_id': 0, 'name': '所在所有部门', 'own_departid': 0, 'own_departname': '',
				         'own_roleid': 0, 'own_rolename': '', 'create_time': '', 'update_time': '', 'state': 'open',
				         'children': ''}]  # 索引标题
				value = []
				# 根据用户id，获取部门树
				# 1、根据user_id查出其所在部门的id,name,node
				departs = models.Department.objects.filter(users__user_id=user_id)
				for depart in departs: #所有顶级节点即用户所在部门
					values['id'] = index['index']
					values['trueid'] = depart.id  #真实id
					values['nature_id'] = 1  #用来划分是索引节点，还是部门，还是角色，还是用户
					values['name'] = depart.name
					values['own_departid'] = 0
					values['own_departname'] = ''
					values['own_roleid'] = 0
					values['own_rolename'] = ''
					#values['create_time'] = depart.create_time
					#values['update_time'] = depart.update_time
					values['state'] = 'closed'
					# 在所有部门中找到用户所在部门的所有子部门
					#select * from Department_Table where node like '%1000'用模糊查询
					ztrees = models.Department.objects.filter(node__startswith=depart.node)
					children2 = GetSubRoleUserTreeGrid(depart.id, depart.name, index) #先获取其下所有角色和角色下的用户
					children1 = GetDepart_SubTree(depart, ztrees, index) #再获取子部门    因为index索引

					index['index'] += 1
					if children1 != [] and children2 != []:#若有子部门就加载子部门
						'''子部门暂时先不做这种数据，树形表格显示形式不太好，一级部门下面会显示一级部门的角色，同时还有二级部门'''
						values['children'] = children2+children1
					elif children2 != []:
						# 否则获取角色信息
						values['children'] = children2
					value.append(values.copy())
					values.clear()  # 防止上次保存的结果干扰下一次的值，比如下一次没有这个键值，而上一次却有，就会保存上一次
			tree[0]['children'] = value
			return HttpResponse(json.dumps(tree))
		elif action == 'LoadToolBar':

			value = []
			if user_id == 2:#只有管理员才能增删改查
				values=	[{'text':'刷新','iconCls':'icon-reload','handler': 'function () {fresh()}'},'-',{'text':'增加','iconCls':'icon-add','handler': 'function () {add()}'},'-',
						 {'text':'编辑','iconCls':'icon-edit','handler': 'function () {edit()}'},'-',	{'text':'删除','iconCls':'icon-remove','handler': 'function () {delte()}'}]

				value.append("{text:'" + "刷新" + "'," + "iconCls:'icon-reload'," + "handler: function () {" + "fresh()" + "}" + "}")
				value.append('-')
				value.append("{text:'" + '增加' + "'," + "iconCls:'icon-add'," + "handler: function () {" + "add()" + "}" + "}")
				value.append('-')
				value.append("{text:'" + '编辑' + "'," + "iconCls:'icon-edit'," + "handler: function () {" + "edit()" + "}" + "}")
				value.append('-')
				value.append("{text:'" + '删除' + "'," + "iconCls:'icon-remove'," + "handler: function () {" + "delte()" + "}" + "}")
				'''	
				[{text:'刷新',iconCls:'icon-reload',handler: function () {fresh()}},	'-',
				{text:'增加',iconCls:'icon-add',handler: function () {add()}},'-',
				{text:'编辑',iconCls:'icon-edit',handler: function () {edit()}},'-',
				{text:'删除',iconCls:'icon-remove',handler: function () {delte()}}]
				'''
			return HttpResponse(json.dumps(value))

			'''
			用户权限
			'''
		elif action == 'LoadAccess':
			value_list = []
			value_dict = {}
			accesses = models.Access.objects.all()
			for access in accesses:
				value_dict['id'] = access.id
				value_dict['name'] = access.access_name
				value_list.append(value_dict.copy())
				value_dict.clear()
			return HttpResponse(json.dumps(value_list))
		elif action == 'LoadUserPermis':
			trueid = request.POST.get('trueid')
			value_list = []
			value_dict = {'user_id':'','menu_id':'','menu_name':'','access_str':'','access_name':''}
			'''	access_name:"浏览,添加,编辑,删除"	   access_str:	"1,2,3,4"	 menu_id:20 	menu_name:	"审批工单"	type:null	user_name:	"4"	'''
			menus = models.Menu.objects.all().order_by('menu_node') #获取所有菜单
			upers = models.User_Menu.objects.filter(user_id=trueid)  #获取所选用户的权限access

			for menu in menus:
				value_dict['user_id'] = trueid
				value_dict['menu_id'] = menu.menu_id
				value_dict['menu_name'] = menu.menu_name
				value_dict['access_str'] = ''
				value_dict['access_name'] = ''
				for uper in upers: #遍历该用户所有权限，如果有当前菜单的权限，则写入access_str,
					access_name = ''
					if uper.menu_id == menu.menu_id:
						value_dict['access_str'] = uper.access_str  #根据该索引找到对应的access_name
						if uper.access_str != '': #如果有权限access_str，再找其名称
							access_id = uper.access_str.split(',')  #['1','2','3']
							i = 0
							for id in access_id:
								access = models.Access.objects.filter(id = id).first() #根据id只会获取一条
								name = access.access_name
								if i == 0:
									access_name = access_name + name
								else:
									access_name = access_name + ',' + name
								i = i + 1
						value_dict['access_name'] = access_name
				value_list.append(value_dict.copy())
			return HttpResponse(json.dumps(value_list)	)

			'''保存修改的用户权限'''
		elif action == 'EditUserPermis':
			rowsString = request.POST.get('rowsString')
			trueid_str = request.POST.get('trueid')
			trueid = int(trueid_str)
			'''		
			1、遍历整个rows将所有的access_name转成新的access_str
			遍历该用户所有权限，如果有当前菜单menu_id的权限，将对应的access_str更新，若access_str=''，则对该菜单没有访问权限，删除该条数据
			对不在用户所有权限的rows，对user_menu新增相应数据
			'''
			rows = json.loads(rowsString)  #json.loads(字符串)=>字典/对象
			pers =  models.User_Menu.objects.all()
			for row in rows:  # rows 是 list [{'user_id':'','menu_id':'','menu_name':'','access_str':'','access_name':''},{},{}...]  row 是 dict  {'user_id':'','menu_id':'','menu_name':'','access_str':'','access_name':''}
				access_name = row['access_name']
				access_str = ''
				if access_name != '':  #有数据再切割
					names = access_name.split(',')    #<class 'list'>: ['浏览', '添加', '编辑', '删除', '查询', '打印', '预览', '导出']
					i =0
					for name in names:
						id = models.Access.objects.filter(access_name=name).values('id').first()
						if i == 0:
							access_str = access_str + str(id['id'])
						else:
							access_str = access_str + ',' + str(id['id'])
						#获取当前菜单的权限access_name对应的id
						i += 1
				ishave = 0 #在遍历row下一个菜单时清零
				for per in pers: #在当前menu_id下遍历用户的权限，若有
					if per.menu_id == row['menu_id']:
						#有当前菜单menu_id的权限，将对应的access_str更新
						ishave = 1

				if ishave == 1:
					update_Uper(trueid, row['menu_id'], access_str)
				elif access_str != '':
					#若本身没有该菜单权限，那么access_str不为空时需新增
					update_Uper(trueid, row['menu_id'], access_str)
			return HttpResponse('1')
			"""添加部门   """
		elif action == 'AddDepartment':
			trueid_str = request.POST.get('trueid')
			trueid = int(trueid_str)
			d_name = request.POST.get('d_name')
			# 如果不是新顶级部门，那么获取的是已有部门的id
			# 根据父节点node，根据Len=len(node)+4，模糊查询子节点，倒序
			#最多只做两级部门，写死了先
			flag = 0
			if trueid != 0:
				depart = models.Department.objects.filter(id = trueid).first()
				parent_node = depart.node
				if len(parent_node)==4:
					zdeparts = models.Department.objects.filter(node__startswith=parent_node).order_by('-node') #所有子部门按倒序排列，选第一个，对其Node+1
					if zdeparts.count() >= 1:  # 最开始不存在
						checknode = '1000'  # 初始节点\
					else:
						checknode = str( int(zdeparts.node)+1 )
					insert_node = parent_node + checknode
					models.Department.objects.create(name=d_name,node=insert_node)
					flag = 1 #顶级部门下添加
				else: #子部门下添加 ，不允许
					flag = 2
			else:#在顶级索引下添加的是顶级部门
				checknode = '1000'
				departs = models.Department.objects.all().order_by('-node')
				if departs.exists()!=True:#最开始不存在
					checknode = '1000'#初始节点
				else:
					for depart in departs:
						if len(depart.node) == 4:
							checknode = str( int(depart.node)+1 )
							break
				models.Department.objects.create(name=d_name,node=checknode)
				flag = 1
			return HttpResponse(flag)
		elif action == 'DeleteDepartment': #直接删除掉该部门  所以对应关系也要删除
			depart_id = request.POST.get('trueid')
			#删除该部门，删除部门角色，部门用户关系
			models.Department.objects.filter(id=depart_id).delete()
			models.Depart_Role.objects.filter(depart_id=depart_id).delete()
			models.Depart_User.objects.filter(depart_id=depart_id).delete()
			return HttpResponse(1)

			'''角色添加'''
		#获取所有角色
		elif action == 'GetRoles':
			trueid_str = request.POST.get('trueid')
			trueid = int(trueid_str)
			value_list = []
			value_dict = {'id':'','text':''}
			#获取该部门下有的角色
			depart_role = models.Role.objects.filter(depart_role__depart_id=trueid)
			#获取所有的角色
			all_role = models.Role.objects.all()
			for row in all_role:
				ishave = 0
				for role in depart_role:#遍历该部门的所有角色，找是否存在当前row的，如果有，则flag=1
					if role.role_id == row.role_id:
						ishave = 1
				#得到该部门下所没有的角色给前端下拉框
				if ishave == 0: #不存在，就存储数据
					value_dict['id'] =row.role_id
					value_dict['text'] = row.name
					value_list.append(value_dict.copy())
					value_dict.clear()
			return HttpResponse(json.dumps(value_list))
		#添加角色
		elif action == 'AddRole':
			trueid_str = request.POST.get('trueid')
			trueid = int(trueid_str)
			jsonString = request.POST.get('roleids')  #前端JSON.stringify(字典/对象)=>字符串   现在需json.loads(字符串)=>字典/对象
			#如果直接输入角色  获取的是["角色XX"]	现在禁止输入只可下拉		#如果是选择下拉框  获取的是角色id  ['3','4']
			role_ids = json.loads(jsonString)
			depart_roles = models.Depart_Role.objects.filter(depart_id=trueid)
			# 遍历role_ids
			back = 0
			value = []
			for role_id in role_ids:
				ishave = 0
			# 在depart_role中找到当前部门对应的所有角色  如果在遍历发现有与role_id相等的，则表示已存在该角色。返回2
				for depart_role in depart_roles:
					if depart_role.role_id == role_id:
						ishave = 1
				if ishave == 1:
					back = 2 #已存在
				else:
					# 如果没有role_id相同，则新增该对应关系 返回1
					# 添加失败 返回0
					models.Depart_Role.objects.create(depart_id=trueid,role_id=role_id)
					back = 1
				#根据role_id获取角色名，返回alert提示用
				role = models.Role.objects.filter(role_id=role_id).first()
				value.append(back)
				value.append(role.name) #<class 'list'>: [1, '副科长']
			return HttpResponse(json.dumps(value))
		elif action == 'DeleteRole':  #只是删除了部门角色对应关系，该角色仍存在
			role_id = request.POST.get('trueid')
			depart_id = request.POST.get('parent_id')
			models.Depart_Role.objects.filter(role_id=role_id, depart_id=depart_id).delete()
			return HttpResponse(1)

			"""添加新用户"""
		elif action == 'AddUser1':
			depart_id = request.POST.get('parent_id')  #depart_id
			role_id = request.POST.get('trueid')     #role_id
			user_name = request.POST.get('user_name')
			user_pwd = request.POST.get('user_pwd')
			back = 0
			#在用户user表添加该用户
			user = models.User.objects.create(name=user_name,pwd=user_pwd)  #生成一个User对象
			if user.DoesNotExist != True:
				user_id = user.user_id
				#在user_role添加关系
				models.User_Role.objects.create(user_id=user_id,role_id=role_id)
				#在depart_user添加关系
				models.Depart_User.objects.create(user_id=user_id,depart_id=depart_id)
				back = 1
			return HttpResponse(back)
			"""加载已有用户"""
		elif action == 'LoadToolBarSlec1':
			pass
		elif action == 'LoadToolBarSlec2':
			pass
		elif action == 'LoadUsers':
			value_list = []
			value_dict = {'user_id':'','name':'','create_time':'','create_uname':''}
			#加载所有用户
			users = models.User.objects.all()
			for user in users:
				value_dict['user_id'] = user.user_id  #虽然不显示在页面上，但是这些数据后面可以从前端返回过来
				value_dict['name'] = user.name
				value_dict['create_time'] = user.create_time.strftime("%Y-%m-%d %H:%M:%S")
				#user.create_time  :  'create_time': datetime.datetime(2018, 12, 31, 8, 15, 21, 944169)
				#strftime 将格式转成转成字符串样式  'create_time': '2018-12-31 08:15：21'
				value_list.append(value_dict.copy())
				value_dict.clear()
			return HttpResponse(json.dumps(value_list))
			"""在已有用户选项卡中保存"""
		elif action == 'AddUser2':
			depart_id = request.POST.get('parent_id')  #depart_id
			role_id = request.POST.get('trueid')     #role_id
			users = json.loads(request.POST.get('users'))
			#<class 'list'>: [{'name': '小红销售', 'create_time': '2019-01-10 14:06:01'}]
			back = 0
			value = []
			for user in users:
				user_id = user['user_id']
				#在user_role添加关系
				models.User_Role.objects.create(user_id=user_id,role_id=role_id)
				#在depart_user添加关系
				models.Depart_User.objects.create(user_id=user_id,depart_id=depart_id)
				back = 1
				#获取用户名 用于前端alert提示
				name = user['name']
				value.append(name)
				value.append(back)
			return HttpResponse(json.dumps(value))
		elif action == "DeleteUser":#只是删除了部门用户，角色用户对应关系，该用户仍存在
			role_id = request.POST.get('parent_id')  # depart_id
			depart_id = request.POST.get('paparent_id')  # role_id
			user_id = json.loads(request.POST.get('trueid'))
			back = 0
			#在UserRole中删除对应关系
			models.User_Role.objects.filter(role_id=role_id,user_id=user_id).delete()
			#在depart_user中删除对应关系
			''' 现在问题是  如果一个用户有多种角色，如果他所属的某一个部门下有多个他所属的角色 删除时该不该删部门用户关系'''
			trees = json.loads(request.POST.get('trees')) #dict
			#{'id': 5, 'trueid': 2, 'nature_id': 1, 'name': '业务部下的销售部', 'own_departid': 0, 'own_departname': '', 'own_roleid': 0, 'own_rolename': '', 'state': 'open',
			# 'children': [{'id': 6, 'trueid': 3, 'nature_id': 2, 'name': '销售人员', 'own_departid': 2, 'own_departname': '业务部下的销售部', 'own_roleid': 0, 'own_rolename': '', 'state': 'closed', 'children': [{'id': 7, 'trueid': 3, 'nature_id': 3, 'name': '小红销售', 'own_departid': 2, 'own_departname': '业务部下的销售部', 'own_roleid': 3, 'own_rolename': '销售人员', '_parentId': 6, 'state': 'open'}], '_parentId': 5}}], '_parentId': 1}
			count = {'count':0}
			user_num = check_user(user_id, trees,count)  # 如果该部门下获取的用户id相等的多于1个，那么意味着该部门下不止有一个他所属的角色，还不能删除对应关系
			if user_num['count']<=1:
				models.Depart_User.objects.filter(depart_id=depart_id,user_id=user_id).delete()
			back = 1
			return HttpResponse(back)



def roleControl(request):
	action = request.POST.get('action')
	if request.method == 'GET':
		return render(request, 'security/role.html')  ##用render，从第二个参数中找
	else:
		if action == 'LoadData':
			roles = models.Role.objects.all()
			value_dict={'name':'','d_describe':''}
			value_list = []
			for role in roles:
				value_dict['role_id'] = role.role_id
				value_dict['name'] = role.name
				value_dict['d_describe'] = role.describe
				value_list.append(value_dict.copy())
				value_dict.clear()
			return HttpResponse(json.dumps(value_list))
		elif action =='addRole':
			name = request.POST.get('role_name')
			describe = request.POST.get('role_describe')
			models.Role.objects.create(name=name,describe = describe)   #目前没加节点
			return HttpResponse(1)
			'''修改权限'''
		elif action == 'LoadAccess':
			value_list = []
			value_dict = {}
			accesses = models.Access.objects.all()
			for access in accesses:
				value_dict['id'] = access.id
				value_dict['name'] = access.access_name
				value_list.append(value_dict.copy())
				value_dict.clear()
			return HttpResponse(json.dumps(value_list))
		elif action == 'getRolePermis':
			role_id = request.POST.get('role_id')
			value_list = []
			value_dict = {'role_id':'','menu_id':'','menu_name':'','access_str':'','access_name':''}
			'''	access_name:"浏览,添加,编辑,删除"	   access_str:	"1,2,3,4"	 menu_id:20 	menu_name:	"审批工单"	type:null	user_name:	"4"	'''
			menus = models.Menu.objects.all().order_by('menu_node') #获取所有菜单
			upers = models.Role_Menu.objects.filter(role_id=role_id)  #获取所选角色的权限access

			for menu in menus:
				value_dict['role_id'] = role_id
				value_dict['menu_id'] = menu.menu_id
				value_dict['menu_name'] = menu.menu_name
				value_dict['access_str'] = ''
				value_dict['access_name'] = ''
				for uper in upers: #遍历该角色所有权限，如果有当前菜单的权限，则写入access_str,
					access_name = ''
					if uper.menu_id == menu.menu_id:
						value_dict['access_str'] = uper.access_str  #根据该索引找到对应的access_name
						if uper.access_str != '': #如果有权限access_str，再找其名称
							access_id = uper.access_str.split(',')  #['1','2','3']
							i = 0
							for id in access_id:
								access = models.Access.objects.filter(id = id).first() #根据id只会获取一条
								name = access.access_name
								if i == 0:
									access_name = access_name + name
								else:
									access_name = access_name + ',' + name
								i = i + 1
						value_dict['access_name'] = access_name
				value_list.append(value_dict.copy())
			return HttpResponse(json.dumps(value_list)	)

			'''保存修改的用户权限'''
		elif action == 'EditRolePermis':
			datagrid = request.POST.get('datagrid')
			role_id = int(request.POST.get('role_id'))

			'''		
			1、遍历整个rows将所有的access_name转成新的access_str
			遍历该角色所有权限，如果有当前菜单menu_id的权限，将对应的access_str更新，若access_str=''，则对该菜单没有访问权限，删除该条数据
			对不在角色所有权限的rows，对user_menu新增相应数据
			'''
			rows = json.loads(datagrid)  #json.loads(字符串)=>字典/对象
			pers =  models.Role_Menu.objects.all()
			for row in rows:  # rows 是 list [{'user_id':'','menu_id':'','menu_name':'','access_str':'','access_name':''},{},{}...]  row 是 dict  {'user_id':'','menu_id':'','menu_name':'','access_str':'','access_name':''}
				access_name = row['access_name']
				access_str = ''
				if access_name != '':  #有数据再切割
					names = access_name.split(',')    #<class 'list'>: ['浏览', '添加', '编辑', '删除', '查询', '打印', '预览', '导出']
					i =0
					for name in names:
						id = models.Access.objects.filter(access_name=name).values('id').first()
						if i == 0:
							access_str = access_str + str(id['id'])
						else:
							access_str = access_str + ',' + str(id['id'])
						#获取当前菜单的权限access_name对应的id
						i += 1
				ishave = 0 #在遍历row下一个菜单时清零
				for per in pers: #在当前menu_id下遍历用户的权限，若有
					if per.menu_id == row['menu_id']:
						#有当前菜单menu_id的权限，将对应的access_str更新
						ishave = 1

				if ishave == 1:
					update_Rper(role_id, row['menu_id'], access_str)
				elif access_str != '':
					#若本身没有该菜单权限，那么access_str不为空时需新增
					update_Rper(role_id, row['menu_id'], access_str)
			return HttpResponse('1')
			'''编辑角色'''
		elif action == 'editRole':
			name = request.POST.get('role_name')
			describe = request.POST.get('role_describe')
			role_id = int(request.POST.get('role_id'))
			models.Role.objects.filter(role_id=role_id).update(describe=describe,name=name)
			return HttpResponse(1)

def menuControl(request):
	action = request.POST.get('action')
	if request.method == 'GET':
		return render(request, 'security/menu.html')  ##用render，从第二个参数中找
	else:
		if action == 'LoadTree':
			menus=models.Menu.objects.all().order_by('menu_node')
			rankMenu=[]
			#values={'id':'','text':'','state':'','children':''}
			values={}
			for row in menus:
				if(len(row.menu_node)==4):
					values['id']=row.menu_id
					values['text']=row.menu_name
					Ztree = getZtree(row,menus)
					values['state'] = 'closed' #有这个显示样式就一定会是可以展开的样式，尽管没有childern也会是这样
					if Ztree != []:
						values['children']=Ztree#row是一个Menu对象，menus是qs
					rankMenu.append(values.copy())
					values.clear()  # 防止上次保存的结果干扰下一次的值，比如下一次没有这个键值，而上一次却有，就会保存上一次
			return HttpResponse(json.dumps(rankMenu))
		elif action == 'LoadMenu':
			menu_id = request.POST.get('menu_id')
			value ={'id':'','name':'','describe':'','url':'','img':'','show':'','node':''}
			list = []
			if menu_id == '0': #加载所有Menu
				menus = models.Menu.objects.all()
			else:
				menus = models.Menu.objects.filter(menu_id=menu_id)
			for menu in menus:
				value['id']=menu.menu_id
				value['name'] = menu.menu_name
				value['describe'] = menu.menu_describe
				value['url']=menu.menu_url
				value['img'] = menu.menu_img
				value['show'] = menu.menu_show
				value['node'] = menu.menu_node
				list.append(value.copy())
				value.clear()  # 防止上次保存的结果干扰下一次的值，比如下一次没有这个键值，而上一次却有，就会保存上一次
			return HttpResponse(json.dumps(list))
		elif action == 'LoadSelectMenu':#新增菜单时初始化下拉选项框，获取所有顶级菜单
			value = {'id': '', 'name': '', 'describe': '', 'url': '', 'img': '', 'show': '', 'node': ''}
			list = []
			#menus = models.Menu.objects.filter(menu_node=4).order_by('menu_node')
			menus=models.Menu.objects.all().order_by('menu_node')
			for menu in menus:
				if len(menu.menu_node)==4:
					value['id'] = menu.menu_id
					value['name'] = menu.menu_name
					value['describe'] = menu.menu_describe
					value['url'] = menu.menu_url
					value['img'] = menu.menu_img
					value['show'] = menu.menu_show
					value['node'] = menu.menu_node
					list.append(value.copy())
					value.clear()  # 防止上次保存的结果干扰下一次的值，比如下一次没有这个键值，而上一次却有，就会保存上一次
			return HttpResponse(json.dumps(list))
		elif action == 'addMenu':
			back = 0
			menu_name=request.POST.get('menu_name')
			pmenu_id=request.POST.get('pmenu_id')
			menu_url=request.POST.get('menu_url')
			menu_show=request.POST.get('menu_show')
			menu_img = request.POST.get('menu_img')
			menu_describe = request.POST.get('menu_describe')
			addmaxchild = '1000'
			if pmenu_id != '0':
			# 如果不是新父菜单，那么获取的是已有菜单的id
			# 根据父节点node，和Maxchild ，将maxchild+1，与父节点node拼接即当前新增菜单的节点
			# 而新增菜单的maxchild为初始值addmaxchild即1000

				pmenu=models.Menu.objects.filter(menu_id=pmenu_id).first()#一个Menu对象
				pmenu_node=pmenu.menu_node
				maxchild=pmenu.maxchild
				checknode = str(int(maxchild)+1)
				insertnode = pmenu_node + checknode

				# 创建一行新建菜单的数据
				models.Menu.objects.create(menu_name=menu_name,menu_describe=menu_describe,menu_url=menu_url,menu_show=menu_show,menu_img=menu_img,menu_node=insertnode,maxchild=addmaxchild)
				#更新其父菜单的maxchild
				models.Menu.objects.filter(menu_id=pmenu_id).update(maxchild=checknode)  #根据id最快，而且id是唯一的，也是Int
				back = 1
			else:  # 此时增加新父节点
				newnode = "1000"  # 父节点初始值
				menus = models.Menu.objects.all().order_by('-menu_node')
				for menu in menus:
					if len(menu.menu_node) == 4:
						newnode = int(menu.menu_node) + 1
						break
				models.Menu.objects.create(menu_name=menu_name, menu_describe=menu_describe, menu_url=menu_url,
				                           menu_show=menu_show, menu_img=menu_img, menu_node=newnode,maxchild=addmaxchild)
				back = 1

			return HttpResponse(back)
		elif action == 'editMenu':#编辑
			back = 0
			menu_name = request.POST.get('menu_name')
			menu_id = request.POST.get('menu_id')
			menu_url = request.POST.get('menu_url')
			menu_show = request.POST.get('menu_show')
			menu_img = request.POST.get('menu_img')
			menu_describe = request.POST.get('menu_describe')
			models.Menu.objects.filter(menu_id=menu_id).update(menu_name=menu_name,menu_url=menu_url,menu_show=menu_show,menu_img=menu_img,menu_describe=menu_describe)
			back = 1
			return HttpResponse(back)

'''
#在menus中找到pmenu的所有子节点
pmenu是对象，menus是qs
'''
def getZtree(pmenu,menus):
	#values = {'id': '', 'text': '', 'state': '', 'children': ''}
	values={}
	value=[]
	for menu in menus:
		if len(menu.menu_node) == len(pmenu.menu_node) + 4 and pmenu.menu_node == menu.menu_node[0:len(pmenu.menu_node)]:
			values['id'] = menu.menu_id
			values['text'] = menu.menu_name
			if getZtree(menu,menus) != []: #如果没有子节点返回[]
				values['state'] = 'closed'
				values['children'] = getZtree(menu, menus)
			value.append(values.copy())
			values.clear()#防止上次保存的结果干扰下一次的值，比如下一次没有这个键值，而上一次却有，就会保存上一次
	return value

"""
获取部门子节点，即下一级部门
depart是department对象，ztrees是qs，所有子节点包括父节点自己
"""
def GetDepart_SubTree(depart,ztrees,index):
	values = {}
	value = []
	for sub in ztrees:
		#节点更长的即为子节点
		if len(depart.node)<len(sub.node):
			index['index'] += 1
			values['id'] =  index['index']
			values['trueid'] = sub.id
			values['nature_id'] = 1
			values['name'] = sub.name
			values['own_departid'] = 0
			values['own_departname'] = ''
			values['own_roleid'] = 0
			values['own_rolename'] = ''
			#values['create_time'] = sub.create_time
			#values['update_time'] = sub.update_time
			values['state'] = 'closed'
			children = GetDepart_SubTree(sub,ztrees,index)
			if children !=[]:
				values['children'] = children
			else:#没有下级部门，找角色信息
				children = GetSubRoleUserTreeGrid(sub.id, sub.name, index)
				if children != []:
					#values['state'] = 'closed'
					values['children'] = children
			value.append(values.copy())
			values.clear()#防止上次保存的结果干扰下一次的值，比如下一次没有这个键值，而上一次却有，就会保存上一次
	return value

"""
根据depart_id	获取部门的角色的role_id	name  node
"""
def GetSubRoleUserTreeGrid(depart_id,depart_name,index):
	roles = models.Role.objects.filter(depart_role__depart_id=depart_id)
	values = {}
	value = []
	for role in roles:
		index['index'] += 1
		values['id'] =  index['index']
		values['trueid'] = role.role_id
		values['nature_id'] = 2
		values['name'] = role.name
		values['own_departid'] = depart_id
		values['own_departname'] = depart_name
		values['own_roleid'] = 0
		values['own_rolename'] = ''
		#values['create_time'] = sub.create_time
		#values['update_time'] = sub.update_time
		values['state'] = 'closed'
		#获取用户树
		users = GetUserByDepartmentRole(depart_id,depart_name,role.role_id,role.name,index)
		if users!=[]:

			values['children'] = users
		value.append(values.copy())
		values.clear()  # 防止上次保存的结果干扰下一次的值，比如下一次没有这个键值，而上一次却有，就会保存上一次
	return value

"""
获取某部门某角色的人
"""
def GetUserByDepartmentRole(depart_id,depart_name, role_id,role_name,index):
	# 根据role_id在User表中找到User
	UinRs = models.User.objects.filter(user_role__role__role_id=role_id)
	# 根据depart_id在User表中找到User
	UinDs = models.User.objects.filter(depart_user__depart_id=depart_id)
	#取部门对应人 角色对应人 的交集
	values={}
	value = []
	for u_in_r in UinRs:
		for u_in_d in UinDs:
			if u_in_r.user_id == u_in_d.user_id:
				index['index'] += 1
				values['id'] = index['index']
				values['trueid'] = u_in_r.user_id
				values['nature_id'] = 3
				values['name'] = u_in_r.name
				values['own_departid'] = depart_id
				values['own_departname'] = depart_name
				values['own_roleid'] = role_id
				values['own_rolename'] = role_name
				# values['create_time'] = sub.create_time
				# values['update_time'] = sub.update_time

				value.append(values.copy())
				values.clear()  # 防止上次保存的结果干扰下一次的值，比如下一次没有这个键值，而上一次却有，就会保存上一次
	return value


'''
根据user_id和menu_id查找是否存在该条数据
	若存在，则表示该用户对此菜单有过权限，根据现access_str做相应更新
		若access_str != ''   则update
		否则表示不存在，删除该条权限
	若不存在该条记录，则表示该用户原来没有权限
		若access_str != ''   则insert
'''
def update_Uper(user_id,menu_id,access_str):
	uper = models.User_Menu.objects.filter(user_id=user_id,menu_id=menu_id) #最多一条数据
	if uper.count() != 0:
		#有数据
			if access_str != '':
				models.User_Menu.objects.filter(user_id=user_id,menu_id=menu_id).update(access_str = access_str)
			else:
				models.User_Menu.objects.filter(user_id=user_id,menu_id=menu_id).delete()
	else:
		if access_str != '':
			models.User_Menu.objects.create(user_id = user_id,menu_id=menu_id,access_str=access_str)

#在部门树形节点下找所有的用户Id,返回与所给id相同的个数
def check_user(user_id,trees,count):

	#不停迭代判断是否有子节点，并且nature_id为3 代表当前是用户节点，没有子节点
	if 'children' in trees:
		children = trees['children']  # children :list
		for tree in children:  #role_trees:list  tree:dict
			ztrees = check_user(user_id,tree,count)
	else:
		if trees['trueid'] == user_id:
			count['count'] += 1
	return count


'''
根据role_id和menu_id查找是否存在该条数据
	若存在，则表示该用户对此菜单有过权限，根据现access_str做相应更新
		若access_str != ''   则update
		否则表示不存在，删除该条权限
	若不存在该条记录，则表示该用户原来没有权限
		若access_str != ''   则insert
'''
def update_Rper(role_id,menu_id,access_str):
	uper = models.Role_Menu.objects.filter(role_id=role_id,menu_id=menu_id) #最多一条数据
	if uper.count() != 0:
		#有数据
			if access_str != '':
				models.Role_Menu.objects.filter(role_id=role_id,menu_id=menu_id).update(access_str = access_str)
			else:
				models.Role_Menu.objects.filter(role_id=role_id,menu_id=menu_id).delete()
	else:
		if access_str != '':
			models.Role_Menu.objects.create(role_id=role_id,menu_id=menu_id,access_str=access_str)