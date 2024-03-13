from django import forms
from Home.models import Content


class ContentForm(forms.ModelForm):

    class Meta:
        model = Content
        fields = ['character'
                  'theme'
                  'text']
