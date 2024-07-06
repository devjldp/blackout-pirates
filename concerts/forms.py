from django import forms
from .models import Concert

class ConcertForm(forms.ModelForm):
  """
    Form for creating and updating Concert instances.

    This form uses the Concert model and includes all its fields. It also sets
    custom placeholders and CSS classes for the form fields.
  """
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