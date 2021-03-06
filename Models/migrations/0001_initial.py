# Generated by Django 2.1.5 on 2019-03-20 14:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_name', models.CharField(max_length=20)),
                ('menu_describe', models.TextField(blank=True, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'Access_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advise', models.TextField(blank=True, null=True)),
                ('step', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Approval_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('type', models.IntegerField(blank=True, null=True)),
                ('node', models.IntegerField(blank=True, null=True)),
                ('prefunc', models.IntegerField(blank=True, null=True)),
                ('curfunc', models.IntegerField(blank=True, null=True)),
                ('afterfunc', models.IntegerField(blank=True, null=True)),
                ('value1', models.IntegerField(blank=True, null=True)),
                ('value2', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Base_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('birthday', models.TextField(blank=True, null=True)),
                ('sex', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('carid', models.TextField(blank=True, db_column='carId', null=True)),
                ('point', models.IntegerField(null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Customer_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Depart_Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'DepartRole_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Depart_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'DepartUser_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('node', models.CharField(max_length=32)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Department_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Device_Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('map_label',models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'DeviceSite_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodsname', models.CharField(db_column='goodsName', max_length=32)),
            ],
            options={
                'db_table': 'Goods_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.TextField(blank=True, db_column='catName', null=True)),
            ],
            options={
                'db_table': 'goodsCat_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_sn', models.CharField(db_column='goodsSn', max_length=100)),
                ('goods_stock', models.IntegerField(db_column='goodsStock', null=True)),
                ('sale_count', models.IntegerField(db_column='saleCount', null=True)),
                ('cost', models.FloatField(null=True)),
                ('price', models.FloatField(null=True)),
                ('exp_date', models.DateTimeField(null=True)),
                ('out_time', models.DateTimeField(null=True)),
                ('value3', models.TextField(blank=True, null=True)),
                ('value4', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'GoodsInfo_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Manufactor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('manager', models.CharField(db_column='managerName', max_length=15)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Manufactor_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.AutoField(primary_key=True, serialize=False)),
                ('menu_name', models.CharField(max_length=20)),
                ('menu_describe', models.TextField(blank=True, null=True)),
                ('menu_url', models.CharField(max_length=64)),
                ('menu_img', models.CharField(max_length=20)),
                ('menu_show', models.IntegerField(blank=True, null=True)),
                ('menu_open', models.IntegerField(blank=True, null=True)),
                ('menu_node', models.CharField(max_length=64)),
                ('maxchild', models.CharField(max_length=32, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Menu_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('node', models.CharField(max_length=32)),
                ('describe', models.TextField(blank=True, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Role_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Role_Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_str', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'RolePermis_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sellername', models.CharField(db_column='SellerName', max_length=10)),
                ('Sellerproperty', models.CharField(max_length=64)),
                ('SellerOwner', models.CharField(max_length=64)),
                ('SellerOwnerPhone', models.CharField(max_length=64)),
                ('SellerOwnerLevel', models.CharField(max_length=64)),
                ('SellerOwnerNo', models.CharField(max_length=64)),
                ('SellerOwnerArea', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'Seller_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SellerPorprety',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SellerpropertyType', models.CharField(db_column='SellerP_Str', max_length=10)),
            ],
            options={
                'db_table': 'SellerPorprety_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('state', models.IntegerField(default=2)),
            ],
            options={
                'db_table': 'Sensor_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Site_Tree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('node', models.CharField(max_length=64, null=True)),
            ],
            options={
                'db_table': 'SiteTree_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StockIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stockin_id', models.IntegerField(null=True)),
                ('goods_sn', models.CharField(db_column='goodsSn', max_length=100)),
                ('in_amount', models.IntegerField(blank=True, db_column='inAmount', null=True)),
                ('cost', models.FloatField(null=True)),
                ('in_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'StockIn_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StockOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stockout_id', models.IntegerField(null=True)),
                ('goods_sn', models.CharField(db_column='goodsSn', max_length=100)),
                ('out_amount', models.IntegerField(blank=True, db_column='outAmount', null=True)),
                ('price', models.FloatField(null=True)),
                ('out_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('customer_phone', models.CharField(db_column='KHPhone', max_length=100)),
                ('customer_name', models.CharField(db_column='KeHuName', max_length=50)),
            ],
            options={
                'db_table': 'StockOut_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('managername', models.CharField(db_column='managerName', max_length=10)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'Supplier_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperate', models.IntegerField(null=True)),
                ('humidity', models.IntegerField(null=True)),
                ('rainfall', models.IntegerField(null=True)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Temperature_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('pwd', models.CharField(max_length=32)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('zgaccess_str', models.CharField(db_column='ZGaccess_str', max_length=20, null=True)),
            ],
            options={
                'db_table': 'User_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User_Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_str', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'UserPermis_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User_Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'UserRole_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('ip', models.GenericIPAddressField()),
                ('port', models.IntegerField(default='80')),
                ('user_name', models.CharField(max_length=20, null=True)),
                ('pwd', models.CharField(max_length=32)),
                ('rtsp_port', models.IntegerField(default='553')),
                ('stream_type', models.IntegerField(default='1')),
                ('device_port', models.IntegerField(default='8000')),
                ('manufacturer', models.CharField(max_length=20, null=True)),
                ('device_type', models.CharField(max_length=20, null=True)),
                ('type', models.IntegerField(default='1')),
            ],
            options={
                'db_table': 'Video_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='videomeau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('node', models.CharField(max_length=64, null=True)),
            ],
            options={
                'db_table': 'VideoMeau_Table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(blank=True, null=True)),
                ('step', models.IntegerField(blank=True, null=True)),
                ('flag', models.IntegerField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('position', models.TextField(blank=True, null=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Work_Table',
                'managed': False,
            },
        ),
    ]
