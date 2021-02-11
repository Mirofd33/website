from django.db import models


class Jids(models.Model):
    class Meta:
        db_table = 'jids'
    jid = models.CharField(max_length=225, blank=True, unique=True)
    load = models.TextField(blank=True)


class Salt_returns(models.Model):
    class Meta:
        managed = False
        db_table = 'salt_returns'
        
    fun = models.CharField(max_length=50, blank=True)
    jid = models.CharField(max_length=255, blank=True)
    returns = models.TextField(db_column='return',blank=True)
    id = models.CharField(max_length=255, blank=True,primary_key=True)
    success = models.CharField(max_length=10, blank=True)
    full_ret = models.TextField(blank=True)
    alter_time = models.DateTimeField(auto_created=True)


class Salt_events(models.Model):
    class Meta:
        db_table = 'salt_events'
    tag = models.CharField(max_length=255, blank=True)
    data = models.TextField(blank=True)
    alter_time = models.DateTimeField(auto_created=True)
    minion_id = models.CharField(max_length=255, blank=True)


class Salt_grains(models.Model):
    class Meta:
        db_table = 'salt_grains'
    minion_id = models.CharField(max_length=255, null=True, blank=True)
    grains = models.TextField(null=True, blank=True)



