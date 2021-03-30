# -*- coding: utf-8 -*-
import socket, struct
from cmdb.models import IpSource,Manufactory,jenkins_source
import re
from abc import abstractmethod, ABCMeta


def format_subnet(subnet_input):
    # netmask auto-append
    if subnet_input.find("/") == -1:
        return subnet_input + "/255.255.255.255"
    else:
        # change prefix to netmask
        subnet = subnet_input.split("/")
        if len(subnet[1]) < 3:
            mask_num = int(subnet[1])
            last_mask_num = mask_num % 8
            last_mask_str = ""
            for i in range(last_mask_num):
                last_mask_str += "1"
            if len(last_mask_str) < 8:
                for i in range(8 - len(last_mask_str)):
                    last_mask_str += "0"
            last_mask_str = str(int(last_mask_str, 2))
            if mask_num / 8 == 0:
                subnet = subnet[0] + "/" + last_mask_str + "0.0.0"
            elif mask_num / 8 == 1:
                subnet = subnet[0] + "/255." + last_mask_str + ".0.0"
            elif mask_num / 8 == 2:
                subnet = subnet[0] + "/255.255." + last_mask_str + ".0"
            elif mask_num / 8 == 3:
                subnet = subnet[0] + "/255.255.255." + last_mask_str
            elif mask_num / 8 == 4:
                subnet = subnet[0] + "/255.255.255.255"
            subnet_input = subnet
            # please input right ip address
        subnet_array = subnet_input.split("/")
        subnet_true = socket.inet_ntoa( \
            struct.pack("!I", struct.unpack("!I", socket.inet_aton(subnet_array[0]))[0] & \
                        struct.unpack("!I", socket.inet_aton(subnet_array[1]))[0])) \
                      + "/" + subnet_array[1]
        return subnet_true


def ip_in_subnet(ip, subnet):
    subnet = format_subnet(str(subnet))
    subnet_array = subnet.split("/")
    ip = format_subnet(ip + "/" + subnet_array[1])
    return ip == subnet


def env_dispatch(host_ip):
    env_list = IpSource.objects.all()
    for iplist in env_list:
        if ip_in_subnet(host_ip, iplist.subnet):
            ipsource = iplist.id
            break
        else:
            ipsource = 1
    return ipsource


def jenkins_env_dispatch(host_ip):
    env_list = jenkins_source.objects.all()
    for iplist in env_list:
        if ip_in_subnet(host_ip, iplist.subnet):
            ipsource = iplist.id
            break
        else:
            ipsource = 1
    return ipsource


def Manufactory_dispatch(host_manufacturer):
    list = Manufactory.objects.all()
    for vendor in list:
        match = re.search(vendor.vendor_name,host_manufacturer)
        if match:
            type = 2
            break
        else:
            type = 1
    return type


def change_metadata(medadata):
    new_meta = []
    for i in medadata:
        new_meta.append({
            'text': i[1],
            'value': i[0]
        })
    return new_meta

'''
设计模式实验
class ShapeFactory(object):
    #工厂类

    def getShape(self):
        return self.shape_name


class Circle(ShapeFactory):

    def __init__(self):
        self.shape_name = "Circle"

    def draw(self):
        print('draw circle')


class Rectangle(ShapeFactory):
    def __init__(self):
        self.shape_name = "Retangle"

    def draw(self):
        print("draw Rectangle")


class ShapeInterfaceFactory(object):
    #接口基类
    def create(self):
        #把要创建的工厂对象装配进来
        raise NotImplementedError


class ShapeCircle(ShapeInterfaceFactory):
    def create(self):
        return Circle()


class ShapeRectangle(ShapeInterfaceFactory):
    def create(self):
        return Rectangle()


shape_interface = ShapeCircle()
obj = shape_interface.create()
obj.getShape()
obj.draw()

shape_interface2 = ShapeRectangle()
obj2 = shape_interface2.create()
obj2.draw()

'''
