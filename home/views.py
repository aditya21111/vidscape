from django.shortcuts import render,HttpResponse,redirect
from pytube import YouTube
from pathlib import Path
from django.http import FileResponse
import os 
import shutil

import re

BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.
def home(request):
    return render(request,'home/index.html')

def download(request):
    
    
    link=request.POST.get("dfile")
    print(link)
    print(type(link))
    print(type(str(link)))
    yt=YouTube(link)
    title=yt.title
    thumbnail=yt.thumbnail_url

        # a=yt.streams.filter(subtype='mp4')[0]
     
    return render(request,'home/preview.html',{'title':title,'thumbnail':thumbnail,"link":link})
    
    

def download_success(request):
    try:
        link=request.POST.get("vidlink")

        yt=YouTube(str(link))
        d_vid = yt.streams.filter(progressive=True, file_extension='mp4').first()
        print(d_vid)
    except Exception as e:
        return HttpResponse(e) 
        # homedir=os.path.expanduser("~")
    # print(homedir)
    # d_vid.download( BASE_DIR / "static")
    print("downloaded")
    pathh=BASE_DIR/"tobedel"
    if os.path.exists(pathh):
        shutil.rmtree(pathh)
        
  
    return FileResponse(open(d_vid.download(BASE_DIR/"tobedel" ,skip_existing=True),'rb'), as_attachment=True)
    
