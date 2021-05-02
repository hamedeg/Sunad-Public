from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

import os
# Create your models here.
Gender = (
    ('Male','ذكر'),
    ('Female','أنثي'), 
)
Help = (
    ('Money','مال'),
    ('Food','طعام'),
    ('Medicine','دواء'),
)
Partner = (
    ('Yes','نعم'),
    ('No','لا'),
    ('Single','غير متزوج'),
)
Cust_Status = (
    ('hold','بالإنتظار'),
    ('verify','تأكيد البيانات'),
    ('handling','تتم المساعده'),
    ('done','تمت المساعده'),
)
def customer_img(instance, filename):
    ext = filename.split('.')[-1]
    filename = "BDP_%s.%s" % (instance.id, ext)
    return os.path.join('BDP', filename)
class Customer(models.Model):
    ssn = models.CharField(max_length=14)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    gender = models.CharField(max_length=6,choices=Gender)
    help_type = MultiSelectField(choices=Help)
    partner_alive = models.CharField(max_length=6,choices=Partner)
    number_children = models.IntegerField(default=0,validators=[MaxValueValidator(50),MinValueValidator(0)])
    number_brother = models.IntegerField(default=0)
    support = models.FloatField(default=0)
    comment = models.CharField(max_length=500,null=True,blank=True)
    status = models.CharField(max_length=9,choices=Cust_Status,default='hold')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "Customer"
    def __str__(self):
        return self.name

class CustomerAttachments(models.Model):
    customer_key = models.ForeignKey(Customer,on_delete=models.CASCADE)
    attachments = models.ImageField(upload_to=customer_img)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "CustomerAttachments"
    def __str__(self):
        return str(self.customer_key)
class CustomerHandel(models.Model):
    customer_key = models.OneToOneField(Customer,on_delete=models.CASCADE,unique=True)
    handel_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "CustomerHandel"
    def __str__(self):
        return str(self.customer_key)+' '+str(self.handel_by)