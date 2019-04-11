# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccessTable(models.Model):
    access_id = models.IntegerField(blank=True, null=True)
    access_name = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Access_Table'


class BaseTable(models.Model):
    title = models.TextField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    node = models.IntegerField(blank=True, null=True)
    prefunc = models.IntegerField(blank=True, null=True)
    curfunc = models.IntegerField(blank=True, null=True)
    afterfunc = models.IntegerField(blank=True, null=True)
    value1 = models.IntegerField(blank=True, null=True)
    value2 = models.IntegerField(blank=True, null=True)
    depart_id = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Base_Table'


class Data55Table(models.Model):
    data_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Data55_Table'


class Data56Table(models.Model):
    data_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Data56_Table'


class Data57Table(models.Model):
    data_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Data57_Table'


class Data58Table(models.Model):
    data_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Data58_Table'


class Data59Table(models.Model):
    data_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Data59_Table'


class Data60Table(models.Model):
    data_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Data60_Table'


class Data61Table(models.Model):
    data_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Data61_Table'


class Data62Table(models.Model):
    data_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Data62_Table'


class Data63Table(models.Model):
    data_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Data63_Table'


class Data64Table(models.Model):
    data_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Data64_Table'


class Data66Table(models.Model):
    data_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Data66_Table'


class Data67Table(models.Model):
    data_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Data67_Table'


class Data69Table(models.Model):
    data_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Data69_Table'


class Data70Table(models.Model):
    data_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Data70_Table'


class Data72Table(models.Model):
    data_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Data72_Table'


class DepartroleTable(models.Model):
    dr_id = models.IntegerField(blank=True, null=True)
    depart_id = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DepartRole_Table'


class DepartuserTable(models.Model):
    dr_id = models.IntegerField(blank=True, null=True)
    depart_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DepartUser_Table'


class DepartmentTable(models.Model):
    depart_id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    node = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Department_Table'


class DepotinfoTable(models.Model):
    depotinfo_id = models.IntegerField(blank=True, null=True)
    depotinfo_style = models.TextField(blank=True, null=True)
    d_id = models.IntegerField(blank=True, null=True)
    d_name = models.TextField(blank=True, null=True)
    data_id = models.IntegerField(blank=True, null=True)
    rfid = models.TextField(blank=True, null=True)
    stock_id = models.IntegerField(blank=True, null=True)
    stock_name = models.TextField(blank=True, null=True)
    opt_time = models.TextField(blank=True, null=True)
    opt_uid = models.IntegerField(blank=True, null=True)
    opt_uname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Depotinfo_Table'


class DictionaryTable(models.Model):
    d_id = models.IntegerField(blank=True, null=True)
    d_name = models.TextField(blank=True, null=True)
    d_describe = models.TextField(blank=True, null=True)
    module_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)
    other_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dictionary_Table'


class ErrorRecordTable(models.Model):
    record_id = models.IntegerField(blank=True, null=True)
    style = models.IntegerField(blank=True, null=True)
    rfid = models.TextField(blank=True, null=True)
    d_id = models.IntegerField(blank=True, null=True)
    data_id = models.IntegerField(blank=True, null=True)
    gettime = models.DateTimeField(blank=True, null=True)
    rfid_id = models.IntegerField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    cause = models.TextField(blank=True, null=True)
    record = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Error_Record_Table'


class ErrorTable(models.Model):
    error_id = models.IntegerField(blank=True, null=True)
    style = models.IntegerField(blank=True, null=True)
    rfid = models.TextField(blank=True, null=True)
    d_id = models.IntegerField(blank=True, null=True)
    data_id = models.IntegerField(blank=True, null=True)
    gettime = models.DateTimeField(blank=True, null=True)
    rfid_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Error_Table'


class Exception(models.Model):
    id = models.IntegerField(blank=True, null=True)
    style = models.CharField(max_length=50, blank=True, null=True)
    method = models.CharField(max_length=50, blank=True, null=True)
    parameter = models.CharField(max_length=50, blank=True, null=True)
    explain = models.CharField(max_length=50, blank=True, null=True)
    etime = models.CharField(max_length=50, blank=True, null=True)
    remark = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Exception'


class Field55Table(models.Model):
    field_id = models.IntegerField(blank=True, null=True)
    field_name = models.TextField(blank=True, null=True)
    field_describe = models.TextField(blank=True, null=True)
    field_default = models.TextField(blank=True, null=True)
    field_type = models.TextField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    create_time = models.TextField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)
    update_time = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Field55_Table'


