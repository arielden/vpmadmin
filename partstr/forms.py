from django.forms import ModelForm
from .models import Part

class PartCreateForm(ModelForm):
    class Meta:
        model = Part
        fields = ['level', 
                  'partnumber', 
                  'designation',
                  'pntype', 
                  'status',
                  'parent',
                  'mass', 
                  'xcg', 'ycg', 'zcg'] #Eliminar 'resp', si se carga automáticamente en la vista.