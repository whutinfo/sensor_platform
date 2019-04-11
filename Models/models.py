from django.db import models
import django.utils.timezone as timezone
'''
角色是用户的组，角色与用户是多对多

角色里的用户当然拥有该角色的所有权限

但对于角色下的个别用户也需要有特殊权限

结论是不仅角色与用户多对多，用户还需要可以单独进行设置权限，，，，，

做系统就要做够灵活的
'''

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    node = models.CharField(max_length=32)
    describe = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    permissions = models.ManyToManyField('Menu', through='Role_Menu',through_fields=('role','menu'))
    # through_fields 接收一个二元组 ('field1', 'field2') ，
    # 其中 field1 为指向定义 ManyToManyField 字段的模型的外键名称（本例中为 role）
    # field2 为指向目标模型的外键的名称（本例中为 menu ）
    #ManyToMany的列名一般用复数

    class Meta:
        managed = False
        db_table = 'Role_Table'


#用户表   每个用户都有多个权限
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    pwd = models.CharField(max_length=32)
    create_time = models.DateTimeField(default = timezone.now)
    update_time = models.DateTimeField(auto_now=True)
    zgaccess_str = models.CharField(db_column='ZGaccess_str', max_length=20,null=True)  # Field name made lowercase.
    roles = models.ManyToManyField('Role', through='User_Role',through_fields=('user','role'))
    menus = models.ManyToManyField('Menu', through='User_Menu',through_fields=('user','menu'))
    class Meta:
        managed = False
        db_table = 'User_Table'

class User_Role(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True) #外键一般用目标模型的小写
    role = models.ForeignKey(Role,on_delete=models.CASCADE,null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        managed = False
        db_table = 'UserRole_Table'

class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    menu_name = models.CharField(max_length=20)
    menu_describe = models.TextField(blank=True, null=True)
    menu_url = models.CharField(max_length=64)
    menu_img = models.CharField(max_length=20)
    menu_show = models.IntegerField(blank=True, null=True)
    menu_open = models.IntegerField(blank=True, null=True)
    menu_node = models.CharField(max_length=64)
    maxchild = models.CharField(max_length=32,null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        managed = False
        db_table = 'Menu_Table'

class Role_Menu(models.Model):
    role = models.ForeignKey(Role,on_delete=models.CASCADE,null=True)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE,null=True)
    access_str = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        managed = False
        db_table = 'RolePermis_Table'

class User_Menu(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    access_str = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        managed = False
        db_table = 'UserPermis_Table'

class Department(models.Model):
    name = models.CharField(max_length=20)
    node = models.CharField(max_length=32)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    roles = models.ManyToManyField('Role', through='Depart_Role',through_fields=('depart','role'))
    users = models.ManyToManyField('User', through='Depart_User',through_fields=('depart','user'))
    class Meta:
        managed = False
        db_table = 'Department_Table'

class Depart_Role(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    depart = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        managed = False
        db_table = 'DepartRole_Table'

#多个部门可能有同一个角色，一个角色对应多个用户
#不能只凭角色找人，不然可能是A部门的也可能是B部门的
class Depart_User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    depart = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        managed = False
        db_table = 'DepartUser_Table'


#菜单的增删改查打印等权限  只是为了前端显示，目前没有实际用
class Access(models.Model):
    access_name = models.CharField(max_length=20)
    menu_describe = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True,null=True)
    update_time = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        managed = False
        db_table = 'Access_Table'


#供应商
class Supplier(models.Model):
    name = models.TextField(blank=True, null=True)
    managername = models.CharField(db_column='managerName',max_length=10) # Field name made lowercase.
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=64)
    class Meta:
        managed = False
        db_table = 'Supplier_Table'

#商品名称
class Goods(models.Model):

    goodsname = models.CharField(db_column='goodsName', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Goods_Table'

#生产厂家
class Manufactor(models.Model):
    name = models.CharField(max_length=40)
    manager = models.CharField(db_column='managerName',max_length=15)  # Field name made lowercase.
    phone = models.CharField(max_length=50)
    address = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Manufactor_Table'



class GoodsCat(models.Model):
    catname = models.TextField(db_column='catName', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'goodsCat_Table'


#销售商   wangyu add
class Seller(models.Model):

    Sellername = models.CharField(db_column='SellerName',max_length=10) #商户名称
    '''Sellerphone本身就有问题，现在影响了公共模板显示列名，故删去'''
   # Sellerphone = models.CharField(max_length=50) #商户名称
    Sellerproperty = models.CharField(max_length=64)#商户属性
    SellerOwner = models.CharField(max_length=64)  # 负责人姓名
    SellerOwnerPhone = models.CharField(max_length=64)  # 负责人手机号
    SellerOwnerLevel = models.CharField(max_length=64)  # 所属楼栋
    SellerOwnerNo = models.CharField(max_length=64)  # 所属编号
    #models.FloatField()
    SellerOwnerArea = models.CharField(max_length=64)  # 占地面积
    class Meta:
        managed = False
        db_table = 'Seller_Table'



#商户信息   wangyu add
'''
class Seller(models.Model):
    name = models.TextField(blank=True, null=True)
    Sellername = models.CharField(db_column='SellerName',max_length=10) # Field name made lowercase.
    Sellerphone = models.CharField(max_length=50) #商户名称
    Sellerproperty = models.CharField(max_length=64)#商户属性
    SellerOwner = models.CharField(max_length=64)  # 负责人姓名
    SellerOwnerPhone = models.CharField(max_length=64)  # 负责人手机号
    SellerOwnerLevel = models.CharField(max_length=64)  # 所属楼栋
    SellerOwnerNo = models.CharField(max_length=64)  # 所属编号
    #models.FloatField()
    SellerOwnerArea = models.CharField(max_length=64)  # 占地面积
    class Meta:
        managed = False
        db_table = 'Seller_Table'


'''
#商户属性信息   wangyu add
class SellerPorprety(models.Model):
    #name = models.TextField(blank=True, null=True)
    SellerpropertyType = models.CharField(db_column='SellerP_Str',max_length=10) # Field name made lowercase.
#    SellerpropertyID = models.AutoField(db_column='Inx')
    class Meta:
        managed = False
        db_table = 'SellerPorprety_Table'


'''工单管理'''
# 基础表
class Base(models.Model):
    title = models.CharField(max_length=64)
    type = models.IntegerField(blank=True, null=True)
    node = models.IntegerField(blank=True, null=True)
    prefunc = models.IntegerField(blank=True, null=True)
    curfunc = models.IntegerField(blank=True, null=True)
    afterfunc = models.IntegerField(blank=True, null=True)
    value1 = models.IntegerField(blank=True, null=True)
    value2 = models.IntegerField(blank=True, null=True)
    depart = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, related_name='depart')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, related_name='role')

    class Meta:
        managed = False
        db_table = 'Base_Table'


class Work(models.Model):
    type = models.IntegerField(blank=True, null=True)
    step = models.IntegerField(blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    position = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='work_user')
    performer1 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='performer1')
    performer2 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='performer2')
    performer3 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='performer3')

    class Meta:
        managed = False
        db_table = 'Work_Table'


