from django.forms import ModelForm
from .models import Painting

class PaintingForm(ModelForm):
    class Meta:
        model = Painting
        fields = ['title', 'featured_image', 'description', 'demo_link', 'tags']
        