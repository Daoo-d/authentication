from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from leads.models import Lead
from Clients.models import Client
from teams.models import Team

# Create your views here.
@login_required
def dashboard(request):
    lead_list = Lead.objects.filter(created_by=request.user,convertd_to_client=False).order_by('-created_at')[0:5]
    client_list = Client.objects.filter(created_by=request.user).order_by('-created_at')[0:5]
    team_list = Team.objects.filter(created_by=request.user)

    return render(request,'dashboard/dashboard.html',{
        'lead_list':lead_list,
        'client_list':client_list,
        'team_list':team_list
    })