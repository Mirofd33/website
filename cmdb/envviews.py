# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import utils
from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from forms import IPsourceForm
from django.views.generic import *
from cmdb.models import Host, IpSource,Project
import logging
import json

class IpSourceView(View):
    form_class = IPsourceForm
    template_name = "cmdb/env.list.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        return render(request, self.template_name, {'form': form})


