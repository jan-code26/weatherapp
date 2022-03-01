from cProfile import label
from django import forms
from django.forms import ModelForm, ValidationError
from .models import notes

class notesforms(ModelForm):
    class Meta:
        model=notes
        fields=['title','text']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control my-5'}),
            'text':forms.Textarea(attrs={'class':'form-control mb-5'})
        }
        labels={
            'text':'write your thoughts here:'
        }

    def clean_title(self):
        title=self.cleaned_data['title']
        if 'django' not in title:
            raise ValidationError("we only accept notes about django")
        return title
