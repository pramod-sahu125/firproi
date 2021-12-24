from django.db import models

# Create your models here.

class Employee(models.Model):
    # id=models.IntegerField(primary_key=True)
    Eid=models.IntegerField()
    name=models.CharField(max_length=254)
    phnum=models.BigIntegerField()
    dept=models.CharField(max_length=50)
    salary=models.BigIntegerField()
    Address=models.TextField()

    def __str__(self):
        return self.dept

    

