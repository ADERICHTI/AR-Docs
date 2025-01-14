from django import forms
from .models import document, doc
from django_summernote.widgets import SummernoteWidget

class DocumentForm(forms.ModelForm):

  class Meta:
    model = document
    fields = ['title', 'content', 'image']
    # widgets = {'content': SummernoteWidget()}

class DocForm(forms.ModelForm):
  class Meta:
    model = doc
    fields = ['title', 'content', 'code', 'image']