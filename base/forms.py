from dataclasses import field, fields
from django.forms import ModelForm
from .models import Audio

class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields