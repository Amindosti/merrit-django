from django import forms
from .models import CreateForm


class DocumentForm(forms.ModelForm):
    class Meta:
        model = CreateForm
        fields = ('dacument_addr')
