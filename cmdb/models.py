# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.timezone import now
from publisher.models import Project
from django.contrib.auth.models import User


# Create your models here.
ASSET_STATUS = (
    (str(1), u"未使用"),
    (str(2), u"已改主机名"),
    (str(3), u"已重新接收key"),
    (str(4), u"已使用"),
    (str(5), u"其他"),
    )

ASSET_TYPE = (
    (str(1), u"物理机"),
    (str(2), u"虚拟机"),
    )


class env(models.Model):
    env_id = models.IntegerField(u"环境ID",)
    shortname = models.CharField(u"环境名称", max_length=30, null=True)
    fullname = models.CharField(u"环境名称", max_length=30, null=True)
    jenkins_url = models.CharField(u"jenkins_url", max_length=100, null=True)
    sftp_url = models.CharField(u"sftp_url", max_length=100, null=True)
    jenkins_username = models.CharField(u"jenkins用户名", max_length=100, null=True)
    jenkins_pwd = models.CharField(u"jenkins密码", max_length=100, null=True)
    jenkins_port = models.CharField(u"jenkins端口", max_length=100, null=True)


class Idc(models.Model):

    name = models.CharField(u"机房名称", max_length=30, null=True)
    address = models.CharField(u"机房地址", max_length=100, null=True)
    tel = models.CharField(u"机房电话", max_length=30, null=True)
    contact = models.CharField(u"客户经理", max_length=30, null=True)
    contact_phone = models.CharField(u"移动电话", max_length=30, null=True)
    jigui = models.CharField(u"机柜信息", max_length=30, null=True)
    ip_range = models.CharField(u"IP范围", max_length=30, null=True)
    bandwidth = models.CharField(u"接入带宽", max_length=30, null=True)

    class Meta:
        verbose_name = u'数据中心配置'
        verbose_name_plural = verbose_name


class HostGroup(models.Model):
    name = models.CharField(u"组名", max_length=30, unique=True)
    desc = models.CharField(u"描述", max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = u'设备组配置'
        verbose_name_plural = verbose_name


class IpSource(models.Model):
    vlan_id = models.IntegerField(u"VLAN_ID")
    subnet = models.CharField(max_length=30,null=True)
    describe = models.CharField(max_length=30,null=True)
    env = models.ForeignKey(env,blank=True,null=True)
    area = models.CharField(max_length=30,null=True)

    class Meta:
        verbose_name = u'环境配置'
        verbose_name_plural = verbose_name


class Host(models.Model):
    hostname = models.CharField(max_length=50, help_text=1, verbose_name=u"主机名")
    ip = models.GenericIPAddressField(u"IP", max_length=15)
    cpu_num = models.IntegerField(u"CPU数量", null=True, blank=True)
    memory = models.CharField(u"内存大小", max_length=30, null=True, blank=True)
    disk = models.CharField(u"硬盘大小", max_length=255, null=True, blank=True)
    position = models.CharField(u"所在位置", max_length=100, null=True, blank=True)
    escode = models.CharField(u"快速服务代码", max_length=100, null=True, blank=True)
    # project = models.ForeignKey(Project, verbose_name=u"项目组", blank=True, null=True, on_delete=models.SET_NULL)
    update_time = models.DateTimeField(u'最后修改日期', auto_now=True, blank=True)
    re_per = models.ForeignKey(User, verbose_name=u"负责人", blank=True, null=True, on_delete=models.SET_NULL)
    status = models.CharField(u"设备状态", choices=ASSET_STATUS, max_length=30, null=True, blank=True)
    uuid = models.CharField(max_length=50, verbose_name=u"唯一编号", unique=True)
    env = models.ForeignKey(IpSource, verbose_name=u"所属环境", on_delete=models.SET_NULL, null=True, blank=True)
    ilo_ip = models.GenericIPAddressField(u"其它IP", max_length=15, null=True, blank=True)
    asset_no = models.CharField(u"固定资产编号", max_length=50, null=True, blank=True)
    asset_type = models.CharField(u"设备类型", choices=ASSET_TYPE, max_length=30, null=True, blank=True)
    os = models.CharField(u"操作系统", max_length=100, null=True, blank=True)
    kernel = models.CharField(u"系统版本", max_length=100, null=True, blank=True)
    kernel_release = models.CharField(u"内核版本", max_length=100, null=True, blank=True)
    vendor = models.CharField(u"设备厂商", max_length=50, null=True, blank=True)
    cpu_model = models.CharField(u"CPU型号", max_length=100, null=True, blank=True)
    vip = models.GenericIPAddressField(u"VIP", max_length=15, null=True, blank=True)
    disks = models.CharField(u"硬盘信息", max_length=255, null=True, blank=True)
    sn = models.CharField(u"SN号 码", max_length=60, blank=True, null=True)
    group = models.ForeignKey(HostGroup, default=1, verbose_name=u"设备组", blank=True, null=True)
    idc = models.ForeignKey(Idc, verbose_name=u"所在数据中心", default=1, on_delete=models.SET_NULL, null=True, blank=True)
    memo = models.TextField(u"备注信息", max_length=200, null=True, blank=True)
    terminal_time = models.DateTimeField(u'过期日期', null=True,blank=False)
    create_time = models.DateTimeField(u'创建日期', default=now, blank=True, null=True,)
    mac = models.CharField(u"mac地址", max_length=100, null=True, blank=True)
    uplink = models.CharField(u"上联端口", max_length=100, null=True, blank=True)
    housecode = models.CharField(u"机房编号", max_length=100, null=True, blank=True) 
    server_id = models.CharField(u"服务器ID", max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = u'服务器配置'
        verbose_name_plural = verbose_name


class InterFace(models.Model):
    name = models.CharField(max_length=30)
    vendor = models.CharField(max_length=30,null=True)
    bandwidth = models.CharField(max_length=30,null=True)
    tel = models.CharField(max_length=30,null=True)
    contact = models.CharField(max_length=30,null=True)
    startdate = models.DateField()
    enddate = models.DateField()
    price = models.IntegerField(verbose_name=u'价格')

    class Meta:
        verbose_name = u'线路配置'
        verbose_name_plural = verbose_name


class Manufactory(models.Model):
    vendor_name = models.CharField(max_length=30)
    asset_type = models.CharField(u"设备类型", choices=ASSET_TYPE, max_length=30, null=True, blank=True)
      
      
class jenkins_source(models.Model):
    vlan_id = models.IntegerField(u"VLAN_ID")
    subnet = models.CharField(max_length=30,null=True)
    describe = models.CharField(max_length=30,null=True)
    env = models.ForeignKey(env,blank=True,null=True)
    area = models.CharField(max_length=30,null=True)

    class Meta:
        verbose_name = u'jenkins配置'
        verbose_name_plural = verbose_name
