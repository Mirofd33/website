#!/usr/bin/env python
#-*- coding: utf-8 -*-
#update:2014-08-30 by liufeily@163.com

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from datetime import timedelta
from website import utils
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

@login_required
def Home(request):
   return render_to_response('home.html',locals(),RequestContext(request))

def About(request):
   return render_to_response('about.html',locals(),RequestContext(request))

#强制token超过一天过期，继承的rest的包
class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        if created or timezone.now() > (token.created + timedelta(utils.DAY)):
            token.delete()
            token = Token.objects.create(user=serializer.validated_data['user'])
            token.created = timezone.now()
            token.save()
        return Response({'token': token.key})
    

obtain_auth_token = ObtainAuthToken.as_view()

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)