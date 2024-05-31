from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Skill, Message

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': "Name",
            "email": "Email Address",
            'psssword1': "Password",
            'password2': "Password Confirmation",
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'location', 'short_intro', 'bio', 'profile_image', 'social_twitter', 'social_github', 'social_linkedin', 'social_website']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description']
        labels = {
            'name': "Skill Name",
            'description': "Skill Description"
        }

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']
        labels = {
            'name': "How to address you",
            'email': "Email address",
        }

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})

