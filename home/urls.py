from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .import views

app_name='home'

urlpatterns = [
    path('',views.HomeView,name='home'),
    path('add/cust/',views.AddCustomerView,name='add_customer'),
    path('handel/',views.HandelView,name='handel'),
    path('handel/<int:id>',views.HandelDetailsView,name='handel_details'),
    path('assign/<int:id>',views.AssignView,name='assign'),
    path('myassign/',views.MyAssignView,name='my_assign'),
    path('edit/cust/<int:id>',views.EditCustView,name='edit_cust'),
    path('remove/assign/<int:id>',views.RemoveAssignView,name='remove_aasign'),
    path('login/',views.LoginView,name='login'),
    path('logout/',views.LogoutView,name="logout"), 
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)