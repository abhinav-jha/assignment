
from django.forms import ModelForm
from .models import Register,Workshop_details
from django import forms 

class Registerform(ModelForm):
    class Meta:
        model=Register
        #fields='__all__'
        fields=['full_name','intro','member_type','profile_pic','skill_set','reason']    


        widgets={

        }   
    def __init__(self,*args,**kwargs):
        super(Registerform,self).__init__(*args,**kwargs)
        self.fields['full_name'].widget.attrs.update({'class':'input','placeholder':'Full Name'})
        self.fields['intro'].widget.attrs.update({'class':'input','placeholder':'Introduction'})
        self.fields['skill_set'].widget.attrs.update({'class':'input','placeholder':'Skill Set'})
        self.fields['reason'].widget.attrs.update({'class':'input','placeholder':'Reason'})             



class Workshopform(ModelForm):
    class Meta:
        model=Workshop_details
        fields=['workshop_name','workshop_date','workshop_time','workshop_subject','workshop_details']


       




     