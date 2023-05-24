from django.db import models

# Create your models here.

class Owners(models.Model):
    fullname=models.CharField(null=False,blank=False,max_length=300)
    username=models.CharField(primary_key=True,null=False,blank=False,max_length=50)
    email_id=models.EmailField(null=False,blank=False)
    phone_no=models.CharField(null=False,blank=False, max_length=50)
    nid_no=models.CharField(null=False,blank=False,max_length=50)
    address=models.CharField(null=True,blank=True,max_length=100)

    class Meta:
        def __str__(self) -> str:
            return str(self.username)

class Renter(models.Model):
    fullname=models.CharField(null=False,blank=False,max_length=300)
    username=models.CharField(primary_key=True,null=False,blank=False,max_length=50)
    email_id=models.EmailField(null=False,blank=False)
    phone_no=models.CharField(null=False,blank=False, max_length=50)
    nid_no=models.CharField(null=False,blank=False,max_length=50)
    occupation=models.CharField(null=False,blank=False,max_length=300)
   
    class Meta:
        def __str__(self) -> str:
            return str(self.username)