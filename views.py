from django.shortcuts import render
from .models import Examqp

# Create your views here.
def examonline(request):
    results = Examqp.objects.all()
    return render(request,'index.html',{'Examqp': results})
