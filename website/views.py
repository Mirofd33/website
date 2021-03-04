#!/usr/bin/env python
#-*- coding: utf-8 -*-
#auth:jusding

from rest_framework import parsers, renderers, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from website import utils
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User
from website.serializers import UserSerializer
from django.apps import apps
from rest_framework.views import APIView
import json

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
        
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class listmodels(APIView):

    def get(self, request):
        #获取model的verbose_name和name的字段
        appname = request.GET['appname']
        modelname = request.GET['modelname']
        exclude = {'disks','project'}

        if appname and modelname:
            modelobj = apps.get_model(appname, modelname)
            filed = modelobj._meta.fields
            fielddic = []
            params = [f for f in filed if f.name not in exclude]
            for i in params:
                #fielddic[i.name] = i.verbose_name
                fielddic.append({
                    'value': i.name,
                    'text': i.verbose_name,
                })
        return Response(json.dumps(fielddic))
