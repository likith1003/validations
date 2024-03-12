from django.shortcuts import render, HttpResponse
from app.forms import *
from app.models import *
# Create your views here.
def djform(request):
    SFO = StudentForm()
    d = {'SFO':SFO}
    if request.method == 'POST':
        SFO=StudentForm(request.POST)
        if SFO.is_valid():
            sname=SFO.cleaned_data['sname']
            sage=SFO.cleaned_data['sage']
            password=SFO.cleaned_data['password']
            gender=SFO.cleaned_data['gender']
            saddress=SFO.cleaned_data['saddress']
            cource=SFO.cleaned_data['cource']
            SO = Student(sname=sname, sage=sage, password=password, gender=gender, saddress=saddress,cource=cource)
            SO.save()
            return HttpResponse('Student Created Successfully')
        else:
            return HttpResponse('Invalid Data')
    return render(request, 'djform.html', d)