from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import AddLeadForm
from django.contrib.auth.decorators import login_required
from .models import Lead
from Clients.models import Client
from teams.models import Team

# Create your views here.
@login_required
def add_lead(request):
    team_list = Team.objects.filter(created_by=request.user)
    if request.method == 'POST':
        form = AddLeadForm(request.POST)
        if form.is_valid():
            new_lead = form.save(commit=False)
            team = Team.objects.get(name=request.POST['selected_team'])
            new_lead.created_by = request.user
            new_lead.team = team
            new_lead.save()
            messages.success(request,"Lead added successfully")
            return redirect('lead_list_page')
    else:
        form = AddLeadForm()
        return render(request,'leads/add_lead.html',{
            'form' : form,
            'team_list': team_list
        })
    
@login_required
def LeadList(request):
    lead_list = Lead.objects.filter(created_by=request.user,convertd_to_client=False)

    return render(request,'leads/leads_list.html',{
        'lead_list' : lead_list
    })

@login_required
def LeadDetail(request,pk):
    lead = get_object_or_404(Lead,created_by=request.user,pk=pk)

    return render(request,'leads/lead_detail.html',{
        'lead': lead
    })

@login_required
def LeadEdit(request,pk):
    team_list = Team.objects.filter(created_by=request.user)
    lead = get_object_or_404(Lead,created_by=request.user,pk=pk)
    if request.method == 'POST':
        form = AddLeadForm(request.POST,instance = lead)
        if form.is_valid():
            new_lead = form.save(commit=False)
            team = Team.objects.get(name=request.POST['selected_team'])
            new_lead.team = team
            form.save()
            messages.success(request,'The lead is updated')
            return redirect('lead_list_page')
    else:
        form = AddLeadForm()    

    return render(request,'leads/lead_edit.html',{
        'form': form,
        'lead':lead,
        'team_list':team_list
    })

@login_required
def LeadDelete(request,pk):
    lead = get_object_or_404(Lead,created_by=request.user,pk=pk)
    lead.delete()

    messages.success(request,"The lead is deleted")

    return redirect('lead_list_page')

@login_required
def LeadConvert(request,pk):
    lead = get_object_or_404(Lead,created_by=request.user,pk=pk)
    
    Client.objects.create(
        name = lead.name,
        email = lead.email,
        description = lead.description,
        team = lead.team,
        created_by = request.user
    )
    lead.convertd_to_client = True
    lead.save()
    messages.success(request,"Lead is successfully converted to client")
    return redirect('lead_list_page')