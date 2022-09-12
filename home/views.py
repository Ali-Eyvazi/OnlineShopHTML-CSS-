from django import views
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from django.views import View
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from . import tasks
from django.contrib import messages
from .forms import UploadFileBucketForm
import os
import sys
from utils import IsAdminUserMixin




class HomeView(View):
    def get(self,request):
        return render(request,'home/home.html')




class BucketHome(IsAdminUserMixin,View):
   
    template_name='home/bucket.html'
    def get(self,request):
      
        objects=tasks.all_bucket_objects_task()
        return render(request,self.template_name, {'objects':objects,})

        

class DeleteObjBucketView(IsAdminUserMixin,View):
    def get(self,request,key):
            tasks.delete_object_task.delay(key)
            messages.success(request,'your object removed','info')
            return redirect('home:bucket')


        
class DownloadBucketObject(IsAdminUserMixin,View):
    def get(self,request,key):
        tasks.download_object_task(key)
        messages.success(request,'your file willl be start soon','info')
        return redirect ('home:bucket')



class FileUPloadBucketView(IsAdminUserMixin,View):
    form_class=UploadFileBucketForm
    def get(self,request):
          form=self.form_class
          return render(request,'home/upload.html', {'form':form})


    def post(self,request):
        form=UploadFileBucketForm(request.POST,request.FILES)
        print('*='*90)
        print(request.FILES)
        # if form.is_valid():
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        object_name = os.path.basename('2142344.jpg')
        obj=sys.path.insert(0, '/home/ali/Documents/2142344.jpg')
        key='/home/ali/Documents/2142344.jpg'
        tasks.upload_object_task('/home/ali/Documents/2142344.jpg')
     
        messages.success(request,'file has been uploaded successfully','success')
        return render(request,'home/upload.html',{'form':form})