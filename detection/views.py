from django.shortcuts import render

# Create your views here.


def homepage(request):
    if request.user.is_authenticated:

        return render(request , 'pages/homepage.html')
    

def dashboard(request):
    if request.user.is_authenticated:

        return render(request , 'pages/dashboard.html')
    

def uploadImage(request):
    if request.user.is_authenticated:

        return render(request , 'pages/uploadImage.html')
    

def viewImages(request):
    if request.user.is_authenticated:

        return render(request , 'pages/viewImages.html')
    