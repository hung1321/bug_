from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from io import BytesIO
import cv2
import cvzone
from .forms import Imageform
from .models import bug,medic
# Create your views here.
def prediction_(bug):
    pass
path_kera = "D:\\recogniztion\\insect\\keras_model.h5"
path_lable = "D:\\recogniztion\\insect\\labels.txt"
def index(request):
    if request.method == 'POST':
        form = Imageform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data['image'])
            myclassifier = cvzone.ClassificationModule.Classifier(path_kera,path_lable)
            file_name = form.cleaned_data['image']
            img = cv2.imread('media/insect/images/{}'.format(file_name))
            prediction = myclassifier.getPrediction(img)
            return redirect('page.html',predictions = prediction[1])
    else:
        form = Imageform()
    return render(request, 'index.html', {'form': form})
def page(request,predictions):
    #print("hello")
    #print(predictions)
    print(predictions)
    if predictions+1 == 3:
        return render(request,'page.html',{"No_bite":True})
    elif predictions == 4:
        bugs = bug.objects.get(id = predictions)
        medicine = medic.objects.filter(bite_used_id = predictions)
        return render(request,'page.html',{"bug":bugs,"medicine":medicine,"No_bite":False})
    else:
        print(predictions)
        bugs = bug.objects.get(id = predictions+1)
        medicine = medic.objects.filter(bite_used_id = predictions+1)
        #print(bugs.name)
        #print(medicine[0].id)
        return render(request,'page.html',{"bug":bugs,"medicine":medicine,"No_bite":False})