class Approval(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE, null=True, related_name='work_approval')
    performer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_approval')
    advise = models.TextField(blank=True, null=True)
    step = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Approval_Table'




'''商品出入库'''

class StockIn(models.Model):
    stockin_id = models.IntegerField(null=True)
    goods = models.ForeignKey(Goods,db_column='goodsId',on_delete=models.CASCADE, null=True, related_name='goods_in')  # Field name made lowercase.
    goods_sn = models.CharField(db_column='goodsSn', max_length=100)  # Field name made lowercase.
    cat = models.ForeignKey(GoodsCat,db_column='catId',on_delete=models.CASCADE, null=True, related_name='goodsCat_in')  # Field name made lowercase.
    in_amount = models.IntegerField(db_column='inAmount', blank=True, null=True)  # Field name made lowercase.
    cost = models.FloatField(null=True)
    performer = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='user_stockIn')
    in_time = models.DateTimeField(default=timezone.now)
    seller = models.ForeignKey(Seller,db_column='sellerId',on_delete=models.CASCADE, null=True, related_name='seller_stockIn')  # Field name made lowercase.
    manufactor = models.ForeignKey(Manufactor,db_column='manufactorId',on_delete=models.CASCADE, null=True, related_name='manufactor_stockIn')  # Field name made lowercase.
    supplier = models.ForeignKey(Supplier,db_column='supplierId', on_delete=models.CASCADE, null=True, related_name='supplier_stockIn')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockIn_Table'


