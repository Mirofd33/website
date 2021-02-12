# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils.timezone import now



# Create your models here.

PROJECT_STATUS = (
    ('0', u"未初始化"),
    ('1', u"已改主机名"),
    ('2', u"已重新接收key"),
    ('3', u"初始化成功")
    )

PUBLISH_STATUS = (
    ('0', u"发布中"),
    ('1', u"已发送"),
    ('2', u"发布失败"),
    ('3', u"丢弃"),
    )

PACKAGE_STATUS = (
    ('0', u"失效"),
    ('1', u"启用"),
    )
PUBLISHE_TYPE = (
    ('0', u"tomcat"),
    ('1', u"springboot"),
    )

PROJECT_NATURE = (
    ('0', u"一般项目"),
    ('1', u"重要项目"),
    )

    
#服务管理models

SERVICE_STATUS = (
    ('0', u"未初始化"),
    ('1', u"已初始化"),
    )
IP_STATUS = (
    ('0', u"未使用"),
    ('1', u"已使用"),
    )
BUILD_STATUS = (
    ('0', u"构建中"),
    ('1', u"构建完成"),
    ('2', u"构建失败"),
    )
class serviceType(models.Model):
    name = models.CharField(u"服务类型", max_length=100, null=True, blank=True)
    
class OutterIpSource(models.Model):
    ipAddress = models.GenericIPAddressField(u"IP地址", max_length=100, null=False, blank=False)
    subnet = models.CharField(u"子网掩码", max_length=100, null=True, blank=True)
    gateway = models.CharField(u"网关", max_length=100, null=True, blank=True)
    belong = models.CharField(u"子网掩码", max_length=100, null=True, blank=True)
    fuction = models.CharField(u"用途", max_length=100, null=True, blank=True)
    isp = models.CharField(u"ISP", max_length=100, null=True, blank=True)
    status = status = models.CharField(u"包状态", choices=IP_STATUS, max_length=30, null=True, blank=True)


class service(models.Model):
    name = models.CharField(u"服务名", max_length=100, null=True, blank=True)
    name_en = models.CharField(u"服务英文名", max_length=100, null=False, blank=True)
    url = models.CharField(u"url", max_length=100, null=True, blank=True)
    ip = models.CharField(u"ip", max_length=100, null=True, blank=True)
    innerUrl = models.CharField(u"url", max_length=100, null=True, blank=True)
    innerIp = models.CharField(u"ip", max_length=100, null=True, blank=True)
    env = models.IntegerField(verbose_name=u"服务环境",blank=True,null=True)
    hosts = models.CharField(u"主机", max_length=100, null=True, blank=True)
    status = models.CharField(u"状态", choices=SERVICE_STATUS, max_length=30, null=True, blank=True)
    createTime = models.DateTimeField(blank=True,null=True)
    serviceType = models.ForeignKey(serviceType,verbose_name=u"服务类型",blank=True,null=True,on_delete=models.SET_NULL)
    OutterIpSource = models.ForeignKey(OutterIpSource,verbose_name=u"外部IP地址",blank=True,null=True,on_delete=models.SET_NULL)


class serviceToHost(models.Model):
    service = models.ForeignKey(service,verbose_name=u"服务名称", related_name="sth" ,blank=True,null=True)
    host = models.IntegerField()
    
class projectType(models.Model):
    name = models.CharField(u"项目类型", max_length=100, null=True, blank=True)    
    
    
class Project(models.Model):
    name = models.CharField(u"名称", max_length=30, unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=u"负责人",blank=True,null=True,on_delete=models.SET_NULL)
    parent = models.ForeignKey('self',verbose_name = u'父节点',null = True,blank = True,help_text = u'如果添加的是子菜单，请选择父菜单',on_delete=models.SET_NULL)
    show = models.BooleanField(verbose_name=u'是否显示',default=True,help_text=u'菜单是否显示，默认添加不显示')
    url = models.CharField(max_length=300,verbose_name=u'菜单url地址',null=True,blank=True,default='javascript:void(0)',help_text=u'是否给菜单设置一个url地址')
    priority = models.IntegerField(verbose_name=u'显示优先级',null=True,blank=True,default=-1,help_text=u'菜单的显示顺序，优先级越大显示越靠前')
    permission_id = models.IntegerField(verbose_name=u'权限编号',help_text=u'给菜单设置一个编号，用于权限控制',error_messages={'field-permission_id': u'只能输入数字'})
    service = models.CharField(u"服务", max_length=100, blank=True,null=True)
    describe = models.CharField(u"描述", max_length=100,blank=True,null=True)
    env = models.IntegerField(verbose_name=u"服务环境",blank=True,null=True)
    rchost = models.CharField(u"RC主机", max_length=100, blank=True,null=True)
    status = models.CharField(u"项目状态", choices=PROJECT_STATUS, max_length=30, null=True, blank=True)
    createTime = models.DateTimeField(blank=True,null=True)
    name_en = models.CharField(u"英文名", max_length=100)
    projectType = models.ForeignKey(projectType,verbose_name=u"项目类型",blank=True,null=True,on_delete=models.SET_NULL)
    publish_type = models.CharField(u"发布类型", choices=PUBLISHE_TYPE, max_length=30, null=True, blank=True)
    project_nature = models.CharField(u"项目属性", choices=PROJECT_NATURE, max_length=30, null=True, blank=True)
    jid = models.CharField(u"任务编号", max_length=255, blank=True,null=True)
    

    class Meta:
        verbose_name = u"项目配置"
        verbose_name_plural = u"项目配置"
        ordering = ["-priority", "id"]

    
