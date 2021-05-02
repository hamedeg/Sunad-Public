from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CustomerForm(ModelForm):
    comment= forms.CharField(widget=forms.Textarea(attrs={"rows":10, "cols":30}),label='تفاصيل أكثر')
    class Meta:
        model = Customer
        fields = ['name','ssn','address','gender','help_type','partner_alive','number_children','number_brother','comment','support','status']
        labels = {
        "name": "الاسم بالكامل",
        "ssn": "الرقم القومي",
        "address": "العنوان",
        "gender": "النوع",
        "help_type": "نقدر نساعدك ازاي",
        "partner_alive": "هل الزوج/الزوجه علي قيد الحياة",
        "number_children": "عدد الأولاد",
        "number_brother": "عدد الاخوه",
        "support": "قيمة الدعم المقدم",
        "status": "حالة الطلب",

        }
        widgets = {
            'ssn': forms.TextInput(attrs={'required': True,'type':'number','placeholder':'الارقام بالإنجليزية'}),
        }

class CustomerAttachmentsForm(ModelForm):
    class Meta:
        model = CustomerAttachments
        fields = '__all__'
        labels = {
        "attachments": "المرفقات",
        }
        widgets = {
        'attachments': forms.ClearableFileInput(attrs={'multiple': True}),
        'customer_key': forms.TextInput(attrs={'required': False,'readonly':True, 'hidden':True}),
        }