class Field56Table(models.Model):
    field_id = models.IntegerField(blank=True, null=True)
    field_name = models.TextField(blank=True, null=True)
    field_describe = models.TextField(blank=True, null=True)
    field_default = models.TextField(blank=True, null=True)
    field_type = models.TextField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    create_time = models.TextField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)
    update_time = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Field56_Table'


class Field57Table(models.Model):
    field_id = models.IntegerField(blank=True, null=True)
    field_name = models.TextField(blank=True, null=True)
    field_describe = models.TextField(blank=True, null=True)
    field_default = models.TextField(blank=True, null=True)
    field_type = models.TextField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    create_time = models.TextField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)
    update_time = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Field57_Table'


class Field58Table(models.Model):
    field_id = models.IntegerField(blank=True, null=True)
    field_name = models.TextField(blank=True, null=True)
    field_describe = models.TextField(blank=True, null=True)
    field_default = models.TextField(blank=True, null=True)
    field_type = models.TextField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    create_time = models.TextField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)
    update_time = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Field58_Table'


class Field59Table(models.Model):
    field_id = models.IntegerField(blank=True, null=True)
    field_name = models.TextField(blank=True, null=True)
    field_describe = models.TextField(blank=True, null=True)
    field_default = models.TextField(blank=True, null=True)
    field_type = models.TextField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    create_time = models.TextField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)
    update_time = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Field59_Table'


class Field60Table(models.Model):
    field_id = models.IntegerField(blank=True, null=True)
    field_name = models.TextField(blank=True, null=True)
    field_describe = models.TextField(blank=True, null=True)
    field_default = models.TextField(blank=True, null=True)
    field_type = models.TextField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    create_time = models.TextField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)
    update_time = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Field60_Table'


class Field61Table(models.Model):
    field_id = models.IntegerField(blank=True, null=True)
    field_name = models.TextField(blank=True, null=True)
    field_describe = models.TextField(blank=True, null=True)
    field_default = models.TextField(blank=True, null=True)
    field_type = models.TextField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    create_time = models.TextField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)
    update_time = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Field61_Table'


class Field62Table(models.Model):
    field_id = models.IntegerField(blank=True, null=True)
    field_name = models.TextField(blank=True, null=True)
    field_describe = models.TextField(blank=True, null=True)
    field_default = models.TextField(blank=True, null=True)
    field_type = models.TextField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    create_time = models.TextField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)
    update_time = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Field62_Table'


class Field63Table(models.Model):
    field_id = models.IntegerField(blank=True, null=True)
    field_name = models.TextField(blank=True, null=True)
    field_describe = models.TextField(blank=True, null=True)
    field_default = models.TextField(blank=True, null=True)
    field_type = models.TextField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    create_time = models.TextField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)
    update_time = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Field63_Table'


class Field64Table(models.Model):
    field_id = models.IntegerField(blank=True, null=True)
    field_name = models.TextField(blank=True, null=True)
    field_describe = models.TextField(blank=True, null=True)
    field_default = models.TextField(blank=True, null=True)
    field_type = models.TextField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    create_time = models.TextField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)
    update_time = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Field64_Table'


class Field66Table(models.Model):
    field_id = models.IntegerField(blank=True, null=True)
    field_name = models.TextField(blank=True, null=True)
    field_describe = models.TextField(blank=True, null=True)
    field_default = models.TextField(blank=True, null=True)
    field_type = models.TextField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    create_time = models.TextField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)
    update_time = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Field66_Table'


class Field67Table(models.Model):
    field_id = models.IntegerField(blank=True, null=True)
    field_name = models.TextField(blank=True, null=True)
    field_describe = models.TextField(blank=True, null=True)
    field_default = models.TextField(blank=True, null=True)
    field_type = models.TextField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    create_time = models.TextField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)
    update_time = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Field67_Table'


class Field69Table(models.Model):
    field_id = models.IntegerField(blank=True, null=True)
    field_name = models.TextField(blank=True, null=True)
    field_describe = models.TextField(blank=True, null=True)
    field_default = models.TextField(blank=True, null=True)
    field_type = models.TextField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    create_time = models.TextField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)
    update_time = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Field69_Table'


class Field70Table(models.Model):
    field_id = models.IntegerField(blank=True, null=True)
    field_name = models.TextField(blank=True, null=True)
    field_describe = models.TextField(blank=True, null=True)
    field_default = models.TextField(blank=True, null=True)
    field_type = models.TextField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    create_time = models.TextField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)
    update_time = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Field70_Table'


