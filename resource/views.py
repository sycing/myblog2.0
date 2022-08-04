from django.shortcuts import render
from resource import models
# Create your views here.
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponseRedirect
import os
from django.http import HttpResponseRedirect
from django.http import HttpResponse

def index(request):
    resoucre=models.Resource.objects.all()
    return render(request, 'resource/index.html')

def upload(request):
    # file = request.FILES  # 一定要调用上传的文件（不管你干嘛，保存也好，啥也不干也好，反正不调用就出错了，估计是默认不调用就不接收吧。。）才能用ajax上传成功，否则报错，原因不明
    if request.method == "POST":  # 请求方法为POST时，进行处理
        myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        destination = open(os.path.join("resource/upload", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        uploadfilepath = os.path.join("upload", myFile.name)
        # user = UploadFile()
        # user.username = myFile.name
        # user.headImg = uploadfilepath
        # user.save()  # 上传附件到数据库
    return HttpResponse()