class projectToHost(models.Model):
    Project = models.ForeignKey(Project,verbose_name=u"项目名称",blank=True,null=True)
    host = models.IntegerField()
    
class projectToService(models.Model):
    Project = models.ForeignKey(Project,verbose_name=u"项目名称",blank=True,null=True)
    service = models.IntegerField()
    
class version(models.Model):
    build_number = models.CharField(u"构建号", max_length=100, null=True, blank=True)
    Project = models.ForeignKey(Project,verbose_name=u"项目名称",blank=True,null=True,on_delete=models.CASCADE)
    jenkins_ver = models.CharField(u"jenkins版本", max_length=100, null=True, blank=True)
    mdno = models.CharField(u"md5版本", max_length=100, null=True, blank=True)
    ftpurl = models.CharField(u"ftpurl",max_length=100, null=True, blank=True)
    createTime = models.DateTimeField(blank=True,null=True)
    finishTime = models.DateTimeField(blank=True,null=True)
    status = models.CharField(u"构建状态", choices=BUILD_STATUS, max_length=30, null=True, blank=True)
    bagName = models.CharField(u"包名",max_length=100, null=True, blank=True)
    
class pubcmd(models.Model):
    pubparam = models.CharField(u"运行参数", max_length=100, null=True, blank=True)
    env = models.IntegerField(verbose_name=u"环境",blank=True,null=True)
    
    class Meta:
        verbose_name = u'发布命令配置'
        verbose_name_plural = verbose_name

#发布管理models  
class publisher(models.Model):
    Project = models.ForeignKey(Project,verbose_name=u"项目名称",blank=False,null=True)
    version = models.ForeignKey(version,verbose_name=u"构建版本",blank=True,null=True)
    publish_no = models.CharField(u"发布号", max_length=100, blank=True,null=True)
    createTime = models.DateTimeField(default=now,blank=True,null=True)
    runtime = models.DateTimeField(blank=True,null=True)
    pubhosts = models.CharField(u"发布主机", max_length=100, blank=False,null=True)
    orderNo = models.IntegerField(u"票号", blank=True,null=True)
    status = models.CharField(u"发布状态", choices=PUBLISH_STATUS, max_length=30, null=True, blank=True)
    env = models.IntegerField(verbose_name=u"服务环境",blank=True,null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=u"负责人",blank=True,null=True,on_delete=models.SET_NULL)
    type = models.CharField(u"发布类型", choices=PUBLISHE_TYPE, max_length=30, null=True, blank=True)
    jid = models.CharField(u"任务编号", max_length=255, blank=True,null=True)
    pubcmd = models.ForeignKey(pubcmd,verbose_name=u"运行参数",blank=True,null=True,on_delete=models.SET_NULL)
    
class publisherToHost(models.Model):
    publisher = models.ForeignKey(publisher,verbose_name=u"发布名称",blank=True,null=True)
    host = models.IntegerField()
    
    
class version_backup(models.Model):
    build_number = models.CharField(u"构建号", max_length=100, null=True, blank=True)
    Project = models.ForeignKey(Project,verbose_name=u"项目名称",blank=True,null=True,on_delete=models.CASCADE)
    ftpurl = models.CharField(u"ftpurl",max_length=100, null=True, blank=True)
    createTime = models.DateTimeField(blank=True,null=True)
    finishTime = models.DateTimeField(blank=True,null=True)
    status = models.CharField(u"构建状态", choices=BUILD_STATUS, max_length=30, null=True, blank=True)
    bagName = models.CharField(u"包名",max_length=100, null=True, blank=True)
    
class svgelement(models.Model):
    class Meta:
        managed = False
        db_table = "svgelement"

    pid = models.CharField(u"项目", primary_key=True,max_length=255)
    sid = models.CharField(u"服务", max_length=255)
    hid = models.CharField(u"主机", max_length=255)
    hname = models.CharField(u"主机名", max_length=255)
    group = models.CharField(u"组", max_length=255)

    

    
    
