from django import forms
from .models import SeedList
from .models import User

class SunRequirementsForm(forms.ModelForm):
    sun_requirements = forms.MultipleChoiceField(choices=SeedList.SUN_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = SeedList
        fields = ['sun_requirements']

class SeedSowMethod(forms.ModelForm):
    sow_method = forms.MultipleChoiceField(choices=SeedList.SOW_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = SeedList
        fields = ['sow_method']



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']
