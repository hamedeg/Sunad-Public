import django_filters
from .models import *
class CustFilter(django_filters.FilterSet):
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
    #name = django_filters.CharFilter(lookup_expr='icontains')
    help_type = django_filters.ChoiceFilter(choices=Help,label='المساعدة',lookup_expr='icontains')
    gender = django_filters.ChoiceFilter(choices=Gender,label='النوع')
    partner_alive = django_filters.ChoiceFilter(choices=Partner,label='الشريك')
    status = django_filters.ChoiceFilter(choices=Cust_Status,label='الحالة')

    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['ssn','name','address','number_children','number_brother','comment','created_at','updated_at','support']
        
