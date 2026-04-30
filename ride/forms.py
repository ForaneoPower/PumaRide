from django import forms
from .models import RideRequest

class RideRequestForm(forms.ModelForm):
    class Meta:
        model = RideRequest
        fields = ['start_name', 
                  'end_name', 
                  'start_lng', 
                  'start_lat', 
                  'end_lng', 
                  'end_lat',]
    
    def clean(self):
        cleaned_data = super().clean()

        start_lng = cleaned_data.get('start_lng')
        start_lat = cleaned_data.get('start_lat')
        end_lng = cleaned_data.get('end_lng')
        end_lat = cleaned_data.get('end_lat')

        return cleaned_data