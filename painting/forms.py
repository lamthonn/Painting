from django import forms 
from .models import Painting
# from .models import ImageAdd



class PaintingForm(forms.ModelForm):
    class Meta:
        model = Painting
        fields = '__all__'

class PaintingUploadForm(forms.ModelForm):
    class Meta:
        model = Painting
        fields = ['name', 'description','image','imagelq']


class PaintingUpdateForm(forms.ModelForm):
    class Meta:
        model = Painting
        fields = '__all__'


