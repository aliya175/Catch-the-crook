"""crime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crimeapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('login', views.login),
    path('adminhome', views.adminhome),
    path('policehome', views.stationhome),
    path('courthome', views.courthome),
    path('stationreg', views.stationreg),
    path('viewstation', views.viewstation),
    path('adminviewpublic', views.adminviewpublic),
    path('adminsendfilestation', views.adminsendfilestation),
    path('adminviewfiles', views.adminviewfiles),
    path('stationaddcriminaldetails', views.stationaddcriminaldetails),
    path('stationaddwantedlist', views.stationaddwantedlist),
    path('stationviewfilerequest', views.stationviewfilerequest),
    path('stationaddfile', views.stationaddfile),
    path('stationviewcriminal', views.stationviewcriminal),
    path('userreg', views.userreg),
    path('userhome', views.userhome),
    path('complaint', views.complaint),
    path('userviewcomplaintstatus', views.userviewcomplaintstatus),
    path('useraddmissingitem', views.useraddmissingitem),
    path('useraddmissingperson', views.useraddmissingperson),
    path('userviewmissingstatus', views.userviewmissingstatus),
    path('userviewmissingpersonstatus', views.userviewmissingpersonstatus),
    path('userviewwantedlist', views.userviewwantedlist),
    path('adminviewwantedlist', views.adminviewwantedlist),
    path('stationviewwantedlist', views.stationviewwantedlist),
    path('stationviewcomplaint', views.stationviewcomplaint),
    path('stationviewmissingitem', views.stationviewmissingitem),
    path('stationviewmissingperson', views.stationviewmissingperson),
    path('stationaddcomplaintresponse', views.stationaddcomplaintresponse),
    path('stationaddmissitemresponse', views.stationaddmissitemresponse),
    path('userviewcomplaintresponse', views.userviewcomplaintresponse),
    path('userviewmissingitemresponse', views.userviewmissingitemresponse),
    path('stationaddcrimedetails', views.stationaddcrimedetails),
    path('stationaddfir', views.stationaddfir),
    path('stationaddheardetails', views.stationaddheardetails),
    path('stationaddhearing', views.stationaddhearing),
    path('adminviewreceivedfile', views.adminviewreceivedfile),
    path('adminviewcriminal', views.adminviewcriminal),
    path('adminviewmissingitems', views.adminviewmissingitems),
    path('adminviewmissingpersons', views.adminviewmissingpersons),
    path('adminviewhearingdetails', views.adminviewhearingdetails),
    path('adminviewfirdetails', views.adminviewfirdetails),
    path('courtviewfir', views.courtviewfir),
    path('courtsearchfir', views.courtsearchfir),
    path('courtaddpunishment', views.courtaddpunishment),
    path('adminviewpunishment', views.adminviewpunishment),
    path('stationviewpunishment', views.stationviewpunishment),
    path('userviewpunishment', views.userviewpunishment),
    path('userviewhearings', views.userviewhearings),
    path('stationaddmisspersonresponse', views.stationaddmisspersonresponse),
    path('userviewmpersonupdate', views.userviewmpersonupdate),
    path('userinactive', views.userinactive),
    path('complaintpost', views.complaintpost),
    path('removewanted', views.removewanted),
    













    





    
]
