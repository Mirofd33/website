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


    

    
    
