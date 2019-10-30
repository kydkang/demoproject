from django.contrib import admin
from django.urls import path, include 
from django.views.generic.base import TemplateView 
from django.contrib.auth import views as auth_views 
from commons import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls), 
    path('account/', include('account.urls')), 
    path('101/', include('sims101.urls')),    
    path('export/csv/', views.export_users_csv, name='export_users_csv'), 

]

## you can add login_required permission as follows.  
## path('', login_required(TemplateView.as_view(template_name='home.html')), name='home'),
## In this project, it is not needed because  {% if user.is_authenticated %} is used in home.html template.