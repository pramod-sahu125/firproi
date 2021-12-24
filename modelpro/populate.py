import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','modelpro.settings')

# export DJANGO_SETTINGS_MODULE=modelpro.settings

# from django.conf import settings
# settings.configure(DEBUG=True)

import django
django.setup()

from faker import Faker
import random
from mapp.models import Employee

def phngen():    
    num=str(random.randint(6,9))
    for i in range(9):
        num=num+str(random.randint(0,9))
    return int(num)

fak=Faker()
def fakegen(n):
    for i in range(n):
        fid=random.randint(100,999)
        fname=fak.name()
        fdept=fak.random_element(elements=['IT','MECH','ECE','PROD','DESIGN','QUALITY','ARCHITECT','CIVIL','MANAGER'])
        fsal=random.randint(10000,100000)
        fadd=fak.address()
        fphn=phngen()
        emp_table=Employee.objects.get_or_create(Eid=fid,name=fname,phnum=fphn,dept=fdept,salary=fsal,Address=fadd)


   
n=int(input('enter how many records you want'))
fakegen(n)
print(f'{n} records created sucessfully')



