from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


PAYMENT_CHOICES = (
    ('s','stripes'),
    ('p','paypal'),
)

class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget = forms.TextInput(attrs={
        'placeholder':'1234 Main St',
        'class':'form-control'
    }))
    apartment_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Apartment or suite',
        'class':'form-control'

    }))
    country = CountryField(blank_label='(Select Country)').formfield(widget=CountrySelectWidget(attrs={
        'class':'custom-select d-block w-100'
        
    }))
    zipcode = forms.CharField(widget=forms.TextInput(attrs={ 
        'class':'form-control',
        'id':'zip'
    }))
    same_as_billing = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices = PAYMENT_CHOICES)
