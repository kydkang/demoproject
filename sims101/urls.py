from django.urls import path
from . import views

app_name = 'sims101'

urlpatterns = [ 
    path('', views.IndexListView, name='index_list'), 
    # path('data/<int:pk>/', views.IndexDetailView.as_view(), name='index_detail'), 
    # path('data/create/', views.IndexCreateView.as_view(), name='index_create'), 
    path('data/<int:pk>/update', views.IndexUpdateView.as_view(), name='index_update'),
    path('data/<int:pk>/delete', views.IndexDeleteView.as_view(), name='index_delete'), 
    path('ajax/change_session/', views.ajax_change_session, name='ajax_change_session'),  
    path('ajax/calculate/', views.ajax_calculate, name='ajax_calculate'), 
    path('ajax/validated/', views.ajax_validated, name='ajax_validated'), 
    path('ajax/expand/', views.ajax_expand, name='ajax_expand'), 
    path('export/csv/', views.export_xls, name='export_users_csv'), 

]


# app_name = 'account'  domain  in urls.py 
# You need to use that namespace when reversing urls with reverse/reverse_lazy or {% url %}:
#  for example,  LOGIN_REDIRECT_URL = reverse_lazy('account:dashboard')