class StockOut(models.Model):
    stockout_id = models.IntegerField(null=True)
    goods = models.ForeignKey(Goods,db_column='goodsId',on_delete=models.CASCADE, null=True, related_name='goods_out')  # Field name made lowercase.
    goods_sn = models.CharField(db_column='goodsSn', max_length=100)   # Field name made lowercase.
    cat = models.ForeignKey(GoodsCat,db_column='catId',on_delete=models.CASCADE, null=True, related_name='goodsCat_out')  # Field name made lowercase.
    out_amount = models.IntegerField(db_column='outAmount', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(null=True)
    performer = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='user_stockOut')
    out_time = models.DateTimeField(default=timezone.now)
    seller = models.ForeignKey(Seller,db_column='sellerId',on_delete=models.CASCADE, null=True, related_name='seller_stockOut')   # Field name made lowercase.
    customer_phone = models.CharField(db_column='KHPhone', max_length=100)  # Field name made lowercase.
    customer_name = models.CharField(db_column='KeHuName',max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockOut_Table'


class GoodsInfo(models.Model):
    stockin = models.ForeignKey(StockIn,db_column='stockIn_id',on_delete=models.CASCADE, null=True)  # Field name made lowercase.
    goods = models.ForeignKey(Goods,db_column='goodsId',on_delete=models.CASCADE, null=True)  # Field name made lowercase.
    cat = models.ForeignKey(GoodsCat,db_column='catId',on_delete=models.CASCADE, null=True)  # Field name made lowercase.
    goods_sn = models.CharField(db_column='goodsSn', max_length=100) # Field name made lowercase.
    goods_stock = models.IntegerField(db_column='goodsStock',null=True)  # Field name made lowercase.
    sale_count = models.IntegerField(db_column='saleCount', null=True)  # Field name made lowercase.
    cost = models.FloatField(null=True)
    price = models.FloatField(null=True)
    exp_date = models.DateTimeField(null=True)
    manufactor = models.ForeignKey(Manufactor,db_column='manufactorId',on_delete=models.CASCADE, null=True)  # Field name made lowercase.
    supplier = models.ForeignKey(Supplier,db_column='supplierId',on_delete=models.CASCADE, null=True)  # Field name made lowercase.
    seller = models.ForeignKey(Seller,db_column='sellerId',on_delete=models.CASCADE, null=True)  # Field name made lowercase.
    out_time = models.DateTimeField(null=True)
    value3 = models.TextField(blank=True, null=True)  #留以备用的列
    value4 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GoodsInfo_Table'

#客户管理
class Customer(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.TextField(blank=True, null=True)
    sex = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    carid = models.TextField(db_column='carId', blank=True, null=True)  # Field name made lowercase.
    point = models.IntegerField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'Customer_Table'

class videomeau(models.Model):

    name = models.CharField(max_length=20)
    node = models.CharField(max_length=64,null=True)
    class Meta:
        managed = False
        db_table = 'VideoMeau_Table'


class Video(models.Model):

    name = models.CharField(max_length=20)

    ip = models.GenericIPAddressField()

    port = models.IntegerField(default='80')

    user_name = models.CharField(max_length=20,null=True)

    pwd = models.CharField(max_length=32)

    rtsp_port = models.IntegerField(default='553')

    stream_type = models.IntegerField(default='1')

    device_port = models.IntegerField(default='8000')

    parent = models.ForeignKey(videomeau,on_delete=models.CASCADE, null=True)

    manufacturer= models.CharField(max_length=20,null=True)
    device_type = models.CharField(max_length=20,null=True)
    type = models.IntegerField(default='1')
    class Meta:
        managed = False
        db_table = 'Video_Table'

class Temperature(models.Model):

    temperate = models.IntegerField(null=True)

    humidity =  models.IntegerField(null=True)

    rainfall =  models.IntegerField(null=True)

    time = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = False
        db_table = 'Temperature_Table'

# 监测站点配置树
class Site_Tree(models.Model):
    name = models.CharField(max_length=20)
    node = models.CharField(max_length=64, null=True)

    class Meta:
        managed = False
        db_table = 'SiteTree_Table'


# 监测站点位置
class Device_Site(models.Model):
    name = models.CharField(max_length=64)

    parent = models.ForeignKey(Site_Tree, on_delete=models.CASCADE, null=True)

    longitude = models.FloatField()  # 经度

    latitude = models.FloatField()  # 纬度

    map_label = models.CharField(max_length=64,null=True)

    class Meta:
        managed = False
        db_table = 'DeviceSite_Table'


# 监测站点位置
class Sensor(models.Model):
    name = models.CharField(max_length=20)

    parent = models.ForeignKey(Device_Site, on_delete=models.CASCADE, null=True)

    #state = models.IntegerField(default=2) # 状态 1 为在线  2 为离线

    class Meta:
        managed = False
        db_table = 'Sensor_Table'



#传感器实时数据
class Sensor_data(models.Model):

    type_1 = models.FloatField(default='0')  # 传感器1号
    type_2 = models.FloatField(default='0')  # 传感器2号
    type_3 = models.FloatField(default='0')  # 传感器3号
    type_4 = models.FloatField(default='0')  # 传感器4号
    type_5 = models.FloatField(default='0')  # 传感器5号
    type_6 = models.FloatField(default='0')  # 传感器6号
    type_7 = models.FloatField(default='0')  # 传感器7号
    type_8 = models.FloatField(default='0')  # 传感器8号
    type_9 = models.FloatField(default='0')  # 传感器9号
    type_10 = models.FloatField(default='0')  # 传感器10号
    type_11 = models.FloatField(default='0')  # 传感器11号
    type_12 = models.FloatField(default='0')  # 传感器12号
    type_13 = models.FloatField(default='0')  # 传感器13号
    type_14 = models.FloatField(default='0')  # 传感器14号
    type_15 = models.FloatField(default='0')  # 传感器15号
    type_16 = models.FloatField(default='0')  # 传感器16号
    type_17 = models.FloatField(default='0')  # 传感器17号
    type_18 = models.FloatField(default='0')  # 传感器18号
    type_19 = models.FloatField(default='0')  # 传感器19号
    type_20 = models.FloatField(default='0')  # 传感器20号
    type_21 = models.FloatField(default='0')  # 传感器21号
    type_22 = models.FloatField(default='0')  # 传感器22号
    type_23 = models.FloatField(default='0')  # 传感器23号
    type_24 = models.FloatField(default='0')  # 传感器24号
    type_25 = models.FloatField(default='0')  # 传感器25号
    create_time = models.DateTimeField(null=False) #数据采集时间   default=timezone.now,
    class Meta:
        #managed = False
        db_table = 'SensorData_Table'


