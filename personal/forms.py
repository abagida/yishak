from django.forms import ModelForm
from personal.models import Thing
from django import forms


class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ('name', 'description',)


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Who are you ?"
        self.fields['contact_name'].widget.attrs.update({'placeholder': 'Name / Surname'})
        self.fields['contact_email'].label = "How can I reach you ?"
        self.fields['contact_email'].widget.attrs.update({'placeholder': 'Your email'})
        self.fields['content'].label = "What is this about ?"
        self.fields['content'].widget.attrs.update({'placeholder': 'Subject'})
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})
