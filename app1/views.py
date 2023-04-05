from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app1.models import *


def Insertion_Topic(request):
    tn=input("enter a Topic_name:")
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse("Data inserted sucesfully in Topic")

def Insertion_Webpage(request):
    tn=input("enter a Topic_name:")
    na=input("enter a name:")
    ur=input("enter a url:")
    email=input("enter a email:")
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=email)[0]
    WO.save()
    return HttpResponse("Data insertion sucessfully in Webpage")

def Insertion_AccessRecord(request):
    tn=input("enter a Topic_name:")
    na=input("enter a name:")
    ur=input("enter a url:")
    email=input("enter a email:")
    auth=input('Enter a author name:')
    dat=input("enter a date:")
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=email)[0]
    WO.save()
    Ao=AccessRecord.objects.get_or_create(name=WO,author=auth,date=dat)[0]
    Ao.save()
    return HttpResponse('data inserted sucessfully in Accessrecord')



def Display_Topic(request):
    LOT=Topic.objects.all()
    d={'topic':LOT}
    return render(request,'Display_Topic.html',d)


def Display_Webpage(request):
    LOW=Webpage.objects.all()
    d={'webpage':LOW}
    return render(request,'Display_Webpage.html',d)


def Display_AccesRecord(request):
    LOA=AccessRecord.objects.all()
    d={'access':LOA}
    return render(request,'Display_AccesRecord.html',d)
