from django.forms import ModelForm
from .models import Painting, Review
from django import forms

class PaintingForm(ModelForm):
    class Meta:
        model = Painting
        fields = ['title', 'featured_image', 'description', 'demo_link']

        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(PaintingForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        labels = {
            'value': "Place your vote",
            'body': "Add a comment with you",
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})


        