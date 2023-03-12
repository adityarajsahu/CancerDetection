from django.shortcuts import render, redirect
from .models import breastImage
from yolov7 import detect
# Create your views here.

def homepage(request):
    if request.user.is_authenticated:

        return render(request , 'pages/homepage.html')
    else:
        return redirect("login")
    

def dashboard(request):
    if request.user.is_authenticated:

        return render(request , 'pages/dashboard.html')
    else:
        return redirect("login")

def uploadImage(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'pages/uploadImage.html')
        elif request.method == 'POST':
            image = request.FILES['cancerImage']
            # print(image)
            mask_img = detect(image)
            obj = breastImage(xrayImage = image,uploadedBy = request.user, maskImage = mask_img)
            obj.save()
            return redirect(singleViewImage,imageId = obj.id)
    else:
        return redirect('login')
    
def singleViewImage(request,imageId):
    if request.user.is_authenticated:
        res = breastImage.objects.get(id = imageId)
        context = {
            'xrayImage' : res.xrayImage.url,
            'uploadedBy' : res.uploadedBy,
            'uploadedOn' : res.uploadedOn
        }

        return render(request , 'pages/singleViewImage.html', context=context)
    else:
        return redirect("login")

    

def viewImages(request):
    if request.user.is_authenticated:
        res = breastImage.objects.all()
        context = {
            'xrayImages' : res
        }
        return render(request , 'pages/viewImages.html', context=context)
    else:
        return redirect("login")