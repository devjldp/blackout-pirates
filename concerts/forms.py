from django import forms
from .models import Concert

class ConcertForm(forms.ModelForm):
  
  class Meta:
    model = Concert
    fields = '__all__'
    
  def __init__(self, *args, **kwargs):  
    super().__init__(*args, **kwargs)
    concerts = Concert.objects.all()
    friendly_names = [(concert.id, concert.get_friendly_name()) for concert in concerts]

    self.fields['category'].choices = friendly_names
    for field_name, field in self.fields.items():
      field.widget.attrs['class'] = 'border-black rounded-0'