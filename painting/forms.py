from django import forms 
from .models import Painting
# from .models import ImageAdd
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PaintingForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
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


