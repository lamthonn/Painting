from django import forms 
from .models import Painting, avatar

class PaintingForm(forms.ModelForm):
    class Meta:
        model = Painting
        fields = '__all__'

class PaintingUploadForm(forms.ModelForm):
    class Meta:
        model = Painting
        fields = ['name', 'description','image']

class PaintingUpdateForm(forms.ModelForm):
    class Meta:
        model = Painting
        fields = '__all__'

class avatar_user(forms.ModelForm):
    class Meta:
        model = avatar
        fields = ['avt']


