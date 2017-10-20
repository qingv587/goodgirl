from django.shortcuts import render,HttpResponse,redirect
from app01 import forms
# Create your views here.
from django.db.models import Count,functions

def register(request):
    if request.method == "GET":
        return render(request,"register.html")
    else:
        obj = forms.RegisterForm(request,request.POST,request.FILES)
        return render(request,"register.html",{"obj":obj})



    # models.Article.objects.filter(blog=blog).extra(select={"c":"data_format('creat_time','%%Y-%%m')"}).values("c").annotate(ct=Count(id))
    # models.Article.objects.filter(blog=blog).annotate(x=functions.ExtractYear("creat_time"))
    # models.Article.objects.filter(blog=blog).annotate(x=functions.Extract("creat_time","year"))
    # models.Article.objects.filter(blog=blog).annotate(x=functions.TruncYear("creat_time"))

def index(request):
    return render(request,"index.html")

def error(request):
    return HttpResponse("404")

#
# from django.db import transaction
# with transaction.atomic():
    pass
#
#

def upload(request):
    file_obj = request.FILES.get("imgFile")
    import os,json
    file_path = os.path.join("static/imge",file_obj.name)
    with open(file_path,"wb") as f:
        for trunk in file_obj.trunks():
            f.write(trunk)
    dic = {"error":0,"url":"/"+file_path,"message":"错误了"}
    return HttpResponse(json.dumps(dic))


from bs4 import BeautifulSoup
content = ''
soup = BeautifulSoup(content,"html.parse")

soup.find(attrs={"id":"i2"})
# soup.find_all(name="p")  //列表
p = soup.find(name="p")
sc = p.find(name="script")


valid_tag = ["p","img","div"]
tags = soup.find_all()

for tag in tags:
    if tag.name not in valid_tag:
        tag.decompose()

content_str = print(soup.decode())