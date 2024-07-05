from django import forms
from .models import Concert

class ConcertForm(forms.ModelForm):
  
  class Meta:
    model = Concert
    fields = '__all__'
    
  def __init__(self, *args, **kwargs):  
    super().__init__(*args, **kwargs)
    concerts = Concert.objects.all()
    
    placeholders = {
            'city': 'City',
            'date': 'Date',
            'price': 'Price £',
        }

    for field_name, field in self.fields.items():
      if field_name in placeholders:
        field.widget.attrs['placeholder'] = placeholders[field_name]
      field.widget.attrs['class'] = 'border-black rounded-0'