class Field72Table(models.Model):
    field_id = models.IntegerField(blank=True, null=True)
    field_name = models.TextField(blank=True, null=True)
    field_describe = models.TextField(blank=True, null=True)
    field_default = models.TextField(blank=True, null=True)
    field_type = models.TextField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    create_time = models.TextField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)
    update_time = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Field72_Table'


class GoodsinfoTable(models.Model):
    id = models.IntegerField(blank=True, null=True)
    stockin_id = models.IntegerField(db_column='stockIn_id', blank=True, null=True)  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='goodsId', blank=True, null=True)  # Field name made lowercase.
    catid = models.TextField(db_column='catId', blank=True, null=True)  # Field name made lowercase.
    goodssn = models.TextField(db_column='goodsSn', blank=True, null=True)  # Field name made lowercase.
    goodsstock = models.IntegerField(db_column='goodsStock', blank=True, null=True)  # Field name made lowercase.
    salecount = models.IntegerField(db_column='saleCount', blank=True, null=True)  # Field name made lowercase.
    cost = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exp_date = models.TextField(blank=True, null=True)
    manufactorid = models.IntegerField(db_column='manufactorId', blank=True, null=True)  # Field name made lowercase.
    supplierid = models.IntegerField(db_column='supplierId', blank=True, null=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='shopId', blank=True, null=True)  # Field name made lowercase.
    out_time = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GoodsInfo_Table'


class GoodsTable(models.Model):
    goodsid = models.IntegerField(db_column='goodsId', blank=True, null=True)  # Field name made lowercase.
    goodsname = models.TextField(db_column='goodsName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Goods_Table'


class InfoTable(models.Model):
    info_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)
    enable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Info_Table'


