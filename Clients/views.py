from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Client
from .forms import AddClientForm
from teams.models import Team

# Create your views here.
@login_required
def ClientLists(request):
    client_list = Client.objects.filter(created_by=request.user)
    return render(request,'Clients/clients_list.html',{
        'client_list': client_list
    })

@login_required
def CLientDetail(request,pk):
    client = get_object_or_404(Client,created_by=request.user,pk=pk)

    return render(request,'Clients/client_detail.html',{
        'client': client
    })

@login_required
def AddClient(request):
    team_list = Team.objects.filter(created_by=request.user)
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            new_client = form.save(commit=False)
            team = Team.objects.get(name=request.POST['selected_team'])
            new_client.team = team
            new_client.created_by = request.user
            new_client.save()
            messages.success(request,"Client added successfully")
            return redirect('clients_list_page')
    else:
        form = AddClientForm()
        return render(request,'Clients/add_client.html',{
            'form' : form,
            'team_list':team_list
        })

@login_required    
def ClientDelete(request,pk):
    client = get_object_or_404(Client,created_by=request.user,pk=pk)
    client.delete()
    messages.success(request,"Client deleted successfully")
    return redirect('clients_list_page')

@login_required    
def ClientEdit(request,pk):
    team_list = Team.objects.filter(created_by=request.user)
    client = get_object_or_404(Client,created_by=request.user,pk=pk)
    if request.method == 'POST':
        form = AddClientForm(request.POST,instance=client)
        if form.is_valid():
            new_client = form.save(commit=False)
            team = Team.objects.get(name=request.POST['selected_team'])
            new_client.team = team
            new_client.save()
            messages.success(request,"Client updated Successfully")
            return redirect('clients_list_page')
    else:
        form = AddClientForm()
        return render(request,'Clients/edit_client.html',{
            'form':form,
            'client':client,
            'team_list':team_list
        })    
    