from django.forms import ModelForm
from .models import Painting
from django import forms

class PaintingForm(ModelForm):
    class Meta:
        model = Painting
        fields = ['title', 'featured_image', 'description', 'demo_link', 'tags']

        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(PaintingForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})

        