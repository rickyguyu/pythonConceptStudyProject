# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Businessinfo(models.Model):
    idbusinessinfo = models.AutoField(db_column='IdBusinessInfo', primary_key=True)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=45)  # Field name made lowercase.
    week = models.CharField(db_column='Week', max_length=20, blank=True, null=True)  # Field name made lowercase.
    estimated_load_date = models.DateField(db_column='Estimated_Load_Date', blank=True, null=True)  # Field name made lowercase.
    pre_etd = models.DateField(db_column='Pre_ETD', blank=True, null=True)  # Field name made lowercase.
    etd = models.DateField(db_column='ETD', blank=True, null=True)  # Field name made lowercase.
    eta = models.DateField(db_column='ETA', blank=True, null=True)  # Field name made lowercase.
    vessel_voyage = models.CharField(db_column='Vessel_Voyage', max_length=45)  # Field name made lowercase.
    pol = models.CharField(db_column='POL', max_length=20)  # Field name made lowercase.
    pod = models.CharField(db_column='POD', max_length=20)  # Field name made lowercase.
    businessinfocol = models.CharField(db_column='BusinessInfocol', max_length=45)  # Field name made lowercase.
    numctrs = models.IntegerField(db_column='NumCtrs')  # Field name made lowercase.
    type_ctrs = models.CharField(db_column='Type_Ctrs', max_length=10)  # Field name made lowercase.
    booking_no = models.CharField(db_column='Booking_No', max_length=45)  # Field name made lowercase.
    master_no = models.CharField(db_column='Master_No', max_length=45, blank=True, null=True)  # Field name made lowercase.
    num_hbls = models.IntegerField(db_column='Num_HBLs', blank=True, null=True)  # Field name made lowercase.
    container_no = models.CharField(db_column='Container_No', max_length=45, blank=True, null=True)  # Field name made lowercase.
    shipping_line = models.CharField(db_column='Shipping_Line', max_length=20)  # Field name made lowercase.
    freeddday = models.IntegerField(db_column='FreeDDday')  # Field name made lowercase.
    cost_org = models.FloatField(db_column='Cost_Org', blank=True, null=True)  # Field name made lowercase.
    sale_org = models.FloatField(db_column='Sale_Org', blank=True, null=True)  # Field name made lowercase.
    venta_dest = models.FloatField(db_column='Venta_Dest', blank=True, null=True)  # Field name made lowercase.
    costhbl_dest_description = models.CharField(db_column='CostHBL_Dest_Description', max_length=45, blank=True, null=True)  # Field name made lowercase.
    costhbl_dest = models.FloatField(db_column='CostHBL_Dest', blank=True, null=True)  # Field name made lowercase.
    costhbl_dest_status = models.CharField(db_column='CostHBL_Dest_Status', max_length=10)  # Field name made lowercase.
    topaid_org_description = models.CharField(db_column='Topaid_Org_Description', max_length=45, blank=True, null=True)  # Field name made lowercase.
    topaid_org = models.FloatField(db_column='Topaid_Org', blank=True, null=True)  # Field name made lowercase.
    topaid_status = models.CharField(db_column='Topaid_Status', max_length=10)  # Field name made lowercase.
    toinvoice_dest_description = models.CharField(db_column='ToInvoice_Dest_Description', max_length=45, blank=True, null=True)  # Field name made lowercase.
    toinvoice_dest = models.FloatField(db_column='ToInvoice_Dest', blank=True, null=True)  # Field name made lowercase.
    toinvoice_dest_status = models.CharField(db_column='ToInvoice_Dest_Status', max_length=10)  # Field name made lowercase.
    profit = models.FloatField(blank=True, null=True)
    hbl_canjeado_status = models.CharField(db_column='HBL_Canjeado_Status', max_length=10)  # Field name made lowercase.
    devolution_ctrs_inidate = models.DateField(db_column='Devolution_Ctrs_IniDate', blank=True, null=True)  # Field name made lowercase.
    devolution_ctrs_findate = models.DateField(db_column='Devolution_Ctrs_FinDate', blank=True, null=True)  # Field name made lowercase.
    operation_status = models.CharField(db_column='Operation_Status', max_length=10)  # Field name made lowercase.
    bl_type = models.CharField(db_column='BL_Type', max_length=3, blank=True, null=True)  # Field name made lowercase.
    release_type = models.CharField(db_column='Release_Type', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'businessinfo'


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
    id = models.BigAutoField(primary_key=True)
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


class PollsUserinfo(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    user_name = models.CharField(max_length=20, blank=True, null=True)
    user_pwd = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'polls_userinfo'
