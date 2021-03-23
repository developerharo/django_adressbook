from django import forms
from django.db.models import fields
from .models import Contact

class ContactCreate(forms.ModelForm):
  class Meta:
    model = Contact
    fields = "__all__"