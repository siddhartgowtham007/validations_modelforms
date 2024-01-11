from django import forms
from app.models import *



class Studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

    botcatch=forms.CharField(max_length=10,required=False,widget=forms.HiddenInput)


    def clean_botcath(self):
        a=self.cleaned_data['botcatch']
        if len(a)>0:
            raise forms.ValidationError('bot')