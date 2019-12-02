from django.db import models
from django import forms
from django.forms import ModelForm
from .models import Seller

# Form for a user to upload a seller to the database.
class SellerForm(ModelForm):
    class Meta:
        model = Seller
        fields = ['email', 'phone_number', 'address', 'country_name', 'total_produced_2018_Gwh', 'price_per_kwh']
        labels = {'email':'Email',
                    'phone_number':'Phone Number',
                    'address':'Address',
                    'country_name':'Country',
                    'total_produced_2018_Gwh':'Electricity produced in 2018 (Gwh)',
                    'price_per_kwh':'Price per Kwh'}

class MatchForm(forms.Form):
	minPrice = forms.FloatField(label='Minimum price per kwh:', required=False, min_value=0.0)
	maxPrice = forms.FloatField(label='Maximum price per kwh:', required=False, min_value=0.001)

	def clean_match_form(self):
		minP = self.cleaned_data['minPrice']
		print(f"in form:{type(minP)}")
		maxP = self.cleaned_data['maxPrice']
		if minP is None:
			minP = 0.0
		if maxP is None:
			maxP = 1000000
		if minP < 0:
			raise ValidationError(_('Invalid price - price is below 0'))
		if maxP <= 0:
			raise ValidationError(_('Invalid price - max price must be ablow 0'))

		check = {
			'minPrice': minP,
			'maxPrice': maxP
		}
		print(f"in form2:{type(check['minPrice'])}")
		return check
    	