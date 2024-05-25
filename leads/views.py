from django.shortcuts import render

# Create your views here.
def add_lead(request):
    return render(request,'leads/add_lead.html')