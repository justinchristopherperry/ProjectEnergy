from django.db import models
from django import forms
from django.forms import ModelForm
from .models import Seller, Country

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
	#get price range
	minPrice = forms.FloatField(label='Minimum price per kwh:', required=False, min_value=0.0)
	maxPrice = forms.FloatField(label='Maximum price per kwh:', required=False, min_value=0.001)
	print(maxPrice)
	#get countries
	cList = Country.objects.values_list('name', flat=True)
	cChoices = []
	for c in cList:
		cChoices.append((c, c))

	countries = forms.MultipleChoiceField(choices=cChoices, label='Pick countrie(s) (REQUIRED):', widget=forms.CheckboxSelectMultiple())
	#get sortBy list
	sortChoices = (('a', 'leave it unsorted'), ('b', 'price'), ('c', 'country'), ('d', 'price, then country'), ('e', 'country, then price'))
	sort = forms.ChoiceField(choices=sortChoices, label='Sort results:', required=False)


	def clean_match_form(self):
		minP = self.cleaned_data['minPrice']
		maxP = self.cleaned_data['maxPrice']
		countries = self.cleaned_data['countries']
		sortBy = self.cleaned_data['sort']
		# prices generally range from .01-.08 per kwh, so if the user decides not to limit by prices 
		# make sure the bounds won't get rid of any
		if minP is None:
			minP = 0.0
		if maxP is None:
			maxP = 1000000
		# make sure price range is valid
		if minP < 0:
			raise ValidationError(_('Invalid price - price is below 0'))
		if maxP <= 0:
			raise ValidationError(_('Invalid price - max price must be ablow 0'))
		#get sort:
		if not sortBy == "":
			if sortBy == 'a': sortBy = []
			elif sortBy == 'b': sortBy = ['price_per_kwh']
			elif sortBy == 'c': sortBy = ['country_name']
			elif sortBy == 'd': sortBy = ['price_per_kwh', 'country_name']
			else: sortBy = ['country_name', 'price_per_kwh']
			
		print(f"in clean_match...: {sortBy}")
		check = {
			'minPrice': minP,
			'maxPrice': maxP,
			'countries': countries,
			'sortBy': sortBy
		}
		return check
    	