from django.shortcuts import render,get_object_or_404,redirect
from .models import Team
from .forms import TeamForm
from django.contrib import messages

# Create your views here.
def edit_team(request,pk):
    team = get_object_or_404(Team,created_by=request.user,pk=pk)
    if request.method == 'POST':
        form = TeamForm(request.POST,instance=team)
        if form.is_valid():
            form.save()

            messages.success(request,'Changes made successfully')
            return redirect('account_page')
    else:
        form = TeamForm(instance=team)
        return render(request,'teams/edit_team.html',{
            'form':form,
            'team':team
        })    