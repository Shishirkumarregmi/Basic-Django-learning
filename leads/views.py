from django.http import HttpRequest
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm,LeadModelForm

# Create your views here.
def lead_list(request):
    leads=Lead.objects.all()
    context={
        "leads":leads,
    }
    return  render(request,'lead_list.html',context)
#go to template setting change import os  'DIRS': [os.path.join(BASE_DIR, 'leads', 'templates', 'leads')] 
# or 'DIRS': [BASE_DIR/"leads/templates/leads"],
 
def lead_detail(request,pk):
    leads=Lead.objects.get(id=pk)
    context={
        "leads":leads,
    }
    
    return  render(request,'lead_detail.html',context)

def lead_create(request):
    #print(request.POST)
    if request.method =="POST":
        print("Receiving the post requests")
        form=LeadModelForm(request.POST)
        if form.is_valid():
            print("The form is valid")
            print(form.cleaned_data)
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            age=form.cleaned_data['age']
            agent=Agent.objects.first()
            Lead.objects.create (
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )
            print("leads has been created")
            return redirect('Home')
    context={
        "form":LeadModelForm(),
    }
    
    return  render(request,'lead_create.html',context)