from django.shortcuts import render
from .models import Employee
# Create your views here.
def view(request):
    data=Employee.objects.order_by('Eid')
    return render(request,'home.html',{'data':data})

