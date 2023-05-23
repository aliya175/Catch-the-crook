from email.policy import default
from pyclbr import Class
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usertypes(models.Model):
    logid=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    utype=models.CharField(max_length=100)

class Publicuser(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    vid=models.CharField(max_length=100,null=True)
    aid=models.CharField(max_length=100,null=True)

class Station(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    district=models.CharField(max_length=100,null=True)

class Filerequest(models.Model):
    sender=models.CharField(max_length=100)
    receiver=models.ForeignKey(Station,on_delete=models.CASCADE,blank=True,null=True)
    fdate=models.DateField(auto_now=True)
    frequest=models.CharField(max_length=100)
    status=models.CharField(max_length=100)

class Filee(models.Model):
    frid=models.ForeignKey(Filerequest,on_delete=models.CASCADE,blank=True,null=True)
    file=models.ImageField()

class Criminal(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=100,null=True)
    height=models.CharField(max_length=100,null=True)
    weight=models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    contact=models.CharField(max_length=100,null=True)
    identification=models.CharField(max_length=100)
    nickname=models.CharField(max_length=100,null=True)
    optype=models.CharField(max_length=100,null=True)
    photo=models.ImageField()
    thumb=models.ImageField(null=True)

class Wantedlist(models.Model):
    crid=models.ForeignKey(Criminal,on_delete=models.CASCADE,blank=True,null=True)
    wdate=models.DateField(auto_now=True)
    status=models.CharField(max_length=100,null=True)

class Missingperson(models.Model):
    pid=models.ForeignKey(Publicuser,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    identification=models.CharField(max_length=100)
    estheight=models.CharField(max_length=100)
    estweight=models.CharField(max_length=100)
    physic=models.CharField(max_length=100)
    missdate=models.DateField()
    missplace=models.CharField(max_length=100)
    photo=models.ImageField(null=True)
    status=models.CharField(default='registered',null=True,max_length=100)

class Missingitems(models.Model):
    sid=models.ForeignKey(Station,on_delete=models.CASCADE,blank=True,null=True)
    pid=models.ForeignKey(Publicuser,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=100)
    identification=models.CharField(max_length=100)
    datemissing=models.DateField()
    placemissing=models.CharField(max_length=100)
    photo=models.ImageField()
    status=models.CharField(max_length=100)

class Complaint(models.Model):
    sid=models.ForeignKey(Station,on_delete=models.CASCADE,blank=True,null=True)
    pid=models.ForeignKey(Publicuser,on_delete=models.CASCADE,blank=True,null=True)
    comptitle=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    identification=models.CharField(max_length=100)
    cdate=models.DateField(auto_now=True)
    status=models.CharField(max_length=100)

class Missingpersonupdate(models.Model):
    mid=models.ForeignKey(Missingperson,on_delete=models.CASCADE,blank=True,null=True)
    stname=models.CharField(max_length=100,default="")
    udate=models.DateField(auto_now=True)
    updates=models.CharField(max_length=100)

class Missingthingsupdate(models.Model):
    mid=models.ForeignKey(Missingitems,on_delete=models.CASCADE,blank=True,null=True)
    udate=models.DateField(auto_now=True)
    updates=models.CharField(max_length=100)

class Complaintupdate(models.Model):
    cid=models.ForeignKey(Complaint,on_delete=models.CASCADE,blank=True,null=True)
    udate=models.DateField(auto_now=True)
    updates=models.CharField(max_length=100)

class Fir(models.Model):
    cid=models.ForeignKey(Complaint,on_delete=models.CASCADE,blank=True,null=True)
    crid=models.ForeignKey(Criminal,on_delete=models.CASCADE,blank=True,null=True)
    firdate=models.DateField(auto_now=True)
    lawapplied=models.CharField(max_length=100)
    details=models.CharField(max_length=100)

class Hearing(models.Model):
    firid=models.ForeignKey(Fir,on_delete=models.CASCADE,blank=True,null=True)
    heardate=models.DateField() 
    updates=models.CharField(max_length=100)

class Punishment(models.Model):
    hid=models.ForeignKey(Hearing,on_delete=models.CASCADE,blank=True,null=True)
    punishment=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)












