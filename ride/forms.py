from django import forms

class RideRequestForm(forms.Form):
    start_name = forms.CharField(widget=forms.HiddenInput())
    end_name = forms.CharField(widget=forms.HiddenInput())
    start_lng = forms.FloatField(widget=forms.HiddenInput())
    start_lat = forms.FloatField(widget=forms.HiddenInput())
    end_lng = forms.FloatField(widget=forms.HiddenInput())
    end_lat = forms.FloatField(widget=forms.HiddenInput())

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data