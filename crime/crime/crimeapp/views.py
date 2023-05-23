from datetime import date
from email import message
from poplib import CR
from tkinter import S
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from datetime import datetime

# Create your views here.


def home(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    data = Wantedlist.objects.all()
    data1 = Criminal.objects.all()
    print(data1)
    return render(request,"commonhome.html",{"data":data,"data1":data1})

def userhome(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    name=request.session["name"] 
    return render(request,"userhome.html",{'name':name})

def courthome(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    return render(request,"courthome.html")

def adminhome(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    return render(request,"adminhome.html")

def stationhome(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    name=request.session["name"] 
    return render(request,"stationhome.html",{'name':name})


def login(request):
    """ 
        The function to check login process 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        email=request.POST.get("uname")
        pwd=request.POST.get("pswd")
        s=User.objects.get(username=email)
        user = authenticate(username=email, password=pwd)
        if user is None:
            messages.info(request,'Invalid Username and Password')
        else:
            s=User.objects.get(username=email)
            if email == "court@gmail.com" and pwd == "court@123":
                    return redirect("/courthome")
            elif s.is_superuser == 1:
                if email == "admin@gmail.com":
                    return redirect("/adminhome")
                else:
                    messages.info(request, 'Something went Wrong')
                    return redirect("/login")    
            else:
                if s.is_staff == 0:
                        r = Usertypes.objects.get(logid=s.id)
                        if r.utype == 'user':
                            us=Publicuser.objects.get(email=s.email)
                            request.session["id"] = us.id
                            request.session["name"] = us.name
                            return redirect("/userhome") 
                        elif r.utype == 'police':
                            us=Station.objects.get(email=s.email)
                            request.session["id"] = us.id
                            request.session["name"] = us.name
                            return redirect("/policehome")
                        else:
                            messages.info(request, 'Something went Wrong')
                        return redirect("/login")
                else:
                        messages.info(request, 'Something went Wrong')
                        return redirect("/login")

    return render(request,"login.html",{"msg":msg})


def stationreg(request):
    if(request.POST):
        name = request.POST["name"]
        address = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        district = request.POST["district"]
        uname = request.POST["uname"]
        password = request.POST["pass"]
        user = authenticate(username=uname, password=password)
        if user is None:
            try:
                r = Station.objects.create(
                    name=name,address=address,email=email,contact=phno,district=district)
                r.save
            except:
                messages.info(request,'Sorry register error')
            else:
                try:
                    u = User.objects.create_user(
                        password=password, username=uname, is_superuser=0, is_active=1, email=email)
                    ut=Usertypes(logid=u,utype="police")
                    u.save()
                    ut.save()
                except:
                    messages.info(request,'Sorry Login Process Error')
                else:
                    messages.info(request,'Registered Successfully')
                    return redirect("/stationreg")
        else:
                messages.info(request,'Already Registered')
                return redirect("/stationreg")
    return render(request, 'adminaddstation.html')


def viewstation(request):
    st=Station.objects.all()
    return render(request,"viewstation.html",{'data':st})

def adminviewpublic(request):
    # f=Filerequest.objects.all().values('id')
    # fr=Filerequest.objects.all()
    # fg=Filee.objects.filter(frid__in=f).values_list('frid',flat=True)
    au=Publicuser.objects.all().values('email')
    st=Publicuser.objects.all()
    sg=User.objects.filter(is_active=1,email__in=au).values_list('email',flat=True)
    return render(request,"adminviewpublic.html",{'data':st,'sg':sg})

def adminsendfilestation(request):
    data = Station.objects.all()
    if(request.POST):
        st = request.POST["dis"]
        sub = request.POST["sub"]
        station=Station.objects.get(id=st)
        try:
            tv=Filerequest.objects.create(sender='admin',receiver=station,frequest=sub,status='requested')
            tv.save
        except:
            messages.info(request,'Some error occured')
        else:
            messages.info(request,'File Request Added Successfully')
            return redirect("/adminsendfilestation")

    return render(request, 'adminstationsendfile.html ',{'data': data})


def adminviewfiles(request):
    f=Filerequest.objects.all().values('id')
    fr=Filerequest.objects.all()
    fg=Filee.objects.filter(frid__in=f).values_list('frid',flat=True)
    return render(request,"adminviewfiles.html",{'fr':fr,'fg':fg})

def stationaddcriminaldetails(request):
    data = Station.objects.all()
    if(request.POST):
        name = request.POST.get("name")
        age = request.POST.get("age")
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        gender = request.POST['r1']
        addr = request.POST.get("addr")
        phone = request.POST.get("phno")
        nick = request.POST.get("nickname")
        mode = request.POST.get("mode")
        idmark = request.POST.get("idmark")
        photo =  request.FILES["f1"]
        thumb =  request.FILES["f11"]
        uid = request.session["id"]
        try:
            tv=Criminal.objects.create(name=name,age=age,height=height,weight=weight,
            gender=gender,address=addr,contact=phone,identification=idmark,nickname=nick,optype=mode,photo=photo,thumb=thumb)
            tv.save
        except:
            messages.info(request,'Some error occured')
        else:
            messages.info(request,'Details Added Successfully')
            return redirect("/stationaddcriminaldetails")

    return render(request, 'stationaddcriminal.html',{'data': data})

def userreg(request):
    """ 
        The function to register user
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    
    if(request.POST):
        name = request.POST["name"]
        address = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        vid = request.POST["vid"]
        aid = request.POST["aid"]
        uname = request.POST["uname"]
        password = request.POST["pass"]
        user = authenticate(username=uname, password=password)
        if user is  None:
            try:
                r = Publicuser.objects.create(
                    name=name,address=address,email=email,contact=phno,vid=vid,aid=aid)
                r.save()
            except:
                messages.info(request, 'Sorry some error occured')
            else:
                try:
                    u = User.objects.create_user(
                        password=password, username=uname, is_superuser=0, is_active=1, email=email)
                    ut=Usertypes(logid=u,utype="user")
                    u.save()
                    ut.save()
                except:
                    messages.info(request, 'Sorry some error occured')
                else:
                    messages.info(request,'Registration successfull')
                    return redirect("/")
        else:
             msg="Already Registered" 
             return redirect("/")          
    return render(request,"userregistration.html")

def stationaddwantedlist(request):
    val=Wantedlist.objects.all().values_list("crid")
    data = Criminal.objects.exclude(id__in=val)
    print(data)
    if(request.POST):
        st = request.POST.get("dis")
        crm=Criminal.objects.get(id=st)
        try:
            tv = Wantedlist.objects.create(crid=crm,status='added')
            tv.save
        except:
            messages.info(request,'Some error Occured')  
        else:
            messages.info(request,'Added Successfully')
            return redirect("/stationaddwantedlist")

    return render(request, 'stationaddwantedlist.html ', {'data': data})

def stationviewfilerequest(request):
    fr=Filerequest.objects.all()
    return render(request,"stationviewfilerequest.html",{'fr':fr})

def stationaddfile(request):

    id=request.GET.get('id')
    req=Filerequest.objects.get(id=id)
    if(request.POST):
        doc=request.FILES['f1']
        try:
            tv = Filee.objects.create(frid=req,file=doc)
            tv.save
            Filerequest.objects.filter(id=id).update(status='responded')
        except:
            messages.info(request,'Some error Occured')  
        else:
            messages.info(request,'File Added Successfully')    
        return redirect("/stationviewfilerequest")

    return render(request, 'stationaddfile.html ')

def stationviewcriminal(request):
    if (request.POST):
        cr = request.POST.get("search")
        data = Criminal.objects.filter(Q(name__contains=cr) | Q(nickname__contains=cr)
         | Q(identification__contains=cr) | Q(optype__contains=cr))
        return render(request,'stationviewcriminal.html ', {'data': data})
    return render(request, 'stationviewcriminal.html ')


def adminviewcriminal(request):
    if (request.POST):
        cr = request.POST.get("search")
        data = Criminal.objects.filter(Q(name__contains=cr) | Q(nickname__contains=cr)
         | Q(identification__contains=cr) | Q(optype__contains=cr))
        return render(request,'adminviewcriminal.html ', {'data': data})
    return render(request, 'adminviewcriminal.html ')

def complaint(request):
    data=""
    uid=request.session['id']
    pid=Publicuser.objects.get(id=uid)
    if(request.POST):
        dst=request.POST['district']
        data=Station.objects.filter(district__contains=dst)
    return render(request, 'customeraddcomplaints.html',{'data':data})

def complaintpost(request):    
    if(request.POST):
        st=request.POST['station']
        comp=request.POST['comp']
        desc=request.POST['desc']
        id=request.POST['id']
        uid=request.session['id']
        pid=Publicuser.objects.get(id=uid)
        stid=Station.objects.get(id=st)
        try:
            Complaint.objects.create(sid=stid,pid=pid,comptitle=comp,desc=desc,identification=id,status='registered')
        except:
            messages.info(request,"Some eroor occured")
            return redirect("/complaint")
        else:
            messages.info(request,"Complaint Added Successfully")
            return redirect("/complaint")





def userviewcomplaintstatus(request):
    cid = request.session["id"]
    cmp=Complaint.objects.filter(pid__id=cid)
    cu = Complaintupdate.objects.filter(cid__pid__id=cid)
    return render(request, 'userviewcomplaintstatus.html', {'cmp':cmp,'cu':cu})

def useraddmissingitem(request):
    data=Station.objects.all()
    uid=request.session['id']
    pid=Publicuser.objects.get(id=uid)
    dt=date.today()
    print(dt)
    if(request.POST):
        dis=request.POST['dis']
        mitem=request.POST['mitem']
        mdate=request.POST['mdate']
        mdesc=request.POST['mdesc']
        place=request.POST['place']
        photo=request.FILES['img']
        dt1 = datetime.strptime(mdate, '%Y-%m-%d')
        print(mdate)
        if dt1.date() > dt:
            messages.info(request,"Invalid Date")
            return redirect("/useraddmissingitem")
        stid=Station.objects.get(id=dis)
        try:
            mi=Missingitems.objects.create(sid=stid,pid=pid,name=mitem,identification=mdesc,datemissing=mdate,placemissing=place,photo=photo,status='registered')
            mi.save
        except:
            messages.info(request,"Some eroor occured")
        else:
            messages.info(request,"Data Added Successfully")
            return redirect("/useraddmissingitem")
    return render(request, 'useraddmissingitem.html',{'data':data})

def useraddmissingperson(request):
    data=Station.objects.all()
    uid=request.session['id']
    pid=Publicuser.objects.get(id=uid)
    dt=date.today()
    print(dt)
    if(request.POST):
        name=request.POST['name']
        address=request.POST['address']
        contact=request.POST['contact']
        identification=request.POST['identification']
        estheight=request.POST['estheight']
        estweight=request.POST['estweight']
        physic=request.POST['physic']
        missdate=request.POST['missdate']
        missplace=request.POST['missplace']
        photo=request.FILES['photo']
        dt1 = datetime.strptime(missdate,'%Y-%m-%d')
        print(missdate)
        if dt1.date() > dt:
            messages.info(request,"Invalid Date")
            return redirect("/useraddmissingitem")
        try:
            mp=Missingperson.objects.create(pid=pid,name=name,address=address,contact=contact,identification=identification,estheight=estheight,estweight=estweight,physic=physic,missdate=missdate,missplace=missplace,photo=photo)
            mp.save
        except:
            messages.info(request,"Some eroor occured")
        else:
            messages.info(request,"Data Added Successfully")
            return redirect("/useraddmissingitem")
    return render(request, 'useraddmissingperson.html',{'data':data})

def userviewmissingstatus(request):
    cid = request.session["id"]
    cmp=Missingitems.objects.filter(pid__id=cid)
    cu = Missingthingsupdate.objects.filter(mid__pid__id=cid)
    return render(request, 'userviewmissingstatus.html', {'cmp':cmp,'cu':cu})

def userviewmissingpersonstatus(request):
    cid = request.session["id"]
    cmp=Missingperson.objects.filter(pid__id=cid)
    cu = Missingpersonupdate.objects.filter(mid__pid__id=cid)
    return render(request, 'userviewmissingpersonstatus.html', {'cmp':cmp,'cu':cu})
    
def userviewwantedlist(request):
    data = Wantedlist.objects.all()
    return render(request, 'userviewwantedlist.html', {'data': data})

def adminviewwantedlist(request):
    data = Wantedlist.objects.all()
    return render(request, 'adminviewwantedlist.html', {'data': data})

def stationviewwantedlist(request):
    data = Wantedlist.objects.all()
    return render(request, 'stationviewwantedlist.html', {'data': data})

def stationviewcomplaint(request):
    id=request.session['id']
    data = Complaint.objects.filter(sid=id).exclude(status='completed')
    return render(request, 'stationviewcomplaints.html', {'data': data})

def stationviewmissingitem(request):
    id=request.session['id']
    data = Missingitems.objects.filter(sid=id).exclude(status='completed')
    return render(request, 'stationviewmissingdetails.html', {'data': data})

def adminviewmissingitems(request):
    data = Missingitems.objects.exclude(status='completed')
    return render(request, 'adminviewmissingdetails.html', {'data': data})

def adminviewhearingdetails(request):
    h=Hearing.objects.all().values('id')
    d=Punishment.objects.filter(hid__in=h).values_list('hid',flat=True)
    data = Hearing.objects.all()
    return render(request, 'adminviewhearingdetails.html', {'data': data,'d':d})

def adminviewpunishment(request):
    id=request.GET.get('id')
    data = Punishment.objects.filter(hid=id)
    return render(request, 'adminviewpunishment.html', {'data': data})

def stationviewpunishment(request):
    data = Punishment.objects.all()
    return render(request, 'stationviewpunishment.html', {'data': data})

def userviewpunishment(request):
    data = Punishment.objects.all()
    return render(request, 'userviewpunishment.html', {'data': data})

def userviewhearings(request):
    data = Hearing.objects.filter(heardate__gte=date.today())
    return render(request, 'userviewhearings.html', {'data': data})

def adminviewfirdetails(request):
    id=request.GET.get('id')
    data = Fir.objects.filter(id=id)
    return render(request, 'adminviewfirdetails.html', {'data': data})

def courtviewfir(request):
    data = Fir.objects.all
    return render(request, 'courtviewfir.html', {'data': data})


def stationviewmissingperson(request):
    data = Missingperson.objects.exclude(status='completed')
    return render(request, 'stationviewmissingperson.html', {'data': data})

def adminviewmissingpersons(request):
    data = Missingperson.objects.exclude(status='completed')
    return render(request, 'adminviewmissingperson.html', {'data': data})

def stationaddcomplaintresponse(request):
    cid=request.GET.get('id')
    data = Complaint.objects.get(id=cid)
    if (request.POST):
        upd=request.POST['upd']
        status=request.POST['r1']
        try:
            cu=Complaintupdate.objects.create(cid=data,updates=upd)
            cu.save
            Complaint.objects.filter(id=cid).update(status=status)
        except:
            messages.info(request,'some error occured')
        else:
            messages.info(request,'successfully Updated') 
            return redirect("/stationviewcomplaint")   
    return render(request, 'stationaddcomplaintstatus.html', {'data': data})

def stationaddmissitemresponse(request):
    cid=request.GET.get('id')
    data = Missingitems.objects.get(id=cid)
    if (request.POST):
        upd=request.POST['upd']
        status=request.POST['r1']
        try:
            cu=Missingthingsupdate.objects.create(mid=data,updates=upd)
            cu.save
            Missingitems.objects.filter(id=cid).update(status=status)
        except:
            messages.info(request,'some error occured')
        else:
            messages.info(request,'successfully Updated') 
            return redirect("/stationviewmissingitem")   
    return render(request, 'stationaddmissingstatus.html', {'data': data})

def stationaddmisspersonresponse(request):
    cid=request.GET.get('id')
    data = Missingperson.objects.get(id=cid)
    sid=request.session['id']
    st=Station.objects.get(id=sid)
    if (request.POST):
        upd=request.POST['upd']
        status=request.POST['r1']
        try:
            cu=Missingpersonupdate.objects.create(mid=data,stname=st.name,updates=upd)
            cu.save
            Missingperson.objects.filter(id=cid).update(status=status)
        except:
            messages.info(request,'some error occured')
        else:
            messages.info(request,'successfully Updated') 
            return redirect("/stationviewmissingperson")   
    return render(request, 'stationaddmisspersonresponse.html', {'data': data,'st':st})

def userviewcomplaintresponse(request):
    cid=request.GET.get('id')
    data = Complaintupdate.objects.filter(cid__id=cid)
    return render(request, 'userviewcomplaintresponse.html', {'data': data})

def userviewmissingitemresponse(request):
    cid=request.GET.get('id')
    data = Missingthingsupdate.objects.filter(mid__id=cid)
    return render(request, 'userviewmissingitemresponse.html', {'data': data})

def userviewmpersonupdate(request):
    cid=request.GET.get('id')
    data = Missingpersonupdate.objects.filter(mid__id=cid)
    return render(request, 'userviewmpersonupdate.html', {'data': data})

def removewanted(request):
    id=request.GET.get('id')
    data = Wantedlist.objects.filter(id=id).delete()
    return redirect("/stationviewwantedlist")

def stationaddcrimedetails(request):
    cid=Complaint.objects.filter(status='completed').values('id')
    d = Fir.objects.filter(cid__in=cid).values_list('cid',flat=True)
    print(d)
    data=Complaint.objects.filter(status='completed')
    return render(request, 'stationaddcrimedetails.html', {'data': data,'d':d})

def stationaddfir(request):
    cid=request.GET.get('id')
    cr=Criminal.objects.all()
    data = Complaint.objects.get(id=cid)
    if (request.POST):
        crm=request.POST['crm']
        det=request.POST['det']
        law=request.POST['law']
        crid=Criminal.objects.get(id=crm)
        try:
            cu=Fir.objects.create(cid=data,crid=crid,lawapplied=law,details=det)
            cu.save
        except:
            messages.info(request,'some error occured')
        else:
            messages.info(request,'Fir Added') 
            return redirect("/stationaddcrimedetails")   
    return render(request, 'stationaddfir.html', {'cr':cr})

def stationaddheardetails(request):
    fid=Fir.objects.all().values('id')
    d = Hearing.objects.filter(firid__in=fid).values_list('firid',flat=True)
    print(d)
    data=Fir.objects.all()
    return render(request, 'stationaddheardetails.html', {'data': data,'d':d})

def stationaddhearing(request):
    fid=request.GET.get('id')
    data = Fir.objects.get(id=fid)
    if (request.POST):
        dtt=date.today()
        dt=request.POST['dt']
        det=request.POST['det']
        dt1 = datetime.strptime(dt, '%Y-%m-%d')
        print(dt1)
        if dt1.date() < dtt:
            messages.info(request,'invaid date')
            return redirect("/stationaddheardetails") 
        try:
            cu=Hearing.objects.create(firid=data,heardate=dt,updates=det)
            cu.save
        except:
            messages.info(request,'some error occured')
        else:
            messages.info(request,'HearingScheduled') 
            return redirect("/stationaddheardetails")   
    return render(request, 'stationaddhearing.html')



def adminviewreceivedfile(request):
    id=request.GET.get('id')
    data = Filee.objects.filter(frid=id)
    return render(request, 'adminviewreceivedfile.html',{'data': data})


def courtsearchfir(request):
    if (request.POST):
        cr = request.POST.get("search")
        h=Hearing.objects.all().values('id')
        p=Punishment.objects.filter(hid__in=h).values_list('hid',flat=True)
        print(p)
        data = Hearing.objects.filter(Q(firid__cid__comptitle__contains=cr) | Q(firid__lawapplied__contains=cr)
         | Q(firid__details__contains=cr) | Q(firid__cid__desc__contains=cr))
        return render(request,'courtsearchfir.html ', {'data': data,'p':p})
    return render(request, 'courtsearchfir.html ')

def courtaddpunishment(request):
    fid=request.GET.get('id')
    data = Hearing.objects.get(firid=fid)
    if (request.POST):
        pun=request.POST['pun']
        dur=request.POST['dur'] 
        try:
            cu=Punishment.objects.create(hid=data,punishment=pun,duration=dur)
            cu.save
        except:
            messages.info(request,'some error occured')
        else:
            messages.info(request,'Punishment Added') 
            return redirect("/courtsearchfir")   
    return render(request, 'courtaddpunishment.html')


def userinactive(request):
    
    cid=request.GET.get("id")
    c=Publicuser.objects.get(id=cid)
    try:
        User.objects.filter(email=c.email).update(is_active=0)
    except:
        messages.info(request, 'Something went Wrong')
        return redirect("/adminviewpublic")
    else:
        print("wow")
        messages.info(request, 'Blocked')
        return redirect("/adminviewpublic")