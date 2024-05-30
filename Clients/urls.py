from django.urls import path
from . import views

urlpatterns = [
    path('add-client/',views.AddClient,name='add_client'),
    path('<int:pk>/delete/',views.ClientDelete,name='client_delete'),
    path('<int:pk>/edit/',views.ClientEdit,name='client_edit'),
    path('',views.ClientLists,name='clients_list_page'),
    path('<int:pk>/',views.CLientDetail,name='client_detail'),
]
