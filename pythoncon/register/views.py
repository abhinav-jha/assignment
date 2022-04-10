from django.shortcuts import render , redirect
from django.http import HttpResponse

from .models import Register, Workshop_details
from .forms import Registerform , Workshopform

# Create your views here.

def register(request):
    #query db for list of members 
    register=Register.objects.all()

    context={'register': register}

    return render(request,'register/register.html', context)


def view_workshop(request):
    view_workshop=Workshop_details.objects.all()

    context ={'view_workshop':view_workshop}
   
    return render(request,'register/view_workshop.html', context)



def member_details(request , pk):
    
    #query single member details 
    memberObj= Register.objects.get( id = pk )

    #get workshop details for this member     
    workshop_details=memberObj.Workshop_details.all()

    return render(request,'register/member_details.html',{'memberObj':memberObj,'workshop_details':workshop_details})

def create_member(request):

    form=Registerform()

    if request.method =='POST':

        form=Registerform(request.POST,request.FILES)

        if form.is_valid():
            form.save()

        return redirect('register')

    context={'form':form}

    return render(request, 'register/create_member.html',context)

def update_member(request,pk):
    update_member=Register.objects.get(id=pk)
    form= Registerform(instance=update_member)
    if request.method == 'POST':
        form=Registerform(request.POST,request.FILES,instance=update_member)
        if form.is_valid():
            form.save()
            return redirect('register')
    context={'form':form}
    return render(request,'register/create_member.html',context)

def delete_member(request,pk):
    delete_member=Register.objects.get(id=pk)
    if request.method == 'POST':
        delete_member.delete()
        return redirect('register')
    
    context={'member':delete_member}
    return render(request,'register/delete.html',context)


# create workshop views 
def create_workshop(request):
    form=Workshopform()
    if request.method=='POST':
        form=Workshopform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_workshop')
    context={'form':form}
    return render(request,'register/create_workshop.html',context)

#view workshop details 
def workshop_details(request , pk):
    
    #query single member details 
    workshopObj= Workshop_details.objects.get( id = pk )

    return render(request,'register/workshop_details.html',{'workshopObj':workshopObj})


    






