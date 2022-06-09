from pyexpat import model
from django import forms

from leads.models import Lead


class LeadModelForm(forms.ModelForm):
    class Meta:
        model=Lead
        fields=(
            'first_name',
            'last_name',
            'age',
            'agent',
        )


class LeadForm(forms.Form):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    age=forms.IntegerField(min_value=0)