class KhcontrolTable(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    birthday = models.TextField(blank=True, null=True)
    sex = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    carid = models.TextField(db_column='carId', blank=True, null=True)  # Field name made lowercase.
    point = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.TextField(blank=True, null=True)
    update_time = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KHcontrol_Table'


class ManufactorTable(models.Model):
    manufactorid = models.IntegerField(db_column='manufactorId', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    managername = models.TextField(db_column='managerName', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Manufactor_Table'


class MapmenuTable(models.Model):
    map_id = models.IntegerField(blank=True, null=True)
    node = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MapMenu_Table'


class MappointTable(models.Model):
    point_id = models.IntegerField(blank=True, null=True)
    map_id = models.IntegerField(blank=True, null=True)
    px = models.TextField(blank=True, null=True)
    py = models.TextField(blank=True, null=True)
    msg1 = models.TextField(blank=True, null=True)
    msg2 = models.TextField(blank=True, null=True)
    msg3 = models.TextField(blank=True, null=True)
    video_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MapPoint_Table'


class MenuTable(models.Model):
    menu_id = models.IntegerField(blank=True, null=True)
    menu_name = models.TextField(blank=True, null=True)
    menu_describe = models.TextField(blank=True, null=True)
    menu_align = models.TextField(blank=True, null=True)
    menu_url = models.TextField(blank=True, null=True)
    menu_img = models.TextField(blank=True, null=True)
    menu_show = models.IntegerField(blank=True, null=True)
    menu_open = models.IntegerField(blank=True, null=True)
    menu_node = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Menu_Table'


class MokuaiTable(models.Model):
    id = models.IntegerField(blank=True, null=True)
    mokuai_name = models.TextField(blank=True, null=True)
    mokuai_describe = models.TextField(blank=True, null=True)
    mokuai_node = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MoKuai_Table'


class ModuleTable(models.Model):
    module_id = models.IntegerField(blank=True, null=True)
    module_name = models.TextField(blank=True, null=True)
    module_describe = models.TextField(blank=True, null=True)
    module_node = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Module_Table'


class NodeTable(models.Model):
    node_id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    node = models.TextField(blank=True, null=True)
    maxchild = models.TextField(blank=True, null=True)
    tree_id = models.IntegerField(blank=True, null=True)
    info_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Node_Table'


class ObjectTable(models.Model):
    object_id = models.IntegerField(blank=True, null=True)
    obj_name = models.TextField(blank=True, null=True)
    obj_tableid = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Object_Table'


class PatchTable(models.Model):
    suoyin = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    step = models.IntegerField(blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    position = models.TextField(blank=True, null=True)
    create_time = models.TextField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    performer1 = models.IntegerField(blank=True, null=True)
    performer2 = models.IntegerField(blank=True, null=True)
    performer3 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Patch_Table'


class Receiverfidinfo(models.Model):
    id = models.IntegerField(blank=True, null=True)
    receivetime = models.DateTimeField(db_column='receiveTime', blank=True, null=True)  # Field name made lowercase.
    cardid = models.TextField(db_column='cardId', blank=True, null=True)  # Field name made lowercase.
    stationname = models.TextField(db_column='stationName', blank=True, null=True)  # Field name made lowercase.
    style = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ReceiveRfidInfo'


class RfidalarmtestTable(models.Model):
    rfid_number = models.IntegerField(blank=True, null=True)
    rfid = models.TextField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RfidAlarmTest_Table'


class RfidinfoTable(models.Model):
    rfid_id = models.IntegerField(blank=True, null=True)
    rfid_name = models.TextField(blank=True, null=True)
    rfid_describe = models.TextField(blank=True, null=True)
    rfid_serverip = models.TextField(db_column='rfid_serverIp', blank=True, null=True)  # Field name made lowercase.
    rfid_serverport = models.TextField(db_column='rfid_serverPort', blank=True, null=True)  # Field name made lowercase.
    rfid_clientip = models.TextField(db_column='rfid_clientIp', blank=True, null=True)  # Field name made lowercase.
    rfid_clientport = models.TextField(db_column='rfid_clientPort', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    update_time = models.TextField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RfidInfo_Table'


class RfidtestTable1(models.Model):
    rfid_number = models.IntegerField(blank=True, null=True)
    rfid = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RfidTest_Table1'


class RfidtestTable2(models.Model):
    rfid_number = models.IntegerField(blank=True, null=True)
    rfid = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RfidTest_Table2'


class RfidtestTable3(models.Model):
    rfid_number = models.IntegerField(blank=True, null=True)
    rfid = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RfidTest_Table3'


class RolepermisTable(models.Model):
    per_id = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    menu_id = models.IntegerField(blank=True, null=True)
    access_str = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RolePermis_Table'


class RoleTable(models.Model):
    role_id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    node = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Role_Table'


class SellercatTable(models.Model):
    id = models.IntegerField(blank=True, null=True)
    cat_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SellerCat_Table'


class ShenpiTable(models.Model):
    id = models.IntegerField(blank=True, null=True)
    suoyin = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    advise = models.TextField(blank=True, null=True)
    step = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ShenPi_Table'


class StockinTable(models.Model):
    in_id = models.IntegerField(blank=True, null=True)
    stockin_id = models.IntegerField(db_column='stockIn_id', blank=True, null=True)  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='goodsId', blank=True, null=True)  # Field name made lowercase.
    goodssn = models.TextField(db_column='goodsSn', blank=True, null=True)  # Field name made lowercase.
    catid = models.IntegerField(db_column='catId', blank=True, null=True)  # Field name made lowercase.
    inamount = models.IntegerField(db_column='inAmount', blank=True, null=True)  # Field name made lowercase.
    cost = models.TextField(blank=True, null=True)
    performer = models.IntegerField(blank=True, null=True)
    in_time = models.TextField(blank=True, null=True)
    shopid = models.IntegerField(db_column='shopId', blank=True, null=True)  # Field name made lowercase.
    manufactorid = models.IntegerField(db_column='manufactorId', blank=True, null=True)  # Field name made lowercase.
    supplierid = models.IntegerField(db_column='supplierId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockIn_Table'


class StockoutTable(models.Model):
    out_id = models.IntegerField(blank=True, null=True)
    stockout_id = models.IntegerField(db_column='stockOut_id', blank=True, null=True)  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='goodsId', blank=True, null=True)  # Field name made lowercase.
    catid = models.IntegerField(db_column='catId', blank=True, null=True)  # Field name made lowercase.
    goodssn = models.TextField(db_column='goodsSn', blank=True, null=True)  # Field name made lowercase.
    outamount = models.IntegerField(db_column='outAmount', blank=True, null=True)  # Field name made lowercase.
    price = models.TextField(blank=True, null=True)
    performer = models.IntegerField(blank=True, null=True)
    out_time = models.TextField(blank=True, null=True)
    shopid = models.IntegerField(db_column='shopId', blank=True, null=True)  # Field name made lowercase.
    khphone = models.CharField(db_column='KHPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kehuname = models.TextField(db_column='KeHuName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockOut_Table'


class SupplierTable(models.Model):
    supplierid = models.IntegerField(db_column='supplierId', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    managername = models.TextField(db_column='managerName', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Supplier_Table'


class Text10Table(models.Model):
    text_id = models.IntegerField(blank=True, null=True)
    text_name = models.TextField(blank=True, null=True)
    text_str = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Text10_Table'


class Text11Table(models.Model):
    text_id = models.IntegerField(blank=True, null=True)
    text_name = models.TextField(blank=True, null=True)
    text_str = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Text11_Table'


class Text14Table(models.Model):
    text_id = models.IntegerField(blank=True, null=True)
    text_name = models.TextField(blank=True, null=True)
    text_str = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Text14_Table'


class Text15Table(models.Model):
    text_id = models.IntegerField(blank=True, null=True)
    text_name = models.TextField(blank=True, null=True)
    text_str = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Text15_Table'


class Text16Table(models.Model):
    text_id = models.IntegerField(blank=True, null=True)
    text_name = models.TextField(blank=True, null=True)
    text_str = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Text16_Table'


class Text17Table(models.Model):
    text_id = models.IntegerField(blank=True, null=True)
    text_name = models.TextField(blank=True, null=True)
    text_str = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Text17_Table'


class Text1Table(models.Model):
    text_id = models.IntegerField(blank=True, null=True)
    text_name = models.TextField(blank=True, null=True)
    text_str = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Text1_Table'


class Text2Table(models.Model):
    text_id = models.IntegerField(blank=True, null=True)
    text_name = models.TextField(blank=True, null=True)
    text_str = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Text2_Table'


class Text3Table(models.Model):
    text_id = models.IntegerField(blank=True, null=True)
    text_name = models.TextField(blank=True, null=True)
    text_str = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Text3_Table'


class Text4Table(models.Model):
    text_id = models.IntegerField(blank=True, null=True)
    text_name = models.TextField(blank=True, null=True)
    text_str = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Text4_Table'


class Text5Table(models.Model):
    text_id = models.IntegerField(blank=True, null=True)
    text_name = models.TextField(blank=True, null=True)
    text_str = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Text5_Table'


class Text6Table(models.Model):
    text_id = models.IntegerField(blank=True, null=True)
    text_name = models.TextField(blank=True, null=True)
    text_str = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Text6_Table'


class Text7Table(models.Model):
    text_id = models.IntegerField(blank=True, null=True)
    text_name = models.TextField(blank=True, null=True)
    text_str = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Text7_Table'


class Text8Table(models.Model):
    text_id = models.IntegerField(blank=True, null=True)
    text_name = models.TextField(blank=True, null=True)
    text_str = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Text8_Table'


class Text9Table(models.Model):
    text_id = models.IntegerField(blank=True, null=True)
    text_name = models.TextField(blank=True, null=True)
    text_str = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Text9_Table'


class TreeTable(models.Model):
    tree_id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    maxnode = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    info_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tree_Table'


class Useroptrecord(models.Model):
    id = models.IntegerField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    opt = models.CharField(max_length=50, blank=True, null=True)
    opttime = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserOptRecord'


class UserpermisTable(models.Model):
    per_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    menu_id = models.IntegerField(blank=True, null=True)
    access_str = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserPermis_Table'


class UserroleTable(models.Model):
    ur_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserRole_Table'


class UserTable(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    pwd = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)
    zgaccess_str = models.TextField(db_column='ZGaccess_str', blank=True, null=True)  # Field name made lowercase.
    value2 = models.TextField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User_Table'


class Value10Table(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value10_Table'


class Value11Table(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value11_Table'


class Value14Table(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value14_Table'


class Value15Table(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value15_Table'


class Value16Table(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value16_Table'


class Value17Table(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value17_Table'


class Value1Table(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value1_Table'


class Value22Table(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value22_Table'


class Value23Table(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value23_Table'


class Value24Table(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value24_Table'


class Value26Table(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value26_Table'


class Value2Table(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value2_Table'


class Value34Table(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value34_Table'


class Value3Table(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value3_Table'


class Value4Table(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value4_Table'


class Value5Table(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value5_Table'


class Value6Table(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value6_Table'


class Value7Table(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value7_Table'


class Value8Table(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value8_Table'


class Value9Table(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value9_Table'


class ValueTable20151224(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value_Table_2015_12_24'


class ValueTable20151228(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value_Table_2015_12_28'


class ValueTable20151229(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value_Table_2015_12_29'


class ValueTable20151230(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value_Table_2015_12_30'


class ValueTable20151231(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value_Table_2015_12_31'


class ValueTable20160120(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value_Table_2016_01_20'


class ValueTable20160301(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value_Table_2016_03_01'


class ValueTable20160303(models.Model):
    value_id = models.IntegerField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    value2 = models.TextField(blank=True, null=True)
    value3 = models.TextField(blank=True, null=True)
    value4 = models.TextField(blank=True, null=True)
    value5 = models.TextField(blank=True, null=True)
    value6 = models.TextField(blank=True, null=True)
    value7 = models.TextField(blank=True, null=True)
    value8 = models.TextField(blank=True, null=True)
    value9 = models.TextField(blank=True, null=True)
    value10 = models.TextField(blank=True, null=True)
    value11 = models.TextField(blank=True, null=True)
    value12 = models.TextField(blank=True, null=True)
    value13 = models.TextField(blank=True, null=True)
    value14 = models.TextField(blank=True, null=True)
    value15 = models.TextField(blank=True, null=True)
    value16 = models.TextField(blank=True, null=True)
    value17 = models.TextField(blank=True, null=True)
    value18 = models.TextField(blank=True, null=True)
    value19 = models.TextField(blank=True, null=True)
    value20 = models.TextField(blank=True, null=True)
    value21 = models.TextField(blank=True, null=True)
    value22 = models.TextField(blank=True, null=True)
    value23 = models.TextField(blank=True, null=True)
    value24 = models.TextField(blank=True, null=True)
    value25 = models.TextField(blank=True, null=True)
    value26 = models.TextField(blank=True, null=True)
    value27 = models.TextField(blank=True, null=True)
    value28 = models.TextField(blank=True, null=True)
    value29 = models.TextField(blank=True, null=True)
    value30 = models.TextField(blank=True, null=True)
    value31 = models.TextField(blank=True, null=True)
    value32 = models.TextField(blank=True, null=True)
    value33 = models.TextField(blank=True, null=True)
    value34 = models.TextField(blank=True, null=True)
    value35 = models.TextField(blank=True, null=True)
    value36 = models.TextField(blank=True, null=True)
    value37 = models.TextField(blank=True, null=True)
    value38 = models.TextField(blank=True, null=True)
    value39 = models.TextField(blank=True, null=True)
    value40 = models.TextField(blank=True, null=True)
    value41 = models.TextField(blank=True, null=True)
    value42 = models.TextField(blank=True, null=True)
    value43 = models.TextField(blank=True, null=True)
    value44 = models.TextField(blank=True, null=True)
    value45 = models.TextField(blank=True, null=True)
    value46 = models.TextField(blank=True, null=True)
    value47 = models.TextField(blank=True, null=True)
    value48 = models.TextField(blank=True, null=True)
    value49 = models.TextField(blank=True, null=True)
    value50 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value_Table_2016_03_03'


class VideoinfoTable(models.Model):
    video_id = models.IntegerField(blank=True, null=True)
    video_name = models.TextField(blank=True, null=True)
    video_describe = models.TextField(blank=True, null=True)
    video_loginip = models.TextField(db_column='video_loginIp', blank=True, null=True)  # Field name made lowercase.
    video_loginport = models.TextField(db_column='video_loginPort', blank=True, null=True)  # Field name made lowercase.
    video_loginname = models.TextField(db_column='video_loginName', blank=True, null=True)  # Field name made lowercase.
    video_loginpwd = models.TextField(db_column='video_loginPwd', blank=True, null=True)  # Field name made lowercase.
    video_channelnum = models.IntegerField(db_column='video_channelNum', blank=True, null=True)  # Field name made lowercase.
    video_streamtype = models.IntegerField(db_column='video_streamType', blank=True, null=True)  # Field name made lowercase.
    video_linkmode = models.IntegerField(db_column='video_linkMode', blank=True, null=True)  # Field name made lowercase.
    video_speed = models.IntegerField(blank=True, null=True)
    create_time = models.TextField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    update_time = models.TextField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VideoInfo_Table'


class ZidianTable(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    describe = models.TextField(blank=True, null=True)
    mokuai_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ZiDian_Table'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GoodscatTable(models.Model):
    catid = models.IntegerField(db_column='catId', blank=True, null=True)  # Field name made lowercase.
    catname = models.TextField(db_column='catName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodsCat_Table'


class ShanghuTable(models.Model):
    sellerid = models.IntegerField(db_column='sellerId', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    managername = models.TextField(db_column='managerName', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=50, blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)
    addressnumber = models.IntegerField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shanghu_Table'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    principal_id = models.IntegerField(blank=True, null=True)
    diagram_id = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
