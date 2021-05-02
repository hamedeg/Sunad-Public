from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import auth
from .forms import *
from .models import *
from .filters import *
from .decorators import *
# Create your views here.
def HomeView(request):
    return render(request,'home.html')

def AddCustomerView(request):
    get_customer_form = CustomerForm()
    get_customer_attachments_form = CustomerAttachmentsForm()
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        attach_form = CustomerAttachmentsForm(request.POST,request.FILES)
        if customer_form.is_valid():
            customer_form.name = request.POST['name']
            customer_form.address = request.POST['address']
            customer_form.gender = request.POST['gender']
            customer_form.help_type = request.POST['help_type']
            customer_form.partner_alive = request.POST['partner_alive']
            customer_form.number_children = request.POST['number_children']
            customer_form.number_brother = request.POST['number_brother']
            customer_form.ssn = request.POST['ssn']
            customer_form.comment = request.POST['comment']
            customer_form.support = request.POST['support']
            customer_form.status = request.POST['status']

            ssn_len = len(customer_form.ssn)
            attachments = request.FILES.getlist('attachments')
            if int(ssn_len) == int(14):
                x = customer_form.save()
                if x:
                    for attach in attachments:
                        insert_attach = CustomerAttachments.objects.create(
                            customer_key = Customer.objects.latest('id'),
                            attachments = attach,
                        )
                messages.info(request,"تم إستلام الطلب")
                return redirect(reverse("home_page:home"))
            else:
                messages.info(request,"خطأ بالبيانات")
        else:
            messages.info(request,"خطأ بالبيانات")
    context = {'form':get_customer_form,'attach':get_customer_attachments_form}
    return render(request,'add_customer.html',context)

@unauthenticated_user
def HandelView(request):
    get_cust_data = Customer.objects.all()
    ##Filter
    my_filter = CustFilter(request.GET,queryset=get_cust_data)
    get_cust_data = my_filter.qs
    get_cust_handel = CustomerHandel.objects.filter(customer_key__in=get_cust_data)
    context = {'form':get_cust_data,'handel':get_cust_handel,'filter':my_filter}
    return render(request,'handel.html',context)

@unauthenticated_user
def HandelDetailsView(request,id):
    get_cust_data = Customer.objects.get(id=id)
    try:
        get_cust_attach = CustomerAttachments.objects.filter(customer_key=get_cust_data)
    except:
        get_cust_attach = ''
    try:
        get_cust_handel = CustomerHandel.objects.get(customer_key=get_cust_data)
    except:
        get_cust_handel = ''
    context = {'form':get_cust_data,'handel':get_cust_handel,'attach':get_cust_attach}
    return render(request,'handel_details.html',context)

@unauthenticated_user
def AssignView(request,id):
    get_cust_data = Customer.objects.get(id=id)
    if request.method == 'POST':
        get_cust_id = request.POST['cust_id']
        get_cust = Customer.objects.get(id=get_cust_id)
        Customer.objects.filter(id=id).update(status='verify')
        CustomerHandel.objects.create(handel_by=request.user,customer_key=get_cust)
        messages.info(request,"تم تبني الحالة")
        return redirect(reverse("home_page:my_assign"))
    context = {'form':get_cust_data}
    return render(request,'assign.html',context)

@unauthenticated_user
def MyAssignView(request):
    get_cust_handel_data = CustomerHandel.objects.filter(handel_by=request.user)
    context = {'form':get_cust_handel_data}
    return render(request,'my_assign.html',context)

@unauthenticated_user
def EditCustView(request,id):
    get_cust_data = get_object_or_404(Customer,id=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST,instance=get_cust_data)
        form.save()
        messages.info(request,"تم التعديل")
        return redirect(reverse("home_page:my_assign"))
    else:
        form = CustomerForm(instance=get_cust_data)
    context = {'form':form}
    return render(request,'edit_cust.html',context)

@unauthenticated_user
def RemoveAssignView(request,id):
    get_assign = CustomerHandel.objects.get(handel_by=request.user,id=id)
    get_cust = get_assign.customer_key
    if request.method == 'POST':
        get_assign.delete()
        get_cust.status = 'hold'
        get_cust.save()
        messages.info(request,"تم حذف التبني")
        return redirect(reverse("home_page:my_assign"))
    return render(request,'remove_assign.html')

def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/handel')
            else:
                messages.info(request, 'الحساب غير مفعل من قبل إدارة الموقع')                
        else:
            messages.info(request, 'بيانات خاطئة! من فضلك اعد المحاولة')
    context = {}
    return render(request, 'login.html',context)

@unauthenticated_user
def LogoutView(request):
    auth.logout(request)
    return redirect('/')
