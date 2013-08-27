#coding=utf8
'''
Created on 2012-12-18

@author: damon
'''

from django.db import models
from django.contrib.auth.models import BaseUserManager

class BaseModelManager(BaseUserManager, models.Manager):
    #django.contrib.auth.models.BaseUserManager
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None