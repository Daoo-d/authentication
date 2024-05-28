from django.urls import path
from . import views

urlpatterns = [
    path('add-lead/',views.add_lead,name='add_lead'),
    path('<int:pk>/delete/',views.LeadDelete,name='lead_delete'),
    path('<int:pk>/edit/',views.LeadEdit,name='lead_edit'),
    path('<int:pk>/convert/',views.LeadConvert,name='lead_convert'),
    path('',views.LeadList,name='lead_list_page'),
    path('<int:pk>/',views.LeadDetail,name='leads_detail')
]
