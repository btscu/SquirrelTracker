from django.forms import ModelForm
from .models import SquirrelViewing

class ViewForm(ModelForm):
    class Meta:
        model = SquirrelViewing
        fields = '__all__'
