from django import forms
from .models import Profile



class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = "__all__"
    
    widgets = {
      "date_of_birth": forms.TextInput(attrs={'type': 'date'}),
      "tel": forms.TextInput(attrs={'type': 'tel'}),
      "mother_tel": forms.TextInput(attrs={'type': 'tel'}),
      "father_tel": forms.TextInput(attrs={'type': 'tel'}),
      "guardian_tel": forms.TextInput(attrs={'type': 'tel'}),
    }