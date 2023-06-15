from django.forms import ModelForm
from .models import Part

class PartCreateForm(ModelForm):
    class Meta:
        model = Part
        fields = ['partnumber', 'designation', 'mass', 'xcg', 'ycg', 'zcg', 'resp']