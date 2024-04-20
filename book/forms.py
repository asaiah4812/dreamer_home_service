from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'date', 'time', 'location', 'service_desc']
        exclude = ['user']
        labels = {
            'service': 'Category',
            'service_desc':'service description',
            'date': 'Date of Service', 
            'time': 'Time of Service',  
            'location': 'Location'
        }
        widgets ={
            'service_desc': forms.Textarea(),
            'date': forms.DateTimeInput(attrs={'type': 'date'}),
            'time':forms.TimeInput(attrs={'type':'time'})
        }

        